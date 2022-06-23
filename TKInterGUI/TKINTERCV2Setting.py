import tkinter as tk
import csv
from PIL import Image, ImageTk
from tkinter import messagebox
import os
import OCRFlow as OCRF
import toml
from tkinter import ttk
import CV2Setting as CV2S


class Application(tk.Frame):
    def __init__(self, master=None):
        global TKimg  # 画像オブジェクト用グローバル変数
        global txt
        # Windowの初期設定を行う。
        super().__init__(master)
        # Windowの画面サイズを設定する。
        # geometryについて : https://kuroro.blog/python/rozH3S2CYE0a0nB3s2QL/
        self.master.geometry("1480x800+0+0")  # Window表示位置指定
        # 画像の読込#####################################################################
        IR = LoadImg()
        CW, CH, HCW, HCH, TKimg = IR[0], IR[1], IR[2], IR[3], IR[4]
        # ##############################################################################
        self.top = tk.Toplevel()  # サブWindow作成
        self.top.wm_attributes("-topmost", True)  # 常に一番上のウィンドウに指定
        # self.top.overrideredirect(True)  # ウィンドウのタイトル部分を消去
        self.top.geometry("1480x800+0+0")  # トップWindow表示位置指定
        self.top.forward = tk.Canvas(
            self.top, background="white", width=CW, height=CH
        )  # 透過キャンバス作成
        self.top.forward.pack(fill=tk.BOTH, expand=True)  # 透過キャンバスを配置
        # ##############################################################################
        # 配置
        # テキストボックスの作成と配置---------------------------------------------------
        txt = tk.Entry(self.top, width=90)
        txt.pack(side=tk.TOP, pady=50, padx=50, anchor=tk.E)
        # フレーム配置------------------------------------------------------------------
        frame0 = tk.Frame(
            self.top,
            bg="White",
            height=50,
            width=90,
            # pady=10,
            padx=10,
            relief=tk.GROOVE,
        )
        frame0.pack(
            side=tk.TOP, padx=200, anchor=tk.E
        )  # , pady=10, padx=10, anchor=tk.E)
        # リストボックス-----------------------------------------------------------------
        tlc = tomlListCreate(frame0)
        tlc[0].pack(
            side=tk.RIGHT,
            pady=10,
            padx=10,
        )
        tlc[1].pack(side=tk.RIGHT, fill=tk.BOTH)
        # フレーム配置------------------------------------------------------------------
        frame = tk.Frame(
            self.top,
            bg="White",
            height=500,
            width=90,
            pady=10,
            padx=50,
            relief=tk.GROOVE,
        )
        frame.pack(side=tk.TOP, pady=50, padx=50, anchor=tk.E)
        # ##############################################################################
        BW = 38  # ボタン横幅
        BH = 2  # ボタン縦幅
        fonts = ("", 16)  # ボタンフォントの設定
        # ##############################################################################
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
        button.pack(side=tk.TOP, pady=10, padx=10, fill=tk.BOTH)
        # 横直線追加ボタン---------------------------------------------------------------
        button = tk.Button(
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
        button.pack(side=tk.TOP, pady=10, padx=10, fill=tk.BOTH)
        # 新規直線描画ボタン---------------------------------------------------------------
        button = tk.Button(
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
        button.pack(side=tk.TOP, pady=10, padx=10, fill=tk.BOTH)
        # 確定ボタン---------------------------------------------------------------
        button = tk.Button(
            # self.top,
            frame,
            text="確定",
            fg="White",
            command=lambda: EnterP(self.top.forward, HCW, HCH, self, tlc[0]),
            bg="blue",
            font=fonts,
            width=BW,
            height=BH,
        )  # ボタン作成
        button.pack(side=tk.TOP, pady=10, padx=10, fill=tk.BOTH)
        # 削除ボタン---------------------------------------------------------------
        button = tk.Button(
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
        button.pack(side=tk.TOP, pady=10, padx=10, fill=tk.BOTH)
        # ##############################################################################
        Gra(self.top.forward, readcsv1, readcsv2, HCW, HCH)  # 透過キャンバスに罫線描画
        # ##############################################################################
        self.top.wm_attributes("-transparentcolor", "white")  # トップWindowの白色を透過
        self.back = tk.Canvas(self.master, background="white", width=CW, height=CH)
        # 下Windowのキャンバス作成
        self.back.create_image(0, 0, image=TKimg, anchor=tk.NW)  # 下Windowのキャンバスに画像挿入
        self.back.pack(fill=tk.BOTH, expand=True)  # 下Windowを配置
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
            MSG = messagebox.showinfo("直線描画失敗", "直線描画に失敗しました。")
            map(self)


# ---------------------------------------------------------------------------------------------
def tomlListCreate(self):
    """
    リストボックス作成
    return:リストボックス(obj),スクロールバー(obj)
    """
    module = Banktoml["DataList"]["Datas"]
    var = tk.StringVar(value=module)
    listbox = tk.Listbox(self, listvariable=var, selectmode="multiple", height=6)
    scrollbar = ttk.Scrollbar(self, orient="vertical", command=listbox.yview)
    listbox["yscrollcommand"] = scrollbar.set
    return listbox, scrollbar


# ---------------------------------------------------------------------------------------------
def LoadImg():
    global MaxW, MaxH
    global imgurl
    # 画像の読込#####################################################################
    # 画像を指定
    img = Image.open(imgurl)
    Par = 4.5  # 倍率
    MaxW, MaxH = img.width, img.height
    CW, CH = img.width // Par, img.height // Par  # 基準サイズ値
    CW, CH = int(CW), int(CH)
    HCW, HCH = CW / img.width, CH / img.height  # リサイズ比率
    img = img.resize((CW, CH))  # 画像リサイズ
    TKimg = ImageTk.PhotoImage(img)  # 下Windowに表示する画像オブジェクト
    return CW, CH, HCW, HCH, TKimg
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
    TSS = [TName, CW - 50, 0, CW - 50, CH]
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
    TSS = [TName, 0, CH - 50, CW, CH - 50]
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
        ripar0 = readcsv1Item[0] * HCH  # * CHh
        ripar1 = readcsv1Item[1] * HCW  # * CWw
        ripar2 = readcsv1Item[2] * HCH  # * CHh
        ripar3 = readcsv1Item[3] * HCW  # * CWw
        TName = "Line" + str(ri)
        canvas.create_line(ripar0, ripar1, ripar2, ripar3, tags=TName, fill="#FF0000")
        canvas.tag_bind(TName, "<ButtonPress-1>", click1)
        canvas.tag_bind(TName, "<B1-Motion>", drag1)
        canvas.place(x=0, y=0)
        BtagsList.append([TName, ripar0, ripar1, ripar2, ripar3, "Yoko"])
    for readcsv2Item in readcsv2:
        ri += 1
        ripar0 = readcsv2Item[0] * HCH  # * CHh
        ripar1 = readcsv2Item[1] * HCW  # * CWw
        ripar2 = readcsv2Item[2] * HCH  # * CHh
        ripar3 = readcsv2Item[3] * HCW  # * CWw
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
def EnterP(self, HCW, HCH, selfmother, ListBoxobj):
    """
    確定ボタンクリック
    """
    global tagsList
    global MaxW, MaxH
    FList = []
    FYokoList = []
    FTateList = []

    selected = ListBoxobj.curselection()
    if len(selected) == 0:
        unmap(selfmother)
        MSG = messagebox.showinfo("通帳設定未選択", "通帳設定を選択して下さい。データが未選択です。")
        map(selfmother)
    elif len(selected) == 1:
        tomltitle = ListBoxobj.get(selected)
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
        MSG = messagebox.askokcancel("確認", FYokoList)
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
            OM = OCRF.Main(imgurl, FYokoList, FTateList, Banktoml, tomltitle)
            if OM[0] is True:
                unmap(selfmother)
                MSG = messagebox.showinfo("抽出完了", str(OM[1]) + "_に保存しました。")
                map(selfmother)
            else:
                unmap(selfmother)
                MSG = messagebox.showinfo("抽出失敗", "エラーにより抽出に失敗しました。")
                map(selfmother)
        else:
            map(selfmother)
    else:
        unmap(selfmother)
        MSG = messagebox.showinfo("通帳設定複数選択", "通帳設定が複数選択されています。一つのみ選択して下さい。")
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
    TName = "Line" + str(id1[0])
    self.delete(TName)


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


def Main(imgurl):
    global readcsv1, readcsv2
    URL = os.getcwd()
    # imgurl = URL + r"\TKInterGUI\OCR0.png"
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

    # Windowについて : https://kuroro.blog/python/116yLvTkzH2AUJj8FHLx/
    root = tk.Tk()  # Window生成
    app = Application(master=root)
    # frame = tk.Frame(root, height=3840, width=3840)  # frame生成
    # --- 基本的な表示準備 ----------------

    app.mainloop()


URL = os.getcwd()
imgurl = r"D:\Souzoku_JAPng\Souzoku_JA-07.png"
# toml読込------------------------------------------------------------------------------
with open(os.getcwd() + r"/TKInterGUI/BankSetting.toml", encoding="utf-8") as f:
    Banktoml = toml.load(f)
    print(Banktoml)
# -----------------------------------------------------------
if __name__ == "__main__":

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
