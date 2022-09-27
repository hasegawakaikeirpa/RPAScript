import tkinter as tk
import csv
from PIL import Image, ImageTk

# import subprocess

from tkinter import messagebox
import os

import OCRFlow as OCRF

# from OCRFlow import Main
import toml

# from tkinter import ttk
import DataGrid as DG

# import CV2Setting as CV2S
from CV2Setting import straightlinesetting
import ScrollableFrame as SF
import tomlCreate as toml_c

# from tkinter import filedialog

###################################################################################################
class Application(tk.Frame):
    def __init__(self, master=None):
        global TKimg  # 画像オブジェクト用グローバル変数
        global txt
        global CW, CH
        global Banktoml
        global Entries
        global tomlEntries
        # Windowの初期設定を行う。
        super().__init__(master)
        # Windowの画面サイズを設定する。
        G_logger.debug("TKINTERCV2Setting_Application起動")  # Log出力
        # geometryについて : https://kuroro.blog/python/rozH3S2CYE0a0nB3s2QL/
        self.master.geometry("1480x750+0+0")  # Window表示位置指定
        # 画像の読込#####################################################################
        # 透過キャンバスの画像範囲検出の為リサイズ比率等を算出
        print(self.master.geometry())
        W = self.master.geometry().split("x")
        Wwidth = int(1480 * 0.8)  # int(W[0]) * 0.7
        W = W[1].split("+")
        Wheight = int(750 * 0.8)  # int(W[0]) * 0.7
        IR = LoadImg(Wwidth, Wheight)
        CW, CH, HCW, HCH, TKimg = IR[0], IR[1], IR[2], IR[3], IR[4]
        # ##############################################################################
        self.top = tk.Toplevel()  # サブWindow作成
        self.top.bind("<Motion>", self.change)  # 透過ウィンドウにマウス移動関数bind
        self.master.bind("<Motion>", self.change)  # 下ウィンドウにマウス移動関数bind
        self.top.protocol("WM_DELETE_WINDOW", self.click_close)  # 閉じる処理設定
        self.master.protocol("WM_DELETE_WINDOW", self.click_close)  # 閉じる処理設定
        self.top.wm_attributes("-topmost", True)  # 常に一番上のウィンドウに指定
        # self.top.overrideredirect(True)  # ウィンドウのタイトル部分を消去
        self.top.geometry("1480x750+0+0")  # トップWindow表示位置指定
        # 透過キャンバスフレーム##########################################################
        self.topFrame = tk.Frame(
            self.top,
            bg="snow",
            height=CH,
            width=CW,
            relief=tk.GROOVE,
            bd=2,
        )
        self.topFrame.grid(row=0, column=0, sticky=tk.N)
        # self.topFrame.pack(side=tk.LEFT, anchor=tk.N)
        self.top.forward = tk.Canvas(
            self.topFrame, background="white", width=CW, height=CH
        )  # 透過キャンバス作成
        # self.top.forward.pack(side=tk.LEFT, anchor=tk.N)  # 透過キャンバスを配置
        self.top.forward.grid(row=0, column=0)
        # ##############################################################################
        # 配置
        # サイドメニューフレーム##########################################################
        self.frame0 = tk.Frame(
            self.top,
            bg="snow",
            width=5,
            bd=2,
            relief=tk.GROOVE,
        )
        self.frame0.grid(row=0, column=1, sticky=tk.N)
        # self.frame0.pack(side=tk.RIGHT, anchor=tk.N)
        self.frame0.propagate(0)
        #################################################################################
        # サイドメニュー内フレーム########################################################
        Tframe = tk.Frame(
            self.frame0,
            bg="gray94",
            bd=2,
            relief=tk.GROOVE,
        )
        Tframe.grid(sticky=tk.W + tk.E)
        # LineNo表示テキスト
        tk.Label(Tframe, text="選択ライン名").grid(row=0, column=0)  # 位置指定
        # テキストボックスの作成と配置
        txt = tk.Entry(Tframe, width=30)
        txt.grid(row=0, column=1)
        # 行数表示テキスト
        tk.Label(Tframe, text="元帳日付列名").grid(row=1, column=0)  # 位置指定
        self.LimitCol = tk.Entry(Tframe, width=30, bg="snow")
        self.LimitCol.insert(0, "伝票日付")
        self.LimitCol.grid(row=1, column=1)
        # 行数表示テキスト
        tk.Label(Tframe, text="設定ファイル").grid(row=2, column=0)  # 位置指定
        self.tomlurl = tk.Entry(Tframe, width=30, bg="snow")
        self.tomlurl.insert(0, tomlurl)
        self.tomlurl.grid(row=2, column=1)
        # 行数表示テキスト
        # 設定ファイル変更ボタン--------------------------------------------------------
        self.tomlbutton = tk.Button(
            # self.top,
            Tframe,
            text="設定ファイル変更",
            fg="White",
            command=self.ChangeToml,
            bg="gray",
            font=1,
            width=23,
            height=1,
        )  # ボタン作成
        self.tomlbutton.grid(row=3, column=0, columnspan=2, sticky=tk.N)
        #################################################################################
        # 列名設定フレーム################################################################
        tk.Label(self.frame0, text="出力列名設定").grid(
            row=1, column=0, sticky=tk.W + tk.E
        )  # フレームテキスト
        self.SF = SF.ScrollableFrame(self.frame0, CW, bar_x=False)
        self.SF.grid(sticky=tk.W + tk.E)  # , ipadx=500, ipady=100)
        # エントリーウィジェットマネージャを初期化
        self.Entries = []  # エントリーウィジェットのインスタンス
        self.insertEntries = []  # 追加するボタンのようなラベル
        self.removeEntries = []  # 削除するボタンのようなラベル
        # こちらはインデックスマネージャ。ウィジェットの数や並び方を管理
        self.index = 0  # 最新のインデックス番号
        self.indexes = []  # インデックスの並び
        # self.createEntry(0, bar_x=False)
        self.ColList = Banktoml["ColList"]["List"]
        i = 0
        for ColListItem in self.ColList:
            self.createEntry(i, bar_x=False)
            self.Entries[i].insert(0, ColListItem)
            i += 1
        #################################################################################
        # サイドメニュー内変換設定フレーム#################################################
        Setframe = tk.Frame(
            self.frame0,
            bg="gray94",
            relief=tk.GROOVE,
            width=5,
            bd=2,
        )
        Setframe.grid(sticky=tk.W + tk.E)
        tomlEntries = []
        # テキストボックスの作成と配置
        tk.Label(Setframe, text="日付列番号").grid(row=0, column=0)  # 位置指定
        self.DaySet = tk.Entry(Setframe, width=30, bg="snow")
        tomlEntries.append(self.DaySet)
        self.TomlInsert(self.DaySet, Banktoml["Setframe"]["DaySetList"])
        # self.DaySet.insert(0, Banktoml["Setframe"]["DaySetList"])
        self.DaySet.bind("<Return>", tomlreturn)
        self.DaySet.bind("<Tab>", tomlreturn)
        self.DaySet.grid(row=0, column=1)
        tk.Label(Setframe, text="金額表示列番号").grid(row=1, column=0)  # 位置指定
        self.MoneySet = tk.Entry(Setframe, width=30, bg="snow")
        tomlEntries.append(self.MoneySet)
        self.TomlInsert(self.MoneySet, Banktoml["Setframe"]["MoneySet"])
        # self.MoneySet.insert(0, Banktoml["Setframe"]["MoneySet"])
        self.MoneySet.bind("<Return>", tomlreturn)
        self.MoneySet.bind("<Tab>", tomlreturn)
        self.MoneySet.grid(row=1, column=1)
        tk.Label(Setframe, text="置換対象列番号").grid(row=2, column=0)  # 位置指定
        self.ReplaceSet = tk.Entry(Setframe, width=30, bg="snow")
        tomlEntries.append(self.ReplaceSet)
        self.TomlInsert(self.ReplaceSet, Banktoml["Setframe"]["ReplaceSet"])
        # self.ReplaceSet.insert(0, Banktoml["Setframe"]["ReplaceSet"])
        self.ReplaceSet.bind("<Return>", tomlreturn)
        self.ReplaceSet.bind("<Tab>", tomlreturn)
        self.ReplaceSet.grid(row=2, column=1)
        tk.Label(Setframe, text="置換対象文字列").grid(row=3, column=0)  # 位置指定
        self.ReplaceStr = tk.Entry(Setframe, width=30, bg="snow")
        tomlEntries.append(self.ReplaceStr)
        self.TomlInsert(self.ReplaceStr, Banktoml["Setframe"]["ReplaceStr"])
        # self.ReplaceStr.insert(0, Banktoml["Setframe"]["ReplaceStr"])
        self.ReplaceStr.bind("<Return>", tomlreturn)
        self.ReplaceStr.bind("<Tab>", tomlreturn)
        self.ReplaceStr.bind("<Double-1>", self.tomlFrameOpen)

        self.ReplaceStr.grid(row=3, column=1)
        #################################################################################
        # サイドメニュー内ボタンフレーム###################################################
        frame = tk.Frame(
            self.frame0,
            bg="gray94",
            relief=tk.GROOVE,
            width=5,
            bd=2,
        )
        frame.grid(sticky=tk.W + tk.E)
        # frame.pack(side=tk.TOP, pady=50, padx=10, anchor=tk.E)
        BW = 25  # ボタン横幅
        BH = 1  # ボタン縦幅
        fonts = ("", 16)  # ボタンフォントの設定
        # 縦直線追加ボタン---------------------------------------------------------------
        button = tk.Button(
            # self.top,
            frame,
            text="縦直線追加",
            fg="White",
            command=lambda: StLine(self.top.forward, CW, CH),
            bg="tomato",
            font=fonts,
            width=BW,
            height=BH,
        )  # ボタン作成
        button.grid(row=0, column=0, sticky=tk.N)
        # 横直線追加ボタン---------------------------------------------------------------
        button2 = tk.Button(
            # self.top,
            frame,
            text="横直線追加",
            fg="White",
            command=lambda: StWLine(self.top.forward, CW, CH),
            bg="seagreen3",
            font=fonts,
            width=BW,
            height=BH,
        )  # ボタン作成
        button2.grid(row=1, column=0, sticky=tk.N)
        # 削除ボタン---------------------------------------------------------------
        button5 = tk.Button(
            # self.top,
            frame,
            text="選択直線削除",
            fg="White",
            command=lambda: LineDelete(self.top.forward),
            bg="Orange",
            font=fonts,
            width=BW,
            height=BH,
        )  # ボタン作成
        button5.grid(row=2, column=0, sticky=tk.N)
        # 新規直線描画ボタン---------------------------------------------------------------
        button3 = tk.Button(
            # self.top,
            frame,
            text="新規直線描画",
            fg="White",
            command=lambda: NewLineCreate(self, self.top.forward, HCW, HCH),
            bg="mediumPurple",
            font=fonts,
            width=BW,
            height=BH,
        )  # ボタン作成
        button3.grid(row=3, column=0, sticky=tk.N)
        # 置換ボタン---------------------------------------------------------------
        button7 = tk.Button(
            # self.top,
            frame,
            text="置換対象文字列設定",
            fg="White",
            command=lambda: self.tomlFrameOpen(self),
            bg="hotpink1",
            font=fonts,
            width=BW,
            height=BH,
        )  # ボタン作成
        button7.grid(row=4, column=0, sticky=tk.N)
        # 確定ボタン---------------------------------------------------------------
        button4 = tk.Button(
            # self.top,
            frame,
            text="確定",
            fg="White",
            command=lambda: EnterP(self.top.forward, HCW, HCH, self),
            bg="steelblue3",
            font=fonts,
            width=BW,
            height=BH,
        )  # ボタン作成
        button4.grid(row=5, column=0, sticky=tk.N)
        # 戻るボタン---------------------------------------------------------------
        button6 = tk.Button(
            # self.top,
            frame,
            text="戻る",
            fg="White",
            command=lambda: ReturnBack(self),
            bg="gray",
            font=fonts,
            width=BW,
            height=BH,
        )  # ボタン作成
        button6.grid(row=6, column=0, sticky=tk.N)
        # ##############################################################################
        Gra(self.top.forward, readcsv1, readcsv2, HCW, HCH)  # 透過キャンバスに罫線描画
        self.top.wm_attributes("-transparentcolor", "white")  # トップWindowの白色を透過
        # 下Windowのキャンバス作成
        # 画像の配置#####################################################################
        self.InportIMG()
        # ##############################################################################
        Entries = self.Entries
        G_logger.debug("TKINTERCV2Setting_Application起動完了")  # Log出力

    # 以下self関数###################################################################################
    def tomlFrameOpen(self, event):
        """
        置換設定隠しサイドメニューの表示
        """
        MSG = messagebox.askokcancel("確認", "置換設定ウィンドウを起動します。")
        if MSG is True:
            # self.topFrame.grid_remove()
            self.frame0.grid_remove()
            print(self.top.geometry())
            CWgeo = int(self.top.geometry().split("x")[0])
            CHgeo = int(self.top.geometry().split("x")[1].split("+")[0])
            self.topRepFrame = tk.Frame(
                self.top,
                bg="snow",
                height=CHgeo,
                width=CWgeo,
                relief=tk.GROOVE,
                bd=2,
            )
            self.BRS = Banktoml["Setframe"]["ReplaceStr"]
            self.topRepFrame.grid(
                row=0, column=1, sticky=tk.NSEW
            )  # , ipadx=500, ipady=100)
            self.topRepSF = SF.SubScrollableFrame(
                self.topRepFrame, CWgeo, CHgeo, len(self.BRS), bar_x=False
            )
            self.topRepSF.grid(row=0, column=0, sticky=tk.W)  # , ipadx=500, ipady=100)
            self.BRSTxt = []
            self.BRSPlus = []
            self.BRSDel = []
            i = 0
            for BRSItem in self.BRS:
                if len(self.BRS) == 1:
                    # テキストボックス----------------------------------------------------
                    txt = tk.Entry(self.topRepSF.scrollable_frame, width=35, bg="snow")
                    txt.insert(0, BRSItem)
                    txt.bind("<MouseWheel>", self.topRepSF.mouse_y_scroll)
                    txt.grid(row=i, column=0, sticky=tk.W)
                    self.BRSTxt.insert(i, txt)
                    # -------------------------------------------------------------------
                else:
                    # テキストボックス----------------------------------------------------
                    txt = tk.Entry(self.topRepSF.scrollable_frame, width=35, bg="snow")
                    txt.insert(0, BRSItem)
                    txt.bind("<MouseWheel>", self.topRepSF.mouse_y_scroll)
                    txt.grid(row=i, column=0, sticky=tk.W)
                    self.BRSTxt.insert(i, txt)
                    # -------------------------------------------------------------------
                    # ボタン--------------------------------------------------------------
                    btn = tk.Label(
                        self.topRepSF.scrollable_frame,
                        text="+",
                        fg="#33ff33",
                        font=("Arial Black", 20),
                    )
                    # 追加するボタンのようなラベルにクリックイベントを設定
                    btn.bind(
                        "<1>",
                        lambda event, id=self.index: self.tomlFrameOpen_click(
                            event, "+"
                        ),
                    )
                    btn.grid(row=i, column=1)
                    self.BRSPlus.insert(i, btn)
                    # -------------------------------------------------------------------
                    # ボタン--------------------------------------------------------------
                    btn = tk.Label(
                        self.topRepSF.scrollable_frame,
                        text="−",
                        fg="#ff3333",
                        font=("Arial Black", 20),
                    )
                    # 追加するボタンのようなラベルにクリックイベントを設定
                    btn.bind(
                        "<1>",
                        lambda event, id=self.index: self.tomlFrameOpen_click(
                            event, "−"
                        ),
                    )
                    btn.grid(row=i, column=2)
                    self.BRSDel.insert(i, btn)
                    # -------------------------------------------------------------------
                i += 1
            # 確定ボタン--------------------------------------------------------------
            btn = tk.Button(
                self.topRepFrame,
                text="確定",
                fg="Snow",
                command=self.tomlFrameClose,
                height=2,
                bg="Gray",
                font=("Arial Black", 10),
            )
            btn.grid(row=1, column=0, columnspan=3, sticky=tk.NSEW)

    # ---------------------------------------------------------------------------------------------
    def tomlFrameClose(self):
        """
        SideMenutoml変換設定の更新
        """
        l_s = []
        for B_t in self.BRSTxt:
            l_s.append(B_t.get())
        Banktoml["Setframe"]["ReplaceStr"] = l_s
        toml_c.dump_toml(Banktoml, tomlurl)
        self.TomlInsert(self.ReplaceStr, Banktoml["Setframe"]["ReplaceStr"])
        self.frame0.grid()
        self.topRepFrame.grid_forget()
        G_logger.debug("SideMenutoml変換設定の更新完了")  # Log出力

    # ---------------------------------------------------------------------------------------------
    def tomlFrameOpen_click(self, event, Fl):
        """
        置換設定隠しサイドメニューのボタンクリック関数
        """
        w_Name = event.widget._name
        if Fl == "−":
            b = 0
            for B_i in self.BRSDel:
                if B_i._name == w_Name:
                    self.BRSTxt[b].destroy()
                    self.BRSPlus[b].destroy()
                    self.BRSDel[b].destroy()
                    self.BRSTxt.pop(b)
                    self.BRSPlus.pop(b)
                    self.BRSDel.pop(b)
                b += 1
        elif Fl == "+":
            if len(self.BRS) == 1:
                i = len(self.BRSTxt)
                # テキストボックス----------------------------------------------------
                txt = tk.Entry(self.topRepSF.scrollable_frame, width=35, bg="snow")
                txt.insert(0, "")
                txt.bind("<MouseWheel>", self.topRepSF.mouse_y_scroll)
                txt.grid(row=i, column=0, sticky=tk.W)
                self.BRSTxt.insert(i, txt)
                # -------------------------------------------------------------------
                # ボタン--------------------------------------------------------------
                btn = tk.Label(
                    self.topRepSF.scrollable_frame,
                    text="+",
                    fg="#33ff33",
                    font=("Arial Black", 20),
                )
                # 追加するボタンのようなラベルにクリックイベントを設定
                btn.bind(
                    "<1>",
                    lambda event, id=self.index: self.tomlFrameOpen_click(event, "+"),
                )
                btn.grid(row=i, column=1)
                self.BRSPlus.insert(i, btn)
                # -------------------------------------------------------------------
                # ボタン--------------------------------------------------------------
                btn = tk.Label(
                    self.topRepSF.scrollable_frame,
                    text="−",
                    fg="#ff3333",
                    font=("Arial Black", 20),
                )
                # 追加するボタンのようなラベルにクリックイベントを設定
                btn.bind(
                    "<1>",
                    lambda event, id=self.index: self.tomlFrameOpen_click(event, "−"),
                )
                btn.grid(row=i, column=2)
                self.BRSDel.insert(i, btn)
            else:
                i = len(self.BRSTxt)
                # テキストボックス----------------------------------------------------
                txt = tk.Entry(self.topRepSF.scrollable_frame, width=35, bg="snow")
                txt.insert(0, "")
                txt.bind("<MouseWheel>", self.topRepSF.mouse_y_scroll)
                txt.grid(row=i, column=0)
                self.BRSTxt.insert(i, txt)
                # -------------------------------------------------------------------
                # ボタン--------------------------------------------------------------
                btn = tk.Label(
                    self.topRepSF.scrollable_frame,
                    text="+",
                    fg="#33ff33",
                    font=("Arial Black", 20),
                )
                # 追加するボタンのようなラベルにクリックイベントを設定
                btn.bind(
                    "<1>",
                    lambda event, id=self.index: self.tomlFrameOpen_click(event, "+"),
                )
                btn.grid(row=i, column=1)
                self.BRSPlus.insert(i, btn)
                # -------------------------------------------------------------------
                # ボタン--------------------------------------------------------------
                btn = tk.Label(
                    self.topRepSF.scrollable_frame,
                    text="−",
                    fg="#ff3333",
                    font=("Arial Black", 20),
                )
                # 追加するボタンのようなラベルにクリックイベントを設定
                btn.bind(
                    "<1>",
                    lambda event, id=self.index: self.tomlFrameOpen_click(event, "−"),
                )
                btn.grid(row=i, column=2)
                self.BRSDel.insert(i, btn)

    # ---------------------------------------------------------------------------------------------
    def ChangeToml(self):
        """
        tomlリストを変更
        """
        try:
            typ = [("tomlファイル", "*.toml")]
            self.top.withdraw()
            tomlurl = tk.filedialog.askopenfilename(filetypes=typ)
            if tomlurl != "":
                self.master.destroy()
                self.top.destroy()
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
        img = Image.open(imgurl)
        img = img.resize((CW, CH))  # 画像リサイズ
        self.back = tk.Canvas(self.master, background="white", width=CW, height=CH)
        TKimg = ImageTk.PhotoImage(img, master=self.back)  # 下Windowに表示する画像オブジェクト
        self.back.create_image(0, 0, image=TKimg, anchor=tk.NW)  # 下Windowのキャンバスに画像挿入
        self.back.pack(side=tk.LEFT, anchor=tk.N)  # 下Windowを配置
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
        # next = self.indexes.index(id) + 1
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
        # current = self.indexes.index(id)
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
            self.Entries[i].grid(column=0, row=i)
            self.Entries[i].bind("<MouseWheel>", self.SF.mouse_y_scroll)
            self.Entries[i].bind("<Return>", ColumnTomlIn)
            self.Entries[i].bind("<Tab>", ColumnTomlIn)
            self.Entries[i].lift()
            self.insertEntries[i].grid(column=1, row=i)
            self.insertEntries[i].bind("<MouseWheel>", self.SF.mouse_y_scroll)
            self.removeEntries[i].grid(column=2, row=i)
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
            next, tk.Entry(self.SF.scrollable_frame, width=35, bg="snow")
        )
        # エントリーウィジェットを追加するボタンのようなラベルを作成
        self.insertEntries.insert(
            next,
            tk.Label(
                self.SF.scrollable_frame,
                text="+",
                fg="#33ff33",
                font=("Arial Black", 20),
            ),
        )
        # エントリーウィジェットを削除するボタンのようなラベルを作成（初期の段階では表示しない）
        self.removeEntries.insert(
            next,
            tk.Label(
                self.SF.scrollable_frame,
                text="−",
                fg="#ff3333",
                font=("Arial Black", 20),
            ),
        )
        # 追加するボタンのようなラベルにクリックイベントを設定
        self.insertEntries[next].bind(
            "<1>", lambda event, id=self.index: self.insertEntry_click(event, id)
        )
        # 削除するボタンのようなラベルにクリックイベントを設定
        self.removeEntries[next].bind(
            "<1>", lambda event, id=self.index: self.removeEntry_click(event, id)
        )
        # インデックスマネージャに登録
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
        Banktoml["ColList"]["List"] = TEntries
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
        Banktoml["Setframe"]["DaySetList"] = l_s
    else:
        l_s = DaySet.split(",")
        Banktoml["Setframe"]["DaySetList"] = l_s
    # ----------------------------------------------------------
    MoneySet = tomlEntries[1].get()
    if "," not in MoneySet:
        l_s = []
        l_s.append(MoneySet)
        Banktoml["Setframe"]["MoneySet"] = l_s
    else:
        l_s = MoneySet.split(",")
        Banktoml["Setframe"]["MoneySet"] = l_s
    # ----------------------------------------------------------
    ReplaceSet = tomlEntries[2].get()
    if "," not in ReplaceSet:
        l_s = []
        l_s.append(ReplaceSet)
        Banktoml["Setframe"]["ReplaceSet"] = l_s
    else:
        l_s = ReplaceSet.split(",")
        Banktoml["Setframe"]["ReplaceSet"] = l_s
    # ----------------------------------------------------------
    ReplaceStr = tomlEntries[3].get()
    if "," not in ReplaceStr:
        l_s = []
        l_s.append(ReplaceStr)
        Banktoml["Setframe"]["ReplaceStr"] = l_s
    else:
        l_s = ReplaceStr.split(",")
        Banktoml["Setframe"]["ReplaceStr"] = l_s
    toml_c.dump_toml(Banktoml, tomlurl)
    G_logger.debug("toml変換設定の更新完了")  # Log出力


# ---------------------------------------------------------------------------------------------
def ReturnNext(self):
    """
    次UI起動
    """
    self.top.withdraw()
    self.master.withdraw()
    # Master.deiconify()
    # root.destroy()


# ---------------------------------------------------------------------------------------------
def ReturnBack(self):
    """
    前UI起動
    """
    self.top.destroy()
    self.master.destroy()
    Master.deiconify()
    # root.destroy()


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
            with open(
                URL + r"\StraightListYoko.csv",
                "w",
                newline="",
            ) as file:
                writer = csv.writer(file)
                writer.writerow(SLS[1])
            with open(
                URL + r"\StraightListTate.csv",
                "w",
                newline="",
            ) as file:
                writer = csv.writer(file)
                writer.writerow(SLS[2])
            ####################################################################################
            AllLineDelete(selfC)
            tagsList = []
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
    # 画像を指定
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
        width=5,
        fill="#FF0000",
        activefill="#DBDD6F",
    )
    canvastop.tag_bind(TName, "<ButtonPress-1>", click1)
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
        width=5,
        fill="#00FF40",
        activefill="#DBDD6F",
    )
    canvastop.tag_bind(TName, "<ButtonPress-1>", click1)
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
        canvas.create_line(
            ripar0,
            ripar1,
            ripar2,
            ripar3,
            tags=TName,
            width=5,
            fill="#FF0000",
            activefill="#DBDD6F",
        )
        canvas.tag_bind(TName, "<ButtonPress-1>", click1)
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
            width=5,
            fill="#00FF40",
            activefill="#DBDD6F",
        )
        canvas.tag_bind(TName, "<ButtonPress-1>", click1)
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
def EnterP(self, HCW, HCH, selfmother):
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
    ReplaceSet = selfmother.ReplaceSet.get()
    ReplaceStr = selfmother.ReplaceStr.get()
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
    if "," in ReplaceSet:
        ReplaceSet = ReplaceSet.split(",")
    elif " " in ReplaceSet:
        ReplaceSet = ReplaceSet.split(" ")
    else:
        ReplaceSet = list(ReplaceSet)
    # --------------------------------------------------------
    if "," in ReplaceStr:
        ReplaceStr = ReplaceStr.split(",")
    elif " " in ReplaceStr:
        ReplaceStr = ReplaceStr.split(" ")
    else:
        ReplaceStr = list(ReplaceStr)
    # ------------------------------------------------------
    # 条件テキストボックスの内容で処理分け-------------------------------------------------------------------
    if listintCheck(DaySet) is False:
        messagebox.showinfo("エラー", "日付列番号が不正です。数値以外を指定していないか確認してください。")
    elif listintCheck(MoneySet) is False:
        messagebox.showinfo("エラー", "金額表示列番号が不正です。数値以外を指定していないか確認してください。")
    elif listintCheck(ReplaceSet) is False:
        messagebox.showinfo("エラー", "置換対象列番号が不正です。数値以外を指定していないか確認してください。")
    else:
        for tagsListItem in tagsList:
            BB = self.bbox(tagsListItem[0][0])
            BBS = [BB[0], BB[1], BB[2], BB[3]]
            FList.append([tagsListItem[0], tagsListItem[1], BBS])
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
        # メッセージボックス（OK・キャンセル）
        unmap(selfmother)
        if len(FYokoList) == len(SGEL):
            MSG = messagebox.askokcancel("確認", str(SGEL) + "の列名で出力します。")
            if MSG is True:
                map(selfmother)
                ####################################################################################
                with open(
                    URL + r"\StraightListYoko.csv",
                    "w",
                    newline="",
                ) as file:
                    writer = csv.writer(file)
                    writer.writerow(FYokoList)
                with open(
                    URL + r"\StraightListTate.csv",
                    "w",
                    newline="",
                ) as file:
                    writer = csv.writer(file)
                    writer.writerow(FTateList)
                ####################################################################################
                print("csv保存完了")
                G_logger.debug("縦横リスト書出完了")  # Log出力
                OM = OCRF.Main(
                    imgurl,
                    FYokoList,
                    FTateList,
                    Banktoml,
                    SGEL,
                    MoneySet,
                    ReplaceSet,
                    ReplaceStr,
                    G_logger,
                )
            if OM[0] is True:
                G_logger.debug("GoogleVisionAPI完了")  # Log出力
                unmap(selfmother)
                MSG = tk.messagebox.showinfo("抽出完了", str(OM[1]) + "_に保存しました。")
                Viw = tk.messagebox.askokcancel(
                    "確認", "抽出内容を表示いたしますか？\n初めにミロクから出力した仕訳CSVを指定してください。"
                )
                map(selfmother)
                if Viw is True:
                    ReturnNext(selfmother)
                    csvurl = imgurl.replace(".png", ".csv")
                    DG.Main(
                        csvurl,
                        Banktoml,
                        self.tomlurl,
                        DaySet,
                        MoneySet,
                        ReplaceSet,
                        ReplaceStr,
                        SGEL,
                        selfmother.master,
                    )
            else:
                G_logger.debug("GoogleVisionAPI抽出中断")  # Log出力
                unmap(selfmother)
                MSG = tk.messagebox.showinfo("抽出失敗", "エラーにより抽出に失敗しました。")
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
    TName = "Line" + str(id1[0])
    self.delete(TName)
    G_logger.debug(TName + "_削除完了")  # Log出力
    r = 0
    for tagsListItem in tagsList:
        if TName == tagsListItem[0][0]:
            tagsList.pop(r)
            break
        r += 1


# ---------------------------------------------------------------------------------------------
def AllLineDelete(self):
    """
    選択直線の削除
    """
    global tagsList
    for tagsListItem in tagsList:
        self.delete(tagsListItem[0][0])


# ---------------------------------------------------------------------------------------------
# 円、矩形、直線を描画＆ドラッグできるようにする【tkinter】
# https://irohaplat.com/python-tkinter-line-rectangle-oval-drag-and-drop-sample/
def click1(event):
    """
    縦直線描画処理(画面クリック)
    """
    # https://office54.net/python/tkinter/tkinter-bind-event#section2
    global x1
    global y1
    global id1
    txt.delete(0, tk.END)
    x2 = event.x
    y2 = event.y
    id1 = event.widget.find_closest(x2, y2)
    TName = "Line" + str(id1[0])
    G_logger.debug(TName + "_縦直線描画処理完了")  # Log出力
    txt.insert(tk.END, TName)
    x1 = x2
    y1 = y2


# ---------------------------------------------------------------------------------------------
def drag1(event):
    """
    縦直線移動処理(ドラッグ)
    """
    # https://office54.net/python/tkinter/tkinter-bind-event#section2
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
def Main(MUI, US, turl, logger):
    """
    呼出関数
    """
    global Master, imgurl
    global readcsv1, readcsv2
    global URL, G_logger
    global Banktoml, tomlurl

    Master = MUI
    imgurl = US.replace(r"\\\\", r"\\")
    URL = os.getcwd()
    Master.withdraw()
    tomlurl = turl
    G_logger = logger
    # imgurl = URL + r"\TKInterGUI\OCR0.png"
    # toml読込------------------------------------------------------------------------------
    with open(turl, encoding="utf-8") as f:
        Banktoml = toml.load(f)
        print(Banktoml)
    # -----------------------------------------------------------
    try:
        readcsv1 = []
        with open(
            URL + r"\StraightListYoko.csv",
            "r",
            newline="",
        ) as inputfile:
            for row in csv.reader(inputfile):
                for rowItem in row:
                    rsp = (
                        rowItem.replace("[", "")
                        .replace("]", "")
                        .replace(" ", "")
                        .split(",")
                    )
                    readcsv1.append(
                        [int(rsp[0]), int(rsp[1]), int(rsp[2]), int(rsp[3])]
                    )
        readcsv2 = []
        with open(
            URL + r"\StraightListTate.csv",
            "r",
            newline="",
        ) as inputfile:
            for row in csv.reader(inputfile):
                for rowItem in row:
                    rsp = (
                        rowItem.replace("[", "")
                        .replace("]", "")
                        .replace(" ", "")
                        .split(",")
                    )
                    readcsv2.append(
                        [int(rsp[0]), int(rsp[1]), int(rsp[2]), int(rsp[3])]
                    )
    except:
        print("行列CSVインポートエラー")
        readcsv1 = []
        readcsv2 = []
    # Windowについて : https://kuroro.blog/python/116yLvTkzH2AUJj8FHLx/
    root = tk.Tk()  # Window生成
    app = Application(master=root)
    # frame = tk.Frame(root, height=3840, width=3840)  # frame生成
    # --- 基本的な表示準備 ----------------

    app.mainloop()


# ------------------------------------------------------------------------------------------
if __name__ == "__main__":
    import logging.config

    # logger設定-----------------------------------------------------------------------------------------------------
    logging.config.fileConfig(os.getcwd() + r"\LogConf\logging_debug.conf")
    G_logger = logging.getLogger(__name__)
    # ---------------------------------------------------------------------------------------------------------------

    global Banktoml, tomlurl
    URL = os.getcwd()
    imgurl = r"D:\OCRTESTPDF\PDFTEST\Hirogin_1page.png"
    tomlurl = r"D:\OCRTESTPDF\PDFTEST\Setting.toml"
    # toml読込------------------------------------------------------------------------------
    with open(tomlurl, encoding="utf-8") as f:
        Banktoml = toml.load(f)
        print(Banktoml)
    # -----------------------------------------------------------
    readcsv1 = []
    with open(
        URL + r"\TKInterGUI\StraightListYoko.csv",
        "r",
        newline="",
    ) as inputfile:
        for row in csv.reader(inputfile):
            for rowItem in row:
                rsp = (
                    rowItem.replace("[", "")
                    .replace("]", "")
                    .replace(" ", "")
                    .split(",")
                )
                readcsv1.append([int(rsp[0]), int(rsp[1]), int(rsp[2]), int(rsp[3])])
    readcsv2 = []
    with open(
        URL + r"\TKInterGUI\StraightListTate.csv",
        "r",
        newline="",
    ) as inputfile:
        for row in csv.reader(inputfile):
            for rowItem in row:
                rsp = (
                    rowItem.replace("[", "")
                    .replace("]", "")
                    .replace(" ", "")
                    .split(",")
                )
                readcsv2.append([int(rsp[0]), int(rsp[1]), int(rsp[2]), int(rsp[3])])
    COLArray = True, readcsv1, readcsv2

    # Windowについて : https://kuroro.blog/python/116yLvTkzH2AUJj8FHLx/
    root = tk.Tk()  # Window生成
    app = Application(master=root)
    # frame = tk.Frame(root, height=3840, width=3840)  # frame生成
    # --- 基本的な表示準備 ----------------

    app.mainloop()
