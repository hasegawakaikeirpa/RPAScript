import tkinter as tk
import csv
from PIL import Image, ImageTk
from tkinter import messagebox
import os

from pyparsing import col
import OCRFlow as OCRF
import toml
from tkinter import ttk
import CV2Setting as CV2S
import DataGrid as DG
import ScrollableFrame as SF

###################################################################################################
class Application(tk.Frame):
    def __init__(self, master=None):
        global TKimg  # 画像オブジェクト用グローバル変数
        global txt
        global CW, CH

        # Windowの初期設定を行う。
        super().__init__(master)
        # Windowの画面サイズを設定する。
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
        self.top.wm_attributes("-topmost", True)  # 常に一番上のウィンドウに指定
        # self.top.overrideredirect(True)  # ウィンドウのタイトル部分を消去
        self.top.geometry("1480x750+0+0")  # トップWindow表示位置指定
        # 透過キャンバスフレーム##########################################################
        self.topFrame = tk.Frame(
            self.top,
            bg="White",
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
        frame0 = tk.Frame(
            self.top,
            bg="white",
            width=5,
            bd=2,
            relief=tk.GROOVE,
        )
        frame0.grid(row=0, column=1, sticky=tk.N)
        # frame0.pack(side=tk.RIGHT, anchor=tk.N)
        frame0.propagate(0)
        #################################################################################
        # サイドメニュー内フレーム########################################################
        Tframe = tk.Frame(
            frame0,
            bg="white",
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
        self.LimitCol = tk.Entry(Tframe, width=30)
        self.LimitCol.insert(0, "元帳日付列名")
        self.LimitCol.grid(row=1, column=1)
        #################################################################################
        # 列名設定フレーム################################################################
        tk.Label(frame0, text="出力列名設定").grid(row=1, column=0)  # フレームテキスト
        self.SF = SF.ScrollableFrame(frame0, bar_x=False)
        self.SF.grid(sticky=tk.W + tk.E)  # , ipadx=500, ipady=100)
        # エントリーウィジェットマネージャを初期化
        self.Entries = []  # エントリーウィジェットのインスタンス
        self.insertEntries = []  # 追加するボタンのようなラベル
        self.removeEntries = []  # 削除するボタンのようなラベル
        # こちらはインデックスマネージャ。ウィジェットの数や並び方を管理
        self.index = 0  # 最新のインデックス番号
        self.indexes = []  # インデックスの並び
        # self.createEntry(0, bar_x=False)
        self.ColList = ["日付", "摘要", "出金", "入金", "残高"]
        i = 0
        for ColListItem in self.ColList:
            self.createEntry(i, bar_x=False)
            self.Entries[i].insert(0, ColListItem)
            i += 1
        #################################################################################
        # サイドメニュー内変換設定フレーム#################################################
        Setframe = tk.Frame(
            frame0,
            bg="white",
            relief=tk.GROOVE,
            width=5,
            bd=2,
        )
        Setframe.grid(sticky=tk.W + tk.E)
        # テキストボックスの作成と配置
        tk.Label(Setframe, text="日付列番号").grid(row=0, column=0)  # 位置指定
        self.DaySet = tk.Entry(Setframe, width=30)
        self.DaySet.insert(0, "1")
        self.DaySet.grid(row=0, column=1)
        tk.Label(Setframe, text="金額表示列番号").grid(row=1, column=0)  # 位置指定
        self.MoneySet = tk.Entry(Setframe, width=30)
        self.MoneySet.insert(0, "3,4,5")
        self.MoneySet.grid(row=1, column=1)
        tk.Label(Setframe, text="置換対象列番号").grid(row=2, column=0)  # 位置指定
        self.ReplaceSet = tk.Entry(Setframe, width=30)
        self.ReplaceSet.insert(0, "2,3,4")
        self.ReplaceSet.grid(row=2, column=1)
        tk.Label(Setframe, text="置換対象文字列").grid(row=3, column=0)  # 位置指定
        self.ReplaceStr = tk.Entry(Setframe, width=30)
        self.ReplaceStr.insert(0, "CDカード,マツモトトソウテン,ザンダカショウメイショ")
        self.ReplaceStr.grid(row=3, column=1)
        #################################################################################
        # サイドメニュー内ボタンフレーム###################################################
        frame = tk.Frame(
            frame0,
            bg="white",
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
            bg="red",
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
            bg="green",
            font=fonts,
            width=BW,
            height=BH,
        )  # ボタン作成
        button2.grid(row=1, column=0, sticky=tk.N)
        # 新規直線描画ボタン---------------------------------------------------------------
        button3 = tk.Button(
            # self.top,
            frame,
            text="新規直線描画",
            fg="White",
            command=lambda: NewLineCreate(self, self.top.forward, HCW, HCH),
            bg="Purple",
            font=fonts,
            width=BW,
            height=BH,
        )  # ボタン作成
        button3.grid(row=2, column=0, sticky=tk.N)
        # 確定ボタン---------------------------------------------------------------
        button4 = tk.Button(
            # self.top,
            frame,
            text="確定",
            fg="White",
            command=lambda: EnterP(self.top.forward, HCW, HCH, self),
            bg="blue",
            font=fonts,
            width=BW,
            height=BH,
        )  # ボタン作成
        button4.grid(row=3, column=0, sticky=tk.N)
        # 削除ボタン---------------------------------------------------------------
        button5 = tk.Button(
            # self.top,
            frame,
            text="削除",
            fg="White",
            command=lambda: LineDelete(self.top.forward),
            bg="gray",
            font=fonts,
            width=BW,
            height=BH,
        )  # ボタン作成
        button5.grid(row=4, column=0, sticky=tk.N)
        # 戻るボタン---------------------------------------------------------------
        button6 = tk.Button(
            # self.top,
            frame,
            text="戻る",
            fg="White",
            command=lambda: ReturnBack(self),
            bg="Orange",
            font=fonts,
            width=BW,
            height=BH,
        )  # ボタン作成
        button6.grid(row=5, column=0, sticky=tk.N)
        # ##############################################################################
        Gra(self.top.forward, readcsv1, readcsv2, HCW, HCH)  # 透過キャンバスに罫線描画
        self.top.wm_attributes("-transparentcolor", "white")  # トップWindowの白色を透過
        # 下Windowのキャンバス作成
        # 画像の配置#####################################################################
        self.InportIMG()
        # ##############################################################################

    # 以下self関数###################################################################################
    def InportIMG(self):
        global TKimg
        global imgurl
        global CW, CH
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
        self.top.withdraw()

    # ---------------------------------------------------------------------------------------------
    def map(self, event):
        self.lift()
        self.top.wm_deiconify()
        self.top.attributes("-topmost", True)

    # ---------------------------------------------------------------------------------------------
    def change(self, event):
        x, y = self.back.winfo_rootx(), self.back.winfo_rooty()
        w, h = self.winfo_width(), self.winfo_height()
        self.top.geometry(f"{w}x{h}+{x}+{y}")

    # エントリーウィジェットを追加するボタンのようなラベルをクリック
    # -------------------------------------------------------------------------------------
    def insertEntry_click(self, event, id):
        # 追加する位置
        next = self.indexes.index(id) + 1
        self.index = self.index + 1
        # エントリーウィジェットを作成して配置
        self.createEntry(next, bar_x=False)

    # -------------------------------------------------------------------------------------
    # エントリーウィジェットを削除するボタンのようなラベルをクリック
    def removeEntry_click(self, event, id):
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
        # 再配置
        self.updateEntries()

    # -------------------------------------------------------------------------------------
    # エントリーウィジェットを再配置
    def updateEntries(self, bar_x=True, bar_y=True):
        # エントリーウィジェットマネージャを参照して再配置
        for i in range(len(self.indexes)):
            self.Entries[i].grid(column=0, row=i)
            self.Entries[i].bind("<MouseWheel>", self.SF.mouse_y_scroll)
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
            self.SF.scrollbar_y = ttk.Scrollbar(
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
            self.SF.scrollbar_x = ttk.Scrollbar(
                self.SF.scrollable_frame,
                orient="horizontal",
                command=self.SF.canvas.xview,
            )
            # ---------------------------------------------------------------------
            self.SF.scrollbar_x.grid(
                row=len(self.indexes), column=0, columnspan=4, sticky=tk.E + tk.W
            )
            self.SF.canvas.configure(xscrollcommand=self.SF.scrollbar_x.set)

    # -------------------------------------------------------------------------------------
    # エントリーウィジェットを作成して配置
    def createEntry(self, next, bar_x=True, bar_y=True):
        # 最初のエントリーウィジェットを追加
        self.Entries.insert(next, tk.Entry(self.SF.scrollable_frame, width=35))
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
    # テキストを取得するボタンを押す
    def GetEntryTextButton_click(self):
        GetEntry = []

        # 全てのエントリーウィジェットの内容を配列化
        for i in range(len(self.indexes)):
            GetEntry.append(self.Entries[i].get())

        # コンソールに表示
        return GetEntry

    # -------------------------------------------------------------------------------------


# 以下関数######################################################################################
# ---------------------------------------------------------------------------------------------
def ReturnBack(self):
    self.top.destroy()
    self.master.destroy()
    # root.destroy()


# ---------------------------------------------------------------------------------------------
def NewLineCreate(self, selfC, HCW, HCH):
    global tagsList
    # メッセージボックス（OK・キャンセル）
    unmap(self)
    MSG = messagebox.askokcancel("確認", "新たに直線を描画しますか？")
    if MSG is True:
        SLS = CV2S.straightlinesetting(imgurl)
        if SLS[0] is True:
            ####################################################################################
            with open(
                URL + r"\TKInterGUI\StraightListYoko.csv",
                "w",
                newline="",
            ) as file:
                writer = csv.writer(file)
                writer.writerow(SLS[1])
            with open(
                URL + r"\TKInterGUI\StraightListTate.csv",
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
    scrollbar = ttk.Scrollbar(self, orient="vertical", command=listbox.yview)
    listbox["yscrollcommand"] = scrollbar.set
    return listbox, scrollbar


# ---------------------------------------------------------------------------------------------
def LoadImg(Wwidth, Wheight):
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
    縦の直線描画
    """
    TName = "Line" + str(len(tagsList) + 1)
    canvastop.create_line(CW - 50, 0, CW - 50, CH, tags=TName, fill="#FF0000")
    canvastop.tag_bind(TName, "<ButtonPress-1>", click1)
    canvastop.tag_bind(TName, "<B1-Motion>", drag1)
    BSS = [0, 0, 0, 0]
    TSS = [TName, CW - 50, 0, CW - 50, CH, "Yoko"]
    tagsList.append([TSS, BSS])


# ---------------------------------------------------------------------------------------------
def StWLine(canvastop, CW, CH):
    """
    横の直線描画
    """
    TName = "Line" + str(len(tagsList) + 1)
    canvastop.create_line(0, CH - 50, CW, CH - 50, tags=TName, fill="#00FF40")
    canvastop.tag_bind(TName, "<ButtonPress-1>", click1)
    canvastop.tag_bind(TName, "<B1-Motion>", drag1)
    TSS = [TName, 0, CH - 50, CW, CH - 50, "Tate"]
    BSS = [0, 0, 0, 0]
    tagsList.append([TSS, BSS])


# ---------------------------------------------------------------------------------------------
def Gra(canvas, readcsv1, readcsv2, HCW, HCH):

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
        canvas.create_line(ripar0, ripar1, ripar2, ripar3, tags=TName, fill="#FF0000")
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
        canvas.create_line(ripar0, ripar1, ripar2, ripar3, tags=TName, fill="#00FF40")
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


# ---------------------------------------------------------------------------------------------
def listintCheck(list):
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

    FList = []
    FYokoList = []
    FTateList = []
    SGEL = selfmother.GetEntryTextButton_click()
    # 条件テキストボックスの値格納---------------------------
    DaySet = selfmother.DaySet.get()
    MoneySet = selfmother.MoneySet.get()
    ReplaceSet = selfmother.ReplaceSet.get()
    ReplaceStr = selfmother.ReplaceStr.get()
    # ------------------------------------------------------
    # 条件テキストボックスのリスト化---------------------------
    if "," in DaySet:
        DaySet = DaySet.split(",")
    else:
        DaySet = list(DaySet)
    if "," in MoneySet:
        MoneySet = MoneySet.split(",")
    else:
        MoneySet = list(MoneySet)
    if "," in ReplaceSet:
        ReplaceSet = ReplaceSet.split(",")
    else:
        ReplaceSet = list(ReplaceSet)
    if "," in ReplaceStr:
        ReplaceStr = ReplaceStr.split(",")
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
        MSG = messagebox.askokcancel("確認", str(SGEL) + "の列名で出力します。")
        if MSG is True:
            map(selfmother)
            ####################################################################################
            with open(
                URL + r"\TKInterGUI\StraightListYoko.csv",
                "w",
                newline="",
            ) as file:
                writer = csv.writer(file)
                writer.writerow(FYokoList)
            with open(
                URL + r"\TKInterGUI\StraightListTate.csv",
                "w",
                newline="",
            ) as file:
                writer = csv.writer(file)
                writer.writerow(FTateList)
            ####################################################################################
            print("csv保存完了")
            OM = OCRF.Main(
                imgurl,
                FYokoList,
                FTateList,
                Banktoml,
                SGEL,
                MoneySet,
                ReplaceSet,
                ReplaceStr,
            )
            if OM[0] is True:
                unmap(selfmother)
                MSG = messagebox.showinfo("抽出完了", str(OM[1]) + "_に保存しました。")
                Viw = messagebox.askokcancel("確認", "抽出内容を表示いたしますか？")
                map(selfmother)
                if Viw is True:
                    ReturnBack(selfmother)
                    csvurl = imgurl.replace(".png", ".csv")
                    DG.Main(
                        csvurl,
                        Banktoml,
                        DaySet,
                        MoneySet,
                        ReplaceSet,
                        ReplaceStr,
                    )
            else:
                unmap(selfmother)
                MSG = messagebox.showinfo("抽出失敗", "エラーにより抽出に失敗しました。")
                map(selfmother)
        else:
            messagebox.showinfo("中断", "処理を中断します。")
            map(selfmother)


# ---------------------------------------------------------------------------------------------
def unmap(self):
    self.top.withdraw()


# ---------------------------------------------------------------------------------------------
def map(self):
    self.lift()
    self.top.wm_deiconify()
    self.top.attributes("-topmost", True)


# ---------------------------------------------------------------------------------------------
def change(self):
    x, y = self.back.winfo_rootx(), self.back.winfo_rooty()
    w, h = self.winfo_width(), self.winfo_height()
    self.top.geometry(f"{w}x{h}+{x}+{y}")


# ---------------------------------------------------------------------------------------------
def LineDelete(self):
    """
    選択直線の削除
    """
    global id1
    global tagsList
    TName = "Line" + str(id1[0])
    self.delete(TName)
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
    # https://office54.net/python/tkinter/tkinter-bind-event#section2
    global x1
    global y1
    global id1
    txt.delete(0, tk.END)
    x2 = event.x
    y2 = event.y
    id1 = event.widget.find_closest(x2, y2)
    TName = "Line" + str(id1[0])
    txt.insert(tk.END, TName)
    x1 = x2
    y1 = y2


# ---------------------------------------------------------------------------------------------
def drag1(event):
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


def Main(US):
    global imgurl
    global readcsv1, readcsv2
    global URL
    global Banktoml

    imgurl = US
    URL = os.getcwd()
    # imgurl = URL + r"\TKInterGUI\OCR0.png"
    # toml読込------------------------------------------------------------------------------
    with open(os.getcwd() + r"/TKInterGUI/BankSetting.toml", encoding="utf-8") as f:
        Banktoml = toml.load(f)
        print(Banktoml)
    # -----------------------------------------------------------
    try:
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
                    readcsv1.append(
                        [int(rsp[0]), int(rsp[1]), int(rsp[2]), int(rsp[3])]
                    )
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
    URL = os.getcwd()
    imgurl = r"D:\OCRTESTPDF\PDFTEST\Hirogin_1page.png"
    # toml読込------------------------------------------------------------------------------
    with open(os.getcwd() + r"/TKInterGUI/BankSetting.toml", encoding="utf-8") as f:
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
