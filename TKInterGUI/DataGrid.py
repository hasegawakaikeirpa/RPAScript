import tkinter as tk
import tkinter.ttk as ttk

# from tkinter import messagebox
import pandas as pd
import os
import csv
import toml


class DataGrid:
    def __init__(self, window_root, default_path):
        global imgurl, Banktoml, tomltitle

        # toml読込------------------------------------------------------------------------------
        self.Banktoml = Banktoml
        # -----------------------------------------------------------
        self.FileName = imgurl
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
        # メインウィンドウ設定-------------------------------------------------------------------
        self.root = tk.Tk()  # ウインド画面の作成
        self.root.geometry("1400x700")  # 画面サイズの設定
        self.root.title("OCRTEXT")  # 題名
        # -------------------------------------------------------------------------------------
        # フレーム設定--------------------------------------------------------------------------
        self.frame = tk.Frame(self.root)
        self.frame.grid(row=0, column=0)
        self.Treeview_1 = ttk.Treeview(
            self.frame, show="headings", height=30
        )  # Treeviewの設定
        self.Treeview_1[
            "columns"
        ] = self.ColumnName  # ("No", "コード", "銘柄名", "単価")  # ヘッダー
        self.Treeview_1.bind("<<TreeviewSelect>>", self.on_tree_select)
        # -------------------------------------------------------------------------------------
        # フレーム設定--------------------------------------------------------------------------
        self.frame2 = tk.Frame(self.root)
        self.frame2.grid(row=0, column=1, sticky=tk.N)
        # -------------------------------------------------------------------------------------
        # フレーム設定--------------------------------------------------------------------------
        self.frame3 = tk.Frame(self.root)
        self.frame3.grid(row=0, column=1, sticky=tk.W)
        # -------------------------------------------------------------------------------------
        # フレーム設定--------------------------------------------------------------------------
        self.menu = tk.Frame(self.root)
        self.menu.grid(row=0, column=2, sticky=tk.N)
        # -------------------------------------------------------------------------------------
        # フレーム設定--------------------------------------------------------------------------
        self.frame4 = tk.Frame(self.root)
        self.frame4.grid(row=0, column=3, sticky=tk.N)
        # -------------------------------------------------------------------------------------
        # ツリービューを配置
        self.treeviewEntries()
        # tomlListを配置
        self.tomlEntries()

    # -----------------------------------------------------------------------------------------
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

        r = 0
        c = 0
        for ColNameItem in self.ColumnName:
            cMax = []
            with open(
                self.FileName, "r", encoding="cp932"
            ) as f:  # csv読込み(Treeview 表示用)
                reader = csv.reader(f, delimiter=",", quotechar='"')
                for cells in reader:
                    cMax.append(len(f"{cells[c]}".encode()))
                c += 1
                cM = max(cMax)
                cW = int(cM * 10)
                self.Treeview_1.column(ColNameItem, width=cW, stretch="No")  # 列幅
                self.Treeview_1.heading(ColNameItem, text=ColNameItem)  # タイトル
                self.Treeview_1.grid(row=0, column=0)  # 位置指定
                # ラベル＆Entryフレームへ追加----------------------------------------------
                self.createEntry(r, ColNameItem)  # Entryを作成配置
                # ----------------------------------------------------------------------
            r += 1
        r = 0
        # ボタン-------------------------------------------------------------------------
        # 確定ボタン---------------------------------------------------------------------
        self.ebtn = tk.Button(
            self.frame2,
            text="確定",
            width=20,
            command=lambda: self.InStartVal(),
        )
        self.ebtn.grid(row=len(self.indexes), column=0, columnspan=2)  # 位置指定
        # URLテキストボックス-----------------------------------------------------------
        tk.Label(self.menu, text="URL").grid(row=0, column=0)  # 位置指定
        self.Label_URL = tk.Entry(self.menu, width=50)
        self.Label_URL.insert(0, self.FileName)
        self.Label_URL.grid(row=0, column=1, columnspan=3)
        # tomlNameテキストボックス-----------------------------------------------------------
        tk.Label(self.menu, text="設定ファイル名").grid(row=1, column=0)  # 位置指定
        self.Label_ChangeURL = tk.Entry(self.menu, width=15)
        self.Label_ChangeURL.insert(0, tomltitle)
        self.Label_ChangeURL.grid(row=1, column=1, columnspan=3)
        # 摘要列名-----------------------------------------------------------
        # tk.Label(self.menu, text="変換元列名").grid(row=2, column=0)  # 位置指定
        # self.Label_MChangeURL = tk.Entry(self.menu, width=15)
        # self.Label_MChangeURL.insert(0, self.Henkan)
        # self.Label_MChangeURL.grid(row=2, column=1)
        # tk.Label(self.menu, text="変換先列名").grid(row=2, column=2)  # 位置指定
        # self.Label_SChangeURL = tk.Entry(self.menu, width=15)
        # self.Label_SChangeURL.insert(0, self.Henkan)
        # self.Label_SChangeURL.grid(row=2, column=3)
        # 開始残高ボタン----------------------------------------------------------------
        tk.Label(self.frame3, text="開始残高").grid(
            row=len(self.indexes) + 1, column=0
        )  # 位置指定
        self.ZanNametxt = tk.Entry(self.frame3, width=15)
        self.ZanNametxt.grid(row=len(self.indexes) + 1, column=1)  # 位置指定
        self.ebtn2 = tk.Button(
            self.frame3,
            text="再計算",
            width=20,
            command=lambda: self.ZanNamedaka(),
        )
        self.ebtn2.grid(row=len(self.indexes) + 2, column=0, columnspan=2)  # 位置指定
        # ------------------------------------------------------------------------------
        with open(
            self.FileName,
            "r",
            encoding="cp932",
            errors="ignore",
            newline="",
        ) as f:  # csv読込み(Treeview 表示用)
            reader = csv.reader(f, delimiter=",", quotechar='"')
            for cells in reader:
                if not r == 0:
                    cvalue = []
                    for c in range(len(self.ColumnName)):
                        cvalue.append(f"{cells[c]}")
                    self.Treeview_1.insert(
                        "",
                        "end",
                        values=cvalue,
                    )  # Treeview にセット
                r += 1
        ysb = tk.Scrollbar(
            self.frame, orient=tk.VERTICAL, width=16, command=self.Treeview_1.yview
        )
        self.Treeview_1.configure(yscrollcommand=ysb.set)
        ysb.grid(row=0, column=1, sticky="news")  # 位置指定

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
        with open(self.FileName, "r", encoding="cp932") as f:  # csv読込み(Treeview 表示用)
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
        with open(self.FileName, "r", encoding="cp932") as f:  # csv読込み(Treeview 表示用)
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
    # エントリーウィジェットを再配置
    def updateEntries(self):

        # エントリーウィジェットマネージャを参照して再配置
        for i in range(len(self.indexes)):
            self.Entries[i].grid(column=1, row=i)
            self.Entries[i].bind("<Return>", self.EveRecalc)
            self.Entries[i].lift()
            self.insertEntries[i].grid(column=0, row=i)

    # -----------------------------------------------------------------------------------------
    # エントリーウィジェットを作成して配置
    def createEntry(self, next, ColNameItem):

        # 最初のエントリーウィジェットを追加
        self.Entries.insert(next, tk.Entry(self.frame2, width=20))
        lb = tk.Label(self.frame2, text=ColNameItem)

        lb.grid(row=next, column=0)  # 位置指定

        txtxt = tk.Entry(self.frame2, width=15)

        txtxt.grid(row=next, column=1)  # 位置指定
        # ラベルを作成
        self.insertEntries.insert(
            next,
            tk.Label(
                self.frame2,
                text=str(ColNameItem),
            ),
        )
        # インデックスマネージャに登録
        self.indexes.insert(next, self.index)
        # 再配置
        self.updateEntries()

    # -----------------------------------------------------------------------------------------
    def on_tree_select(self, event=None):
        global tr  # 選択行インデックス

        """
        ツリービュークリックイベント
        """
        # 全てのEntryを空に
        for i in range(len(self.Entries)):
            self.Entries[i].delete(0, tk.END)
        # 選択行のテキスト取得
        for item in self.Treeview_1.selection():
            item_text = self.Treeview_1.item(item, "values")
            tr = self.Treeview_1.index(item)  # 選択行インデックス
        # 全てのEntryにテキスト挿入
        for i in range(len(item_text)):
            self.Entries[i].insert(i, item_text[i])

    # -----------------------------------------------------------------------------------------
    def InStartVal(self):
        global tr  # 選択行インデックス

        # CSV読込
        with open(self.FileName, "r", encoding="cp932") as f:  # csv読込み(Treeview 表示用)
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
    global imgurl, Banktoml, tomltitle

    imgurl = US
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
    global imgurl, Banktoml, tomltitle
    imgurl = r"D:\OCRTESTPDF\PDFTEST\JA_1page.csv"
    # Roolurl = r"D:\PythonScript\RPAScript\TKInterGUI\Mototyou\18_仕訳日記帳.csv"
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
