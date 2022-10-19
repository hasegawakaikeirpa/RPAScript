import tkinter as tk
from PIL import Image, ImageTk
import P_Table as PT
from tkinter import messagebox
import os
import OCRFlow as OCRF
import toml
import customtkinter as ck
from CV2Setting import straightlinesetting
from GCloudVision import AutoLine, LineTomlOut
import ScrollableFrame as SF
import tomlCreate as toml_c
from tkinter import filedialog
import ProgressBar as PB
import IconCode
import threading

###################################################################################################
class Application(tk.Frame):
    # class Application(tk.Toplevel):
    def __init__(
        self,
        Menu,
        window_root,
        window_root_top,
        title_n,
        default_path,
        master=None,
    ):
        # Windowの初期設定を行う。
        # super().__init__(master)
        # ウィジェットサイズ設定##########################################################
        self.master = window_root
        self.top = window_root_top
        self.width_of_window = int(int(self.master.winfo_screenwidth()) * 0.95)
        self.height_of_window = int(int(self.master.winfo_screenheight()) * 0.85)
        self.Wwidth = int(self.width_of_window)  # int(W[0]) * 0.7
        self.Wheight = int(self.height_of_window * 0.8)  # int(W[0]) * 0.7
        self.wid_Par = self.width_of_window / 1459
        self.hei_Par = self.height_of_window / 820
        self.SideWidth = int(100 * self.wid_Par)
        self.SideHeight = int(50 * self.hei_Par)
        self.LabelWidth = int(50 * self.wid_Par)
        self.LabelHeight = int(20 * self.hei_Par)
        self.BtnWidth = int(170 * self.wid_Par)
        self.BtnHeight = int(20 * self.hei_Par)
        self.EntWidth = int(300 * self.hei_Par)
        self.EntHeight = int(20 * self.wid_Par)
        self.t_font = (1, int(8 * self.wid_Par))
        ###############################################################################
        # toml読込------------------------------------------------------------------------------
        with open(Menu.tomlPath, encoding="utf-8") as f:
            self.Banktoml = toml.load(f)
        # -----------------------------------------------------------
        try:
            self.Yoko_N = self.FN + "_Yoko"
            self.Tate_N = self.FN + "_Tate"
            self.rep_N = self.FN + "_ReplaceStr"
            self.readcsv1 = self.Banktoml["LineSetting"][self.Yoko_N]
            self.readcsv2 = self.Banktoml["LineSetting"][self.Tate_N]
        except:
            print("行列tomlインポートエラー")
            self.readcsv1 = self.Banktoml["LineSetting"]["Nomal_Yoko"]
            self.readcsv2 = self.Banktoml["LineSetting"]["Nomal_Tate"]
        # -----------------------------------------------------------
        # 画像の読込#####################################################################
        # 透過キャンバスの画像範囲検出の為リサイズ比率等を算出
        self.LoadImgstr()
        self.IR = LoadImg(self.Wwidth, self.Wheight, self.Imgurl)
        self.CW, self.CH, self.HCW, self.HCH, self.TKimg = (
            self.IR[0],
            self.IR[1],
            self.IR[2],
            self.IR[3],
            self.IR[4],
        )
        # ##############################################################################
        # 下のウィンドウ##########################
        # self.master = tk.Toplevel()  # サブWindow作成
        self.master.bind("<Motion>", self.change)  # 下ウィンドウにマウス移動関数bind
        self.master.protocol("WM_DELETE_WINDOW", self.click_close)  # 閉じる処理設定
        self.master.geometry(
            "%dx%d+%d+%d" % (self.width_of_window, self.height_of_window, 0, 0)
        )
        self.master.resizable(0, 0)
        # 上のウィンドウ##########################
        # self.top = tk.Toplevel()  # サブWindow作成
        self.top.minsize(self.width_of_window, self.height_of_window)
        self.top.bind("<Motion>", self.change)  # 透過ウィンドウにマウス移動関数bind
        self.top.protocol("WM_DELETE_WINDOW", self.click_close)  # 閉じる処理設定
        self.top.wm_attributes("-topmost", True)  # 常に一番上のウィンドウに指定
        self.top.geometry(
            "%dx%d+%d+%d" % (self.width_of_window, self.height_of_window, 0, 0)
        )
        self.top.resizable(0, 0)
        # 透過キャンバスフレーム##########################################################
        self.topFrame = tk.Frame(
            self.top,
            bg="snow",
            height=self.CH,
            width=self.CW,
            relief=tk.GROOVE,
            bd=2,
        )
        self.topFrame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.top.forward = tk.Canvas(
            self.topFrame, background="white", width=self.CW, height=self.CH
        )  # 透過キャンバス作成
        self.top.forward.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.top.forward.bind("Enter", self.change)
        # キャンバス内ダブルクリックイベントに関数バインド
        self.top.forward.bind(
            "<Double-1>", lambda: self.RedLine(self, self.CW, self.CH)
        )
        # ##############################################################################
        # 配置
        # サイドメニューフレーム##########################################################
        self.frame0 = tk.Frame(
            self.top,
            width=self.width_of_window,
            height=self.height_of_window,
            bg="#ecb5f5",
            relief=tk.GROOVE,
        )
        self.frame0.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        self.frame0.propagate(0)
        #################################################################################
        # サイドメニュー内フレーム########################################################
        self.Tframe = tk.Frame(
            self.frame0,
            width=self.SideWidth,
            height=self.SideHeight,
            bg="#ecb5f5",
            relief=tk.GROOVE,
        )
        self.Tframe.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        # LineNo表示テキスト
        self.L_Name = ck.CTkLabel(
            master=self.Tframe,
            text="選択ライン名",
            width=self.LabelWidth,
            height=self.LabelHeight,
            corner_radius=8,
            text_font=self.t_font,
        ).grid(row=0, column=0, pady=5)
        # テキストボックスの作成と配置
        self.L_Nametxt = ck.CTkEntry(
            master=self.Tframe,
            width=self.EntWidth,
            height=self.EntHeight,
            border_width=2,
            corner_radius=8,
            text_color="black",
            border_color="snow",
            fg_color="snow",
        )
        self.L_Nametxt.grid(row=0, column=1, pady=5)
        # テキスト変換一致率
        self.TxtPar = ck.CTkLabel(
            master=self.Tframe,
            text="テキスト変換一致率",
            width=self.LabelWidth,
            height=self.LabelHeight,
            corner_radius=8,
            text_font=self.t_font,
        ).grid(row=1, column=0, pady=5)
        # テキストボックスの作成と配置
        self.ChangeVar = ck.CTkEntry(
            master=self.Tframe,
            width=self.EntWidth,
            height=self.EntHeight,
            border_width=2,
            corner_radius=8,
            text_color="black",
            border_color="snow",
            fg_color="snow",
        )
        self.ChangeVar.insert(0, 50)
        self.ChangeVar.grid(row=1, column=1, pady=5)
        # 行数表示テキスト
        self.setfile = ck.CTkLabel(
            master=self.Tframe,
            text="設定ファイル",
            width=self.LabelWidth,
            height=self.LabelHeight,
            corner_radius=8,
            text_font=self.t_font,
        ).grid(row=3, column=0, pady=5)
        self.tomlurlent = ck.CTkEntry(
            master=self.Tframe,
            width=self.EntWidth,
            height=self.EntHeight,
            border_width=2,
            corner_radius=8,
            text_color="black",
            border_color="snow",
            fg_color="snow",
        )
        self.tomlurlent.insert(0, Menu.tomlPath)
        self.tomlurlent.grid(row=3, column=1, pady=5)
        # 行数表示テキスト
        # 設定ファイル変更ボタン--------------------------------------------------------
        self.tomlbutton = ck.CTkButton(
            master=self.Tframe,
            text="設定ファイル変更",
            command=lambda: self.ChangeToml(Menu),
            width=self.BtnWidth,
            height=self.BtnHeight,
            border_width=2,
            corner_radius=8,
            text_color="snow",
            border_color="snow",
        )
        self.tomlbutton.grid(row=4, column=0, columnspan=2, sticky=tk.N)
        #################################################################################
        # 列名設定フレーム################################################################
        # サイドメニュー内フレーム########################################################
        self.Tframe2 = tk.Frame(
            self.frame0,
            width=self.SideWidth,
            height=self.SideHeight,
            bg="#ecb5f5",
            relief=tk.GROOVE,
        )
        self.Tframe2.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        ck.CTkLabel(
            master=self.Tframe2,
            text="出力列名設定",
            width=self.LabelWidth,
            height=self.LabelHeight,
            corner_radius=8,
            text_font=self.t_font,
        ).grid(
            row=0, column=0, sticky=tk.W + tk.E
        )  # フレームテキスト
        threading.Thread(target=self.createSC(Menu))
        #################################################################################
        # サイドメニュー内変換設定フレーム#################################################
        Setframe = tk.Frame(
            self.frame0,
            bg="#ecb5f5",
            relief=tk.GROOVE,
            width=int(5 * self.wid_Par),
            bd=2,
        )
        Setframe.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        tomlEntries = []
        # テキストボックスの作成と配置
        # Start ####################################################################
        ck.CTkLabel(
            master=Setframe,
            text="日付列番号",
            width=self.LabelWidth,
            height=self.LabelHeight,
            corner_radius=8,
            text_font=self.t_font,
        ).grid(row=0, column=0)
        self.DaySet = ck.CTkEntry(
            master=Setframe,
            width=self.EntWidth,
            height=self.EntHeight,
            border_width=2,
            corner_radius=8,
            text_color="black",
            border_color="snow",
            fg_color="snow",
        )
        tomlEntries.append(self.DaySet)
        # tomlインポート------------------------------------------------------------
        try:
            self.TomlInsert(self.DaySet, self.Banktoml["Setframe"][F_N + "_DaySetList"])
        except:
            self.TomlInsert(self.DaySet, self.Banktoml["Setframe"]["Nomal_DaySetList"])
        # --------------------------------------------------------------------------
        self.DaySet.bind("<Return>", tomlreturn)
        self.DaySet.bind("<Tab>", tomlreturn)
        self.DaySet.grid(row=0, column=1, padx=5, pady=5)
        # Start ####################################################################
        ck.CTkLabel(
            master=Setframe,
            text="金額表示列番号",
            width=self.LabelWidth,
            height=self.LabelHeight,
            corner_radius=8,
            text_font=self.t_font,
        ).grid(row=1, column=0)
        self.MoneySet = ck.CTkEntry(
            master=Setframe,
            width=self.EntWidth,
            height=self.EntHeight,
            border_width=2,
            corner_radius=8,
            text_color="black",
            border_color="snow",
            fg_color="snow",
        )
        tomlEntries.append(self.MoneySet)
        # tomlインポート------------------------------------------------------------
        try:
            self.TomlInsert(self.MoneySet, self.Banktoml["Setframe"][F_N + "_MoneySet"])
        except:
            self.TomlInsert(self.MoneySet, self.Banktoml["Setframe"]["Nomal_MoneySet"])
        # --------------------------------------------------------------------------
        self.MoneySet.bind("<Return>", tomlreturn)
        self.MoneySet.bind("<Tab>", tomlreturn)
        self.MoneySet.grid(row=1, column=1, padx=5, pady=5)
        # サイドメニュー内ボタンフレーム###################################################
        frame = tk.Frame(
            self.frame0,
            bg="#ecb5f5",
            relief=tk.GROOVE,
            width=int(5 * self.wid_Par),
            bd=2,
        )
        # frame.grid(row=0, column=4, sticky=tk.N)
        frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        # 縦直線追加ボタン---------------------------------------------------------------
        button = ck.CTkButton(
            master=frame,
            text="縦直線追加",
            command=lambda: StLine(self.top.forward, self.CW, self.CH),
            width=self.BtnWidth,
            height=self.BtnHeight,
            border_width=2,
            corner_radius=8,
            text_color="snow",
            border_color="snow",
            fg_color="tomato",
        )
        button.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W + tk.E)
        # 横直線追加ボタン---------------------------------------------------------------
        button2 = ck.CTkButton(
            master=frame,
            text="横直線追加",
            command=lambda: StWLine(self.top.forward, self.CW, self.CH),
            width=self.BtnWidth,
            height=self.BtnHeight,
            border_width=2,
            corner_radius=8,
            text_color="snow",
            border_color="snow",
            fg_color="seagreen3",
        )
        button2.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W + tk.E)
        # 削除ボタン---------------------------------------------------------------
        button5 = ck.CTkButton(
            master=frame,
            text="選択直線削除",
            command=lambda: LineDelete(self.top.forward),
            width=self.BtnWidth,
            height=self.BtnHeight,
            border_width=2,
            corner_radius=8,
            text_color="snow",
            border_color="snow",
            fg_color="Orange",
        )
        button5.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W + tk.E)
        # 新規直線描画ボタン---------------------------------------------------------------
        button3 = ck.CTkButton(
            master=frame,
            text="新規直線描画",
            command=lambda: NewLineCreate(self, self.top.forward, self.HCW, self.HCH),
            width=self.BtnWidth,
            height=self.BtnHeight,
            border_width=2,
            corner_radius=8,
            text_color="snow",
            border_color="snow",
            fg_color="mediumPurple",
        )
        button3.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W + tk.E)
        # # 置換ボタン---------------------------------------------------------------
        # button7 = ck.CTkButton(
        #     master=frame,
        #     text="置換対象文字列設定",
        #     command=lambda: self.tomlFrameOpen(self),
        #     width=BtnWidth,
        #     height=BtnHeight,
        #     border_width=2,
        #     corner_radius=8,
        #     text_color="snow",
        #     border_color="snow",
        #     fg_color="hotpink1",
        # )
        # button7.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W + tk.E)
        # 自動直線描画ボタン---------------------------------------------------------------
        button3 = ck.CTkButton(
            master=frame,
            text="自動直線描画",
            command=lambda: self.AutoNewLineCreate(
                self.top.forward, self.HCW, self.HCH
            ),
            width=self.BtnWidth,
            height=self.BtnHeight,
            border_width=2,
            corner_radius=8,
            text_color="snow",
            border_color="snow",
            fg_color="#2b5cff",
        )
        button3.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W + tk.E)
        # サイドメニュー内ボタンフレーム2###################################################
        frame2 = tk.Frame(
            self.frame0,
            bg="#ecb5f5",
            relief=tk.GROOVE,
            width=int(5 * self.wid_Par),
            bd=2,
        )
        frame2.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        # 確定ボタン---------------------------------------------------------------
        button4 = ck.CTkButton(
            master=frame2,
            text="確定",
            command=lambda: EnterP(
                self.top.forward,
                self.HCW,
                self.HCH,
                self,
                self.master,
                self.top,
                self.ChangeVar,
            ),
            width=self.BtnWidth,
            height=self.BtnHeight,
            border_width=2,
            corner_radius=8,
            text_color="snow",
            border_color="snow",
            fg_color="steelblue3",
        )
        button4.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W + tk.E)
        # 戻るボタン---------------------------------------------------------------
        button6 = ck.CTkButton(
            master=frame2,
            text="戻る",
            command=lambda: ReturnBack(self),
            width=self.BtnWidth,
            height=self.BtnHeight,
            border_width=2,
            corner_radius=8,
            text_color="snow",
            border_color="snow",
            fg_color="gray",
        )
        button6.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W + tk.E)
        # ##############################################################################
        threading.Thread(
            target=Gra(
                self.top.forward, self.readcsv1, self.readcsv2, self.HCW, self.HCH
            )
        )
        self.top.wm_attributes("-transparentcolor", "white")  # トップWindowの白色を透過
        # 下Windowのキャンバス作成
        # 画像の配置#####################################################################
        self.InportIMG(Menu)
        # ##############################################################################
        Entries = self.Entries
        self.master.attributes("-topmost", True)
        self.master.attributes("-topmost", False)
        self.top.attributes("-topmost", True)
        logger.debug("TKINTERCV2Setting_Application起動完了")  # Log出力
        return

    # ----------------------------------------------------------------------------------
    def __del__(self):
        print("インスタンスが破棄されました")

    # 以下self関数##################################################################################
    def LoadImgstr(self):
        pat = os.getcwd() + r"\\OCRViewFromMenu\\OCR.png"
        if os.path.isfile(pat) is True:
            self.Imgurl = pat
            self.FN = os.path.splitext(os.path.basename(pat))[0]
        else:
            pat = os.getcwd() + r"\\OCR.png"
            self.Imgurl = pat
            self.FN = os.path.splitext(os.path.basename(pat))[0]
        return

    # ---------------------------------------------------------------------------------------------
    def RedLine(self, CW, CH):
        """
        縦直線追加ボタン処理
        """
        TName = "Line" + str(len(tagsList) + 1)
        logger.debug("縦直線追加ボタン処理開始")  # Log出力
        self.create_line(
            CW - 50,
            0,
            CW - 50,
            CH,
            tags=TName,
            width=7,
            fill="#FF0000",
            activefill="#DBDD6F",
        )
        self.tag_bind(TName, "<ButtonPress-1>", click1)
        self.tag_bind(TName, "<Double-1>", EventDelete)
        self.tag_bind(TName, "<B1-Motion>", drag1)
        BSS = [0, 0, 0, 0]
        TSS = [TName, CW - 50, 0, CW - 50, CH, "Yoko"]
        tagsList.append([TSS, BSS])

    # ---------------------------------------------------------------------------------------------
    def createSC(self, Menu):
        self.SF = SF.ScrollableFrame(self.Tframe2, self.CW, self.CH, bar_x=False)
        self.SF.grid(sticky=tk.W + tk.E)  # , ipadx=500, ipady=100)
        # エントリーウィジェットマネージャを初期化
        self.Entries = []  # エントリーウィジェットのインスタンス
        self.insertEntries = []  # 追加するボタンのようなラベル
        self.removeEntries = []  # 削除するボタンのようなラベル
        # こちらはインデックスマネージャ。ウィジェットの数や並び方を管理
        self.index = 0  # 最新のインデックス番号
        self.indexes = []  # インデックスの並び
        try:
            self.ColList = self.Banktoml["ColList"][self.FN + "_List"]
        except:
            self.ColList = self.Banktoml["ColList"]["Nomal_List"]
        i = 0
        for ColListItem in self.ColList:
            self.createEntry(i, Menu, bar_x=False)
            self.Entries[i].insert(0, ColListItem)
            i += 1

    # ---------------------------------------------------------------------------------------------
    def tomlFrameClose(self):
        """
        SideMenutoml変換設定の更新
        """
        l_s = []
        for B_t in self.BRSTxt:
            l_s.append(B_t.get())
        self.Banktoml["LineSetting"][rep_N] = l_s
        toml_c.dump_toml(self.Banktoml, tomlurl)
        self.TomlInsert(self.ReplaceStr, self.Banktoml["LineSetting"][rep_N])
        self.frame0.grid()
        self.topRepFrame.grid_forget()
        logger.debug("SideMenutoml変換設定の更新完了")  # Log出力

    # ---------------------------------------------------------------------------------------------

    # ---------------------------------------------------------------------------------------------
    def ChangeToml(self, Menu):
        """
        tomlリストを変更
        """
        try:
            typ = [("tomlファイル", "*.toml")]
            self.top.withdraw()
            tomlurl = filedialog.askopenfilename(filetypes=typ)
            if tomlurl != "":
                try:
                    self.top.destroy()
                    self.master.destroy()
                except:
                    print("")
                messagebox.showinfo("設定ファイル再読込", "設定ファイルを再読み込みします。")
                logger.debug("tomlファイル再読込")  # Log出力
                Main(Master, imgurl, tomlurl, logger)
                logger.debug("tomlファイル再読込完了")  # Log出力
                print("toml変更")
            else:
                messagebox.showinfo("確認", "設定ファイルを指定してください。")
                self.top.deiconify()
        except:
            logger.debug("tomlファイル変更Err")  # Log出力
            self.top.deiconify()

    # ---------------------------------------------------------------------------------------------
    def TomlInsert(self, Ent, List):
        """
        tomlリストをTKentryに挿入
        """
        Ent.delete(0, tk.END)
        l_s = ",".join(List)
        Ent.insert(0, l_s)

    # ---------------------------------------------------------------------------------------------
    def InportIMG(self, Menu):
        """
        下ウィンドウに画像をリサイズして配置
        """
        logger.debug("下ウィンドウに画像をリサイズして配置開始")  # Log出力
        self.img = Image.open(self.Imgurl)
        self.img = self.img.resize((self.CW, self.CH))  # 画像リサイズ
        self.back = tk.Canvas(
            self.master, background="white", width=self.CW, height=self.CH
        )
        self.TKimg = ImageTk.PhotoImage(
            self.img, master=self.back
        )  # 下Windowに表示する画像オブジェクト
        self.back.create_image(
            0, 0, image=self.TKimg, anchor=tk.NW
        )  # 下Windowのキャンバスに画像挿入
        self.back.pack(side=tk.TOP, fill=tk.BOTH, expand=True)  # 下Windowを配置
        self.top.bind("<Configure>", self.change)
        self.back.bind("<Unmap>", self.unmap)
        self.back.bind("<Map>", self.map)

    # ---------------------------------------------------------------------------------------------
    def unmap(self, event):
        """
        上下ウィンドウ連携処理(上を隠す)
        """
        self.top.withdraw()

    # ---------------------------------------------------------------------------------------------
    def map(self, event):
        """
        上下ウィンドウ連携処理(上を表示)
        """
        self.lift()
        self.top.wm_deiconify()
        self.top.attributes("-topmost", True)

    # ---------------------------------------------------------------------------------------------
    def change(self, event):
        """
        上下ウィンドウ連携処理(ウィンドウサイズ変更)
        """
        top_geometry = self.top.geometry()
        self.master.geometry(top_geometry)

    # -------------------------------------------------------------------------------------
    def insertEntry_click(self, event, id):
        """
        列名設定項目追加ボタン処理
        """
        global Entries

        logger.debug("列名設定項目追加ボタン処理開始")  # Log出力
        # 追加する位置
        wn = event.widget
        si_r = 0
        for si in self.insertEntries:
            if si == wn:
                break
            si_r += 1
        next = si_r + 1
        self.index = self.index + 1
        # エントリーウィジェットを作成して配置
        self.createEntry(next, bar_x=False)
        Entries = self.Entries
        ColumnTomlIn(self)

    # -------------------------------------------------------------------------------------
    def removeEntry_click(self, event, id):
        """
        列名設定項目削除ボタン処理
        """
        global Entries

        logger.debug("列名設定項目削除ボタン処理開始")  # Log出力
        id = 0
        for SRI in self.removeEntries:
            if SRI == event.widget:
                break
            id += 1
        # 削除する位置
        current = id
        # エントリーウィジェットと追加・削除ボタンのようなラベルを削除
        self.Entries[current].destroy()
        self.insertEntries[current].destroy()
        self.removeEntries[current].destroy()
        # エントリーウィジェットマネージャから削除
        self.Entries.pop(current)
        self.insertEntries.pop(current)
        self.removeEntries.pop(current)
        self.indexes.pop(current)
        Entries = self.Entries
        # 再配置
        self.updateEntries()
        ColumnTomlIn(self)

    # -------------------------------------------------------------------------------------
    def updateEntries(self, bar_x=False, bar_y=True):
        """
        列名設定項目を再配置
        """

        logger.debug("列名設定項目を再配置開始")  # Log出力
        # エントリーウィジェットマネージャを参照して再配置
        for i in range(len(self.indexes)):
            self.Entries[i].grid(column=0, row=i, padx=5)
            self.Entries[i].bind("<MouseWheel>", self.SF.mouse_y_scroll)
            self.Entries[i].bind("<Return>", ColumnTomlIn)
            self.Entries[i].bind("<Tab>", ColumnTomlIn)
            self.Entries[i].lift()
            self.insertEntries[i].grid(column=1, row=i, padx=5)
            self.insertEntries[i].bind("<MouseWheel>", self.SF.mouse_y_scroll)
            self.removeEntries[i].grid(column=2, row=i, padx=5)
            self.removeEntries[i].bind("<MouseWheel>", self.SF.mouse_y_scroll)
        # 1つしかないときは削除ボタンのようなラベルを表示しない
        if len(self.indexes) == 1:
            self.removeEntries[0].grid_forget()
        if bar_y:  # スクロールバー縦
            self.SF.scrollbar_y.grid_forget()  # スクロールバー削除
            # スクロールバー再作成--------------------------------------------------
            self.SF.scrollbar_y = tk.ttk.Scrollbar(
                self.SF.scrollable_frame,
                orient="vertical",
                command=self.SF.canvas.yview,
            )
            # ---------------------------------------------------------------------
            if len(self.indexes) == 1:
                self.SF.scrollbar_y.grid(row=0, column=2, sticky=tk.S + tk.N)
            else:
                self.SF.scrollbar_y.grid(
                    row=0, rowspan=len(self.indexes), column=3, sticky=tk.S + tk.N
                )
            self.SF.canvas.configure(yscrollcommand=self.SF.scrollbar_y.set)
        if bar_x:  # スクロールバー横
            self.SF.scrollbar_x.grid_forget()  # スクロールバー削除
            # スクロールバー再作成--------------------------------------------------
            self.SF.scrollbar_x = tk.ttk.Scrollbar(
                self.SF.scrollable_frame,
                orient="horizontal",
                command=self.SF.canvas.xview,
            )
            # ---------------------------------------------------------------------
            self.SF.scrollbar_x.grid(
                row=len(self.indexes), column=0, columnspan=4, sticky=tk.E + tk.W
            )
            self.SF.canvas.configure(xscrollcommand=self.SF.scrollbar_x.set)
        logger.debug("列名設定項目を再配置完了")  # Log出力

    # -------------------------------------------------------------------------------------
    def createEntry(self, next, Menu, bar_x=False, bar_y=True):
        """
        列名設定項目を作成して再配置
        """

        logger.debug("列名設定項目を作成して再配置開始")  # Log出力
        # 最初のエントリーウィジェットを追加
        self.Entries.insert(
            next,
            ck.CTkEntry(
                master=self.SF.scrollable_frame,
                width=self.EntWidth,
                height=self.EntHeight,
                border_width=2,
                corner_radius=8,
                text_color="black",
                border_color="snow",
                fg_color="snow",
            ),
        )
        self.insertEntries.insert(
            next,
            tk.Label(
                self.SF.scrollable_frame,
                text="+",
                fg="#33ff33",
                bg="#ecb5f5",
                font=("Arial Black", 20),
            ),
        )  # エントリーウィジェットを削除するボタンのようなラベルを作成（初期の段階では表示しない）
        self.removeEntries.insert(
            next,
            tk.Label(
                self.SF.scrollable_frame,
                text="−",
                fg="#ff3333",
                bg="#ecb5f5",
                font=("Arial Black", 20),
            ),
        )  # 追加するボタンのようなラベルにクリックイベントを設定
        self.insertEntries[next].bind(
            "<1>", lambda event, id=self.index: self.insertEntry_click(event, id)
        )  # 削除するボタンのようなラベルにクリックイベントを設定
        self.removeEntries[next].bind(
            "<1>", lambda event, id=self.index: self.removeEntry_click(event, id)
        )  # インデックスマネージャに登録
        self.indexes.insert(next, self.index)
        # 再配置
        self.updateEntries(bar_x=False)

    # -------------------------------------------------------------------------------------
    def GetEntryTextButton_click(self, Menu):
        """
        列名設定項目取得関数
        """
        GetEntry = []
        logger.debug("列名設定項目取得関数開始")  # Log出力
        # 全てのエントリーウィジェットの内容を配列化
        for i in range(len(self.indexes)):
            GetEntry.append(self.Entries[i].get())
        # コンソールに表示
        return GetEntry

    # -------------------------------------------------------------------------------------
    def click_close(self):
        """
        ウィンドウ×ボタンクリック
        """
        self.top.withdraw()
        if messagebox.askokcancel("確認", "終了しますか？"):
            self.top.destroy()
            self.master.destroy()
            logger.debug("TKINTERCV2SettingClose完了")  # Log出力
        else:
            self.top.deiconify()
            logger.debug("TKINTERCV2SettingClose失敗")  # Log出力

    # ---------------------------------------------------------------------------------------------
    def AutoNewLineCreate(self, selfC, HCW, HCH):
        """
        自動直線描画ボタン処理
        """
        unmap(self)
        MSG = messagebox.askokcancel("確認", "自動直線描画しますか？")
        if MSG is True:
            logger.debug("新規直線描画処理開始")  # Log出力
            selfC = self.top.forward
            AL = AutoLine(imgurl, 1)
            if AL[0] is True:
                ####################################################################################
                F_N = os.path.splitext(os.path.basename(imgurl))[0]
                Yoko_N = F_N + "_Yoko"
                Tate_N = F_N + "_Tate"
                self.Banktoml["LineSetting"][Yoko_N] = AL[1]
                self.Banktoml["LineSetting"][Tate_N] = AL[2]
                toml_c.dump_toml(self.Banktoml, tomlurl)
                ####################################################################################
                AllLineDelete(self, selfC)
                Gra(selfC, AL[1], AL[2], HCW, HCH)  # 透過キャンバスに罫線描画
                map(self)
            else:
                MSG = messagebox.showinfo("確認", "自動直線描画に失敗しました。")

    # ---------------------------------------------------------------------------------------------
    # 以下関数######################################################################################


# ---------------------------------------------------------------------------------------------
def ColumnTomlIn(self):
    """
    toml列名設定の更新
    """
    global Entries
    try:
        TEntries = []
        for item in Entries:
            TEntries.append(item.get())
        self.Banktoml["ColList"][F_N + "_List"] = TEntries
        toml_c.dump_toml(self.Banktoml, tomlurl)
        logger.debug("toml列名設定の更新完了")  # Log出力
    except:
        logger.debug("toml列名設定の更新Err")  # Log出力


# ---------------------------------------------------------------------------------------------
def tomlreturn(self):
    """
    toml変換設定の更新
    """
    global tomlEntries

    # ----------------------------------------------------------
    DaySet = tomlEntries[0].get()
    if "," not in DaySet:
        l_s = []
        l_s.append(DaySet)
        self.Banktoml["Setframe"][F_N + "_DaySetList"] = l_s
    else:
        l_s = DaySet.split(",")
        self.Banktoml["Setframe"][F_N + "_DaySetList"] = l_s
    # ----------------------------------------------------------
    MoneySet = tomlEntries[1].get()
    if "," not in MoneySet:
        l_s = []
        l_s.append(MoneySet)
        self.Banktoml["Setframe"][F_N + "_MoneySet"] = l_s
    else:
        l_s = MoneySet.split(",")
        self.Banktoml["Setframe"][F_N + "_MoneySet"] = l_s
    # ----------------------------------------------------------
    # ReplaceSet = tomlEntries[2].get()
    # if "," not in ReplaceSet:
    #     l_s = []
    #     l_s.append(ReplaceSet)
    #     self.Banktoml["Setframe"][F_N + "_ReplaceSet"] = l_s
    # else:
    #     l_s = ReplaceSet.split(",")
    #     self.Banktoml["Setframe"][F_N + "_ReplaceSet"] = l_s
    # ----------------------------------------------------------
    # ReplaceStr = tomlEntries[3].get()
    # if "," not in ReplaceStr:
    #     l_s = []
    #     l_s.append(ReplaceStr)
    #     self.Banktoml["LineSetting"][rep_N] = l_s
    # else:
    #     l_s = ReplaceStr.split(",")
    #     self.Banktoml["LineSetting"][rep_N] = l_s
    toml_c.dump_toml(self.Banktoml, tomlurl)
    logger.debug("toml変換設定の更新完了")  # Log出力


# ---------------------------------------------------------------------------------------------
def ReturnNext(self):
    """
    次UI起動
    """
    self.top.withdraw()
    self.master.withdraw()


# ---------------------------------------------------------------------------------------------
def ReturnBack(self):
    """
    前UI起動
    """
    self.top.destroy()
    self.master.destroy()
    Master.deiconify()


# ---------------------------------------------------------------------------------------------
def NewLineCreate(self, selfC, HCW, HCH):
    """
    新規直線描画ボタン処理
    """
    global tagsList
    # メッセージボックス（OK・キャンセル）
    unmap(self)
    MSG = messagebox.askokcancel("確認", "新たに直線を描画しますか？")
    if MSG is True:
        logger.debug("新規直線描画処理開始")  # Log出力
        SLS = straightlinesetting(imgurl)
        if SLS[0] is True:
            ####################################################################################
            F_N = os.path.splitext(os.path.basename(imgurl))[0]
            Yoko_N = F_N + "_Yoko"
            Tate_N = F_N + "_Tate"
            self.Banktoml["LineSetting"][Yoko_N] = SLS[1]
            self.Banktoml["LineSetting"][Tate_N] = SLS[2]
            toml_c.dump_toml(self.Banktoml, tomlurl)
            ####################################################################################
            AllLineDelete(self, selfC)
            Gra(selfC, SLS[1], SLS[2], HCW, HCH)  # 透過キャンバスに罫線描画
            map(self)
        else:
            logger.debug("新規直線描画失敗")  # Log出力
            MSG = messagebox.showinfo(
                "直線描画失敗", "直線描画に失敗しました。画像ファイル名に日本語が混じっている可能性があります。"
            )
            map(self)


# ---------------------------------------------------------------------------------------------
def tomlListCreate(self):
    """
    リストボックス作成
    return:リストボックス(obj),スクロールバー(obj)
    """
    global Banktoml
    module = self.Banktoml["DataList"]["Datas"]
    var = tk.StringVar(value=module)
    listbox = tk.Listbox(self, listvariable=var, selectmode="multiple", height=6)
    scrollbar = tk.ttk.Scrollbar(self, orient="vertical", command=listbox.yview)
    listbox["yscrollcommand"] = scrollbar.set
    return listbox, scrollbar


# ---------------------------------------------------------------------------------------------
def LoadImg(Wwidth, Wheight, imgurl):
    """
    画像ファイル読込
    """
    global MaxW, MaxH
    # 画像の読込#####################################################################
    img = Image.open(imgurl)
    MaxW, MaxH = img.width, img.height
    CW, CH = int(Wwidth), int(Wheight)
    HCW, HCH = CW / MaxW, CH / MaxH  # リサイズ比率
    img = img.resize((CW, CH))  # 画像リサイズ
    imgobj = ImageTk.PhotoImage(img)  # 下Windowに表示する画像オブジェクト
    return CW, CH, HCW, HCH, imgobj
    # ##############################################################################


# ---------------------------------------------------------------------------------------------
def StLine(canvastop, CW, CH):
    """
    縦直線追加ボタン処理
    """
    TName = "Line" + str(len(tagsList) + 1)
    logger.debug("縦直線追加ボタン処理開始")  # Log出力
    canvastop.create_line(
        CW - 50,
        0,
        CW - 50,
        CH,
        tags=TName,
        width=7,
        fill="#FF0000",
        activefill="#DBDD6F",
    )
    canvastop.tag_bind(TName, "<ButtonPress-1>", click1)
    canvastop.tag_bind(TName, "<Double-1>", EventDelete)
    canvastop.tag_bind(TName, "<B1-Motion>", drag1)
    BSS = [0, 0, 0, 0]
    TSS = [TName, CW - 50, 0, CW - 50, CH, "Yoko"]
    tagsList.append([TSS, BSS])


# ---------------------------------------------------------------------------------------------
def StWLine(canvastop, CW, CH):
    """
    横直線追加ボタン処理
    """
    TName = "Line" + str(len(tagsList) + 1)
    logger.debug("横直線追加ボタン処理開始")  # Log出力
    canvastop.create_line(
        0,
        CH - 50,
        CW,
        CH - 50,
        tags=TName,
        width=7,
        fill="#00FF40",
        activefill="#DBDD6F",
    )
    canvastop.tag_bind(TName, "<ButtonPress-1>", click1)
    canvastop.tag_bind(TName, "<Double-1>", EventDelete)
    canvastop.tag_bind(TName, "<B1-Motion>", drag1)
    TSS = [TName, 0, CH - 50, CW, CH - 50, "Tate"]
    BSS = [0, 0, 0, 0]
    tagsList.append([TSS, BSS])


# ---------------------------------------------------------------------------------------------
def Gra(canvas, readcsv1, readcsv2, HCW, HCH):
    """
    透過キャンバス(上ウィンドウ)に罫線描画処理
    """
    # .create_line(Ⅹ座標（始点）, Ｙ座標（始点）,Ⅹ座標（終点）, Ｙ座標（終点）)
    global tagsList
    BtagsList = []
    tagsList = []
    ri = 0
    for readcsv1Item in readcsv1:
        ri += 1
        ripar0 = readcsv1Item[0] * HCW  # * CHh
        ripar1 = readcsv1Item[1] * HCH  # * CWw
        ripar2 = readcsv1Item[2] * HCW  # * CHh
        ripar3 = readcsv1Item[3] * HCH  # * CWw
        TName = "Line" + str(ri)
        try:
            canvas.dtag(TName, TName)
        except:
            print("dtagErr")
        canvas.create_line(
            ripar0,
            ripar1,
            ripar2,
            ripar3,
            tags=TName,
            width=7,
            fill="#FF0000",
            activefill="#DBDD6F",
        )
        canvas.tag_bind(TName, "<ButtonPress-1>", click1)
        canvas.tag_bind(TName, "<Double-1>", EventDelete)
        canvas.tag_bind(TName, "<B1-Motion>", drag1)
        canvas.place(x=0, y=0)
        BtagsList.append([TName, ripar0, ripar1, ripar2, ripar3, "Yoko"])
    for readcsv2Item in readcsv2:
        ri += 1
        ripar0 = readcsv2Item[0] * HCW  # * CHh
        ripar1 = readcsv2Item[1] * HCH  # * CWw
        ripar2 = readcsv2Item[2] * HCW  # * CHh
        ripar3 = readcsv2Item[3] * HCH  # * CWw
        TName = "Line" + str(ri)
        canvas.create_line(
            ripar0,
            ripar1,
            ripar2,
            ripar3,
            tags=TName,
            width=7,
            fill="#00FF40",
            activefill="#DBDD6F",
        )
        canvas.tag_bind(TName, "<ButtonPress-1>", click1)
        canvas.tag_bind(TName, "<Double-1>", EventDelete)
        canvas.tag_bind(TName, "<B1-Motion>", drag1)
        canvas.place(x=0, y=0)
        BtagsList.append([TName, ripar0, ripar1, ripar2, ripar3, "Tate"])
    TL = len(BtagsList)
    for TTL in range(TL):
        tagsListItem = BtagsList[TTL]
        BB = canvas.bbox(tagsListItem[0])
        BSS = [
            tagsListItem[1] - BB[0],
            tagsListItem[2] - BB[1],
            tagsListItem[3] - BB[2],
            tagsListItem[4] - BB[3],
        ]
        tagsList.append([tagsListItem, BSS])
    print("直線描画完了")
    logger.debug("透過キャンバス(上ウィンドウ)に罫線描画処理完了")  # Log出力


# ---------------------------------------------------------------------------------------------
def listintCheck(list):
    """
    条件テキストボックスの文字列に","があるか判定
    """
    for listItem in list:
        try:
            int(listItem)
        except:
            return False
    return True


# ---------------------------------------------------------------------------------------------
def EnterP(self, HCW, HCH, selfmother, Mter, Top, ChangeVar):
    """
    確定ボタンクリック
    """
    global tagsList
    global MaxW, MaxH

    logger.debug("確定ボタンクリック処理開始")  # Log出力
    FList = []
    FYokoList = []
    FTateList = []
    SGEL = selfmother.GetEntryTextButton_click()  # OCR出力列名
    # 条件テキストボックスの値格納---------------------------
    DaySet = selfmother.DaySet.get()
    MoneySet = selfmother.MoneySet.get()
    # ReplaceSet = selfmother.ReplaceSet.get()
    # ReplaceStr = selfmother.ReplaceStr.get()
    # ------------------------------------------------------
    # 条件テキストボックスのリスト化---------------------------
    if "," in DaySet:
        DaySet = DaySet.split(",")
    elif " " in DaySet:
        DaySet = DaySet.split(" ")
    else:
        DaySet = list(DaySet)
    # --------------------------------------------------------
    if "," in MoneySet:
        MoneySet = MoneySet.split(",")
    elif " " in MoneySet:
        MoneySet = MoneySet.split(" ")
    else:
        MoneySet = list(MoneySet)
    # --------------------------------------------------------
    # if "," in ReplaceSet:
    #     ReplaceSet = ReplaceSet.split(",")
    # elif " " in ReplaceSet:
    #     ReplaceSet = ReplaceSet.split(" ")
    # else:
    #     ReplaceSet = list(ReplaceSet)
    # --------------------------------------------------------
    # if "," in ReplaceStr:
    #     ReplaceStr = ReplaceStr.split(",")
    # elif " " in ReplaceStr:
    #     ReplaceStr = ReplaceStr.split(" ")
    # else:
    #     ReplaceStr = list(ReplaceStr)
    # ------------------------------------------------------
    # 条件テキストボックスの内容で処理分け-------------------------------------------------------------------
    if listintCheck(DaySet) is False:
        messagebox.showinfo("エラー", "日付列番号が不正です。数値以外を指定していないか確認してください。")
    elif listintCheck(MoneySet) is False:
        messagebox.showinfo("エラー", "金額表示列番号が不正です。数値以外を指定していないか確認してください。")
    # elif listintCheck(ReplaceSet) is False:
    #     messagebox.showinfo("エラー", "置換対象列番号が不正です。数値以外を指定していないか確認してください。")
    else:
        if len(tagsList) == 0:
            messagebox.showinfo("エラー", "軸が設定されていません。")
        else:
            for tagsListItem in tagsList:
                BB = self.bbox(tagsListItem[0][0])
                try:
                    BBS = [BB[0], BB[1], BB[2], BB[3]]
                    FList.append([tagsListItem[0], tagsListItem[1], BBS])
                except:
                    print("BBSErr")
            for FListItem in FList:
                FSSC1 = round((FListItem[1][0] + FListItem[2][0]) / HCW)
                FSSC2 = round((FListItem[1][1] + FListItem[2][1]) / HCH)
                FSSC3 = round((FListItem[1][2] + FListItem[2][2]) / HCW)
                FSSC4 = round((FListItem[1][3] + FListItem[2][3]) / HCH)
                if FSSC1 < 0 and FSSC1 < MaxW:
                    FSSC1 = 0
                elif FSSC1 > MaxW:
                    FSSC1 = MaxW
                if FSSC2 < 0 and FSSC2 < MaxH:
                    FSSC2 = 0
                elif FSSC2 > MaxH:
                    FSSC2 = MaxH
                if FSSC3 < 0 and FSSC3 < MaxW:
                    FSSC3 = 0
                elif FSSC3 > MaxW:
                    FSSC3 = MaxW
                if FSSC4 < 0 and FSSC4 < MaxH:
                    FSSC4 = 0
                elif FSSC4 > MaxH:
                    FSSC4 = MaxH
                FSS = [FSSC1, FSSC2, FSSC3, FSSC4]
                if FListItem[0][5] == "Yoko":
                    FYokoList.append(FSS)
                else:
                    FTateList.append(FSS)
                print(FSS)
            if len(FTateList) == 0:
                messagebox.showinfo("エラー", "横軸が設定されていません。")
            elif len(FYokoList) == 0:
                messagebox.showinfo("エラー", "縦軸が設定されていません。")
            else:
                # メッセージボックス（OK・キャンセル）
                unmap(selfmother)
                if len(FYokoList) == len(SGEL):
                    # --------------------------------------------------------------
                    if Master.HeaderCol_c == len(SGEL) or Master.HeaderCol_c == 0:
                        try:
                            ChangeVar = int(ChangeVar.get())
                        except:
                            MSG = messagebox.showinfo("エラー", "テキスト変換一致率に数値以外が入力されています。")
                            map(selfmother)
                            return
                        MSG = messagebox.askokcancel("確認", str(SGEL) + "の列名で出力します。")
                        if MSG is True:
                            map(selfmother)
                            PBAR = PB.Open(tk.Toplevel())  # サブWindow作成
                            ####################################################################################
                            F_N = os.path.splitext(os.path.basename(imgurl))[0]
                            Yoko_N = F_N + "_Yoko"
                            Tate_N = F_N + "_Tate"
                            self.Banktoml["LineSetting"][Yoko_N] = FYokoList
                            self.Banktoml["LineSetting"][Tate_N] = FTateList
                            toml_c.dump_toml(self.Banktoml, tomlurl)
                            ####################################################################################
                            print("csv保存完了")
                            logger.debug("縦横リスト書出完了")  # Log出力
                            OM = OCRF.Main(
                                imgurl,
                                FYokoList,
                                FTateList,
                                self.Banktoml,
                                SGEL,
                                DaySet,
                                MoneySet,
                                "ReplaceSet",
                                "ReplaceStr",
                                logger,
                                PBAR,
                                ChangeVar,
                            )
                            if OM[0] is True:
                                Read_Url = str(OM[1])
                                PBAR._target.step(10)
                                PBAR._target.master.destroy()
                                logger.debug("GoogleVisionAPI完了")  # Log出力
                                unmap(selfmother)
                                MSG = messagebox.showinfo(
                                    "抽出完了", Read_Url + "_に保存しました。"
                                )
                                MSG = messagebox.askokcancel(
                                    "確認", "次ページ読込を行いますか？\nキャンセルで比較ウィンドウを起動します。"
                                )
                                if MSG is True:
                                    Master.HeaderCol_c = len(SGEL)
                                    if "抽出文字列" in SGEL:
                                        Master.HeaderCol_c = Master.HeaderCol_c - 1
                                    if "抽出数値" in SGEL:
                                        Master.HeaderCol_c = Master.HeaderCol_c - 1
                                    logger.debug("次ページ読込開始")  # Log出力
                                    FUL.append(Read_Url)  # 書出しCSVURLリスト
                                    ReturnBack(selfmother)
                                else:
                                    FUL.append(Read_Url)  # 書出しCSVURLリスト
                                    if len(FUL) == 1:
                                        selfmother.top.withdraw()  # 透過ウィンドウ最小化
                                        selfmother.master.withdraw()  # 下ウィンドウ最小化

                                        PT.Main(
                                            self,
                                            Read_Url,
                                            logger,
                                            Mter,
                                            Top,
                                            imgurl,
                                            self.Banktoml,
                                            tomlurl,
                                        )
                                    else:
                                        RU = OCRF.JoinCSV(FUL)
                                        if RU[0] is True:
                                            Read_Url = RU[1]
                                            selfmother.top.withdraw()  # 透過ウィンドウ最小化
                                            selfmother.master.withdraw()  # 下ウィンドウ最小化

                                            PT.Main(
                                                self,
                                                Read_Url,
                                                logger,
                                                Mter,
                                                Top,
                                                imgurl,
                                                self.Banktoml,
                                                tomlurl,
                                            )
                                        else:
                                            logger.debug("CSV連結後出力失敗")  # Log出力
                            else:
                                logger.debug("GoogleVisionAPI抽出失敗")  # Log出力
                                unmap(selfmother)
                                MSG = messagebox.showinfo("抽出失敗", "エラーにより抽出に失敗しました。")
                                map(selfmother)
                        else:
                            logger.debug("GoogleVisionAPI抽出中断")  # Log出力
                            messagebox.showinfo("中断", "処理を中断します。")
                            map(selfmother)
                    else:
                        logger.debug("先頭ページの列数と設定列名数不一致。")  # Log出力
                        messagebox.showinfo("エラー", "先頭ページの列数と設定列名の数が一致しません。再確認してください。")
                        map(selfmother)
                else:
                    logger.debug("GoogleVisionAPI縦軸数と設定列名数不一致。")  # Log出力
                    messagebox.showinfo("確認", "縦軸数と設定列名の数が一致しません。再確認してください。")
                    map(selfmother)


# ---------------------------------------------------------------------------------------------
def unmap(self):
    """
    最上部ウィンドウを非表示
    """
    self.top.withdraw()


# ---------------------------------------------------------------------------------------------
def map(self):
    """
    self.topを最上部へ
    """
    self.lift()
    self.top.wm_deiconify()
    self.top.attributes("-topmost", True)


# ---------------------------------------------------------------------------------------------
def LineDelete(self):
    """
    選択直線の削除
    """
    global id1
    global tagsList
    # TName = "Line" + str(id1[0])
    TName = str(txt.get())
    self.delete(TName)
    logger.debug(TName + "_削除完了")  # Log出力
    r = 0
    for tagsListItem in tagsList:
        if TName == tagsListItem[0][0]:
            tagsList.pop(r)
            break
        r += 1
    nptag_L = LineTomlOut(tagsList, HCW, HCH)
    if nptag_L[0] is True:
        ####################################################################################
        F_N = os.path.splitext(os.path.basename(imgurl))[0]
        Yoko_N = F_N + "_Yoko"
        Tate_N = F_N + "_Tate"
        self.Banktoml["LineSetting"][Yoko_N] = nptag_L[1]
        self.Banktoml["LineSetting"][Tate_N] = nptag_L[2]
        toml_c.dump_toml(self.Banktoml, tomlurl)
        ####################################################################################
    else:
        print("Err")


# ---------------------------------------------------------------------------------------------
def AllLineDelete(self, selfC):
    """
    選択直線の削除
    """
    global tagsList
    r = len(tagsList) - 1
    selfC.delete("all")
    for tagsListItem in reversed(tagsList):
        selfC.delete(tagsListItem[0][0])
        tagsList.pop(r)
        r -= 1


# ---------------------------------------------------------------------------------------------
# 円、矩形、直線を描画＆ドラッグできるようにする【tkinter】
def click1(event):
    """
    縦直線描画処理(画面クリック)
    """
    global x1
    global y1
    global id1
    txt.delete(0, tk.END)
    x2 = event.x
    y2 = event.y
    id1 = event.widget.find_closest(x2, y2)
    TName = event.widget.gettags(id1[0])[0]
    logger.debug(TName + "_縦直線描画処理完了")  # Log出力
    txt.insert(tk.END, TName)
    x1 = x2
    y1 = y2


# ---------------------------------------------------------------------------------------------
def EventDelete(event):
    """
    縦直線描画処理(画面ダブルクリック)
    """
    global x1
    global y1
    global id1

    x2 = event.x
    y2 = event.y
    id1 = event.widget.find_closest(x2, y2)
    TName = event.widget.gettags(id1[0])[0]
    event.widget.delete(TName)
    logger.debug(TName + "_削除完了")  # Log出力
    r = 0
    for tagsListItem in tagsList:
        if TName == tagsListItem[0][0]:
            tagsList.pop(r)
            break
        r += 1
    nptag_L = LineTomlOut(tagsList, HCW, HCH)
    if nptag_L[0] is True:
        ####################################################################################
        F_N = os.path.splitext(os.path.basename(imgurl))[0]
        Yoko_N = F_N + "_Yoko"
        Tate_N = F_N + "_Tate"
        self.Banktoml["LineSetting"][Yoko_N] = nptag_L[1]
        self.Banktoml["LineSetting"][Tate_N] = nptag_L[2]
        toml_c.dump_toml(self.Banktoml, tomlurl)
        ####################################################################################
    else:
        print("Err")
    txt.delete(0, tk.END)


# ---------------------------------------------------------------------------------------------
def drag1(event):
    """
    縦直線移動処理(ドラッグ)
    """
    global x1
    global y1

    global id1
    x2 = event.x
    y2 = event.y
    id1 = event.widget.find_closest(x2, y2)
    del_x1 = x2 - x1
    del_y1 = y2 - y1
    x0, y0, x1, y1 = event.widget.coords(id1)
    event.widget.coords(id1, x0 + del_x1, y0 + del_y1, x1 + del_x1, y1 + del_y1)
    x1 = x2
    y1 = y2


# ---------------------------------------------------------------------------------------------
def tomlread():
    """
    tomlリード
    """
    try:
        r_toml = os.getcwd() + r"\OCRView\Setting.toml"
        return r_toml
    except:
        r_toml = os.getcwd() + r"\Setting.toml"
        return r_toml


# ---------------------------------------------------------------------------------------------
def setopen(Menu, app):
    app.top.deiconify()
    app.master.deiconify()
    app.InportIMG(Menu)


# ------------------------------------------------------------------------------------
def Open(Menu, w_root, w_root_top, url, log):
    global logger
    logger = log
    TKCV2 = Application(Menu, w_root, w_root_top, "OCR読取 Ver:0.9", url)
    # 　フレームループ処理
    # TKCV2.window_root.mainloop()


# ---------------------------------------------------------------------------------------------
def Main(self):
    """
    呼出関数
    """
    global logger
    # root = tk.Tk()  # Window生成
    logger = self.logger
    app = Application(self, master=self.window_rootFrame)
    # --- 基本的な表示準備 ----------------
    return app
