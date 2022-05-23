from PIL import Image, ImageOps
import numpy as np
import cv2
import matplotlib.pyplot as plt
from numba import jit

# loggerインポート
from logging import getLogger

logger = getLogger()


def show_image(img, **kwargs):
    """
    Show an RGB numpy array of an image without any interpolation
    """
    plt.subplot()
    plt.axis("off")
    plt.imshow(X=img, interpolation="none", **kwargs)


def ColorInverter(img):
    """
    概要: 画像白黒反転
    @param img: Image.openで開いた画像
    @return 白黒反転した画像(cv2)
    """
    img.convert("RGB")
    Inv_img = ImageOps.invert(img)
    return Inv_img


def NoiseRemoval(img):
    """
    概要: 画像ノイズ除去（収縮⇒膨張）
    @param img: Image.openで開いた画像
    @return 画像ノイズ除去した画像(cv2)
    """
    kernel = np.ones((2, 2))
    Open_img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    ksize = 29
    # 中央値フィルタ
    Open_img = cv2.medianBlur(Open_img, ksize)
    return Open_img


def NoiseExpCont(img):
    """
    概要: 画像膨張・収縮処理
    @param img: cv2で開いた画像
    @return 膨張・収縮した画像(cv2)
    """
    # 近傍の定義
    neiborhood = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]], np.uint8)
    # 収縮
    img_erode = cv2.erode(img, neiborhood, iterations=100)
    # 膨張
    img_dilate = cv2.dilate(img_erode, neiborhood, iterations=100)
    # 膨張
    img_dilate = cv2.dilate(img_dilate, neiborhood, iterations=100)
    # 収縮
    img_erode = cv2.erode(img_dilate, neiborhood, iterations=100)
    return img_erode


@jit
def trimImageNum(URL, img):
    """
    概要: 画像の余白をトリミング
    @param URL: 画像フォルダ(str)
    @param img: cv2で開いた画像
    @return トリミング軸数値
    """
    size = img.shape
    tPix = 100000000
    bPix = -1
    lPix = -1
    rPix = -1

    # # ピクセル操作
    for x in range(size[0]):
        for y in range(size[1]):
            r, g, b = img[x, y]
            rr, rg, rb = img[(size[0] - x - 1, size[1] - y - 1)]

            # 色付きのピクセルかどうか（白もしくは白に近しい色を切り抜くため）
            if (r + g + b) < 600:
                if lPix == -1:
                    lPix = x
                if y < tPix:
                    tPix = y

            if (rr + rg + rb) < 600:
                if rPix == -1:
                    rPix = size[0] - x
                if size[1] - y > bPix:
                    bPix = size[1] - y
    try:
        tPix = tPix - 20
        lPix = lPix - 20
        bPix = bPix + 20
        rPix = rPix + 20
    except:
        return tPix, lPix, bPix, rPix
    return tPix - 10, lPix - 10, bPix + 10, rPix + 10


def trimImageSave(URL, img, lPix, tPix, rPix, bPix, imgurl):
    try:
        trimImageFile = img.crop((lPix, tPix, rPix, bPix))  # トリミング
        trimImageFile.save(imgurl, quality=100)  # 保存
        return imgurl
    except:
        print("Error")
        return "エラー"


def OCRIMGChange(URL, imgurl):
    """
    概要: 画像白黒反転後画像ノイズ除去（収縮⇒膨張）
    @param URL: 画像フォルダ(str)
    @param imgurl: 画像URL(str)
    @return 画像白黒反転後画像ノイズ除去した画像URL(str)
    """
    img = Image.open(imgurl)  # 画像オープン
    Inv_img = ColorInverter(img)  # 白黒反転
    Inv_img.save(URL + "\\CI.png")  # 白黒反転保存
    img = cv2.imread(URL + "\\CI.png", 0)  # 白黒反転画像
    CleanUp_img = NoiseRemoval(img)  # ノイズ除去
    cv2.imwrite(URL + "\\CleanUp_img.png", CleanUp_img)  # ノイズ除去保存
    img = Image.open(URL + "\\CleanUp_img.png")  # 画像オープン
    Inv_img = ColorInverter(img)  # 白黒反転
    Inv_img.save(URL + "\\Last.png")  # 白黒反転保存
    img = cv2.imread(
        filename=URL + "\\Last.png",
        flags=cv2.IMREAD_COLOR,
    )
    # imgsize = img.shape
    img = NoiseExpCont(img)
    lPix, tPix, rPix, bPix = trimImageNum(URL, img)
    img = Image.open(imgurl)  # 画像オープン
    img = trimImageSave(URL, img, lPix, tPix, rPix, bPix, imgurl)
    img = Image.open(img)
    img = img.resize(size=(8000, 8000), resample=Image.BILINEAR)
    img.save(imgurl)
    return imgurl
