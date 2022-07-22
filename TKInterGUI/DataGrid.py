import tkinter as tk
import tkinter.ttk as ttk

# from tkinter import messagebox
import pandas as pd
import os
import csv
import toml
import MyTable as MT
import MyTable2 as MT2
import MyTable3 as MT3
import AutoJournal as AJ
import CSVOut as CSVO


class DataGrid:
    def __init__(self, window_root, default_path):
        global csvurl, Banktoml, AJurl, AJSeturl, Roolurl, tomltitle

        # toml読込------------------------------------------------------------------------------
        self.Banktoml = Banktoml
        # -----------------------------------------------------------
        self.FileName = csvurl
        self.JounalFileName = AJurl
        self.Roolurl = Roolurl
        self.tomlList = self.Banktoml["ParList"]["Name"]
        self.HidukeColNo = self.Banktoml[tomltitle]["HidukeColNo"]
        self.MoneyCol = self.Banktoml[tomltitle]["MoneyCol"]
        self.ChangeTextCol = self.Banktoml[tomltitle]["ChangeTextCol"]
        self.ColumnName = self.Banktoml[tomltitle]["ColumnName"]
        self.NyuName = self.Banktoml[tomltitle]["NyuName"]
        self.SyutuName = self.Banktoml[tomltitle]["SyutuName"]
        self.ZanName = self.Banktoml[tomltitle]["ZanName"]
        self.Henkan = self.Banktoml[tomltitle]["Henkan"]
        self.ChangeText = self.Banktoml[tomltitle]["ChangeText"]
        # ------------------------------------
        self.CsvHeader()
        # メインウィンドウ設定-------------------------------------------------------------------
        self.root = tk.Tk()  # ウインド画面の作成
        self.root.geometry("1400x700")  # 画面サイズの設定
        self.root.title("OCRTEXT")  # 題名
        # -------------------------------------------------------------------------------------
        # -------------------------------------------------------------------------------------
        # フレーム設定--------------------------------------------------------------------------
        self.frame3 = tk.Frame(self.root)
        self.frame3.grid(row=1, column=0, sticky=tk.W)
        # -------------------------------------------------------------------------------------
        # フレーム設定--------------------------------------------------------------------------
        self.frame4 = tk.Frame(self.root)
        self.frame4.grid(row=1, column=0)
        # -------------------------------------------------------------------------------------
        # フレーム設定--------------------------------------------------------------------------
        self.frame6 = tk.Frame(self.root)
        self.frame6.grid(row=1, column=0, sticky=tk.E)
        tk.Label(self.frame6, text="選択行自動仕訳作成").grid(row=0, column=0)  # 位置指定
        self.AJ_Btn = tk.Button(
            self.frame6,
            text="選択行自動仕訳作成",
            width=20,
            command=lambda: self.AJCalc(csvurl),
        )
        self.AJ_Btn.grid(row=1, column=0)  # 位置指定
        # -------------------------------------------------------------------------------------
        # フレーム設定--------------------------------------------------------------------------
        self.frame5 = tk.Frame(self.root, width=650)
        self.frame5.grid(row=1, column=1, sticky=tk.W)
        # -------------------------------------------------------------------------------------
        # ツリーフレーム設定---------------------------------------------------------------------
        self.tree_frame = tk.Frame(self.root, width=650, height=500)
        self.tree_frame.grid(row=0, column=0, sticky=tk.N + tk.S + tk.W + tk.E)
        # df = TableModel.getSampleData()
        # pt = Table(self.tree_frame)
        pt = MT.MyTable(
            self.tree_frame, width=650, height=500, sticky=tk.N + tk.S + tk.W + tk.E
        )  # テーブルをサブクラス化
        enc = CSVO.getFileEncoding(csvurl)
        self.table = pt.importCSV(csvurl, encoding=enc)
        self.pt = pt
        pt.show()
        # -------------------------------------------------------------------------------------
        # ツリーフレーム設定---------------------------------------------------------------------
        self.tree2_frame = tk.Frame(self.root, width=650, height=500)
        self.tree2_frame.grid(
            row=0, column=1, columnspan=2, sticky=tk.N + tk.S + tk.W + tk.E
        )
        # df = TableModel.getSampleData()
        # pt2 = Table(self.tree2_frame)
        pt2 = MT2.MyTable(
            self.tree2_frame, width=650, height=500, sticky=tk.N + tk.S + tk.W + tk.E
        )  # テーブルをサブクラス化
        enc = CSVO.getFileEncoding(AJurl)
        self.table2 = pt2.importCSV(AJurl, encoding=enc)
        self.pt2 = pt2
        pt2.show()
        # -------------------------------------------------------------------------------------
        # ツリービューを配置
        self.treeviewEntries()
        # tomlListを配置
        self.tomlEntries()

    # -----------------------------------------------------------------------------------------
    def AJCalc(self, csvurl):
        global AJSeturl
        self.FileName = csvurl
        self.JounalFileName = AJurl
        self.Roolurl = Roolurl

        print(self.pt.startrow)
        # self.endrow
        # self.startcol
        # self.endcol

        AJ_List = AJ.mainListUp(
            self.Henkan, "ガソリン代", self.JounalFileName, self.Roolurl, self.Banktoml, "JA"
        )
        AJDF = pd.DataFrame(AJ_List)
        AJDF.to_csv(AJSeturl, index=False, header=False)
        pt3 = MT3.MyTable(
            self.frame5, width=650, height=100, sticky=tk.N + tk.S + tk.W + tk.E
        )  # テーブルをサブクラス化
        enc = CSVO.getFileEncoding(AJSeturl)
        self.table3 = pt3.importCSV(AJSeturl, encoding=enc)
        pt3.show()

    # -----------------------------------------------------------------------------------------
    def CsvHeader(self):
        enc = CSVO.getFileEncoding(self.FileName)
        with open(self.FileName, "r", encoding=enc) as f:  # csv読込み(Treeview 表示用)
            reader = csv.reader(f, delimiter=",", quotechar='"')
            for cells in reader:
                # print(cells)
                # c = 0
                # p = 1
                # for cellsItem in cells:
                #     if cellsItem == "":
                #         cells[c] = str(p)
                #         p += 1
                #         c += 1
                #     else:
                #         c += 1
                # for cr in range(len(cells)):
                #     p = 2
                #     CC = cells.count(cells[cr])
                #     if CC > 1:
                #         c = 0
                #         for cellsItem in cells:
                #             if cells[cr] == cellsItem:
                #                 if cr != c:
                #                     cells[c + 1] = cells[cr] + str(p)
                #                     c += 1
                #                     p += 1
                #             else:
                #                 c += 1
                self.ColumnName = cells
                break
        enc = CSVO.getFileEncoding(self.JounalFileName)
        with open(self.JounalFileName, "r", encoding=enc) as f:  # csv読込み(Treeview 表示用)
            reader = csv.reader(f, delimiter=",", quotechar='"')
            for cells in reader:
                # print(cells)
                # c = 0
                # p = 1
                # for cellsItem in cells:
                #     if cellsItem == "":
                #         cells[c] = str(p)
                #         p += 1
                #         c += 1
                #     else:
                #         c += 1
                # for cr in range(len(cells)):
                #     p = 2
                #     CC = cells.count(cells[cr])
                #     if CC > 1:
                #         c = 0
                #         for cellsItem in cells:
                #             if cells[cr] == cellsItem:
                #                 if cr != c:
                #                     cells[c + 1] = cells[cr] + str(p)
                #                     c += 1
                #                     p += 1
                #             else:
                #                 c += 1
                self.ColumnName2 = cells
                break

    # -----------------------------------------------------------------------------------------
    def tomlEntries(self):
        self.tomlEntries = []  # Entryのインスタンス
        self.tomlinsertEntries = []  # ラベルインスタンス
        self.tomlindex = 0  # 最新のインデックス番号
        self.tomlindexes = []  # インデックスの並び
        r = 0
        for ColNameItem in self.tomlList:
            # ラベル＆Entryフレームへ追加----------------------------------------------
            self.createtomlEntry(r, ColNameItem)  # Entryを作成配置
            # ----------------------------------------------------------------------
            r += 1

    # -----------------------------------------------------------------------------------------
    # エントリーウィジェットを再配置
    def updatetomlEntries(self):

        # エントリーウィジェットマネージャを参照して再配置
        for i in range(len(self.tomlindexes)):
            self.tomlEntries[i].grid(column=1, row=i)
            self.tomlEntries[i].bind("<Return>", self.EveRecalc)
            self.tomlEntries[i].lift()
            self.tomlinsertEntries[i].grid(column=0, row=i)

    # -----------------------------------------------------------------------------------------
    # エントリーウィジェットを作成して配置
    def createtomlEntry(self, next, ColNameItem):

        # 最初のエントリーウィジェットを追加
        self.tomlEntries.insert(next, tk.Entry(self.frame4, width=20))
        lb = tk.Label(self.frame4, text=ColNameItem)

        lb.grid(row=next, column=0)  # 位置指定
        cn = self.Banktoml["ParList"][ColNameItem]
        tom = self.Banktoml[tomltitle][cn]
        tomtx = ""
        try:
            print(type(tom).__name__)
            if type(tom).__name__ == "list":
                txtxt = tk.Entry(self.frame4, width=15)
                for tomItem in tom:
                    tomtx += "," + str(tomItem)
                tomtx = tomtx.lstrip(",")
                txtxt.insert(0, tomtx)
            else:
                txtxt = tk.Entry(self.frame4, width=15)
                txtxt.insert(0, tom)
        except:
            txtxt = tk.Entry(self.frame4, width=15)
            txtxt.insert(0, tom)
        txtxt.grid(row=next, column=1)  # 位置指定
        # ラベルを作成
        self.tomlinsertEntries.insert(
            next,
            tk.Label(
                self.frame4,
                text=str(ColNameItem),
            ),
        )
        # インデックスマネージャに登録
        self.tomlindexes.insert(next, self.tomlindex)
        # 再配置
        # self.updatetomlEntries()

    # -----------------------------------------------------------------------------------------
    def treeviewEntries(self):
        """
        ツリービューを配置
        """
        # エントリーウィジェットマネージャを初期化
        self.Entries = []  # Entryのインスタンス
        self.insertEntries = []  # ラベルインスタンス
        # インデックスマネージャを初期化
        self.index = 0  # 最新のインデックス番号
        self.indexes = []  # インデックスの並び
        # URLテキストボックス-----------------------------------------------------------
        tk.Label(self.frame3, text="URL").grid(row=0, column=0)  # 位置指定
        self.Label_URL = tk.Entry(self.frame3, width=15)
        self.Label_URL.insert(0, self.FileName)
        self.Label_URL.grid(row=0, column=1, columnspan=3)
        # tomlNameテキストボックス-----------------------------------------------------------
        tk.Label(self.frame3, text="設定ファイル名").grid(row=1, column=0)  # 位置指定
        self.Label_ChangeURL = tk.Entry(self.frame3, width=15)
        self.Label_ChangeURL.insert(0, tomltitle)
        self.Label_ChangeURL.grid(row=1, column=1, columnspan=3)
        # 開始残高ボタン----------------------------------------------------------------
        tk.Label(self.frame3, text="開始残高").grid(
            row=len(self.indexes) + 2, column=0
        )  # 位置指定
        self.ZanNametxt = tk.Entry(self.frame3, width=15)
        self.ZanNametxt.grid(row=len(self.indexes) + 2, column=1)  # 位置指定
        self.ebtn2 = tk.Button(
            self.frame3,
            text="再計算",
            width=20,
            command=lambda: self.ZanNamedaka(),
        )
        self.ebtn2.grid(row=len(self.indexes) + 3, column=0, columnspan=2)  # 位置指定
        # ------------------------------------------------------------------------------

    # -----------------------------------------------------------------------------------------
    # 以下self関数
    def EveRecalc(self, event):
        c = 0
        self.InStartVal()
        # 列名一致で列番号取得----------------------------------------------------------
        for ColNameItem in self.ColumnName:
            if ColNameItem == self.NyuName:
                NyuCol = c
            elif ColNameItem == self.SyutuName:
                SyutuCol = c
            elif ColNameItem == self.ZanName:
                ZanCol = c
            c += 1
        # ---------------------------------------------------------------------------
        # CSV読込
        enc = CSVO.getFileEncoding(self.FileName)
        with open(self.FileName, "r", encoding=enc) as f:  # csv読込み(Treeview 表示用)
            reader = csv.reader(f, delimiter=",", quotechar='"')
            next(reader)
            CList = list(reader)
        # 残高再計算-----------------------------------------------------------------
        c = 0
        clr = len(CList)
        print(CList[0][ZanCol])
        zanstr = self.ZanNametxt.get()
        if zanstr == "":
            zanstr = CList[0][ZanCol]
        else:
            CList[0][ZanCol] = zanstr
        for r in range(clr):
            if not r == clr - 1:
                try:
                    if r == 0:
                        Zanint = int(zanstr)
                    else:
                        Zanint = int(CList[r][ZanCol])
                except:
                    Zanint = 0
                try:
                    Nyuint = int(CList[r + 1][NyuCol])
                except:
                    Nyuint = 0
                try:
                    Syutuint = int(CList[r + 1][SyutuCol])
                except:
                    Syutuint = 0

                NZan = Zanint + Nyuint - Syutuint
                CList[r + 1][ZanCol] = str(NZan)
        df = pd.DataFrame(CList, columns=self.ColumnName)
        try:
            df.to_csv(self.FileName, index=False, encoding="cp932")
        except:
            with open(
                self.FileName,
                mode="w",
                encoding="cp932",
                errors="ignore",
                newline="",
            ) as f:
                df.to_csv(f, index=False)

        self.removeEntry()
        self.treeviewEntries()

    # -----------------------------------------------------------------------------------------

    def ZanRecalc(self):
        c = 0
        # 列名一致で列番号取得----------------------------------------------------------
        for ColNameItem in self.ColumnName:
            if ColNameItem == self.NyuName:
                NyuCol = c
            elif ColNameItem == self.SyutuName:
                SyutuCol = c
            elif ColNameItem == self.ZanName:
                ZanCol = c
            c += 1
        # ---------------------------------------------------------------------------
        # CSV読込
        enc = CSVO.getFileEncoding(self.FileName)
        with open(self.FileName, "r", encoding=enc) as f:  # csv読込み(Treeview 表示用)
            reader = csv.reader(f, delimiter=",", quotechar='"')
            next(reader)
            CList = list(reader)
        # 残高再計算-----------------------------------------------------------------
        c = 0
        clr = len(CList)
        print(CList[0][ZanCol])
        zanstr = self.ZanNametxt.get()
        if zanstr == "":
            zanstr = CList[0][ZanCol]
        else:
            CList[0][ZanCol] = zanstr
        for r in range(clr):
            if not r == clr - 1:
                try:
                    if r == 0:
                        Zanint = int(zanstr)
                    else:
                        Zanint = int(CList[r][ZanCol])
                except:
                    Zanint = 0
                try:
                    Nyuint = int(CList[r + 1][NyuCol])
                except:
                    Nyuint = 0
                try:
                    Syutuint = int(CList[r + 1][SyutuCol])
                except:
                    Syutuint = 0

                NZan = Zanint + Nyuint - Syutuint
                CList[r + 1][ZanCol] = str(NZan)
        df = pd.DataFrame(CList, columns=self.ColumnName)
        try:
            df.to_csv(self.FileName, index=False, encoding="cp932")
        except:
            df.to_csv(self.FileName, index=False, encoding="utf8")
        self.removeEntry()
        self.treeviewEntries()

    # -----------------------------------------------------------------------------------------
    def Zandaka(self):
        zanstr = self.ZanNametxt.get()
        if zanstr == "":
            Messagebox = tk.messagebox.askquestion("再計算", "残高を再計算しますか？", icon="warning")
            if Messagebox == "yes":  # If関数
                self.ZanNameRecalc()
            else:
                tk.messagebox.showinfo("戻る", "アプリケーション画面に戻ります")
        else:
            Messagebox = tk.messagebox.askquestion(
                "開始残高登録", "開始残高を登録し再計算しますか？", icon="warning"
            )
            if Messagebox == "yes":  # If関数
                self.ZanNameRecalc()
            else:
                tk.messagebox.showinfo("戻る", "アプリケーション画面に戻ります")

    # -----------------------------------------------------------------------------------------
    # エントリーウィジェットを削除
    def removeEntry(self):
        for i in self.Treeview_1.get_children():
            self.Treeview_1.delete(i)

    # -----------------------------------------------------------------------------------------
    def InStartVal(self):
        global tr  # 選択行インデックス

        # CSV読込
        enc = CSVO.getFileEncoding(self.FileName)
        with open(self.FileName, "r", encoding=enc) as f:  # csv読込み(Treeview 表示用)
            reader = csv.reader(f, delimiter=",", quotechar='"')
            next(reader)
            CList = list(reader)

        c = 0
        for ColNameItem in self.ColumnName:
            print(CList[tr][c])
            print(self.Entries[c].get())
            CList[tr][c] = str(self.Entries[c].get())
            c += 1
        df = pd.DataFrame(CList, columns=self.ColumnName)
        try:
            df.to_csv(self.FileName, index=False, encoding="cp932")
        except:
            with open(
                self.FileName,
                mode="w",
                encoding="cp932",
                errors="ignore",
                newline="",
            ) as f:
                df.to_csv(f, index=False)

        self.ZanNameRecalc()


def Main(US, Bk, tl):
    global csvurl, Banktoml, tomltitle

    csvurl = US
    Banktoml = Bk
    tomltitle = tl
    # 　Tk MainWindow 生成
    main_window = tk.Tk()
    main_window.withdraw()
    # Viewクラス生成
    DataGrid(main_window, "./")

    # 　フレームループ処理
    main_window.mainloop()


# -----------------------------------------------------------------------------------------
if __name__ == "__main__":
    global csvurl, Banktoml, AJurl, AJSeturl, Roolurl, tomltitle
    csvurl = r"D:\OCRTESTPDF\PDFTEST\JA_1page.csv"
    AJurl = r"D:\OCRTESTPDF\PDFTEST\JA_1page_AutoJounal.csv"
    AJSeturl = r"D:\OCRTESTPDF\PDFTEST\AJSet.csv"
    Roolurl = r"D:\PythonScript\RPAScript\TKInterGUI\Mototyou\18_仕訳日記帳.csv"
    tomltitle = "JA"
    # toml読込------------------------------------------------------------------------------
    with open(os.getcwd() + r"/TKInterGUI/BankSetting.toml", encoding="utf-8") as f:
        Banktoml = toml.load(f)
        print(Banktoml)
    # -----------------------------------------------------------
    # 　Tk MainWindow 生成
    main_window = tk.Tk()
    main_window.withdraw()
    # Viewクラス生成
    DataGrid(main_window, "./")

    # 　フレームループ処理
    main_window.mainloop()
