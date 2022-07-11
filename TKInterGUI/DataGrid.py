import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd
import os
import csv
import toml

if __name__ == "__main__":
    # toml読込------------------------------------------------------------------------------
    with open(os.getcwd() + r"/TKInterGUI/BankSetting.toml", encoding="utf-8") as f:
        Banktoml = toml.load(f)
        print(Banktoml)
    # -----------------------------------------------------------
    FileName = r"D:\OCRTESTPDF\TEST3.csv"
    ColName = Banktoml["HiroginSouzoku"]["ColumnName"]

    root = tk.Tk()  # ウインド画面の作成
    root.geometry("1400x800")  # 画面サイズの設定
    root.title("家計簿システム")  # 題名
    frame = tk.Frame(root)
    frame.place(x=30, y=50, width=1400, height=800)
    Treeview_1 = ttk.Treeview(frame, show="headings", height=800)  # Treeviewの設定

    Treeview_1["columns"] = ColName  # ("No", "コード", "銘柄名", "単価")  # ヘッダー
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
            Treeview_1.column(ColNameItem, width=cW, stretch="No")  # 列幅
            Treeview_1.heading(ColNameItem, text=ColNameItem)  # タイトル
            Treeview_1.grid(row=0, column=0, sticky=tk.N + tk.S)  # 位置指定
        # with open(FileName, "r", encoding="cp932") as f:  # csv読込み(Treeview 表示用)
        #     cMax = []
        #     reader = csv.reader(f, delimiter=",", quotechar='"')
        r = 0
    with open(FileName, "r", encoding="cp932") as f:  # csv読込み(Treeview 表示用)
        reader = csv.reader(f, delimiter=",", quotechar='"')
        for cells in reader:
            if not r == 0:
                cvalue = []
                for c in range(len(ColName)):
                    cvalue.append(f"{cells[c]}")
                Treeview_1.insert(
                    "",
                    "end",
                    values=cvalue,  # (f"{cells[0]}", f"{cells[1]}", f"{cells[2]}", f"{cells[3]}"),
                )  # Treeview にセット
            r += 1
    ysb = tk.Scrollbar(frame, orient=tk.VERTICAL, width=16, command=Treeview_1.yview)
    Treeview_1.configure(yscrollcommand=ysb.set)
    ysb.grid(row=0, column=1, sticky=tk.N + tk.S)  # sticky="news")  # 位置指定
    Treeview_1.grid_rowconfigure(1, weight=1)
    # 画面の表示
    root.mainloop()
