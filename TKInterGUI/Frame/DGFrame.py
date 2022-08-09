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
    self.frame3.grid(row=1, column=0, sticky=tk.N + tk.S)
    # -------------------------------------------------------------------------------------
    # フレーム設定--------------------------------------------------------------------------
    self.ChangeFrame = tk.Frame(self.Mframe.scrollable_frame, bd=2, relief=tk.RIDGE)
    self.ChangeFrame.grid(row=1, column=1, sticky=tk.N + tk.S)
    # -------------------------------------------------------------------------------------
    # フレーム設定--------------------------------------------------------------------------
    self.frame4 = tk.Frame(self.Mframe.scrollable_frame, bd=2, relief=tk.RIDGE)
    self.frame4.grid(row=1, column=2, sticky=tk.N + tk.S)
    # -------------------------------------------------------------------------------------
    # フレーム設定--------------------------------------------------------------------------
    self.frame6 = tk.Frame(self.Mframe.scrollable_frame, bd=2, relief=tk.RIDGE)
    self.frame6.grid(row=1, column=3, sticky=tk.N + tk.S)
    # MotoCyou------------------------------------------------------------------------------
    # フレーム設定--------------------------------------------------------------------------
    self.frame7 = tk.Frame(self.Mframe.scrollable_frame, bd=2, relief=tk.RIDGE)
    self.frame7.grid(row=1, column=4, sticky=tk.N + tk.S)
    self.frame7EntryList = []  # このフレームのEntryのインスタンス
    # -------------------------------------------------------------------------------------
    tk.Label(self.frame6, text="元帳日付列名").grid(row=0, column=0)  # 位置指定
    self.Moto_Day = tk.Entry(self.frame6, width=10)
    self.Moto_Day.insert(0, "元帳日付列名")
    self.Moto_Day.grid(row=0, column=1)
    # ---------------------------------------------------------------------------------------
    tk.Label(self.frame6, text="元帳金額列名").grid(row=1, column=0)  # 位置指定
    self.Moto_Money = tk.Entry(self.frame6, width=10)
    self.Moto_Money.insert(0, "元帳金額列名")
    self.Moto_Money.grid(row=1, column=1)
    # ---------------------------------------------------------------------------------------
    tk.Label(self.frame6, text="元帳摘要列名").grid(row=2, column=0)  # 位置指定
    self.Moto_Tekiyou = tk.Entry(self.frame6, width=10)
    self.Moto_Tekiyou.insert(0, "元帳摘要列名")
    self.Moto_Tekiyou.grid(row=2, column=1)
    # ---------------------------------------------------------------------------------------
    tk.Label(self.frame6, text="元帳借方科目列名").grid(row=3, column=0)  # 位置指定
    self.Moto_Karikata = tk.Entry(self.frame6, width=10)
    self.Moto_Karikata.insert(0, "（借）科目名")
    self.Moto_Karikata.grid(row=3, column=1)
    # ---------------------------------------------------------------------------------------
    tk.Label(self.frame6, text="元帳貸方科目列名").grid(row=4, column=0)  # 位置指定
    self.Moto_Kashikata = tk.Entry(self.frame6, width=10)
    self.Moto_Kashikata.insert(0, "（貸）科目名")
    self.Moto_Kashikata.grid(row=4, column=1)
    # ---------------------------------------------------------------------------------------
    # 全行自動仕訳ボタン-------------------------------------------------------------
    self.AllRun = tk.Button(
        self.frame6,
        text="全行自動仕訳",
        bg="LavenderBlush",
        width=20,
        command=lambda: self.AJAllCalc(self.FileName),
    )
    self.AllRun.grid(row=5, column=0, columnspan=2, sticky=tk.W + tk.E)  # 位置指定
    # 選択行自動仕訳作成ボタン----------------------------------------------------------------
    self.AJ_Btn = tk.Button(
        self.frame6,
        text="選択行仕訳予想検索",
        width=20,
        command=lambda: self.AJCalc(self.FileName),
        bg="lightblue",
    )
    self.AJ_Btn.grid(row=6, column=0, columnspan=2, sticky=tk.W + tk.E)  # 位置指定
    # -------------------------------------------------------------------------------------
    # 抽出仕訳転記ボタン----------------------------------------------------------------
    self.AJ_copy = tk.Button(
        self.frame6,
        text="抽出仕訳転記",
        width=20,
        command=lambda: self.AJ_copyCalc(self.FileName),
        bg="pink",
    )
    self.AJ_copy.grid(row=7, column=0, columnspan=2, sticky=tk.W + tk.E)  # 位置指定
    # -------------------------------------------------------------------------------------
    # 元帳表示ボタン----------------------------------------------------------------
    self.AJ_copy = tk.Button(
        self.frame6,
        text="元帳表示",
        width=20,
        command=lambda: self.ReadM(self.Roolurl),
        bg="PaleGreen",
    )
    self.AJ_copy.grid(row=8, column=0, columnspan=2, sticky=tk.W + tk.E)  # 位置指定
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
    self.Mframe.scrollbar_y.grid_forget()  # スクロールバー削除
    # スクロールバー再作成--------------------------------------------------
    self.Mframe.scrollbar_y = ttk.Scrollbar(
        self.Mframe.scrollable_frame,
        orient="vertical",
        command=self.Mframe.canvas.yview,
    )
    # ---------------------------------------------------------------------
    self.Mframe.scrollbar_y.grid(row=0, rowspan=3, column=5, sticky=tk.S + tk.N)
    self.Mframe.canvas.configure(yscrollcommand=self.Mframe.scrollbar_y.set)
    self.Mframe.scrollbar_x.grid_forget()  # スクロールバー削除
    # スクロールバー再作成--------------------------------------------------
    self.Mframe.scrollbar_x = ttk.Scrollbar(
        self.Mframe.scrollable_frame,
        orient="horizontal",
        command=self.Mframe.canvas.xview,
    )
    # ---------------------------------------------------------------------
    self.Mframe.scrollbar_x.grid(row=2, column=0, columnspan=5, sticky=tk.E + tk.W)
    self.Mframe.canvas.configure(xscrollcommand=self.Mframe.scrollbar_x.set)


# ####################################################################################################
# サブフレーム#########################################################################################
def create_Frame4(self):

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
    pt5.show()

    self.AJsetFrame = tk.Frame(
        self.Sub_Frame, width=650, height=400, bd=2, relief=tk.RIDGE
    )  # 親フレーム
    self.AJsetFrame.grid(row=1, column=0, sticky=tk.N + tk.S + tk.W + tk.E)
    self.AJsetSub_Frame = tk.Frame(self.AJsetFrame, width=650, height=400)
    tk.Label(self.AJsetFrame, text="テキスト変換ルール").grid(
        row=0, column=0, sticky=tk.W
    )  # 位置指定
    self.AJsetSub_Frame.grid(
        row=1, column=0, columnspan=5, sticky=tk.N + tk.S + tk.W + tk.E
    )
    pt4 = MT.MyTable4(
        self.AJsetSub_Frame, width=650, height=150, sticky=tk.N + tk.S + tk.W + tk.E
    )  # テーブルをサブクラス化
    enc = CSVO.getFileEncoding(self.ChangeTxtURL)
    self.table4 = pt4.importCSV(self.ChangeTxtURL, encoding=enc)
    self.pt4 = pt4
    pt4.show()
    # 行追加ボタン--------------------------------------------------------------------
    self.Sub_RowInsert = tk.Button(
        self.AJsetFrame,
        text="行追加",
        bg="LightYellow",
        width=20,
        command=self.Sub_RowInsert,
    )
    self.Sub_RowInsert.grid(row=2, column=0, sticky=tk.W)  # 位置指定
    # 列追加ボタン--------------------------------------------------------------------
    self.Sub_ColumnInsert = tk.Button(
        self.AJsetFrame,
        text="列追加",
        bg="Lightblue",
        width=20,
        command=self.Sub_ColumnInsert,
    )
    self.Sub_ColumnInsert.grid(row=2, column=1)  # 位置指定
    # 行削除ボタン--------------------------------------------------------------------
    self.Sub_RowDelete = tk.Button(
        self.AJsetFrame,
        text="行削除",
        bg="darkorange",
        width=20,
        command=self.Sub_RowDelete,
    )
    self.Sub_RowDelete.grid(row=2, column=2)  # 位置指定
    # 列削除ボタン--------------------------------------------------------------------
    self.Sub_ColumnDelete = tk.Button(
        self.AJsetFrame,
        text="列削除",
        bg="darkgreen",
        width=20,
        command=self.Sub_ColumnDelete,
    )
    self.Sub_ColumnDelete.grid(row=2, column=3)  # 位置指定
    # 戻るボタン--------------------------------------------------------------------
    self.Sub_CloseBtn = tk.Button(
        self.AJsetFrame,
        text="戻る",
        bg="gray80",
        width=20,
        command=self.Sub_ReturnBack,
    )
    self.Sub_CloseBtn.grid(row=2, column=4, sticky=tk.E)  # 位置指定
    # メニューフレーム作成-----------------------------------------------------------
    self.AJsetMenuFrame = tk.Frame(
        self.Sub_Frame, width=650, height=400, bd=2, relief=tk.RIDGE
    )  # 親フレーム
    self.AJsetMenuFrame.grid(row=2, column=0, sticky=tk.N + tk.S + tk.W + tk.E)
