# from msilib.schema import ListBox
import tkinter as tk
from datetime import datetime as dt
import WarekiHenkan as wh
import tomlCreate as toml_c
import customtkinter as ck

# -----------------------------------------------------------------------------------------
def tomlEntries(self):  # , tomltitle):
    """
    概要: tomlファイルのインポート
    """
    global Banktoml, tomlParList, tomlurl
    self.tomlEntries = []  # Entryのインスタンス
    self.tomlinsertEntries = []  # ラベルインスタンス
    self.tomlindex = 0  # 最新のインデックス番号
    self.tomlindexes = []  # インデックスの並び
    self.entryList = []  # Entryのインスタンス
    Banktoml = self.Banktoml
    tomlParList = self.tomlParList
    tomlurl = self.BanktomlUrl
    r = 0
    for ColNameItem in self.tomlList:
        # ラベル＆Entryフレームへ追加----------------------------------------------
        createtomlEntry(self, r, ColNameItem)  # , tomltitle)  # Entryを作成配置
        self.entryList.append(ColNameItem)
        # ----------------------------------------------------------------------
        r += 1


# -----------------------------------------------------------------------------------------
# エントリーウィジェットを再配置
def updatetomlEntries(self):
    """
    概要: toml要素の再配置
    """
    # エントリーウィジェットマネージャを参照して再配置
    for i in range(len(self.tomlindexes)):
        self.tomlEntries[i].grid(column=1, row=i)
        self.tomlEntries[i].bind("<Return>", self.EveRecalc)
        self.tomlEntries[i].lift()
        self.tomlinsertEntries[i].grid(column=0, row=i)


# -----------------------------------------------------------------------------------------
# エントリーウィジェットを作成して配置
def createtomlEntry(self, next, ColNameItem):  # , tomltitle):
    """
    概要: toml要素の作成
    """
    global HidukeColNo, MoneyCol, ChangeTextCol, HidukeColName, NyuName
    global SyutuName, ZanName, Henkan, Hani
    # 最初のエントリーウィジェットを追加
    lb = ck.CTkLabel(
        master=self.frame4,
        text=ColNameItem,
        width=self.LabelWidth,
        height=self.LabelHeight,
        corner_radius=8,
        text_font=self.t_font,
    )
    lb.grid(row=next, column=0)  # 位置指定
    # ラベル名からself変数を取得---------------------------------------
    if ColNameItem == "日付列":
        Par = self.tomlParList[ColNameItem]
        tom = Par
        self.HidukeColNo = tomEntry(self, next, tom)
        self.HidukeColNo._name = "日付列"
        HidukeColNo = self.HidukeColNo

    elif ColNameItem == "金額列":
        Par = self.tomlParList[ColNameItem]
        tom = Par
        self.MoneyCol = tomEntry(self, next, tom)
        self.MoneyCol._name = "金額列"
        MoneyCol = self.MoneyCol

    elif ColNameItem == "変換対象列":
        Par = self.tomlParList[ColNameItem]
        tom = Par
        self.ChangeTextCol = tomEntry(self, next, tom)
        self.ChangeTextCol._name = "変換対象列"
        ChangeTextCol = self.ChangeTextCol

    elif ColNameItem == "日付列名":
        Par = self.tomlParList[ColNameItem]
        tom = Par
        self.HidukeColName = tomEntry(self, next, tom)
        self.HidukeColName._name = "日付列名"
        HidukeColName = self.HidukeColName

    elif ColNameItem == "入金列名":
        Par = self.tomlParList[ColNameItem]
        tom = Par
        self.NyuName = tomEntry(self, next, tom)
        self.NyuName._name = "入金列名"
        NyuName = self.NyuName

    elif ColNameItem == "出金列名":
        Par = self.tomlParList[ColNameItem]
        tom = Par
        self.SyutuName = tomEntry(self, next, tom)
        self.SyutuName._name = "出金列名"
        SyutuName = self.SyutuName

    elif ColNameItem == "残高列名":
        Par = self.tomlParList[ColNameItem]
        tom = Par
        self.ZanName = tomEntry(self, next, tom)
        self.ZanName._name = "残高列名"
        ZanName = self.ZanName

    elif ColNameItem == "自動仕訳基準列名":
        Par = self.tomlParList[ColNameItem]
        tom = Par
        self.Henkan = tomEntry(self, next, tom)
        self.Henkan._name = "自動仕訳基準列名"
        Henkan = self.Henkan

    elif ColNameItem == "自動仕訳検索範囲月":
        Par = self.tomlParList[ColNameItem]
        tom = Par
        self.Hani = tomEntry(self, next, tom)
        self.Hani._name = "自動仕訳検索範囲月"
        Hani = self.Hani
    # ---------------------------------------------------------------
    # ラベルを作成
    self.tomlinsertEntries.insert(
        next,
        ck.CTkLabel(
            master=self.frame4,
            text=ColNameItem,
            width=self.LabelWidth,
            height=self.LabelHeight,
            corner_radius=8,
            text_font=self.t_font,
        ),
    )

    # インデックスマネージャに登録
    self.tomlindexes.insert(next, self.tomlindex)
    # 再配置
    # self.updatetomlEntries()


# -----------------------------------------------------------------------------------------
# エントリーウィジェットを作成して配置
def tomEntry(self, next, tom):
    tomtx = ""
    # self変数がリストの場合文字列に変換-------------------------------
    try:
        print(type(tom).__name__)
        if type(tom).__name__ == "list":
            # txtxt = tk.Entry(self.frame4, width=10)
            txtxt = ck.CTkEntry(
                master=self.frame4,
                width=self.EntWidth,
                height=self.EntHeight,
                border_width=2,
                corner_radius=8,
                text_color="black",
                border_color="snow",
                fg_color="snow",
            )
            for tomItem in tom:
                tomtx += "," + str(tomItem)
            tomtx = tomtx.lstrip(",")
            txtxt.insert(0, tomtx)
        else:
            # txtxt = tk.Entry(self.frame4, width=10)
            txtxt = ck.CTkEntry(
                master=self.frame4,
                width=self.EntWidth,
                height=self.EntHeight,
                border_width=2,
                corner_radius=8,
                text_color="black",
                border_color="snow",
                fg_color="snow",
            )
            txtxt.insert(0, tom)
    except:
        # txtxt = tk.Entry(self.frame4, width=10)
        txtxt = ck.CTkEntry(
            master=self.frame4,
            width=self.EntWidth,
            height=self.EntHeight,
            border_width=2,
            corner_radius=8,
            text_color="black",
            border_color="snow",
            fg_color="snow",
        )
        txtxt.insert(0, tom)
    # ---------------------------------------------------------------
    txtxt.grid(row=next, column=1)  # 位置指定
    txtxt.bind("<Return>", tomlreturn)
    self.tomlEntries.insert(next, txtxt)
    return txtxt


# -----------------------------------------------------------------------------------------
def tomlreturn(self):
    """
    toml変換設定の更新
    """
    ParListName = self.widget._name
    if ParListName == "日付列":
        ParTxt = HidukeColNo.get()
        tomlreturn_sub(ParListName, ParTxt)
    elif ParListName == "金額列":
        ParTxt = MoneyCol.get()
        tomlreturn_sub(ParListName, ParTxt)
    elif ParListName == "変換対象列":
        ParTxt = ChangeTextCol.get()
        tomlreturn_sub(ParListName, ParTxt)
    elif ParListName == "日付列名":
        ParTxt = HidukeColName.get()
        tomlreturn_sub(ParListName, ParTxt)
    elif ParListName == "入金列名":
        ParTxt = NyuName.get()
        tomlreturn_sub(ParListName, ParTxt)
    elif ParListName == "出金列名":
        ParTxt = SyutuName.get()
        tomlreturn_sub(ParListName, ParTxt)
    elif ParListName == "残高列名":
        ParTxt = ZanName.get()
        tomlreturn_sub(ParListName, ParTxt)
    elif ParListName == "自動仕訳基準列名":
        ParTxt = Henkan.get()
        tomlreturn_sub(ParListName, ParTxt)
    elif ParListName == "自動仕訳検索範囲月":
        ParTxt = Hani.get()
        tomlreturn_sub(ParListName, ParTxt)

    toml_c.dump_toml(Banktoml, tomlurl)


# -----------------------------------------------------------------------------------------
def tomlreturn_sub(ParListName, ParTxt):
    """
    toml変換設定の更新確定
    """
    if "," not in ParTxt:
        l = []
        l.append(ParTxt)
        Banktoml["ParList"][ParListName] = l
    else:
        l = ParTxt.split(",")
        Banktoml["ParList"][ParListName] = l


# -----------------------------------------------------------------------------------------
def treeviewEntries(self):  # , tomltitle):
    """
    URL指定ツリービューを配置
    """
    # エントリーウィジェットマネージャを初期化
    self.Entries = []  # Entryのインスタンス
    self.insertEntries = []  # ラベルインスタンス
    # インデックスマネージャを初期化
    self.index = 0  # 最新のインデックス番号
    self.indexes = []  # インデックスの並び

    # URLテキストボックス-----------------------------------------------------------
    # tk.Label(self.frame3, text="仕訳一致率").grid(row=0, column=0)  # 位置指定
    ck.CTkLabel(
        master=self.frame3,
        text="仕訳一致率",
        width=self.LabelWidth,
        height=self.LabelHeight,
        corner_radius=8,
        text_font=self.t_font,
    ).grid(
        row=0, column=0
    )  # 位置指定
    # self.SortVar = tk.Entry(self.frame3, width=10)
    self.SortVar = ck.CTkEntry(
        master=self.frame3,
        width=self.EntWidth,
        height=self.EntHeight,
        border_width=2,
        corner_radius=8,
        text_color="black",
        border_color="snow",
        fg_color="snow",
    )
    self.SortVar.insert(0, 50)
    self.SortVar.grid(row=0, column=1, columnspan=3)
    # URLテキストボックス-----------------------------------------------------------
    # tk.Label(self.frame3, text="OCRURL").grid(row=1, column=0)  # 位置指定
    ck.CTkLabel(
        master=self.frame3,
        text="OCRURL",
        width=self.LabelWidth,
        height=self.LabelHeight,
        corner_radius=8,
        text_font=self.t_font,
    ).grid(
        row=1, column=0
    )  # 位置指定
    # self.Label_URL = tk.Entry(self.frame3, width=10)
    self.Label_URL = ck.CTkEntry(
        master=self.frame3,
        width=self.EntWidth,
        height=self.EntHeight,
        border_width=2,
        corner_radius=8,
        text_color="black",
        border_color="snow",
        fg_color="snow",
    )
    self.Label_URL.insert(0, self.FileName)
    self.Label_URL.grid(row=1, column=1, columnspan=3)
    # 出力先テキストボックス-----------------------------------------------------------
    # tk.Label(self.frame3, text="出力先URL").grid(row=2, column=0)  # 位置指定
    ck.CTkLabel(
        master=self.frame3,
        text="出力先URL",
        width=self.LabelWidth,
        height=self.LabelHeight,
        corner_radius=8,
        text_font=self.t_font,
    ).grid(
        row=2, column=0
    )  # 位置指定
    # self.Label_OutURL = tk.Entry(self.frame3, width=10)
    self.Label_OutURL = ck.CTkEntry(
        master=self.frame3,
        width=self.EntWidth,
        height=self.EntHeight,
        border_width=2,
        corner_radius=8,
        text_color="black",
        border_color="snow",
        fg_color="snow",
    )
    self.Label_OutURL.insert(0, self.JounalFileName)
    self.Label_OutURL.grid(row=2, column=1, columnspan=3)
    # 元帳URLテキストボックス-----------------------------------------------------------
    # tk.Label(self.frame3, text="元帳URL").grid(row=3, column=0)  # 位置指定
    ck.CTkLabel(
        master=self.frame3,
        text="元帳URL",
        width=self.LabelWidth,
        height=self.LabelHeight,
        corner_radius=8,
        text_font=self.t_font,
    ).grid(
        row=3, column=0
    )  # 位置指定
    # self.Label_ChangeURL = tk.Entry(self.frame3, width=10)
    self.Label_ChangeURL = ck.CTkEntry(
        master=self.frame3,
        width=self.EntWidth,
        height=self.EntHeight,
        border_width=2,
        corner_radius=8,
        text_color="black",
        border_color="snow",
        fg_color="snow",
    )
    self.Label_ChangeURL.insert(0, self.Roolurl)
    self.Label_ChangeURL.grid(row=3, column=1, columnspan=3)
    # URL指定ボタン-------------------------------------------------------------
    # self.URL_In = tk.Button(
    #     self.frame3,
    #     text="OCR抽出結果CSV選択",
    #     width=20,
    #     bg="LemonChiffon",
    #     command=self.OCR_Open,
    # )
    self.URL_In = ck.CTkButton(
        master=self.frame3,
        text="設定ファイル変更",
        command=self.OCR_Open,
        width=self.BtnWidth,
        height=self.BtnHeight,
        border_width=2,
        corner_radius=8,
        text_color="black",
        border_color="snow",
        fg_color="#ffcb21",
    )
    self.URL_In.grid(row=4, column=0, columnspan=2, sticky=tk.W + tk.E)  # 位置指定
    # self.URL_In2 = tk.Button(
    #     self.frame3,
    #     text="出力先CSV選択",
    #     width=20,
    #     bg="Honeydew",
    #     command=self.Out_Open,
    # )
    self.URL_In2 = ck.CTkButton(
        master=self.frame3,
        text="出力先CSV選択",
        command=self.Out_Open,
        width=self.BtnWidth,
        height=self.BtnHeight,
        border_width=2,
        corner_radius=8,
        text_color="black",
        border_color="snow",
        fg_color="#a8fc00",
    )
    self.URL_In2.grid(row=5, column=0, columnspan=2, sticky=tk.W + tk.E)  # 位置指定
    # self.URL_In3 = tk.Button(
    #     self.frame3,
    #     text="元帳CSV選択",
    #     width=20,
    #     bg="AntiqueWhite",
    #     command=self.Moto_Open,
    # )
    self.URL_In3 = ck.CTkButton(
        master=self.frame3,
        text="元帳CSV選択",
        command=self.Moto_Open,
        width=self.BtnWidth,
        height=self.BtnHeight,
        border_width=2,
        corner_radius=8,
        text_color="black",
        border_color="snow",
        fg_color="#ff723b",
    )
    self.URL_In3.grid(row=6, column=0, columnspan=2, sticky=tk.W + tk.E)  # 位置指定
    # テキスト変換ルール設定ボタン----------------------------------------------------
    # self.Txt_C = tk.Button(
    #     self.frame3,
    #     text="テキスト変換ルール設定",
    #     bg="LightSkyBlue",
    #     width=20,
    #     command=self.Txt_ChangeSetOpen,
    # )
    self.Txt_C = ck.CTkButton(
        master=self.frame3,
        text="テキスト変換ルール設定",
        command=self.Txt_ChangeSetOpen,
        width=self.BtnWidth,
        height=self.BtnHeight,
        border_width=2,
        corner_radius=8,
        text_color="black",
        border_color="snow",
        fg_color="#1bfac6",
    )
    self.Txt_C.grid(
        row=len(self.indexes) + 7, column=0, columnspan=2, sticky=tk.W + tk.E
    )  # 位置指定
    # ------------------------------------------------------------------------------
    # 戻るボタン--------------------------------------------------------------------
    # self.CloseBtn = tk.Button(
    #     self.frame3,
    #     text="戻る",
    #     bg="gray80",
    #     width=20,
    #     command=self.ReturnBack,
    # )
    self.CloseBtn = ck.CTkButton(
        master=self.frame3,
        text="戻る",
        command=self.ReturnBack,
        width=self.BtnWidth,
        height=self.BtnHeight,
        border_width=2,
        corner_radius=8,
        text_color="black",
        border_color="snow",
        fg_color="gray80",
    )
    self.CloseBtn.grid(
        row=len(self.indexes) + 8, column=0, columnspan=2, sticky=tk.W + tk.E
    )  # 位置指定
    # ------------------------------------------------------------------------------


# -----------------------------------------------------------------------------------------
def removeEntry(self):
    """
    エントリーウィジェットを削除
    """
    for i in self.Treeview_1.get_children():
        self.Treeview_1.delete(i)


# -----------------------------------------------------------------------------------------
def Frame7createtomlEntry(self, next, AJL, AJR):
    """
    列対応表の要素作成
    """
    try:
        self.Setting_Btn.destroy()
    except:
        print("ボタン無")

    if type(AJL) == list:
        # ---------------------------------------------
        # txtxt = tk.Entry(self.frame7, width=10)
        txtxt = ck.CTkEntry(
            master=self.frame7,
            width=self.EntWidth,
            height=self.EntHeight,
            border_width=2,
            corner_radius=8,
            text_color="black",
            border_color="snow",
            fg_color="snow",
        )
        txtxt.insert(0, AJL[next])
        txtxt.grid(row=next + 1, column=0)  # 位置指定
        # Entrマネージャに登録
        self.Frame7EntL.insert(next, txtxt)
        self.AJL.insert(next, AJL[next])
        # ---------------------------------------------
        # lab = tk.Label(self.frame7, text="→", width=2)
        lab = ck.CTkLabel(
            master=self.frame7,
            text="→",
            width=2,
            height=1,
            corner_radius=8,
            text_font=self.t_font,
        )
        lab.grid(row=next + 1, column=1)  # 位置指定
        # Entrマネージャに登録
        self.Frame7Labels.insert(next, lab)
        # ---------------------------------------------
        # txtxt = tk.Entry(self.frame7, width=10)
        txtxt = ck.CTkEntry(
            master=self.frame7,
            width=self.EntWidth,
            height=self.EntHeight,
            border_width=2,
            corner_radius=8,
            text_color="black",
            border_color="snow",
            fg_color="snow",
        )
        txtxt.insert(0, AJR[next])
        txtxt.grid(row=next + 1, column=2)  # 位置指定
        # Entrマネージャに登録
        self.Frame7EntR.insert(next, txtxt)
        self.AJR.insert(next, AJR[next])
        # ---------------------------------------------
        Btn = tk.Button(
            self.frame7,
            text="X",
            width=1,
        )
        # Btn = ck.CTkButton(
        #     master=self.frame7,
        #     text="X",
        #     width=1,
        #     height=1,
        #     border_width=2,
        #     corner_radius=8,
        #     text_color="black",
        # )

        Btn.bind("<Button-1>", AJ_EntDelete)
        Btn.grid(row=next + 1, column=3, sticky=tk.W + tk.E)
        # Entrマネージャに登録
        self.Frame7Btns.insert(next, Btn)
        # ---------------------------------------------
    else:
        # ---------------------------------------------
        # txtxt = tk.Entry(self.frame7, width=10)
        txtxt = ck.CTkEntry(
            master=self.frame7,
            width=self.EntWidth,
            height=self.EntHeight,
            border_width=2,
            corner_radius=8,
            text_color="black",
            border_color="snow",
            fg_color="snow",
        )
        txtxt.insert(0, AJL)
        txtxt.grid(row=next + 1, column=0)  # 位置指定
        # Entrマネージャに登録
        self.Frame7EntL.insert(next, txtxt)
        self.AJL.insert(next, AJL)
        # ---------------------------------------------
        # lab = tk.Label(self.frame7, text="→", width=2)
        lab = ck.CTkLabel(
            master=self.frame7,
            text="→",
            width=2,
            height=1,
            corner_radius=8,
            text_font=self.t_font,
        )
        lab.grid(row=next + 1, column=1)  # 位置指定
        # Entrマネージャに登録
        self.Frame7Labels.insert(next, lab)
        # ---------------------------------------------
        # txtxt = tk.Entry(self.frame7, width=10)
        txtxt = ck.CTkEntry(
            master=self.frame7,
            width=self.EntWidth,
            height=self.EntHeight,
            border_width=2,
            corner_radius=8,
            text_color="black",
            border_color="snow",
            fg_color="snow",
        )
        txtxt.insert(0, AJR)
        txtxt.grid(row=next + 1, column=2)  # 位置指定
        # Entrマネージャに登録
        self.Frame7EntR.insert(next, txtxt)
        self.AJR.insert(next, AJR)
        # ---------------------------------------------
        Btn = tk.Button(
            self.frame7,
            text="X",
            width=1,
        )
        # Btn = ck.CTkButton(
        #     master=self.frame7,
        #     text="X",
        #     width=1,
        #     height=1,
        #     border_width=2,
        #     corner_radius=8,
        #     text_color="black",
        # )
        Btn.bind("<Button-1>", AJ_EntDelete)
        Btn.grid(row=next + 1, column=3, sticky=tk.W + tk.E)
        # Entrマネージャに登録
        self.Frame7Btns.insert(next, Btn)
        # ---------------------------------------------


# -----------------------------------------------------------------------------------------
def Frame7Entries(self):
    """
    列対応表の作成
    """
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
    self.AJL = []  # Entryのインスタンス
    self.AJR = []  # Entryのインスタンス

    AJL = ["伝票日付", "（借）金額", "（貸）金額"]
    AJR = ["日付", "入金", "出金"]

    self.frame7RowList = []
    for r in range(len(AJL)):
        # ラベル＆Entryフレームへ追加----------------------------------------------
        Frame7createtomlEntry(self, r, AJL, AJR)  # Entryを作成配置
        # self.Frame7entryList.append(ColNameItem)
        # ----------------------------------------------------------------------
    # 詳細設定ボタン--------------------------------
    # self.Setting_Btn = tk.Button(
    #     self.frame7,
    #     text="詳細設定",
    #     width=20,
    #     command=lambda: self.ChangeFrame("詳細設定"),
    #     bg="Thistle",
    # )
    # self.Setting_Btn.grid(
    #     row=len(self.Frame7EntL) + 1,
    #     column=0,
    #     columnspan=4,
    #     sticky=tk.W + tk.E,
    # )  # 位置指定
    g_Frame7EntL = self.Frame7EntL
    g_Frame7EntR = self.Frame7EntR
    g_Frame7Labels = self.Frame7Labels
    g_Frame7Btns = self.Frame7Btns


# -----------------------------------------------------------------------------------------
def AJ_setCalc(self):
    """
    自動仕訳候補の転記
    """
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
                    # 詳細設定ボタン--------------------------------
                    # self.Setting_Btn = tk.Button(
                    #     self.frame7,
                    #     text="詳細設定",
                    #     width=20,
                    #     command=lambda: self.ChangeFrame("詳細設定"),
                    #     bg="BlueViolet",
                    # )
                    # self.Setting_Btn = ck.CTkButton(
                    #     master=self.frame7,
                    #     text="詳細設定",
                    #     command=lambda: self.ChangeFrame("詳細設定"),
                    #     width=self.BtnWidth,
                    #     height=self.BtnHeight,
                    #     border_width=2,
                    #     corner_radius=8,
                    #     text_color="black",
                    #     border_color="snow",
                    #     fg_color="#621bfa",
                    # )
                    # self.Setting_Btn.grid(
                    #     row=len(self.Frame7EntL) + 1,
                    #     column=0,
                    #     columnspan=4,
                    #     sticky=tk.W + tk.E,
                    # )  # 位置指定
        except:
            tk.messagebox.showinfo("確認", "抽出仕訳表のセルが選択されていません。変換先の列のセルを選択して下さい。")


# -----------------------------------------------------------------------------------------
def AJ_EntDelete(self):
    """
    列対応表の削除
    """
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
def Frame7removeEntry(self):
    """
    列対応表の全削除
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


# -----------------------------------------------------------------------------------------
def Frame7updatetomlEntries(self):
    """
    列対応表の再配置
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
def FrameChangeremoveEntry(self):
    """
    エントリーウィジェットを削除
    """
    # Btn_n = self.widget
    for i in self.ChangeTxtEntries:
        i.grid_forget()
        i.destroy()
    for i in self.Sub_ChangeTxtEntries:
        i.grid_forget()
        i.destroy()
    for i in self.ChangeLabelEntries:
        i.grid_forget()
        i.destroy()
    for i in self.Sub_ChangeLabelEntries:
        i.grid_forget()
        i.destroy()


# -----------------------------------------------------------------------------------------
def FrameChangeEntries(self):  # , tomltitle):
    """
    エントリーウィジェットを削除
    """
    self.ChangeTxtEntries = []  # Entryのインスタンス
    self.ChangeTxtinsertEntries = []  # ラベルインスタンス
    self.ChangeTxtindex = 0  # 最新のインデックス番号
    self.ChangeTxtindexes = []  # インデックスの並び
    self.ChangeTxtentryList = []  # Entryのインスタンス
    self.ChangeLabelEntries = []  # Entryのインスタンス

    self.Sub_ChangeTxtEntries = []  # Entryのインスタンス
    self.Sub_ChangeTxtinsertEntries = []  # ラベルインスタンス
    self.Sub_ChangeTxtindex = 0  # 最新のインデックス番号
    self.Sub_ChangeTxtindexes = []  # インデックスの並び
    self.Sub_ChangeTxtentryList = []  # Entryのインスタンス
    self.Sub_ChangeLabelEntries = []  # Entryのインスタンス

    r = 0
    # if len(self.ColumnName) == len(self.ChangeTxtColumns):
    for ColNameItem in self.ChangeTxtColumns:
        # ラベル＆Entryフレームへ追加----------------------------------------------
        createFrameChangeEntry(self, r, ColNameItem)  # , tomltitle)  # Entryを作成配置
        self.ChangeTxtentryList.append(ColNameItem)
        self.Sub_ChangeTxtentryList.append(ColNameItem)
        # ----------------------------------------------------------------------
        r += 1
        # self.ChangeFrame_Sub = tk.Frame(self.ChangeFrame)
        # lb = tk.Label(self.ChangeFrame_Sub, text="検出率")
        # lb.grid(row=0, column=0)  # 位置指定
        # txtxt = tk.Entry(self.ChangeFrame_Sub, width=20)
        # txtxt.insert(0, "月分")
        # txtxt.grid(row=0, column=1)  # 位置指定

        # self.ChangeFrame_Sub.grid(
        #     row=len(self.ChangeTxtEntries) + 1, columnspan=3
        # )  # 位置指定

        # self.ParVal = txtxt
        # self.AJChangeFrame_Sub = tk.Frame(self.AJsetMenuFrame)
        # lb = tk.Label(self.AJChangeFrame_Sub, text="検出率")
        # lb.grid(row=0, column=0)  # 位置指定
        # txtxt = tk.Entry(self.AJChangeFrame_Sub, width=20)
        # txtxt.insert(0, "月分")
        # txtxt.grid(row=0, column=1)  # 位置指定

        # self.AJChangeFrame_Sub.grid(
        #     row=len(self.ChangeTxtEntries) + 1, columnspan=3
        # )  # 位置指定

        # self.SubParVal = txtxt
    return
    # else:
    #     tk.messagebox.showinfo("確認", "変換リストの列数と一致しません。")
    #     return


# -----------------------------------------------------------------------------------------
# エントリーウィジェットを再配置
def updateFrameChangeEntries(self):

    # エントリーウィジェットマネージャを参照して再配置
    for i in range(len(self.ChangeTxtindexes)):
        self.ChangeTxtEntries[i].grid(column=1, row=i)
        # self.ChangeTxtEntries[i].bind("<Return>", self.EveRecalc)
        self.ChangeTxtEntries[i].lift()
        self.ChangeTxtinsertEntries[i].grid(column=0, row=i)

        self.Sub_ChangeTxtEntries[i].grid(column=1, row=i)
        # self.Sub_ChangeTxtEntries[i].bind("<Return>", self.EveRecalc)
        self.Sub_ChangeTxtEntries[i].lift()
        self.Sub_ChangeTxtinsertEntries[i].grid(column=0, row=i)


# -----------------------------------------------------------------------------------------
# エントリーウィジェットを作成して配置
def createFrameChangeEntry(self, next, ColNameItem):  # , tomltitle):
    global L_List, E_List, L_List_Sub, E_List_Sub

    # lb = tk.Label(self.ChangeFrame, text=ColNameItem + "対象列名")
    lb = ck.CTkLabel(
        master=self.ChangeFrame,
        text=ColNameItem + "対象列名",
        width=self.LabelWidth,
        height=self.LabelHeight,
        corner_radius=8,
        text_font=self.t_font,
    )
    lb.grid(row=next, column=0)  # 位置指定
    self.ChangeLabelEntries.insert(next, lb)
    # lb = tk.Label(self.AJsetMenuFrame, text=ColNameItem + "対象列名")
    lb = ck.CTkLabel(
        master=self.ChangeFrame,
        text=ColNameItem + "対象列名",
        width=self.LabelWidth,
        height=self.LabelHeight,
        corner_radius=8,
        text_font=self.t_font,
    )
    lb.grid(row=next, column=0)  # 位置指定
    self.Sub_ChangeLabelEntries.insert(next, lb)
    # ラベル名からself変数を取得---------------------------------------
    # ---------------------------------------------------------------
    # txtxt = tk.Entry(self.ChangeFrame, width=20)
    txtxt = ck.CTkEntry(
        master=self.ChangeFrame,
        width=self.EntWidth,
        height=self.EntHeight,
        border_width=2,
        corner_radius=8,
        text_color="black",
        border_color="snow",
        fg_color="snow",
    )

    if "OCRテキスト" in self.ColumnName[next]:
        lis = list(self.pt.colheader.columnlabels)
        txtxt.insert(0, lis[next])
        # lis = ["摘要", "摘要", "出金", "摘要", "入金", "摘要"]
        # txtxt.insert(0, "摘要")
    else:
        # lis = list(self.pt3.colheader.columnlabels)
        # txtxt.insert(0, lis[next])
        # lis = ["摘要", "摘要", "出金", "摘要", "入金", "摘要"]
        txtxt.insert(0, "摘要")
    # コールバック---------------------------------------------------
    txtxt.bind("<Key>", RetuenTabFunction)
    # ---------------------------------------------------------------
    txtxt.grid(row=next, column=1)  # 位置指定
    self.ChangeTxtEntries.insert(next, txtxt)
    # ---------------------------------------------------------------
    # txtxt = tk.Entry(self.AJsetMenuFrame, width=20)
    txtxt = ck.CTkEntry(
        master=self.AJsetMenuFrame,
        width=self.EntWidth,
        height=self.EntHeight,
        border_width=2,
        corner_radius=8,
        text_color="black",
        border_color="snow",
        fg_color="snow",
    )

    if "OCRテキスト" in self.ColumnName[next]:
        lis = list(self.pt.colheader.columnlabels)
        txtxt.insert(0, lis[next])
        # lis = ["摘要", "摘要", "出金", "摘要", "入金", "摘要"]
        # txtxt.insert(0, "摘要")
    else:
        # lis = list(self.pt3.colheader.columnlabels)
        # txtxt.insert(0, lis[next])
        # lis = ["摘要", "摘要", "出金", "摘要", "入金", "摘要"]
        txtxt.insert(0, "摘要")
    # コールバック---------------------------------------------------
    txtxt.bind("<Key>", RetuenTabFunction)
    # ---------------------------------------------------------------
    txtxt.grid(row=next, column=1)  # 位置指定
    self.Sub_ChangeTxtEntries.insert(next, txtxt)
    # ラベルを作成----------------------------------------------------
    # self.ChangeTxtinsertEntries.insert(
    #     next,
    #     tk.Label(
    #         self.ChangeFrame,
    #         text=str(ColNameItem),
    #     ),
    # )
    self.ChangeTxtinsertEntries.insert(
        next,
        ck.CTkLabel(
            master=self.ChangeFrame,
            text=str(ColNameItem),
            width=self.LabelWidth,
            height=self.LabelHeight,
            corner_radius=8,
            text_font=self.t_font,
        ),
    )
    # インデックスマネージャに登録
    self.ChangeTxtindexes.insert(next, self.ChangeTxtindex)
    # ラベルを作成----------------------------------------------------
    # self.Sub_ChangeTxtinsertEntries.insert(
    #     next,
    #     tk.Label(
    #         self.AJsetMenuFrame,
    #         text=str(ColNameItem),
    #     ),
    # )
    self.Sub_ChangeTxtinsertEntries.insert(
        next,
        ck.CTkLabel(
            master=self.AJsetMenuFrame,
            text=str(ColNameItem),
            width=self.LabelWidth,
            height=self.LabelHeight,
            corner_radius=8,
            text_font=self.t_font,
        ),
    )
    # インデックスマネージャに登録
    self.Sub_ChangeTxtindexes.insert(next, self.ChangeTxtindex)

    # グローバル変数に代入
    L_List = self.ChangeLabelEntries
    E_List = self.ChangeTxtEntries
    L_List_Sub = self.Sub_ChangeLabelEntries
    E_List_Sub = self.Sub_ChangeTxtEntries


# ----------------------------------------------------------------------------
def RetuenTabFunction(self):
    global L_List, E_List, L_List_Sub, E_List_Sub

    WidN = self.widget

    if self.keysym == "Return":
        # エンター処理###############################
        i = 0
        for ListItem in E_List:
            if ListItem == WidN:
                if i == len(E_List) - 1:
                    E_List[0].focus_set()
                else:
                    E_List[i + 1].focus_set()
                break
            i += 1

        i = 0
        for ListItem in E_List_Sub:
            if ListItem == WidN:
                if i == len(E_List_Sub) - 1:
                    E_List_Sub[0].focus_set()
                else:
                    E_List_Sub[i + 1].focus_set()
                break
            i += 1
    elif self.keysym == "Up":
        # Up処理###############################
        i = 0
        for ListItem in E_List:
            if ListItem == WidN:
                if i != 0:
                    E_List[i - 1].focus_set()
                    break
            i += 1

        i = 0
        for ListItem in E_List_Sub:
            if ListItem == WidN:
                if i != 0:
                    E_List_Sub[i - 1].focus_set()
                    break
            i += 1
    elif self.keysym == "Down":
        # Down処理###############################
        i = 0
        for ListItem in E_List:
            if ListItem == WidN:
                if i != len(E_List) - 1:
                    E_List[i + 1].focus_set()
                    break
            i += 1

        i = 0
        for ListItem in E_List_Sub:
            if ListItem == WidN:
                if i != len(E_List) - 1:
                    E_List_Sub[i + 1].focus_set()
                    break
            i += 1


# ----------------------------------------------------------------------------
def AJ_copyCalc_Func(SetList, dfsrow, dfs3row, ChangeTxtURL):
    """
    自動仕訳候補OCR結果
    """
    try:
        for E_r in range(len(g_Frame7EntL)):
            L_txt = g_Frame7EntL[E_r].get()
            R_txt = g_Frame7EntR[E_r].get()
            if dfsrow[R_txt] != dfsrow[R_txt]:
                print("nan")
            else:
                Txt = TxtEdit(L_txt, dfs3row[L_txt], dfsrow[R_txt])
                dfs3row[L_txt] = Txt[1]
        df_c = dfs3row.index
        for dfs3rowItem in df_c:
            if dfs3rowItem == "一致率":
                del dfs3row["一致率"]
            if dfs3rowItem == "仕訳金額差額":
                del dfs3row["仕訳金額差額"]
            if dfs3rowItem == "日付一致率":
                del dfs3row["日付一致率"]
        return dfs3row
    except:
        return dfs3row


# ----------------------------------------------------------------------------
def TxtEdit(Txt, L_txt, R_txt):
    """
    R_txtの書式をL_txtの書式と揃える
    """
    try:
        if "日" in Txt:
            L_txt = (
                L_txt.replace("-", "/")
                .replace("_", "/")
                .replace("\\", "/")
                .replace(".", "/")
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
                .replace(".", "/")
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
            L_txt = (
                str(L_d.year)
                + "/"
                + "{0:02}".format(str(L_d.month))
                + "/"
                + "{0:02}".format(str(L_d.day))
            )
            R_txt = (
                str(R_d.year)
                + "/"
                + "{0:02}".format(str(R_d.month))
                + "/"
                + "{0:02}".format(str(R_d.day))
            )
            return L_txt, R_txt
        else:
            return L_txt, R_txt
    except:
        return L_txt, R_txt
