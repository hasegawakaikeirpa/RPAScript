from tkinter import filedialog, messagebox
import tkinter as tk
import os
import numpy as np
from chardet.universaldetector import UniversalDetector
import tomli_w

# -----------------------------------------------------------------------------------
def getFileEncoding(file_path):  # .format( getFileEncoding( "sjis.csv" ) )
    if os.path.isfile(file_path) is True:
        detector = UniversalDetector()
        with open(file_path, mode="rb") as f:
            for binary in f:
                detector.feed(binary)
                if detector.done:
                    break
        detector.close()
        return detector.result["encoding"]
    else:
        messagebox.showinfo("確認", file_path + "\nが存在しません。")
        return ""


# -----------------------------------------------------------------------------------
def blankno(List):
    if len() != 0:
        TN_List = [int(str(t[0][0]).replace("Line", "")) for t in List]
        TN_List.sort()
        N_TN_r = 0
        for TN_r in TN_List:
            if N_TN_r == 0:
                N_TN_r = TN_r + 1
            else:
                if N_TN_r == TN_r:
                    N_TN_r = TN_r + 1
                else:
                    return N_TN_r
        N_TN_r = TN_r + 1
        return N_TN_r
    else:
        return 1


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
                    df[col] = df[col].astype(np.int16)
                elif (
                    c_min > np.finfo(np.float32).min
                    and c_max < np.finfo(np.float32).max
                ):
                    # df[col] = df[col].astype(np.float32)
                    df[col] = df[col].astype(np.int32)
                else:
                    # df[col] = df[col].astype(np.float64)
                    df[col] = df[col].astype(np.int64)
        else:
            df[col] = df[col].astype("object")
            # df[col] = df[col].astype("category")

    end_mem = df.memory_usage().sum() / 1024**2
    print("Memory usage after optimization is: {:.2f} MB".format(end_mem))
    print("Decreased by {:.1f}%".format(100 * (start_mem - end_mem) / start_mem))

    return df


# -------------------------------------------------------------------------------------
def dump_toml(toml_dict, path):
    """
    tomlで読み込んだ辞書をtomlファイルに出力する
    """
    try:
        with open(path, "wb") as configfile:
            tomli_w.dump(toml_dict, configfile)
    except:
        print("Err")


# def LinOCROpen(self):
#     """
#     OCROpenボタンクリックイベント
#     """
#     typ = [("tomlファイル", "*.toml")]
#     self.tomlPath = tk.filedialog.askopenfilename(
#         filetypes=typ, initialdir=self.dir_path
#     )

#     FDir = self.entry_dir.get()
#     FN = self.combo_file.get()
#     Imgurl = FDir + r"\\" + FN
#     Imgurl = Imgurl.replace("/", r"\\")
#     if "[select file]" in Imgurl:
#         tk.messagebox.showinfo("確認", "画像ファイルを選択してください。")
#     else:
#         Main(main_window, Imgurl, self.tomlPath)
