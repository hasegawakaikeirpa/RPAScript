from re import M
import numpy as np
import pandas as pd

from datetime import date
from dateutil.relativedelta import relativedelta

Url = r"D:\OCRTESTPDF\PDFTEST\1869\1869_仕訳日記帳.csv"
Finddf = pd.read_csv(Url, encoding="cp932")

M = "['3']"
M = M.replace("['", "").replace("']", "")

today = date.today()
next_Month = relativedelta(months=int(M))
D = today - next_Month

FinddfCol = Finddf.columns  # 元帳DFの列名
Finddf = np.array(Finddf)  # 元帳DFをnp変換
ind = np.where(FinddfCol == "伝票日付")  # 元帳DFの日付列番号
F_Data = Finddf[1 : Finddf.shape[0], :]  # 元帳DFData
Finddf_Date = Finddf[1 : Finddf.shape[0], ind]  # 元帳DFの日付列のみ抽出
Finddf_Date_Dim = Finddf_Date.flatten()  # 元帳DFの日付列を1次元化
Finddf_Date = pd.Series(Finddf_Date_Dim)  # 1次元化した元帳DFの日付列をシリーズ化
Finddf_Date = Finddf_Date.astype("datetime64")  # シリーズ化した元帳DFの日付列を型変換
convert_time = Finddf_Date.dt.month  # シリーズ化した元帳DFの日付列から月のみ抽出
convert_time = np.array(convert_time)

ind = np.where(convert_time >= int(D.month))  # 元帳DFの日付列番号
F_Data = F_Data[ind]
Ret_Data = np.vstack([FinddfCol, F_Data])
