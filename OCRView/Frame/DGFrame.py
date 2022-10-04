import tkinter as tk

# import tkinter.ttk as ttk
import Frame.MyTable as MT
import CSVOut as CSVO

# import ScrollableFrame as SF
from pandas import read_csv, concat

# from csv import QUOTE_NONNUMERIC

# メインフレーム######################################################################################
def create_Frame(self, wid, hei):
    # ツリーフレーム設定---------------------------------------------------------------------
    self.OCR_frame = tk.Frame(
        self.Main_Frame, width=wid, height=hei, bd=2, relief=tk.RIDGE
    )  # 親フレーム
    self.OCR_frame.grid(row=0, column=0, sticky=tk.N + tk.S + tk.W + tk.E)
    self.tree_frame = tk.Frame(self.OCR_frame, width=wid, height=hei)  # 子フレーム
    tk.Label(self.OCR_frame, text="OCR抽出結果表").grid(
        row=0, column=0, sticky=tk.N + tk.W
    )  # 位置指定
    self.tree_frame.grid(row=1, column=0, sticky=tk.N + tk.S + tk.W + tk.E)
    # df = TableModel.getSampleData()
    # pt = Table(self.tree_frame)
    pt = MT.MyTable(
        self.tree_frame, width=wid, height=hei, sticky=tk.N + tk.S + tk.W + tk.E
    )  # テーブルをサブクラス化
    enc = CSVO.getFileEncoding(self.FileName)
    self.table = pt.importCSV(self.FileName, encoding=enc)
    self.pt = pt
    self.pt._name = "OCR抽出結果表Main"
    # DF型変換------------------------------
    PandasAstype(self.pt.model.df)
    # --------------------------------------
    pt.show()


# メインフレーム######################################################################################
def create_Frame2(self, wid, hei, CSVList, G_logger):
    # ツリーフレーム設定---------------------------------------------------------------------
    self.OCR_frame2 = tk.Frame(
        self.Main_Frame, width=wid, height=hei, bd=2, relief=tk.RIDGE
    )  # 親フレーム
    self.OCR_frame2.grid(row=0, column=1, sticky=tk.N + tk.S + tk.W + tk.E)
    self.tree_frame2 = tk.Frame(self.OCR_frame2, width=wid, height=hei)  # 子フレーム
    tk.Label(self.OCR_frame2, text="比較ファイル").grid(
        row=0, column=0, sticky=tk.N + tk.W
    )  # 位置指定
    self.tree_frame2.grid(row=1, column=0, sticky=tk.N + tk.S + tk.W + tk.E)
    # df = TableModel.getSampleData()
    # pt = Table(self.tree_frame)
    pt2 = MT.MyTable(
        self.tree_frame2, width=wid, height=hei, sticky=tk.N + tk.S + tk.W + tk.E
    )  # テーブルをサブクラス化
    self.pt2 = pt2
    self.pt2._name = "比較ファイルMain"
    JCSV = JoinCSV(CSVList, G_logger)
    if JCSV[0] is True:
        self.pt2.model.df = JCSV[1]
        # DF型変換------------------------------
        PandasAstype(self.pt2.model.df)
        # --------------------------------------
        pt2.show()


# -------------------------------------------------------------------------------------
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


# -------------------------------------------------------------------------------------
def JoinCSV(CSVList, G_logger):
    """
    概要: 引数リストのURLから連結CSVを作成
    @param CSVList: CSVURLリスト
    @return 連結CSVURL
    """
    try:
        r = 0
        for CSVListItem in CSVList:
            if r == 0:
                enc = CSVO.getFileEncoding(CSVListItem)
                m_csv = read_csv(CSVListItem, encoding=enc)
                G_logger.debug(CSVListItem + "_先頭ページ連結完了")  # Log出力
            else:
                enc = CSVO.getFileEncoding(CSVListItem)
                r_csv = read_csv(CSVListItem, encoding=enc)
                G_logger.debug(CSVListItem + "_" + str(r) + "ページ連結完了")  # Log出力
                m_csv = concat([m_csv, r_csv])
            r += 1
        G_logger.debug("ページ連結完了")  # Log出力
        return True, m_csv
    except:
        G_logger.debug("ページ連結失敗")  # Log出力
        return False, ""
