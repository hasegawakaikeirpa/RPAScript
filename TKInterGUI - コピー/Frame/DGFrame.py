import tkinter as tk
import tkinter.ttk as ttk
import Frame.MyTable as MT
import CSVOut as CSVO
import ScrollableFrame as SF
import TKEntry as tke


# メインフレーム######################################################################################
def create_Frame(self):
    # ツリーフレーム設定---------------------------------------------------------------------
    self.OCR_frame = tk.Frame(
        self.Main_Frame, width=650, height=400, bd=2, relief=tk.RIDGE
    )  # 親フレーム
    self.OCR_frame.grid(row=0, column=0, sticky=tk.N + tk.S + tk.W + tk.E)
    self.tree_frame = tk.Frame(self.OCR_frame, width=650, height=400)  # 子フレーム
    tk.Label(self.OCR_frame, text="OCR抽出結果表").grid(
        row=0, column=0, sticky=tk.N + tk.W
    )  # 位置指定
    self.tree_frame.grid(row=1, column=0, sticky=tk.N + tk.S + tk.W + tk.E)
    # df = TableModel.getSampleData()
    # pt = Table(self.tree_frame)
    pt = MT.MyTable(
        self.tree_frame, width=650, height=400, sticky=tk.N + tk.S + tk.W + tk.E
    )  # テーブルをサブクラス化
    enc = CSVO.getFileEncoding(self.FileName)
    self.table = pt.importCSV(self.FileName, encoding=enc)
    self.pt = pt
    self.pt._name = "OCR抽出結果表Main"
    # DF型変換------------------------------
    PandasAstype(self.pt.model.df)
    # --------------------------------------
    pt.show()


def create_Frame2(self):
    # ツリーフレーム設定---------------------------------------------------------------------
    self.Jounal = tk.Frame(
        self.Main_Frame, width=650, height=400, bd=2, relief=tk.RIDGE
    )  # 親フレーム
    self.Jounal.grid(row=0, column=1, sticky=tk.N + tk.S + tk.W + tk.E)
    self.tree2_frame = tk.Frame(self.Jounal, width=650, height=400)
    tk.Label(self.Jounal, text="作成仕訳表").grid(row=0, column=0, sticky=tk.W)  # 位置指定
    self.tree2_frame.grid(row=1, column=0, sticky=tk.N + tk.S + tk.W + tk.E)
    # df = TableModel.getSampleData()
    # pt2 = Table(self.tree2_frame)
    pt2 = MT.MyTable2(
        self.tree2_frame, width=650, height=400, sticky=tk.N + tk.S + tk.W + tk.E
    )  # テーブルをサブクラス化
    enc = CSVO.getFileEncoding(self.JounalFileName)
    self.table2 = pt2.importCSV(self.JounalFileName, encoding=enc)
    self.pt2 = pt2
    self.pt2._name = "作成仕訳表Main"
    # DF型変換------------------------------
    PandasAstype(self.pt2.model.df)
    # --------------------------------------
    pt2.show()


def create_Frame3(self):
    self.Predict_frame = tk.Frame(
        self.Main_Frame, width=650, height=400, bd=2, relief=tk.RIDGE
    )  # 親フレーム
    self.Predict_frame.grid(row=1, column=1, sticky=tk.N + tk.S + tk.W + tk.E)
    self.frame5 = tk.Frame(self.Predict_frame, width=650, height=400)
    tk.Label(self.Predict_frame, text="仕訳予想結果").grid(
        row=0, column=0, sticky=tk.W
    )  # 位置指定
    self.frame5.grid(row=1, column=0, sticky=tk.N + tk.S + tk.W + tk.E)
    pt3 = MT.MyTable3(
        self.frame5, width=650, height=150, sticky=tk.N + tk.S + tk.W + tk.E
    )  # テーブルをサブクラス化
    enc = CSVO.getFileEncoding(self.AJSeturl)
    self.table3 = pt3.importCSV(self.AJSeturl, encoding=enc)
    self.pt3 = pt3
    self.pt3._name = "仕訳予想結果Main"
    # DF型変換------------------------------
    PandasAstype(self.pt3.model.df)
    # --------------------------------------
    pt3.show()


def create_SettingFrame(self):
    # 設定メインフレーム設定--------------------------------------------------------------------
    self.Mframe = SF.ScrollableFrameDG(self.Main_Frame)
    self.Mframe.grid(
        row=1, column=0, sticky=tk.N + tk.S + tk.W + tk.E
    )  # , ipadx=500, ipady=100)
    tk.Label(self.Mframe.scrollable_frame, text="設定").grid(
        row=0, column=0, sticky=tk.N + tk.W
    )  # 位置指定
    # -------------------------------------------------------------------------------------
    # フレーム設定--------------------------------------------------------------------------
    self.frame3 = tk.Frame(self.Mframe.scrollable_frame, bd=2, relief=tk.RIDGE)
    self.frame3.grid(row=2, column=0, sticky=tk.N + tk.S)
    # -------------------------------------------------------------------------------------
    # フレーム設定--------------------------------------------------------------------------
    self.ChangeFrame = tk.Frame(self.Mframe.scrollable_frame, bd=2, relief=tk.RIDGE)
    self.ChangeFrame.grid(row=2, column=1, sticky=tk.N + tk.S)
    # -------------------------------------------------------------------------------------
    # フレーム設定--------------------------------------------------------------------------
    self.frame4 = tk.Frame(self.Mframe.scrollable_frame, bd=2, relief=tk.RIDGE)
    self.frame4.grid(row=2, column=2, sticky=tk.N + tk.S)
    # -------------------------------------------------------------------------------------
    # フレーム設定--------------------------------------------------------------------------
    self.frame6 = tk.Frame(self.Mframe.scrollable_frame, bd=2, relief=tk.RIDGE)
    self.frame6.grid(row=2, column=3, sticky=tk.N + tk.S)
    # MotoCyou------------------------------------------------------------------------------
    # フレーム設定--------------------------------------------------------------------------
    self.frame7 = tk.Frame(self.Mframe.scrollable_frame, bd=2, relief=tk.RIDGE)
    self.frame7.grid(row=2, column=4, sticky=tk.N + tk.S)
    self.frame7EntryList = []  # このフレームのEntryのインスタンス
    # フレーム設定--------------------------------------------------------------------------
    self.frame8 = tk.Frame(self.Mframe.scrollable_frame, bd=2, relief=tk.RIDGE)
    self.frame8.grid(row=2, column=5, sticky=tk.N + tk.S)
    self.frame8EntryList = []  # このフレームのEntryのインスタンス
    # -------------------------------------------------------------------------------------
    tk.Label(self.frame6, text="元帳日付列名").grid(row=0, column=0)  # 位置指定
    self.Moto_Day = tk.Entry(self.frame6, width=10)
    self.Moto_Day.insert(0, "元帳日付列名")
    self.Moto_Day.grid(row=0, column=1)
    # ---------------------------------------------------------------------------------------
    tk.Label(self.frame6, text="元帳借方金額列名").grid(row=1, column=0)  # 位置指定
    self.Moto_KariMoney = tk.Entry(self.frame6, width=10)
    self.Moto_KariMoney.insert(0, "元帳借方金額列名")
    self.Moto_KariMoney.grid(row=1, column=1)
    # ---------------------------------------------------------------------------------------
    tk.Label(self.frame6, text="元帳貸方金額列名").grid(row=2, column=0)  # 位置指定
    self.Moto_KashiMoney = tk.Entry(self.frame6, width=10)
    self.Moto_KashiMoney.insert(0, "元帳貸方金額列名")
    self.Moto_KashiMoney.grid(row=2, column=1)
    # ---------------------------------------------------------------------------------------
    tk.Label(self.frame6, text="元帳摘要列名").grid(row=3, column=0)  # 位置指定
    self.Moto_Tekiyou = tk.Entry(self.frame6, width=10)
    self.Moto_Tekiyou.insert(0, "元帳摘要列名")
    self.Moto_Tekiyou.grid(row=3, column=1)
    # ---------------------------------------------------------------------------------------
    tk.Label(self.frame6, text="元帳借方科目列名").grid(row=4, column=0)  # 位置指定
    self.Moto_Karikata = tk.Entry(self.frame6, width=10)
    self.Moto_Karikata.insert(0, "（借）科目名")
    self.Moto_Karikata.grid(row=4, column=1)
    # ---------------------------------------------------------------------------------------
    tk.Label(self.frame6, text="元帳貸方科目列名").grid(row=5, column=0)  # 位置指定
    self.Moto_Kashikata = tk.Entry(self.frame6, width=10)
    self.Moto_Kashikata.insert(0, "（貸）科目名")
    self.Moto_Kashikata.grid(row=5, column=1)
    # ---------------------------------------------------------------------------------------
    # 全行自動仕訳ボタン-------------------------------------------------------------
    self.AllRun = tk.Button(
        self.frame6,
        text="全行自動仕訳",
        bg="LavenderBlush",
        width=20,
        command=lambda: self.AJAllCalc(self.FileName),
    )
    self.AllRun.grid(row=6, column=0, columnspan=2, sticky=tk.W + tk.E)  # 位置指定
    # 選択行自動仕訳作成ボタン----------------------------------------------------------------
    self.AJ_Btn = tk.Button(
        self.frame6,
        text="選択行仕訳予想検索",
        width=20,
        command=lambda: self.AJCalc(self.FileName),
        bg="lightblue",
    )
    self.AJ_Btn.grid(row=7, column=0, columnspan=2, sticky=tk.W + tk.E)  # 位置指定
    # -------------------------------------------------------------------------------------
    # 抽出仕訳転記ボタン----------------------------------------------------------------
    self.AJ_copy = tk.Button(
        self.frame6,
        text="抽出仕訳転記",
        width=20,
        command=lambda: self.AJ_copyCalc(),
        bg="pink",
    )
    self.AJ_copy.grid(row=8, column=0, columnspan=2, sticky=tk.W + tk.E)  # 位置指定
    # -------------------------------------------------------------------------------------
    # 元帳表示ボタン----------------------------------------------------------------
    self.AJ_copy = tk.Button(
        self.frame6,
        text="元帳表示",
        width=20,
        command=lambda: self.ReadM(self.Roolurl),
        bg="PaleGreen",
    )
    self.AJ_copy.grid(row=9, column=0, columnspan=2, sticky=tk.W + tk.E)  # 位置指定
    # -------------------------------------------------------------------------------------
    # 置換設定追加ボタン--------------------------------------------------------------------
    self.AJ_set = tk.Button(
        self.frame7,
        text="置換設定追加",
        width=20,
        command=lambda: tke.AJ_setCalc(self),
        bg="Coral",
    )
    self.AJ_set.grid(row=0, column=0, columnspan=4, sticky=tk.W + tk.E)  # 位置指定
    # -------------------------------------------------------------------------------------

    # 列名設定フレーム################################################################
    tk.Label(self.frame8, text="摘要置換設定").grid(row=1, column=0)  # フレームテキスト
    self.SF = SF.ScrollableFrame(self.frame8, 700, bar_x=False)
    self.SF.grid(sticky=tk.W + tk.E)  # , ipadx=500, ipady=100)
    # エントリーウィジェットマネージャを初期化
    self.RepLEntries = []  # エントリーウィジェットのインスタンス
    self.RepREntries = []  # エントリーウィジェットのインスタンス
    self.RepinsertEntries = []  # 追加するボタンのようなラベル
    self.RepremoveEntries = []  # 削除するボタンのようなラベル
    # こちらはインデックスマネージャ。ウィジェットの数や並び方を管理
    self.Repindex = 0  # 最新のインデックス番号
    self.Repindexes = []  # インデックスの並び
    # self.createEntry(0, bar_x=False)
    # 摘要置換設定作成
    RepcreateEntry(self, 0, bar_x=False)
    #################################################################################


# ----------------------------------------------------------------------------
def RepcreateEntry(self, next, bar_x=True, bar_y=True):
    """
    列名設定項目を作成して再配置
    """
    global L_List, E_List
    # 最初のエントリーウィジェットを追加
    self.RepLEntries.insert(next, tk.Entry(self.SF.scrollable_frame, width=10))
    # 最初のエントリーウィジェットを追加
    self.RepREntries.insert(next, tk.Entry(self.SF.scrollable_frame, width=10))
    # エントリーウィジェットを追加するボタンのようなラベルを作成
    self.RepinsertEntries.insert(
        next,
        tk.Label(
            self.SF.scrollable_frame,
            text="+",
            fg="#33ff33",
            font=("Arial Black", 20),
        ),
    )
    # エントリーウィジェットを削除するボタンのようなラベルを作成（初期の段階では表示しない）
    self.RepremoveEntries.insert(
        next,
        tk.Label(
            self.SF.scrollable_frame,
            text="−",
            fg="#ff3333",
            font=("Arial Black", 20),
        ),
    )
    # 追加するボタンのようなラベルにクリックイベントを設定
    self.RepinsertEntries[next].bind(
        "<1>", lambda event, id=self.Repindex: RepinsertEntry_click(self, event, id)
    )
    # 削除するボタンのようなラベルにクリックイベントを設定
    self.RepremoveEntries[next].bind(
        "<1>", lambda event, id=self.Repindex: RepremoveEntry_click(self, event, id)
    )
    # インデックスマネージャに登録
    self.Repindexes.insert(next, self.Repindex)
    # 再配置
    RepupdateEntries(self, bar_x=False)
    L_List = self.RepLEntries
    E_List = self.RepREntries


# -------------------------------------------------------------------------------------
def RepinsertEntry_click(self, event, id):
    """
    列名設定項目追加ボタン処理
    """
    # 追加する位置
    next = self.Repindexes.index(id) + 1
    self.Repindex = self.Repindex + 1
    # エントリーウィジェットを作成して配置
    RepcreateEntry(self, next, bar_x=False)


# -------------------------------------------------------------------------------------
def RepremoveEntry_click(self, event, id):
    """
    列名設定項目削除ボタン処理
    """
    global L_List, E_List
    id = 0
    for SRI in self.RepremoveEntries:
        if SRI == event.widget:
            break
        id += 1
    # 削除する位置
    # current = self.indexes.index(id)
    current = id
    # エントリーウィジェットと追加・削除ボタンのようなラベルを削除
    self.RepLEntries[current].destroy()
    self.RepREntries[current].destroy()
    self.RepinsertEntries[current].destroy()
    self.RepremoveEntries[current].destroy()
    # エントリーウィジェットマネージャから削除
    self.RepLEntries.pop(current)
    self.RepREntries.pop(current)
    self.RepinsertEntries.pop(current)
    self.RepremoveEntries.pop(current)
    self.Repindexes.pop(current)
    # 再配置
    RepupdateEntries(self)
    L_List = self.RepLEntries
    E_List = self.RepREntries


# -------------------------------------------------------------------------------------
def RepupdateEntries(self, bar_x=True, bar_y=True):
    """
    列名設定項目を再配置
    """
    # エントリーウィジェットマネージャを参照して再配置
    for i in range(len(self.Repindexes)):
        self.RepLEntries[i].grid(column=0, row=i)
        self.RepLEntries[i].bind("<MouseWheel>", self.SF.mouse_y_scroll)
        self.RepLEntries[i].bind("<Key>", RepRetuenTabFunction)
        self.RepLEntries[i].lift()

        self.RepREntries[i].grid(column=1, row=i)
        self.RepREntries[i].bind("<MouseWheel>", self.SF.mouse_y_scroll)
        self.RepREntries[i].bind("<Key>", RepRetuenTabFunction)
        self.RepREntries[i].lift()

        self.RepinsertEntries[i].grid(column=2, row=i)
        self.RepinsertEntries[i].bind("<MouseWheel>", self.SF.mouse_y_scroll)
        self.RepremoveEntries[i].grid(column=3, row=i)
        self.RepremoveEntries[i].bind("<MouseWheel>", self.SF.mouse_y_scroll)
    # 1つしかないときは削除ボタンのようなラベルを表示しない
    if len(self.Repindexes) == 1:
        self.RepremoveEntries[0].grid_forget()
    if bar_y:  # スクロールバー縦
        self.SF.scrollbar_y.grid_forget()  # スクロールバー削除
        # スクロールバー再作成--------------------------------------------------
        self.SF.scrollbar_y = ttk.Scrollbar(
            self.SF.scrollable_frame,
            orient="vertical",
            command=self.SF.canvas.yview,
        )
        # ---------------------------------------------------------------------
        if len(self.Repindexes) == 1:
            self.SF.scrollbar_y.grid(row=0, column=4, sticky=tk.S + tk.N)
        else:
            self.SF.scrollbar_y.grid(
                row=0, rowspan=len(self.Repindexes), column=4, sticky=tk.S + tk.N
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
            row=len(self.Repindexes), column=0, columnspan=4, sticky=tk.E + tk.W
        )
        self.SF.canvas.configure(xscrollcommand=self.SF.scrollbar_x.set)


# ----------------------------------------------------------------------------
def RepRetuenTabFunction(self):
    global L_List, E_List
    WidN = self.widget
    if self.keysym == "Return":
        # エンター処理###############################
        i = 0
        for ListItem in E_List:
            if ListItem == WidN:
                if i == len(E_List) - 1:
                    L_List[0].focus_set()
                else:
                    L_List[i + 1].focus_set()
                break
            i += 1

        i = 0
        for ListItem in L_List:
            if ListItem == WidN:
                if i == len(L_List) - 1:
                    E_List[0].focus_set()
                else:
                    E_List[i + 1].focus_set()
                break
            i += 1


# ####################################################################################################
# サブフレーム#########################################################################################
def create_Frame4(self):
    # ------------------------------------------------------------------------------
    # 左側メニュー
    self.AJsetOCRFrame = tk.Frame(
        self.Sub_Frame, width=650, height=400, bd=2, relief=tk.RIDGE
    )  # 親フレーム
    self.AJsetOCRFrame.grid(row=0, column=0, sticky=tk.N + tk.S + tk.W + tk.E)
    self.AJsetOCRFrameSub_Frame = tk.Frame(self.AJsetOCRFrame, width=650, height=400)
    tk.Label(self.AJsetOCRFrame, text="OCR抽出結果表").grid(
        row=0, column=0, sticky=tk.W
    )  # 位置指定
    self.AJsetOCRFrameSub_Frame.grid(
        row=1, column=0, columnspan=5, sticky=tk.N + tk.S + tk.W + tk.E
    )
    pt5 = MT.MyTable4(
        self.AJsetOCRFrameSub_Frame,
        width=650,
        height=150,
        sticky=tk.N + tk.S + tk.W + tk.E,
    )  # テーブルをサブクラス化
    enc = CSVO.getFileEncoding(self.FileName)
    self.table5 = pt5.importCSV(self.FileName, encoding=enc)
    self.pt5 = pt5
    self.pt5._name = "OCR抽出結果表Sub"
    # DF型変換------------------------------
    PandasAstype(self.pt5.model.df)
    # --------------------------------------
    pt5.show()
    # ------------------------------------------------------------------------------
    self.AJsetRoolFrame = tk.Frame(
        self.Sub_Frame, width=650, height=400, bd=2, relief=tk.RIDGE
    )  # 親フレーム
    self.AJsetRoolFrame.grid(row=1, column=0, sticky=tk.N + tk.S + tk.W + tk.E)
    self.AJsetOCRFrameSub_Frame2 = tk.Frame(self.AJsetRoolFrame, width=650, height=400)
    tk.Label(self.AJsetRoolFrame, text="ミロク元帳").grid(
        row=0, column=0, sticky=tk.W
    )  # 位置指定
    self.AJsetOCRFrameSub_Frame2.grid(
        row=1, column=0, columnspan=5, sticky=tk.N + tk.S + tk.W + tk.E
    )
    pt6 = MT.MyTable5(
        self.AJsetOCRFrameSub_Frame2,
        width=650,
        height=150,
        sticky=tk.N + tk.S + tk.W + tk.E,
    )  # テーブルをサブクラス化
    enc = CSVO.getFileEncoding(self.Roolurl)
    self.table6 = pt6.importCSV(self.Roolurl, encoding=enc)
    self.pt6 = pt6
    self.pt6._name = "ミロク元帳Sub"
    # DF型変換------------------------------
    PandasAstype(self.pt6.model.df)
    # --------------------------------------
    pt6.show()
    # ------------------------------------------------------------------------------
    self.AJsetFrame = tk.Frame(
        self.Sub_Frame, width=650, height=400, bd=2, relief=tk.RIDGE
    )  # 親フレーム
    self.AJsetFrame.grid(row=2, column=0, sticky=tk.N + tk.S + tk.W + tk.E)
    self.AJsetSub_Frame = tk.Frame(self.AJsetFrame, width=650, height=400)
    tk.Label(self.AJsetFrame, text="テキスト変換ルール").grid(
        row=0, column=0, sticky=tk.W
    )  # 位置指定
    self.AJsetSub_Frame.grid(
        row=1, column=0, columnspan=5, sticky=tk.N + tk.S + tk.W + tk.E
    )
    pt4 = MT.MyTable6(
        self.AJsetSub_Frame, width=650, height=150, sticky=tk.N + tk.S + tk.W + tk.E
    )  # テーブルをサブクラス化
    enc = CSVO.getFileEncoding(self.ChangeTxtURL)
    self.table4 = pt4.importCSV(self.ChangeTxtURL, encoding=enc)
    self.pt4 = pt4
    self.pt4._name = "テキスト変換ルールSub"
    # DF型変換------------------------------
    PandasAstype(self.pt4.model.df)
    # --------------------------------------
    pt4.show()
    # 行追加ボタン--------------------------------------------------------------------
    self.Sub_RowInsert = tk.Button(
        self.AJsetFrame,
        text="行追加",
        bg="LightYellow",
        width=20,
        command=self.Sub_RowInsert,
    )
    self.Sub_RowInsert.grid(row=3, column=0, sticky=tk.W)  # 位置指定
    # 列追加ボタン--------------------------------------------------------------------
    self.Sub_ColumnInsert = tk.Button(
        self.AJsetFrame,
        text="列追加",
        bg="Lightblue",
        width=20,
        command=self.Sub_ColumnInsert,
    )
    self.Sub_ColumnInsert.grid(row=3, column=1)  # 位置指定
    # 行削除ボタン--------------------------------------------------------------------
    self.Sub_RowDelete = tk.Button(
        self.AJsetFrame,
        text="行削除",
        bg="darkorange",
        width=20,
        command=self.Sub_RowDelete,
    )
    self.Sub_RowDelete.grid(row=3, column=2)  # 位置指定
    # 列削除ボタン--------------------------------------------------------------------
    self.Sub_ColumnDelete = tk.Button(
        self.AJsetFrame,
        text="列削除",
        bg="darkgreen",
        width=20,
        command=self.Sub_ColumnDelete,
    )
    self.Sub_ColumnDelete.grid(row=3, column=3)  # 位置指定
    # 戻るボタン--------------------------------------------------------------------
    self.Sub_CloseBtn = tk.Button(
        self.AJsetFrame,
        text="戻る",
        bg="gray80",
        width=20,
        command=self.Sub_ReturnBack,
    )
    self.Sub_CloseBtn.grid(row=3, column=4, sticky=tk.E)  # 位置指定
    # メニューフレーム作成-----------------------------------------------------------
    # 右側メニュー
    self.AJM = tk.Frame(
        self.Sub_Frame,
        width=650,
        height=400,
        bd=2,
        relief=tk.RIDGE,
    )  # 親フレーム
    self.AJM.grid(row=0, column=1, rowspan=4, sticky=tk.N + tk.S + tk.W + tk.E)

    self.AJsetMenuFrame = tk.Frame(
        self.AJM,
        width=650,
        height=400,
        bd=2,
        relief=tk.RIDGE,
    )  # 親フレーム
    tk.Label(self.AJM, text="仕訳候補判定基準列設定").grid(row=0, column=0, sticky=tk.N)  # 位置指定
    self.AJsetMenuFrame.grid(row=1, column=0)


def s_bar_Reset(self):
    self.Mframe.scrollbar_y.grid_forget()  # スクロールバー削除
    # スクロールバー再作成--------------------------------------------------
    self.Mframe.scrollbar_y = ttk.Scrollbar(
        self.Mframe.scrollable_frame,
        orient="vertical",
        command=self.Mframe.canvas.yview,
    )
    # ---------------------------------------------------------------------
    self.Mframe.scrollbar_y.grid(row=0, rowspan=4, column=6, sticky=tk.S + tk.N)
    self.Mframe.canvas.configure(yscrollcommand=self.Mframe.scrollbar_y.set)
    self.Mframe.scrollbar_x.grid_forget()  # スクロールバー削除
    # スクロールバー再作成--------------------------------------------------
    self.Mframe.scrollbar_x = ttk.Scrollbar(
        self.Mframe.scrollable_frame,
        orient="horizontal",
        command=self.Mframe.canvas.xview,
    )
    # ---------------------------------------------------------------------
    self.Mframe.scrollbar_x.grid(row=1, column=0, columnspan=6, sticky=tk.E + tk.W)
    self.Mframe.canvas.configure(xscrollcommand=self.Mframe.scrollbar_x.set)


def PandasAstype(P_df):
    """
    Pandasデータフレーム型変換
    """
    # DF型変換------------------------------
    ptc = P_df.columns
    for ptcItem in ptc:
        ptc_n = P_df[ptcItem].dtype
        if "float" == ptc_n.name:
            P_df[ptcItem].astype(int)
        elif "float64" == ptc_n.name:
            P_df[ptcItem] = P_df[ptcItem].fillna(0)
            P_df[ptcItem] = P_df[ptcItem].astype(int)
            P_df[ptcItem] = P_df[ptcItem].astype(str)
            P_df[ptcItem] = P_df[ptcItem].replace("0", "")
    # --------------------------------------
