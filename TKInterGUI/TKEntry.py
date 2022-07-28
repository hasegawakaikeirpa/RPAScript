import tkinter as tk
from datetime import datetime as dt
import WarekiHenkan as wh
import AutoJournal as AJ

# -----------------------------------------------------------------------------------------
def tomlEntries(self, tomltitle):
    self.tomlEntries = []  # Entryのインスタンス
    self.tomlinsertEntries = []  # ラベルインスタンス
    self.tomlindex = 0  # 最新のインデックス番号
    self.tomlindexes = []  # インデックスの並び
    self.entryList = []  # Entryのインスタンス

    r = 0
    for ColNameItem in self.tomlList:
        # ラベル＆Entryフレームへ追加----------------------------------------------
        createtomlEntry(self, r, ColNameItem, tomltitle)  # Entryを作成配置
        self.entryList.append(ColNameItem)
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
def createtomlEntry(self, next, ColNameItem, tomltitle):

    # 最初のエントリーウィジェットを追加
    # self.tomlEntries.insert(next, tk.Entry(self.frame4, width=20))
    lb = tk.Label(self.frame4, text=ColNameItem)

    lb.grid(row=next, column=0)  # 位置指定
    cn = self.Banktoml["ParList"][ColNameItem]
    tom = self.Banktoml[tomltitle][cn]
    tomtx = ""
    try:
        print(type(tom).__name__)
        if type(tom).__name__ == "list":
            txtxt = tk.Entry(self.frame4, width=10)
            for tomItem in tom:
                tomtx += "," + str(tomItem)
            tomtx = tomtx.lstrip(",")
            txtxt.insert(0, tomtx)
        else:
            txtxt = tk.Entry(self.frame4, width=10)
            txtxt.insert(0, tom)
    except:
        txtxt = tk.Entry(self.frame4, width=10)
        txtxt.insert(0, tom)
    txtxt.grid(row=next, column=1)  # 位置指定

    self.tomlEntries.insert(next, txtxt)

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
def treeviewEntries(self, tomltitle):
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
    self.Label_URL = tk.Entry(self.frame3, width=10)
    self.Label_URL.insert(0, self.FileName)
    self.Label_URL.grid(row=0, column=1, columnspan=3)
    # tomlNameテキストボックス-----------------------------------------------------------
    tk.Label(self.frame3, text="設定ファイル名").grid(row=1, column=0)  # 位置指定
    self.Label_ChangeURL = tk.Entry(self.frame3, width=10)
    self.Label_ChangeURL.insert(0, tomltitle)
    self.Label_ChangeURL.grid(row=1, column=1, columnspan=3)
    # 開始残高ボタン----------------------------------------------------------------
    tk.Label(self.frame3, text="開始残高").grid(row=len(self.indexes) + 2, column=0)  # 位置指定
    self.ZanNametxt = tk.Entry(self.frame3, width=10)
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
# エントリーウィジェットを削除
def removeEntry(self):
    for i in self.Treeview_1.get_children():
        self.Treeview_1.delete(i)


# -----------------------------------------------------------------------------------------
# エントリーウィジェットを作成して配置
def Frame7createtomlEntry(self, next, AJL, AJR):
    if type(AJL) == list:
        # ---------------------------------------------
        txtxt = tk.Entry(self.frame7, width=10)
        txtxt.insert(0, AJL[next])
        txtxt.grid(row=next + 1, column=0)  # 位置指定
        # Entrマネージャに登録
        self.Frame7EntL.insert(next, txtxt)
        # ---------------------------------------------
        lab = tk.Label(self.frame7, text="→", width=2)
        lab.grid(row=next + 1, column=1)  # 位置指定
        # Entrマネージャに登録
        self.Frame7Labels.insert(next, lab)
        # ---------------------------------------------
        txtxt = tk.Entry(self.frame7, width=10)
        txtxt.insert(0, AJR[next])
        txtxt.grid(row=next + 1, column=2)  # 位置指定
        # Entrマネージャに登録
        self.Frame7EntR.insert(next, txtxt)
        # ---------------------------------------------
        Btn = tk.Button(
            self.frame7,
            text="X",
            width=5,
        )
        Btn.bind("<Button-1>", AJ_EntDelete)
        Btn.grid(row=next + 1, column=3)
        # Entrマネージャに登録
        self.Frame7Btns.insert(next, Btn)
        # ---------------------------------------------
    else:
        # ---------------------------------------------
        txtxt = tk.Entry(self.frame7, width=10)
        txtxt.insert(0, AJL)
        txtxt.grid(row=next + 1, column=0)  # 位置指定
        # Entrマネージャに登録
        self.Frame7EntL.insert(next, txtxt)
        # ---------------------------------------------
        lab = tk.Label(self.frame7, text="→", width=2)
        lab.grid(row=next + 1, column=1)  # 位置指定
        # Entrマネージャに登録
        self.Frame7Labels.insert(next, lab)
        # ---------------------------------------------
        txtxt = tk.Entry(self.frame7, width=10)
        txtxt.insert(0, AJR)
        txtxt.grid(row=next + 1, column=2)  # 位置指定
        # Entrマネージャに登録
        self.Frame7EntR.insert(next, txtxt)
        # ---------------------------------------------
        Btn = tk.Button(
            self.frame7,
            text="X",
            width=5,
        )
        Btn.bind("<Button-1>", AJ_EntDelete)
        Btn.grid(row=next + 1, column=3)
        # Entrマネージャに登録
        self.Frame7Btns.insert(next, Btn)
        # ---------------------------------------------


# -----------------------------------------------------------------------------------------
def Frame7Entries(self):
    global g_Frame7EntL
    global g_Frame7EntR
    global g_Frame7Labels
    global g_Frame7Btns

    self.Frame7EntL = []  # Entryのインスタンス
    self.Frame7EntR = []  # Entryのインスタンス
    self.Frame7Labels = []  # Entryのインスタンス
    self.Frame7Btns = []  # Entryのインスタンス
    self.Frame7index = 0  # 最新のインデックス番号
    self.Frame7entryList = []  # Entryのインスタンス

    AJL = ["伝票日付", "金額", "金額"]
    AJR = ["日付", "入金", "出金"]

    self.frame7RowList = []
    for r in range(len(AJL)):
        # ラベル＆Entryフレームへ追加----------------------------------------------
        Frame7createtomlEntry(self, r, AJL, AJR)  # Entryを作成配置
        # self.Frame7entryList.append(ColNameItem)
        # ----------------------------------------------------------------------
    g_Frame7EntL = self.Frame7EntL
    g_Frame7EntR = self.Frame7EntR
    g_Frame7Labels = self.Frame7Labels
    g_Frame7Btns = self.Frame7Btns


# -----------------------------------------------------------------------------------------
def AJ_setCalc(self):
    if self.pt.startcol is None:
        tk.messagebox.showinfo("確認", "OCR表のセルが選択されていません。変換元の列のセルを選択して下さい。")
    else:
        try:
            if self.pt3.startcol is None:
                tk.messagebox.showinfo("確認", "抽出仕訳表のセルが選択されていません。変換先の列のセルを選択して下さい。")
            else:
                dfs = self.pt.model.df  # グリッドをDF化
                dfs3 = self.pt3.model.df  # グリッドをDF化
                dfs_c = dfs.columns.tolist()
                dfs3_c = dfs3.columns.tolist()
                dfs_c_Name = dfs_c[self.pt.startcol]
                dfs3_c_Name = dfs3_c[self.pt3.startcol]
                Messagebox = tk.messagebox.askquestion(
                    "確認",
                    "抽出仕訳表の[" + dfs3_c_Name + "]列をOCR表の[" + dfs_c_Name + "]列に変換しますか？",
                    icon="warning",
                )
                r = len(g_Frame7EntL)
                if Messagebox == "yes":  # If関数
                    # ラベル＆Entryフレームへ追加----------------------------------------------
                    Frame7createtomlEntry(
                        self, r, dfs3_c_Name, dfs_c_Name
                    )  # Entryを作成配置
                    # self.Frame7entryList.append([dfs_c_Name, dfs3_c_Name])
                    # ----------------------------------------------------------------------
        except:
            tk.messagebox.showinfo("確認", "抽出仕訳表のセルが選択されていません。変換先の列のセルを選択して下さい。")


# -----------------------------------------------------------------------------------------
def AJ_EntDelete(self):
    Frame7removeEntry(self)
    wid_n = self.widget
    for g_r in range(len(g_Frame7EntL)):
        if wid_n == g_Frame7Btns[g_r]:
            g_Frame7EntL.pop(g_r)
            g_Frame7EntR.pop(g_r)
            g_Frame7Labels.pop(g_r)
            g_Frame7Btns.pop(g_r)

    Frame7updatetomlEntries(self)


# -----------------------------------------------------------------------------------------
def Frame7updatetomlEntries(self):
    """
    エントリーウィジェットを再配置
    """
    # エントリーウィジェットマネージャを参照して再配置
    for i in range(len(g_Frame7EntL)):
        g_Frame7EntL[i].grid(row=i + 1, column=0)
    for i in range(len(g_Frame7EntR)):
        g_Frame7EntR[i].grid(row=i + 1, column=2)
    for i in range(len(g_Frame7Labels)):
        g_Frame7Labels[i].grid(row=i + 1, column=1)
    for i in range(len(g_Frame7Btns)):
        g_Frame7Btns[i].grid(row=i + 1, column=3)
        g_Frame7Btns[i].bind("<Button-1>", AJ_EntDelete)
    # -----------------------------------------------------------------------------------------
    # エントリーウィジェットを削除


# -----------------------------------------------------------------------------------------
def Frame7removeEntry(self):
    """
    エントリーウィジェットを削除
    """
    # Btn_n = self.widget
    for i in g_Frame7EntL:
        # i.destroy()
        i.grid_forget()
    for i in g_Frame7EntR:
        # i.destroy()
        i.grid_forget()
    for i in g_Frame7Labels:
        # i.destroy()
        i.grid_forget()
    for i in g_Frame7Btns:
        # i.destroy()
        i.grid_forget()


# ----------------------------------------------------------------------------
def TxtEdit(Txt, L_txt, R_txt):
    """
    R_txtの書式をL_txtの書式と揃える
    """

    if "日" in Txt:
        L_txt = (
            L_txt.replace("-", "/")
            .replace("_", "/")
            .replace("\\", "/")
            .replace(".", "")
            .replace("|", "")
            .replace("\\", "")
            .replace(":", "")
            .replace("^", "")
            .replace("~", "")
        )

        R_txt = (
            R_txt.replace("-", "/")
            .replace("_", "/")
            .replace("\\", "/")
            .replace(".", "")
            .replace("|", "")
            .replace("\\", "")
            .replace(":", "")
            .replace("^", "")
            .replace("~", "")
        )
        L_txtSp = L_txt.split("/")
        R_txtSp = R_txt.split("/")
        if len(L_txtSp[0]) < 4:
            L_y = wh.R(int(L_txtSp[0])).to_ad()
            L_txtSp[0] = str(L_y)
            L_txt = "/".join(L_txtSp)
        if len(R_txtSp[0]) < 4:
            R_y = wh.R(int(R_txtSp[0])).to_ad()
            R_txtSp[0] = str(R_y)
            R_txt = "/".join(R_txtSp)
        L_d = dt.strptime(L_txt, "%Y/%m/%d")
        R_d = dt.strptime(R_txt, "%Y/%m/%d")
        L_txt = str(L_d.year) + "/" + str(L_d.month) + "/" + str(L_d.day)
        R_txt = str(R_d.year) + "/" + str(R_d.month) + "/" + str(R_d.day)
        return L_txt, R_txt
    else:
        return L_txt, R_txt


# ----------------------------------------------------------------------------
def AJ_copyCalc_Func(dfsrow, dfs3row):
    """
    自動仕訳候補OCR結果
    """
    for E_r in range(len(g_Frame7EntL)):
        L_txt = g_Frame7EntL[E_r].get()
        R_txt = g_Frame7EntR[E_r].get()
        if dfsrow[R_txt] != dfsrow[R_txt]:
            print("nan")
        else:
            Txt = TxtEdit(L_txt, dfs3row[L_txt], dfsrow[R_txt])
            dfs3row[L_txt] = Txt[1]
    del dfs3row["一致率"]
    del dfs3row["仕訳金額差額"]
    del dfs3row["日付一致率"]
    return dfs3row
