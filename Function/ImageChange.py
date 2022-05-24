from PIL import Image, ImageOps
import numpy as np
import cv2
import matplotlib.pyplot as plt
from numba import jit

# loggerインポート
from logging import getLogger

logger = getLogger()


def ImageYugami(
    URL,
    img,
    lPix,
    tPix,
    rPix,
    bPix,
):
    path = img  # 画像のパス
    i = cv2.imread(path, 1)  # 画像読み込み
    print(i.shape)

    # 変換前後の対応点を設定
    p1 = np.array([46, 159])  # 左上
    p2 = np.array([421, 64])  # 右上
    p3 = np.array([38, 246])  # 左下
    p4 = np.array([428, 174])  # 右下

    o_width = np.linalg.norm(p2 - p1)
    o_width = int(np.floor(o_width))
    o_height = np.linalg.norm(p3 - p1)
    o_height = int(np.floor(o_height))

    ori_cor = np.float32([p1, p2, p3, p4])
    dst_cor = np.float32([[0, 0], [o_width, 0], [0, o_height], [o_width, o_height]])

    # 変換マトリクスと射影変換
    M = cv2.getPerspectiveTransform(ori_cor, dst_cor)
    cor_src = cv2.warpPerspective(i, M, (o_width, o_height))

    cv2.imwrite(URL + "\\ImageYugami.jpg", cor_src)


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
    ksize = 11
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


# @jit
def trimImageNumNum(URL, img):
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
    lPixShape = []
    tPixShape = []
    rPixShape = []
    bPixShape = []
    # # ピクセル操作
    for x in range(size[0]):
        for y in range(size[1]):
            r, g, b = img[x, y]
            rr, rg, rb = img[(size[0] - x - 1, size[1] - y - 1)]

            # 色付きのピクセルかどうか（白もしくは白に近しい色を切り抜くため）
            rgbs = int(r) + int(g) + int(b)
            rrgbs = int(rr) + int(rg) + int(rb)
            if rgbs < 600 and len(lPixShape) == 0:
                if lPix == -1:
                    lPix = x
                    lPixShape = [x, y]
            elif rgbs < 600:
                if y < tPix:
                    tPix = y
                    tPixShape = [x, y]

            if rrgbs < 600 and len(rPixShape) == 0:
                if rPix == -1 and len(rPixShape) == 0:
                    rPix = size[0] - x
                    rPixShape = [size[0] - x, size[1] - y]
            elif rrgbs < 600:
                if size[1] - y > bPix:
                    bPix = size[1] - y
                    bPixShape = [size[0] - x, size[1] - y]
    try:
        tPix = tPix
        lPix = lPix
        bPix = bPix
        rPix = rPix
    except:
        return tPix, lPix, bPix, rPix, lPixShape, tPixShape, rPixShape, bPixShape
    return (
        tPix,
        lPix,
        bPix,
        rPix,
        lPixShape,
        tPixShape,
        rPixShape,
        bPixShape,
    )


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
    lPix, tPix, rPix, bPix = lPix - 200, tPix - 100, rPix + 100, bPix + 200
    img = trimImageSave(URL, img, lPix, tPix, rPix, bPix, imgurl)
    img = Image.open(img)
    img = img.resize(size=(8000, 8000), resample=Image.BILINEAR)
    img.save(imgurl)
    ImageYugami(URL, imgurl)
    return imgurl
