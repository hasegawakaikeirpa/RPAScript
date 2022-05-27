import Function.GCloudVision as GCV
import numpy as np
import csv
from collections import OrderedDict

strs = ""  # テキスト代入変数
FstrList = []
with open(
    r"D:\PythonScript\RPAScript\RPAPhoto\PDFeTaxReadForList\XYList.csv",
    mode="r",
    encoding="shiftjis",
    errors="ignore",
    newline="",
) as f:
    CSVList = list(csv.reader(f))
YList = []
for CSVListItem in CSVList:
    YList.append(int(CSVListItem[3]))
near = 50
YDicList = list(OrderedDict.fromkeys(YList))  # 抽出リストの重複削除
YD = len(YDicList)
NewList = []
# Y軸リストを閾値(near)で統一し置換(行を揃える)----------------------------------
for YDN in range(YD):
    if not YDN == YD - 1:
        key = YDicList[YDN]
        for YDNN in range(YD):
            key2 = YDicList[YDNN]
            Sa = key - key2
            if Sa < 0:
                if Sa >= (near * -1):
                    YDicList[YDNN] = key
            else:
                if Sa <= near:
                    YDicList[YDNN] = key
# Y軸リストを閾値で統一し置換(行を揃える)----------------------------------------
for YDicListItem in YDicList:
    YList = GCV.getNearestValue(YList, YDicListItem, near)
print(YList)
# ---------------------------------------------------------------------------
Ys = 0
# 行を揃えたY軸リストを元にXYListを作成-----------------------------------------
for YListItem in YList:
    CSVList[Ys][3] = YListItem
    Ys += 1
# ---------------------------------------------------------------------------
