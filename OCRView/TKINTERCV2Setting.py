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
# class Application(tk.Frame):
class Application(tk.Toplevel):
    def __init__(self, master=None):
        global TKimg  # 画像オブジェクト用グローバル変数
        global txt
        global CW, CH, HCW, HCH
        global Banktoml
        global Entries
        global tomlEntries
        global SideWidth, SideHeight, LabelWidth
        global LabelHeight, BtnWidth, BtnHeight, EntHeight, EntWidth
        # Windowの初期設定を行う。
        super().__init__(master)
        self.withdraw()
        # Windowの画面サイズを設定する。
        G_logger.debug("TKINTERCV2Setting_Application起動")  # Log出力
        # customtkスタイル
        ck.set_appearance_mode("System")  # Modes: system (default), light, dark
        ck.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green
        width_of_window = int(int(self.winfo_screenwidth()) * 0.95)
        height_of_window = int(int(self.winfo_screenheight()) * 0.95)
        wid_Par = width_of_window / 1459
        hei_Par = height_of_window / 820
        x_coodinate = width_of_window * 0.01
        y_coodinate = height_of_window * 0.01
        # 　メインウィンドウサイズ指定
        self.master.geometry(
            "%dx%d+%d+%d"
            % (width_of_window, height_of_window, x_coodinate, y_coodinate)
        )
        # 　メインウィンドウタイトル
        self.master.title("OCR読取 Ver:0.9-表形式抽出-")
        self.master.minsize(width_of_window, height_of_window)
        self.master.resizable(0, 0)
        # 画像の読込#####################################################################
        # 透過キャンバスの画像範囲検出の為リサイズ比率等を算出
        print(self.master.geometry())
        W = self.master.geometry().split("x")
        # Wwidth = int(1480 * 0.8)  # int(W[0]) * 0.7
        Wwidth = int(width_of_window)  # int(W[0]) * 0.7
        W = W[1].split("+")
        Wheight = int(height_of_window * 0.8)  # int(W[0]) * 0.7
        IR = LoadImg(Wwidth, Wheight)
        CW, CH, HCW, HCH, TKimg = IR[0], IR[1], IR[2], IR[3], IR[4]
        # ##############################################################################
        self.top = tk.Toplevel()  # サブWindow作成
        data = IconCode.icondata()
        self.top.tk.call("wm", "iconphoto", self.top._w, tk.PhotoImage(data=data))
        self.top.minsize(width_of_window, height_of_window)
        self.top.bind("<Motion>", self.change)  # 透過ウィンドウにマウス移動関数bind
        self.master.bind("<Motion>", self.change)  # 下ウィンドウにマウス移動関数bind
        self.top.protocol("WM_DELETE_WINDOW", self.click_close)  # 閉じる処理設定
        self.master.protocol("WM_DELETE_WINDOW", self.click_close)  # 閉じる処理設定
        self.top.wm_attributes("-topmost", True)  # 常に一番上のウィンドウに指定
        self.top.geometry(
            "%dx%d+%d+%d"
            % (width_of_window, height_of_window, x_coodinate, y_coodinate)
        )
        self.top.resizable(0, 0)
        self.top.minsize(width_of_window, height_of_window)
        # 透過キャンバスフレーム##########################################################
        self.topFrame = tk.Frame(
            self.top,
            bg="snow",
            height=CH,
            width=CW,
            relief=tk.GROOVE,
            bd=2,
        )
        self.topFrame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.top.forward = tk.Canvas(
            self.topFrame, background="white", width=CW, height=CH
        )  # 透過キャンバス作成
        self.top.forward.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.top.forward.bind("Enter", self.change)
        # キャンバス内ダブルクリックイベントに関数バインド
        self.top.forward.bind("<Double-1>", lambda: self.RedLine(self, CW, CH))
        # ##############################################################################
        # 配置
        # サイドメニューフレーム##########################################################
        SideWidth = int(100 * wid_Par)
        SideHeight = int(50 * hei_Par)
        LabelWidth = int(50 * wid_Par)
        LabelHeight = int(20 * hei_Par)
        BtnWidth = int(200 * wid_Par)
        BtnHeight = int(20 * hei_Par)
        EntWidth = int(100 * hei_Par)
        EntHeight = int(20 * wid_Par)
        t_font = (1, int(8 * wid_Par))
        self.frame0 = tk.Frame(
            self.top,
            width=width_of_window,
            height=height_of_window,
            bg="#ecb5f5",
            relief=tk.GROOVE,
        )
        # self.frame0.grid(row=1, column=0, sticky=tk.NSEW)
        self.frame0.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        self.frame0.propagate(0)
        #################################################################################
        # サイドメニュー内フレーム########################################################
        Tframe = tk.Frame(
            self.frame0,
            width=SideWidth,
            height=SideHeight,
            bg="#ecb5f5",
            relief=tk.GROOVE,
        )
        Tframe.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        # LineNo表示テキスト
        ck.CTkLabel(
            master=Tframe,
            text="選択ライン名",
            width=LabelWidth,
            height=LabelHeight,
            corner_radius=8,
            text_font=t_font,
        ).grid(row=0, column=0, pady=5)
        # テキストボックスの作成と配置
        txt = ck.CTkEntry(
            master=Tframe,
            width=EntWidth,
            height=EntHeight,
            border_width=2,
            corner_radius=8,
            text_color="black",
            border_color="snow",
            fg_color="snow",
        )
        txt.grid(row=0, column=1, pady=5)
        # テキスト変換一致率
        ck.CTkLabel(
            master=Tframe,
            text="テキスト変換一致率",
            width=LabelWidth,
            height=LabelHeight,
            corner_radius=8,
            text_font=t_font,
        ).grid(row=1, column=0, pady=5)
        # テキストボックスの作成と配置
        self.ChangeVar = ck.CTkEntry(
            master=Tframe,
            width=EntWidth,
            height=EntHeight,
            border_width=2,
            corner_radius=8,
            text_color="black",
            border_color="snow",
            fg_color="snow",
        )
        self.ChangeVar.insert(0, 50)
        self.ChangeVar.grid(row=1, column=1, pady=5)
        # 行数表示テキスト
        ck.CTkLabel(
            master=Tframe,
            text="設定ファイル",
            width=LabelWidth,
            height=LabelHeight,
            corner_radius=8,
            text_font=t_font,
        ).grid(row=3, column=0, pady=5)
        self.tomlurl = ck.CTkEntry(
            master=Tframe,
            width=EntWidth,
            height=EntHeight,
            border_width=2,
            corner_radius=8,
            text_color="black",
            border_color="snow",
            fg_color="snow",
        )
        self.tomlurl.insert(0, tomlurl)
        self.tomlurl.grid(row=3, column=1, pady=5)
        # 行数表示テキスト
        # 設定ファイル変更ボタン--------------------------------------------------------
        self.tomlbutton = ck.CTkButton(
            master=Tframe,
            text="設定ファイル変更",
            command=self.ChangeToml,
            width=BtnWidth,
            height=BtnHeight,
            border_width=2,
            corner_radius=8,
            text_color="snow",
            border_color="snow",
        )
        self.tomlbutton.grid(row=4, column=0, columnspan=2, sticky=tk.N)
        #################################################################################
        # 列名設定フレーム################################################################
        # サイドメニュー内フレーム########################################################
        Tframe2 = tk.Frame(
            self.frame0,
            width=SideWidth,
            height=SideHeight,
            bg="#ecb5f5",
            relief=tk.GROOVE,
        )
        Tframe2.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        ck.CTkLabel(
            master=Tframe2,
            text="出力列名設定",
            width=LabelWidth,
            height=LabelHeight,
            corner_radius=8,
            text_font=t_font,
        ).grid(
            row=0, column=0, sticky=tk.W + tk.E
        )  # フレームテキスト
        thread1 = threading.Thread(target=self.createSC(Tframe2))
        thread1.start()
        #################################################################################
        # サイドメニュー内変換設定フレーム#################################################
        Setframe = tk.Frame(
            self.frame0,
            bg="#ecb5f5",
            relief=tk.GROOVE,
            width=int(5 * wid_Par),
            bd=2,
        )
        Setframe.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        tomlEntries = []
        # テキストボックスの作成と配置
        # Start ####################################################################
        ck.CTkLabel(
            master=Setframe,
            text="日付列番号",
            width=LabelWidth,
            height=LabelHeight,
            corner_radius=8,
            text_font=t_font,
        ).grid(row=0, column=0)
        self.DaySet = ck.CTkEntry(
            master=Setframe,
            width=EntWidth,
            height=EntHeight,
            border_width=2,
            corner_radius=8,
            text_color="black",
            border_color="snow",
            fg_color="snow",
        )
        tomlEntries.append(self.DaySet)
        # tomlインポート------------------------------------------------------------
        try:
            self.TomlInsert(self.DaySet, Banktoml["Setframe"][F_N + "_DaySetList"])
        except:
            self.TomlInsert(self.DaySet, Banktoml["Setframe"]["Nomal_DaySetList"])
        # --------------------------------------------------------------------------
        self.DaySet.bind("<Return>", tomlreturn)
        self.DaySet.bind("<Tab>", tomlreturn)
        self.DaySet.grid(row=0, column=1, padx=5, pady=5)
        # Start ####################################################################
        ck.CTkLabel(
            master=Setframe,
            text="金額表示列番号",
            width=LabelWidth,
            height=LabelHeight,
            corner_radius=8,
            text_font=t_font,
        ).grid(row=1, column=0)
        self.MoneySet = ck.CTkEntry(
            master=Setframe,
            width=EntWidth,
            height=EntHeight,
            border_width=2,
            corner_radius=8,
            text_color="black",
            border_color="snow",
            fg_color="snow",
        )
        tomlEntries.append(self.MoneySet)
        # tomlインポート------------------------------------------------------------
        try:
            self.TomlInsert(self.MoneySet, Banktoml["Setframe"][F_N + "_MoneySet"])
        except:
            self.TomlInsert(self.MoneySet, Banktoml["Setframe"]["Nomal_MoneySet"])
        # --------------------------------------------------------------------------
        self.MoneySet.bind("<Return>", tomlreturn)
        self.MoneySet.bind("<Tab>", tomlreturn)
        self.MoneySet.grid(row=1, column=1, padx=5, pady=5)
        # サイドメニュー内ボタンフレーム###################################################
        frame = tk.Frame(
            self.frame0,
            bg="#ecb5f5",
            relief=tk.GROOVE,
            width=int(5 * wid_Par),
            bd=2,
        )
        # frame.grid(row=0, column=4, sticky=tk.N)
        frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        # 縦直線追加ボタン---------------------------------------------------------------
        button = ck.CTkButton(
            master=frame,
            text="縦直線追加",
            command=lambda: StLine(self.top.forward, CW, CH),
            width=BtnWidth,
            height=BtnHeight,
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
            command=lambda: StWLine(self.top.forward, CW, CH),
            width=BtnWidth,
            height=BtnHeight,
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
            width=BtnWidth,
            height=BtnHeight,
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
            command=lambda: NewLineCreate(self, self.top.forward, HCW, HCH),
            width=BtnWidth,
            height=BtnHeight,
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
            command=lambda: self.AutoNewLineCreate(self.top.forward, HCW, HCH),
            width=BtnWidth,
            height=BtnHeight,
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
            width=int(5 * wid_Par),
            bd=2,
        )
        frame2.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        # 確定ボタン---------------------------------------------------------------
        button4 = ck.CTkButton(
            master=frame2,
            text="確定",
            command=lambda: EnterP(
                self.top.forward, HCW, HCH, self, self.master, self.top, self.ChangeVar
            ),
            width=BtnWidth,
            height=BtnHeight,
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
            width=BtnWidth,
            height=BtnHeight,
            border_width=2,
            corner_radius=8,
            text_color="snow",
            border_color="snow",
            fg_color="gray",
        )
        button6.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W + tk.E)
        # ##############################################################################
        thread2 = threading.Thread(
            target=Gra(self.top.forward, readcsv1, readcsv2, HCW, HCH)
        )
        thread2.start()  # 透過キャンバスに罫線描画
        self.top.wm_attributes("-transparentcolor", "white")  # トップWindowの白色を透過
        # 下Windowのキャンバス作成
        # 画像の配置#####################################################################
        self.InportIMG()
        # ##############################################################################
        Entries = self.Entries
        self.master.attributes("-topmost", True)
        self.master.attributes("-topmost", False)
        self.top.attributes("-topmost", True)
        G_logger.debug("TKINTERCV2Setting_Application起動完了")  # Log出力

    # ----------------------------------------------------------------------------------
    def __del__(self):
        print("インスタンスが破棄されました")

    # 以下self関数##################################################################################
    def RedLine(self, CW, CH):
        """
        縦直線追加ボタン処理
        """
        TName = "Line" + str(len(tagsList) + 1)
        G_logger.debug("縦直線追加ボタン処理開始")  # Log出力
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
    def createSC(self, Tframe2):
        self.SF = SF.ScrollableFrame(Tframe2, CW, CH, bar_x=False)
        self.SF.grid(sticky=tk.W + tk.E)  # , ipadx=500, ipady=100)
        # エントリーウィジェットマネージャを初期化
        self.Entries = []  # エントリーウィジェットのインスタンス
        self.insertEntries = []  # 追加するボタンのようなラベル
        self.removeEntries = []  # 削除するボタンのようなラベル
        # こちらはインデックスマネージャ。ウィジェットの数や並び方を管理
        self.index = 0  # 最新のインデックス番号
        self.indexes = []  # インデックスの並び
        try:
            self.ColList = Banktoml["ColList"][F_N + "_List"]
        except:
            self.ColList = Banktoml["ColList"]["Nomal_List"]
        i = 0
        for ColListItem in self.ColList:
            self.createEntry(i, bar_x=False)
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
        Banktoml["LineSetting"][rep_N] = l_s
        toml_c.dump_toml(Banktoml, tomlurl)
        self.TomlInsert(self.ReplaceStr, Banktoml["LineSetting"][rep_N])
        self.frame0.grid()
        self.topRepFrame.grid_forget()
        G_logger.debug("SideMenutoml変換設定の更新完了")  # Log出力

    # ---------------------------------------------------------------------------------------------

    # ---------------------------------------------------------------------------------------------
    def ChangeToml(self):
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
                G_logger.debug("tomlファイル再読込")  # Log出力
                Main(Master, imgurl, tomlurl, G_logger)
                G_logger.debug("tomlファイル再読込完了")  # Log出力
                print("toml変更")
            else:
                messagebox.showinfo("確認", "設定ファイルを指定してください。")
                self.top.deiconify()
        except:
            G_logger.debug("tomlファイル変更Err")  # Log出力
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
    def InportIMG(self):
        """
        下ウィンドウに画像をリサイズして配置
        """
        global TKimg
        global imgurl
        global CW, CH

        G_logger.debug("下ウィンドウに画像をリサイズして配置開始")  # Log出力
        self.img = Image.open(imgurl)
        self.img = self.img.resize((CW, CH))  # 画像リサイズ
        self.back = tk.Canvas(self.master, background="white", width=CW, height=CH)
        TKimg = ImageTk.PhotoImage(self.img, master=self.back)  # 下Windowに表示する画像オブジェクト
        self.back.create_image(0, 0, image=TKimg, anchor=tk.NW)  # 下Windowのキャンバスに画像挿入
        self.back.pack(side=tk.TOP, fill=tk.BOTH, expand=True)  # 下Windowを配置
        self.bind("<Configure>", self.change)
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

        G_logger.debug("列名設定項目追加ボタン処理開始")  # Log出力
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

        G_logger.debug("列名設定項目削除ボタン処理開始")  # Log出力
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

        G_logger.debug("列名設定項目を再配置開始")  # Log出力
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
        G_logger.debug("列名設定項目を再配置完了")  # Log出力

    # -------------------------------------------------------------------------------------
    def createEntry(self, next, bar_x=False, bar_y=True):
        """
        列名設定項目を作成して再配置
        """

        G_logger.debug("列名設定項目を作成して再配置開始")  # Log出力
        # 最初のエントリーウィジェットを追加
        self.Entries.insert(
            next,
            ck.CTkEntry(
                master=self.SF.scrollable_frame,
                width=EntWidth,
                height=EntHeight,
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
    def GetEntryTextButton_click(self):
        """
        列名設定項目取得関数
        """
        GetEntry = []
        G_logger.debug("列名設定項目取得関数開始")  # Log出力
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
            G_logger.debug("TKINTERCV2SettingClose完了")  # Log出力
        else:
            self.top.deiconify()
            G_logger.debug("TKINTERCV2SettingClose失敗")  # Log出力

    # ---------------------------------------------------------------------------------------------
    def AutoNewLineCreate(self, selfC, HCW, HCH):
        """
        自動直線描画ボタン処理
        """
        unmap(self)
        MSG = messagebox.askokcancel("確認", "自動直線描画しますか？")
        if MSG is True:
            G_logger.debug("新規直線描画処理開始")  # Log出力
            selfC = self.top.forward
            AL = AutoLine(imgurl, 1)
            if AL[0] is True:
                ####################################################################################
                F_N = os.path.splitext(os.path.basename(imgurl))[0]
                Yoko_N = F_N + "_Yoko"
                Tate_N = F_N + "_Tate"
                Banktoml["LineSetting"][Yoko_N] = AL[1]
                Banktoml["LineSetting"][Tate_N] = AL[2]
                toml_c.dump_toml(Banktoml, tomlurl)
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
        Banktoml["ColList"][F_N + "_List"] = TEntries
        toml_c.dump_toml(Banktoml, tomlurl)
        G_logger.debug("toml列名設定の更新完了")  # Log出力
    except:
        G_logger.debug("toml列名設定の更新Err")  # Log出力


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
        Banktoml["Setframe"][F_N + "_DaySetList"] = l_s
    else:
        l_s = DaySet.split(",")
        Banktoml["Setframe"][F_N + "_DaySetList"] = l_s
    # ----------------------------------------------------------
    MoneySet = tomlEntries[1].get()
    if "," not in MoneySet:
        l_s = []
        l_s.append(MoneySet)
        Banktoml["Setframe"][F_N + "_MoneySet"] = l_s
    else:
        l_s = MoneySet.split(",")
        Banktoml["Setframe"][F_N + "_MoneySet"] = l_s
    # ----------------------------------------------------------
    # ReplaceSet = tomlEntries[2].get()
    # if "," not in ReplaceSet:
    #     l_s = []
    #     l_s.append(ReplaceSet)
    #     Banktoml["Setframe"][F_N + "_ReplaceSet"] = l_s
    # else:
    #     l_s = ReplaceSet.split(",")
    #     Banktoml["Setframe"][F_N + "_ReplaceSet"] = l_s
    # ----------------------------------------------------------
    # ReplaceStr = tomlEntries[3].get()
    # if "," not in ReplaceStr:
    #     l_s = []
    #     l_s.append(ReplaceStr)
    #     Banktoml["LineSetting"][rep_N] = l_s
    # else:
    #     l_s = ReplaceStr.split(",")
    #     Banktoml["LineSetting"][rep_N] = l_s
    toml_c.dump_toml(Banktoml, tomlurl)
    G_logger.debug("toml変換設定の更新完了")  # Log出力


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
        G_logger.debug("新規直線描画処理開始")  # Log出力
        SLS = straightlinesetting(imgurl)
        if SLS[0] is True:
            ####################################################################################
            F_N = os.path.splitext(os.path.basename(imgurl))[0]
            Yoko_N = F_N + "_Yoko"
            Tate_N = F_N + "_Tate"
            Banktoml["LineSetting"][Yoko_N] = SLS[1]
            Banktoml["LineSetting"][Tate_N] = SLS[2]
            toml_c.dump_toml(Banktoml, tomlurl)
            ####################################################################################
            AllLineDelete(self, selfC)
            Gra(selfC, SLS[1], SLS[2], HCW, HCH)  # 透過キャンバスに罫線描画
            map(self)
        else:
            G_logger.debug("新規直線描画失敗")  # Log出力
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
    module = Banktoml["DataList"]["Datas"]
    var = tk.StringVar(value=module)
    listbox = tk.Listbox(self, listvariable=var, selectmode="multiple", height=6)
    scrollbar = tk.ttk.Scrollbar(self, orient="vertical", command=listbox.yview)
    listbox["yscrollcommand"] = scrollbar.set
    return listbox, scrollbar


# ---------------------------------------------------------------------------------------------
def LoadImg(Wwidth, Wheight):
    """
    画像ファイル読込
    """
    global MaxW, MaxH
    global imgurl
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
    G_logger.debug("縦直線追加ボタン処理開始")  # Log出力
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
    G_logger.debug("横直線追加ボタン処理開始")  # Log出力
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
    G_logger.debug("透過キャンバス(上ウィンドウ)に罫線描画処理完了")  # Log出力


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

    G_logger.debug("確定ボタンクリック処理開始")  # Log出力
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
                            Banktoml["LineSetting"][Yoko_N] = FYokoList
                            Banktoml["LineSetting"][Tate_N] = FTateList
                            toml_c.dump_toml(Banktoml, tomlurl)
                            ####################################################################################
                            print("csv保存完了")
                            G_logger.debug("縦横リスト書出完了")  # Log出力
                            OM = OCRF.Main(
                                imgurl,
                                FYokoList,
                                FTateList,
                                Banktoml,
                                SGEL,
                                DaySet,
                                MoneySet,
                                "ReplaceSet",
                                "ReplaceStr",
                                G_logger,
                                PBAR,
                                ChangeVar,
                            )
                            if OM[0] is True:
                                Read_Url = str(OM[1])
                                PBAR._target.step(10)
                                PBAR._target.master.destroy()
                                G_logger.debug("GoogleVisionAPI完了")  # Log出力
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
                                    G_logger.debug("次ページ読込開始")  # Log出力
                                    FUL.append(Read_Url)  # 書出しCSVURLリスト
                                    ReturnBack(selfmother)
                                else:
                                    FUL.append(Read_Url)  # 書出しCSVURLリスト
                                    if len(FUL) == 1:
                                        selfmother.top.iconify()  # 透過ウィンドウ最小化
                                        selfmother.master.iconify()  # 下ウィンドウ最小化

                                        PT.Main(
                                            self,
                                            Read_Url,
                                            G_logger,
                                            Mter,
                                            Top,
                                            imgurl,
                                            Banktoml,
                                            tomlurl,
                                        )
                                    else:
                                        RU = OCRF.JoinCSV(FUL)
                                        if RU[0] is True:
                                            Read_Url = RU[1]
                                            selfmother.top.iconify()  # 透過ウィンドウ最小化
                                            selfmother.master.iconify()  # 下ウィンドウ最小化

                                            PT.Main(
                                                self,
                                                Read_Url,
                                                G_logger,
                                                Mter,
                                                Top,
                                                imgurl,
                                                Banktoml,
                                                tomlurl,
                                            )
                                        else:
                                            G_logger.debug("CSV連結後出力失敗")  # Log出力
                            else:
                                G_logger.debug("GoogleVisionAPI抽出失敗")  # Log出力
                                unmap(selfmother)
                                MSG = messagebox.showinfo("抽出失敗", "エラーにより抽出に失敗しました。")
                                map(selfmother)
                        else:
                            G_logger.debug("GoogleVisionAPI抽出中断")  # Log出力
                            messagebox.showinfo("中断", "処理を中断します。")
                            map(selfmother)
                    else:
                        G_logger.debug("先頭ページの列数と設定列名数不一致。")  # Log出力
                        messagebox.showinfo("エラー", "先頭ページの列数と設定列名の数が一致しません。再確認してください。")
                        map(selfmother)
                else:
                    G_logger.debug("GoogleVisionAPI縦軸数と設定列名数不一致。")  # Log出力
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
    G_logger.debug(TName + "_削除完了")  # Log出力
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
        Banktoml["LineSetting"][Yoko_N] = nptag_L[1]
        Banktoml["LineSetting"][Tate_N] = nptag_L[2]
        toml_c.dump_toml(Banktoml, tomlurl)
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
    G_logger.debug(TName + "_縦直線描画処理完了")  # Log出力
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
    G_logger.debug(TName + "_削除完了")  # Log出力
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
        Banktoml["LineSetting"][Yoko_N] = nptag_L[1]
        Banktoml["LineSetting"][Tate_N] = nptag_L[2]
        toml_c.dump_toml(Banktoml, tomlurl)
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
def Main(MUI, US, turl, logger, File_url_List):
    """
    呼出関数
    """
    global Master, imgurl
    global readcsv1, readcsv2
    global URL, G_logger
    global Banktoml, tomlurl
    global FUL, rep_N, F_N

    Master = MUI
    imgurl = US.replace(r"\\\\", r"\\")
    URL = os.getcwd()
    Master.withdraw()
    tomlurl = tomlread()
    G_logger = logger
    FUL = File_url_List

    # toml読込------------------------------------------------------------------------------
    with open(turl, encoding="utf-8") as f:
        Banktoml = toml.load(f)
        print(Banktoml)
    # -----------------------------------------------------------
    try:
        F_N = os.path.splitext(os.path.basename(imgurl))[0]
        Yoko_N = F_N + "_Yoko"
        Tate_N = F_N + "_Tate"
        rep_N = F_N + "_ReplaceStr"
        readcsv1 = Banktoml["LineSetting"][Yoko_N]
        readcsv2 = Banktoml["LineSetting"][Tate_N]
    except:
        print("行列tomlインポートエラー")
        readcsv1 = Banktoml["LineSetting"]["Nomal_Yoko"]
        readcsv2 = Banktoml["LineSetting"]["Nomal_Tate"]

    # root = tk.Tk()  # Window生成
    root = tk.Toplevel()  # Window生成
    data = IconCode.icondata()
    root.tk.call("wm", "iconphoto", root._w, tk.PhotoImage(data=data, master=root))
    app = Application(master=root)
    # --- 基本的な表示準備 ----------------

    app.mainloop()


# ------------------------------------------------------------------------------------------
if __name__ == "__main__":
    import logging.config

    # logger設定-----------------------------------------------------------------------------------------------------
    logging.config.fileConfig(os.getcwd() + r"\LogConf\logging_debug.conf")
    G_logger = logging.getLogger(__name__)
    # ---------------------------------------------------------------------------------------------------------------

    global Banktoml, tomlurl, rep_N, F_N, imgurl
    URL = os.getcwd()
    imgurl = r"D:\OCRTESTPDF\PDFTEST\相続_JA_2page.png"
    # imgurl = r"C:\Users\もちねこ\Desktop\PDFTEST\JA_1page.png"
    tomlurl = tomlread()
    # toml読込------------------------------------------------------------------------------
    with open(tomlurl, encoding="utf-8") as f:
        Banktoml = toml.load(f)
        print(Banktoml)
    # -----------------------------------------------------------
    F_N = os.path.splitext(os.path.basename(imgurl))[0]
    Yoko_N = F_N + "_Yoko"
    Tate_N = F_N + "_Tate"
    rep_N = F_N + "_ReplaceStr"
    try:
        readcsv1 = Banktoml["LineSetting"][Yoko_N]
        readcsv2 = Banktoml["LineSetting"][Tate_N]
    except:
        readcsv1 = Banktoml["LineSetting"]["Nomal_Yoko"]
        readcsv2 = Banktoml["LineSetting"]["Nomal_Tate"]
    COLArray = True, readcsv1, readcsv2

    # Windowについて : https://kuroro.blog/python/116yLvTkzH2AUJj8FHLx/
    root = tk.Tk()  # Window生成
    data = IconCode.icondata()
    root.tk.call("wm", "iconphoto", root._w, tk.PhotoImage(data=data, master=root))
    app = Application(master=root)
    # frame = tk.Frame(root, height=3840, width=3840)  # frame生成
    # --- 基本的な表示準備 ----------------

    app.mainloop()
