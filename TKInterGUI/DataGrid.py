import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd
import csv

if __name__ == "__main__":
    FileName = r"D:\OCRTESTPDF\TEST3.csv"
    root = tk.Tk()  # ウインド画面の作成
    root.geometry("600x300")  # 画面サイズの設定
    root.title("家計簿システム")  # 題名

    Treeview_1 = ttk.Treeview(root, show="headings")  # Treeviewの設定

    Treeview_1["columns"] = ("No", "コード", "銘柄名", "単価")  # ヘッダー

    Treeview_1.column("No", width=30)  # 列幅
    Treeview_1.column("コード", width=50)
    Treeview_1.column("銘柄名", width=90)
    Treeview_1.column("単価", width=50)

    Treeview_1.heading("No", text="No")  # タイトル
    Treeview_1.heading("コード", text="コード")
    Treeview_1.heading("銘柄名", text="銘柄名")
    Treeview_1.heading("単価", text="単価")

    Treeview_1.place(x=30, y=50, height=150)  # 位置指定

    with open(FileName, "r", encoding="cp932") as f:  # csv読込み(Treeview 表示用)

        reader = csv.reader(f, delimiter=",", quotechar='"')
        for cells in reader:
            Treeview_1.insert(
                "",
                "end",
                values=(f"{cells[0]}", f"{cells[1]}", f"{cells[2]}", f"{cells[3]}"),
            )  # Treeview にセット

    # 画面の表示
    root.mainloop()
