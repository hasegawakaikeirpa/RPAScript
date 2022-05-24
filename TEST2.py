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
img = cv2.imread(
    filename=imgurl,
    flags=cv2.IMREAD_COLOR,
)

img = FIC.NoiseRemoval(img)
cv2.imwrite(
    r"D:\PythonScript\RPAScript\RPAPhoto\PDFeTaxReadForList\\NoiseRemovalTEST0.png", img
)
img = Image.open(
    r"D:\PythonScript\RPAScript\RPAPhoto\PDFeTaxReadForList\\NoiseRemovalTEST0.png"
)
img = cv2.imread(
    filename=r"D:\PythonScript\RPAScript\RPAPhoto\PDFeTaxReadForList\\NoiseRemovalTEST0.png",
    flags=cv2.IMREAD_COLOR,
)
(
    lPix,
    tPix,
    rPix,
    bPix,
    lPixShape,
    tPixShape,
    rPixShape,
    bPixShape,
) = FIC.trimImageNumNum(URL, img)
print(lPixShape)

rows, cols, ch = img.shape

# pts1 = np.float32([lPixShape, tPixShape, rPixShape, bPixShape])
pts1 = np.float32([[880, 1865], [3530, 1800], [930, 5257], [3620, 5250]])
# lps1 = lPixShape[0]
# lps2 = lPixShape[1]
# tps1 = tPixShape[0]
# tps2 = tPixShape[1]
# rps1 = rPixShape[0]
# rps2 = rPixShape[1]
# bps1 = bPixShape[0]
# bps2 = bPixShape[1]

pts2 = np.float32([[0, 0], [4135, 0], [0, 5848], [4135, 5848]])

M = cv2.getPerspectiveTransform(pts1, pts2)

dst = cv2.warpPerspective(img, M, (4135, 5848))

plt.subplot(121), plt.imshow(img), plt.title("Input")
plt.subplot(122), plt.imshow(dst), plt.title("Output")
plt.show()
time.sleep(2)
