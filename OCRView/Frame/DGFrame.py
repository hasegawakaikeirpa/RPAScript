import tkinter as tk
import tkinter.ttk as ttk
import Frame.MyTable as MT
import CSVOut as CSVO
import ScrollableFrame as SF


# メインフレーム######################################################################################
def create_Frame(self,wid,hei):
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
