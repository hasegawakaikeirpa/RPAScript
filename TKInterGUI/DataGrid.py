import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd
import os
import csv
import toml


class DataGrid:
    def __init__(self, window_root, default_path):
        # toml読込------------------------------------------------------------------------------
        with open(os.getcwd() + r"/TKInterGUI/BankSetting.toml", encoding="utf-8") as f:
            Banktoml = toml.load(f)
            print(Banktoml)
        # -----------------------------------------------------------
        FileName = r"D:\OCRTESTPDF\TEST3.csv"
        ColName = Banktoml["HiroginSouzoku"]["ColumnName"]
        # メインウィンドウ設定-------------------------------------------------------------------
        self.root = tk.Tk()  # ウインド画面の作成
        self.root.geometry("1400x700")  # 画面サイズの設定
        self.root.title("家計簿システム")  # 題名
        # -------------------------------------------------------------------------------------
        # フレーム設定--------------------------------------------------------------------------
        self.frame = tk.Frame(self.root)
        self.frame.grid(row=0, column=0)
        self.Treeview_1 = ttk.Treeview(
            self.frame, show="headings", height=30
        )  # Treeviewの設定
        self.Treeview_1["columns"] = ColName  # ("No", "コード", "銘柄名", "単価")  # ヘッダー
        self.Treeview_1.bind("<<TreeviewSelect>>", self.on_tree_select)
        # -------------------------------------------------------------------------------------
        # フレーム設定--------------------------------------------------------------------------
        self.frame2 = tk.Frame(self.root)
        self.frame2.grid(row=0, column=1)
        # -------------------------------------------------------------------------------------

        self.treeviewEntries(Banktoml, FileName, ColName)
        # # エントリーウィジェットマネージャを初期化
        # self.Entries = []  # Entryのインスタンス
        # self.insertEntries = []  # ラベルインスタンス
        # # インデックスマネージャを初期化
        # self.index = 0  # 最新のインデックス番号
        # self.indexes = []  # インデックスの並び
        # for ColNameItem in ColName:
        #     cMax = []
        #     with open(FileName, "r", encoding="cp932") as f:  # csv読込み(Treeview 表示用)
        #         reader = csv.reader(f, delimiter=",", quotechar='"')
        #         for cells in reader:
        #             cMax.append(len(f"{cells[c]}".encode()))
        #         c += 1
        #         cM = max(cMax)
        #         cW = int(cM * 10)
        #         self.Treeview_1.column(ColNameItem, width=cW, stretch="No")  # 列幅
        #         self.Treeview_1.heading(ColNameItem, text=ColNameItem)  # タイトル
        #         self.Treeview_1.grid(row=0, column=0)  # 位置指定
        #         # ラベル＆Entryフレームへ追加----------------------------------------------
        #         self.createEntry(r, ColNameItem, Banktoml, FileName)  # Entryを作成配置
        #         # ----------------------------------------------------------------------
        #     r += 1
        r = 0
        # ボタン
        self.ebtn = tk.Button(
            self.frame2,
            text="確定",
            width=20,
            command=lambda: self.InStartVal(Banktoml, FileName, ColName),
        )
        self.ebtn.grid(row=len(self.indexes), column=0, columnspan=2)  # 位置指定
        with open(FileName, "r", encoding="cp932") as f:  # csv読込み(Treeview 表示用)
            reader = csv.reader(f, delimiter=",", quotechar='"')
            for cells in reader:
                if not r == 0:
                    cvalue = []
                    for c in range(len(ColName)):
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
    # ツリービューを再配置
    def treeviewEntries(self, Banktoml, FileName, ColName):
        # エントリーウィジェットマネージャを初期化
        self.Entries = []  # Entryのインスタンス
        self.insertEntries = []  # ラベルインスタンス
        # インデックスマネージャを初期化
        self.index = 0  # 最新のインデックス番号
        self.indexes = []  # インデックスの並び
        r = 0
        c = 0
        for ColNameItem in ColName:
            cMax = []
            with open(FileName, "r", encoding="cp932") as f:  # csv読込み(Treeview 表示用)
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
                self.createEntry(r, ColNameItem, Banktoml, FileName)  # Entryを作成配置
                # ----------------------------------------------------------------------
            r += 1

    # -----------------------------------------------------------------------------------------
    # エントリーウィジェットを再配置
    def updateEntries(self, Banktoml, FileName):

        # エントリーウィジェットマネージャを参照して再配置
        for i in range(len(self.indexes)):
            self.Entries[i].grid(column=1, row=i)
            self.Entries[i].lift()
            self.insertEntries[i].grid(column=0, row=i)

    # -----------------------------------------------------------------------------------------
    # エントリーウィジェットを作成して配置
    def createEntry(self, next, ColNameItem, Banktoml, FileName):

        # 最初のエントリーウィジェットを追加
        self.Entries.insert(next, tk.Entry(self.frame2, width=20))
        tk.Label(self.frame2, text=ColNameItem).grid(row=next, column=0)  # 位置指定
        tk.Entry(self.frame2, width=15).grid(row=next, column=1)  # 位置指定
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
        self.updateEntries(Banktoml, FileName)

    # -----------------------------------------------------------------------------------------
    def on_tree_select(self, event):
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
    def InStartVal(self, Banktoml, FileName, ColName):
        global tr  # 選択行インデックス

        Nyu = Banktoml["HiroginSouzoku"]["NyuName"]
        Syutu = Banktoml["HiroginSouzoku"]["SyutuName"]
        Zan = Banktoml["HiroginSouzoku"]["ZanName"]
        # CSV読込
        with open(FileName, "w", encoding="cp932") as f:  # csv読込み(Treeview 表示用)
            reader = csv.reader(f, delimiter=",", quotechar='"')
            CList = list(reader)
            print(CList)

        c = 0
        for ColNameItem in ColName:
            print(self.Entries[c].get())
            df[dfloc[ColNameItem]] = str(self.Entries[c].get())
            c += 1

        print(
            "#########################################################################"
        )
        print(df)
        df.to_csv(FileName, encoding="cp932", index=False)
        self.treeviewEntries(Banktoml, FileName, ColName)


# -----------------------------------------------------------------------------------------
if __name__ == "__main__":
    # 　Tk MainWindow 生成
    main_window = tk.Tk()

    # Viewクラス生成
    DataGrid(main_window, "./")

    # 　フレームループ処理
    main_window.mainloop()
