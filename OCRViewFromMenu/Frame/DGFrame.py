import tkinter as tk
import Frame.MyTable as MT
import CSVOut as CSVO
import numpy as np
from pandas import read_csv, concat
from pandastable import config

# メインフレーム######################################################################################
def create_Frame(self, wid, hei, t_font, hei_Par):
    # ツリーフレーム設定---------------------------------------------------------------------
    self.OCR_frame = tk.Frame(
        self.Main_Frame, width=wid, height=hei, bd=2, bg="#fce4d2", relief=tk.RIDGE
    )  # 親フレーム
    # self.OCR_frame.grid(row=0, column=0, sticky=tk.N + tk.S + tk.W + tk.E)
    self.OCR_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    self.tree_frame = tk.Frame(
        self.OCR_frame, width=wid, height=hei, bg="#fce4d2"
    )  # 子フレーム
    # サイズグリップ
    # sizegrip = ttk.Sizegrip(self.OCR_frame)
    # sizegrip.grid(row=0, column=0, sticky=(tk.S, tk.E))
    tk.Label(self.OCR_frame, text="OCR抽出結果表", bg="#fce4d2").grid(
        row=0, column=0, sticky=tk.N + tk.W
    )  # 位置指定

    self.pt_bln = tk.BooleanVar()
    self.pt_bln.set(False)
    self.pt_chk = tk.Checkbutton(
        self.OCR_frame,
        bg="#fce4d2",
        text="変更を記録する",
        command=lambda: self.chk_click(self.pt_bln),
    )
    self.pt_chk.grid(row=1, column=0, sticky=tk.N + tk.W)

    self.tree_frame.grid(row=2, column=0, padx=30, sticky=tk.N + tk.S + tk.W + tk.E)
    # df = TableModel.getSampleData()
    # pt = Table(self.tree_frame)
    pt = MT.MyTable(
        self.tree_frame,
        width=int(wid * 0.90),
        height=int(hei * (hei_Par * 0.75)),
        sticky=tk.N + tk.S + tk.W + tk.E,
    )  # テーブルをサブクラス化
    enc = CSVO.getFileEncoding(self.FileName)
    self.table = pt.importCSV(self.FileName, encoding=enc)
    self.pt = pt
    self.pt._name = "OCR抽出結果表Main"
    # options is a dict that you can set yourself
    options = {"fontsize": t_font[1]}
    config.apply_options(options, self.pt)
    # DF型変換------------------------------
    Pandas_mem_usage(self.pt.model.df)
    # --------------------------------------
    self.pt.resized
    self.pt.show()


# メインフレーム######################################################################################
def create_Frame2(self, wid, hei, CSVList, t_font, hei_Par, G_logger):
    # ツリーフレーム設定---------------------------------------------------------------------
    self.OCR_frame2 = tk.Frame(
        self.Main_Frame, width=wid, height=hei, bd=2, bg="#fce4d2", relief=tk.RIDGE
    )  # 親フレーム
    # self.OCR_frame2.grid(row=0, column=1, sticky=tk.N + tk.S + tk.W + tk.E)
    self.OCR_frame2.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    self.tree_frame2 = tk.Frame(
        self.OCR_frame2, width=wid, height=hei, bg="#fce4d2"
    )  # 子フレーム
    tk.Label(self.OCR_frame2, text="比較ファイル", bg="#fce4d2").grid(
        row=0, column=0, sticky=tk.N + tk.W
    )  # 位置指定
    # ###########################################################################
    tk.Label(self.OCR_frame2, text="", bg="#fce4d2").grid(
        row=1, column=0, sticky=tk.N + tk.W
    )  # 位置指定
    # self.pt2_bln = tk.BooleanVar()
    # self.pt2_bln.set(False)
    # self.pt2_chk = tk.Checkbutton(
    #     self.OCR_frame2,
    #     bg="#fce4d2",
    #     text="変更を記録する",
    #     command=lambda: self.chk_click(self.pt2_bln),
    # )
    # self.pt2_chk.grid(row=1, column=0, sticky=tk.N + tk.W)
    # ###########################################################################
    self.tree_frame2.grid(row=2, column=0, sticky=tk.N + tk.S + tk.W + tk.E)
    # df = TableModel.getSampleData()
    # pt = Table(self.tree_frame)
    pt2 = MT.MyTable(
        self.tree_frame2,
        width=int(wid * 0.95),
        height=int(hei * (hei_Par * 0.75)),
        sticky=tk.N + tk.S + tk.W + tk.E,
    )  # テーブルをサブクラス化
    self.pt2 = pt2
    self.pt2._name = "比較ファイルMain"
    self.pt2.fontsize = 6
    JCSV = JoinCSV(CSVList, G_logger)
    if JCSV[0] is True:
        self.pt2.model.df = JCSV[1]
        options = {"fontsize": t_font[1]}
        config.apply_options(options, self.pt2)
        # DF型変換------------------------------
        Pandas_mem_usage(self.pt2.model.df)
        # --------------------------------------
        self.pt2.show()


# -------------------------------------------------------------------------------------
def Pandas_mem_usage(df):
    """
    Pandasデータフレームのメモリ最適化
    """
    start_mem = df.memory_usage().sum() / 1024**2
    print("Memory usage of dataframe is {:.2f} MB".format(start_mem))

    for col in df.columns:
        col_type = df[col].dtype

        if col_type != object:
            c_min = df[col].min()
            c_max = df[col].max()
            if str(col_type)[:3] == "int":
                if c_min > np.iinfo(np.int8).min and c_max < np.iinfo(np.int8).max:
                    df[col] = df[col].astype(np.int8)
                elif c_min > np.iinfo(np.int16).min and c_max < np.iinfo(np.int16).max:
                    df[col] = df[col].astype(np.int16)
                elif c_min > np.iinfo(np.int32).min and c_max < np.iinfo(np.int32).max:
                    df[col] = df[col].astype(np.int32)
                elif c_min > np.iinfo(np.int64).min and c_max < np.iinfo(np.int64).max:
                    df[col] = df[col].astype(np.int64)
            else:
                if (
                    c_min > np.finfo(np.float16).min
                    and c_max < np.finfo(np.float16).max
                ):
                    # df[col] = df[col].astype(np.float16)
                    df[col] = df[col].astype("object")
                elif (
                    c_min > np.finfo(np.float32).min
                    and c_max < np.finfo(np.float32).max
                ):
                    # df[col] = df[col].astype(np.float32)
                    df[col] = df[col].astype("object")
                else:
                    # df[col] = df[col].astype(np.float64)
                    df[col] = df[col].astype("object")
        else:
            df[col] = df[col].astype("object")
            # df[col] = df[col].astype("category")

    end_mem = df.memory_usage().sum() / 1024**2
    print("Memory usage after optimization is: {:.2f} MB".format(end_mem))
    print("Decreased by {:.1f}%".format(100 * (start_mem - end_mem) / start_mem))

    return df


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
