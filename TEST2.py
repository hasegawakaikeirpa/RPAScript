import os
import csv
import toml
import Function.ImageChange as FIC
from PIL import Image, ImageOps
import cv2
import numpy as np
import matplotlib.pyplot as plt
import time

# # toml読込------------------------------------------------------------------------------
# with open(
#     os.getcwd() + r"/RPAPhoto/PDFeTaxReadForList/BankSetting.toml", encoding="utf-8"
# ) as f:
#     Banktoml = toml.load(f)
#     Banktoml = Banktoml["Hirogin"]
#     print(Banktoml)
# # -----------------------------------------------------------
URL = os.getcwd()
imgurl = r"D:\PythonScript\RPAScript\RPAPhoto\PDFeTaxReadForList\NoiseRemovalTEST0.png"
img = cv2.imread(imgurl)
size = img.shape  # 画像のサイズ x,y
Pix = int(size[0] / 400)  # 検出ピクセル数
if Pix <= 0:
    Pix = 1
# FLDインスタンス生成
FLDs = FIC.FastLineDetector(
    imgurl,
    Pix,
    1.41421356,
    50.0,
    50.0,
    3,
    True,
)  # boolean,yx値
FLnum = FLDs[1]
FLSort = FLnum[FLnum[:, 0][:, 1].argsort(), :]  # x軸基準に昇順並びかえ
print(FLSort)
# 　線形ピクセル配列ループ---------------------------------------
for FL in range(len(FLSort)):
    if not FL == len(FLSort) - 1:  # 最終行でなければ
        ThFL = FLSort[FL][0][1].T  # 現在の上辺x値
        NeFL = FLSort[FL + 1][0][1].T  # 次の上辺x値
        ThUFL = FLSort[FL][0][1].T  # 現在の下辺x値
        if FL == 0:
            GyouRanges = np.array(NeFL - ThFL)  # np配列作成

        else:
            GyouRanges = np.append(GyouRanges, NeFL - ThFL)  # np配列追加
# 　-----------------------------------------------------------
avg = np.average(GyouRanges)  # 全ての行間x値の平均値
FLCount = 0  # Numpy配列インデックス加算用
Frow = 0  # Numpy配列インデックス格納用
FCF = False  # 配列作成フラグ
# 行間のx値が平均値未満の行を一塊として配列格納--------------------
for FL in range(len(FLSort)):
    if not FL == len(FLSort) - 1:  # 最終行でなければ
        FLRn = FLSort[FL + 1][0][1].T - FLSort[FL][0][1].T  # 次のx値 - 現在のx値
        if avg > FLRn:  # 全ての行間x値の平均値より小さければ
            if FLCount == 0:
                FLCount += 1
                Frow = FL
            else:
                FLCount += 1
        else:
            if FCF is False:
                FCFBlock = np.array([[Frow, Frow + FLCount, FLCount]])
                FLCount = 0
                Frow = FL + 1
                FCF = True
            else:
                FCFBlock = np.append(
                    FCFBlock, [[Frow, Frow + FLCount, FLCount]], axis=0
                )
                FLCount = 0
                Frow = FL + 1
                FCF = True
# 　-----------------------------------------------------------
FCBF = False  # 配列作成フラグ
Kijyun = Pix = int(size[0] / 100)
# 行の集合体に基準値より多いデータのみを抽出-----------------------
for FCB in range(len(FCFBlock)):
    if FCFBlock[FCB][2] > Kijyun:  # 基準値
        r1 = FCFBlock[FCB][0]
        r2 = FCFBlock[FCB][1]
        for FCin in range(r1, r2):
            if FCBF is False:
                FinalIn = np.array(FLSort[FCin])
                FCBF = True
            else:
                FinalIn = np.append(FinalIn, FLSort[FCin], axis=0)
# 　-----------------------------------------------------------
print(
    "=================================================================================="
)
FinalIn = FinalIn[FinalIn[:, 1].argsort()]
print(FinalIn)

TopYmin = np.min(FinalIn[:, 0])  # 検出文字上辺y値の最小値(上辺最左)
TopYmax = np.max(FinalIn[:, 0])  # 検出文字上辺y値の最大値(上辺最右)
TopXmin = np.min(FinalIn[:, 1])  # 検出文字上辺x値の最小値(上辺最上)
TopXmax = np.max(FinalIn[:, 1])  # 検出文字上辺x値の最大値(上辺最下)
UnderYmin = np.min(FinalIn[:, 2])  # 検出文字下辺y値の最小値(下辺最左)
UnderYmax = np.max(FinalIn[:, 2])  # 検出文字下辺y値の最大値(下辺最右)
UnderXmin = np.min(FinalIn[:, 3])  # 検出文字下辺x値の最小値(下辺最上)
UnderXmax = np.max(FinalIn[:, 3])  # 検出文字下辺x値の最大値(下辺最下)

LeftHigh = [TopYmin - size[1] / 100, TopXmin - size[0] / 100]
RightHigh = [TopYmax + size[1] / 100, TopXmin - size[0] / 100]
LeftLow = [TopYmin - size[1] / 100, TopXmax + size[0] / 100]
RightLow = [TopYmax + size[1] / 100, TopXmax + size[0] / 100]

img = Image.open(imgurl)
# 回転-----------------------------------------------------------------------
# Kakuavg = np.nanmean(tan) * 10  # 認識文字の上辺と下辺のx値差から回転角度を計算
# img = img.rotate(Kakuavg)
# im_rotate.save(imgurl)
# ---------------------------------------------------------------------------
FIC.trimImageSave(
    URL,
    img,
    int(LeftHigh[0]),
    int(LeftHigh[1]),
    int(RightLow[0]),
    int(RightLow[1]),
    imgurl,
)
time.sleep(2)
