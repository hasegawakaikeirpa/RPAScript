import tkinter as tk
import csv
from PIL import Image, ImageTk
from tkinter import messagebox


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
        imgurl = r"D:\PythonScript\RPAScript\RPAPhoto\PDFeTaxReadForList\OCR0.png"
        # 画像を指定
        img = Image.open(imgurl)
        Par = 4.5  # 倍率
        CW, CH = img.width // Par, img.height // Par  # 基準サイズ値
        CW, CH = int(CW), int(CH)
        HCW, HCH = CW / img.width, CH / img.height  # リサイズ比率
        img = img.resize((CW, CH))  # 画像リサイズ
        TKimg = ImageTk.PhotoImage(img)  # 下Windowに表示する画像オブジェクト
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
        BW = 60  # ボタン横幅
        BH = 5  # ボタン縦幅
        # テキストボックスの作成と配置---------------------------------------------------
        txt = tk.Entry(self.top, width=90)
        # txt.place(x=900, y=325, width=450, height=30)  # テキストボックスを配置
        txt.pack(side=tk.TOP, pady=100, padx=50, anchor=tk.E)
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
        frame.pack(side=tk.TOP, padx=50, anchor=tk.E)
        # 縦直線追加ボタン---------------------------------------------------------------
        button = tk.Button(
            # self.top,
            frame,
            text="縦直線追加",
            fg="White",
            command=lambda: StLine(self.top.forward, CW, CH),
            bg="red",
            width=BW,
            height=BH,
        )  # ボタン作成
        # button.place(x=900, y=200)  # ボタンを配置,横,縦
        button.pack(side=tk.TOP, padx=10, fill=tk.BOTH)
        # 横直線追加ボタン---------------------------------------------------------------
        button = tk.Button(
            # self.top,
            frame,
            text="横直線追加",
            fg="White",
            command=lambda: StWLine(self.top.forward, CW, CH),
            bg="green",
            width=BW,
            height=BH,
        )  # ボタン作成
        # button.place(x=1100, y=200)  # ボタンを配置,横,縦
        button.pack(side=tk.TOP, padx=10, fill=tk.BOTH)
        # 確定ボタン---------------------------------------------------------------
        button = tk.Button(
            # self.top,
            frame,
            text="確定",
            fg="White",
            command=lambda: EnterP(self.top.forward, HCW, HCH, self),
            bg="blue",
            width=BW,
            height=BH,
        )  # ボタン作成
        # button.place(x=1100, y=400)  # ボタンを配置,横,縦
        button.pack(side=tk.TOP, padx=10, fill=tk.BOTH)
        # 削除ボタン---------------------------------------------------------------
        button = tk.Button(
            # self.top,
            frame,
            text="削除",
            fg="White",
            command=lambda: LineDelete(self.top.forward),
            bg="gray",
            width=BW,
            height=BH,
        )  # ボタン作成
        # button.place(x=900, y=400)  # ボタンを配置,横,縦
        button.pack(side=tk.TOP, padx=10, fill=tk.BOTH)
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

    def unmap(self, event):
        self.top.withdraw()

    def map(self, event):
        self.lift()
        self.top.wm_deiconify()
        self.top.attributes("-topmost", True)

    def change(self, event):
        x, y = self.back.winfo_rootx(), self.back.winfo_rooty()
        w, h = self.winfo_width(), self.winfo_height()
        self.top.geometry(f"{w}x{h}+{x}+{y}")


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
        BtagsList.append([TName, ripar0, ripar1, ripar2, ripar3])
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
        BtagsList.append([TName, ripar0, ripar1, ripar2, ripar3])
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


def EnterP(self, HCW, HCH, selfmother):
    """
    確定ボタンクリック
    """
    global tagsList
    FList = []
    for tagsListItem in tagsList:
        BB = self.bbox(tagsListItem[0][0])
        BBS = [BB[0], BB[1], BB[2], BB[3]]
        FList.append([tagsListItem[0], tagsListItem[1], BBS])
    for FListItem in FList:
        FSS = [
            (FListItem[1][0] + FListItem[2][0]) / HCW,
            (FListItem[1][1] + FListItem[2][1]) / HCH,
            (FListItem[1][2] + FListItem[2][2]) / HCW,
            (FListItem[1][3] + FListItem[2][3]) / HCH,
        ]
        print(FSS)
    # メッセージボックス（OK・キャンセル）
    unmap(selfmother)
    MSG = messagebox.askokcancel("確認", FSS)
    if MSG is True:
        map(selfmother)
    else:
        map(selfmother)


def unmap(self):
    self.top.withdraw()


def map(self):
    self.lift()
    self.top.wm_deiconify()
    self.top.attributes("-topmost", True)


def change(self):
    x, y = self.back.winfo_rootx(), self.back.winfo_rooty()
    w, h = self.winfo_width(), self.winfo_height()
    self.top.geometry(f"{w}x{h}+{x}+{y}")


def LineDelete(self):
    """
    選択直線の削除
    """
    global id1
    TName = "Line" + str(id1[0])
    self.delete(TName)


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


# x1 = 0
# y1 = 0
# id1 = -1


if __name__ == "__main__":

    readcsv1 = []
    with open(
        r"D:\PythonScript\RPAScript\RPAPhoto\PDFeTaxReadForList\StraightListYoko.csv",
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
        r"D:\PythonScript\RPAScript\RPAPhoto\PDFeTaxReadForList\StraightListTate.csv",
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
