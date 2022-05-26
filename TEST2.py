from decimal import Underflow
import os
import csv
from wsgiref.headers import tspecials
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
imgurl = r"D:\PythonScript\RPAScript\RPAPhoto\PDFeTaxReadForList\TEST0.png"
# FLDインスタンス生成
FLDs = FIC.FastLineDetector(
    r"D:\PythonScript\RPAScript\RPAPhoto\PDFeTaxReadForList\\NoiseRemovalTEST0.png",
    5,
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
        ThFL = FLSort[FL][0][1].T  # 現在のx値
        NeFL = FLSort[FL + 1][0][1].T  # 次のx値
        if FL == 0:
            GyouRanges = np.array(NeFL - ThFL)  # np配列作成
        else:
            GyouRanges = np.append(GyouRanges, NeFL - ThFL)  # np配列追加
# 　-----------------------------------------------------------
avg = np.average(GyouRanges)  # 全ての行間x値の平均値
FLCount = 0
Frow = 0
FCF = False
# 　線形ピクセル配列ループ---------------------------------------
for FL in range(len(FLSort)):
    if not FL == len(FLSort) - 1:
        FLRn = FLSort[FL + 1][0][1].T - FLSort[FL][0][1].T
        if avg > FLRn:
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
FCBF = False
for FCB in range(len(FCFBlock)):
    if FCFBlock[FCB][2] > 5:
        r1 = FCFBlock[FCB][0]
        r2 = FCFBlock[FCB][1]
        for FCin in range(r1, r2):
            if FCBF is False:
                FinalIn = np.array(FLSort[FCin])
                FCBF = True
            else:
                FinalIn = np.append(FinalIn, FLSort[FCin], axis=0)
F0min = np.min(FinalIn[:, 0])
F0max = np.max(FinalIn[:, 0])
F1min = np.min(FinalIn[:, 1])
F1max = np.max(FinalIn[:, 1])
F2min = np.min(FinalIn[:, 2])
F2max = np.max(FinalIn[:, 2])
F3min = np.min(FinalIn[:, 3])
F3max = np.max(FinalIn[:, 3])

img = cv2.imread(
    r"D:\PythonScript\RPAScript\RPAPhoto\PDFeTaxReadForList\\NoiseRemovalTEST0.png"
)
size = img.shape  # 画像のサイズ x,y

LeftHigh = [FinalIn[0][0] + (size[1] / 100), FinalIn[0][1] + (size[0] / 100)]


img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
LeftHigh, RightHigh, LeftLow, RightLow = FIC.trimImageNumNum(URL, img)

p1 = np.array(LeftHigh)  # 左上
p2 = np.array(RightHigh)  # 右上
p3 = np.array(LeftLow)  # 左下
p4 = np.array(RightLow)  # 右下
o_width = np.linalg.norm(p2 - p1)
o_width = int(np.floor(o_width))
o_height = np.linalg.norm(p3 - p1)
o_height = int(np.floor(o_height))

pts1 = np.float32([LeftHigh, RightHigh, LeftLow, RightLow])
pts2 = np.float32([[0, 0], [o_width, 0], [0, o_height], [o_width, o_height]])

M = cv2.getPerspectiveTransform(pts1, pts2)

dst = cv2.warpPerspective(img, M, (o_width, o_height))

plt.subplot(121), plt.imshow(img), plt.title("Input")
plt.subplot(122), plt.imshow(dst), plt.title("Output")
plt.show()
time.sleep(2)
