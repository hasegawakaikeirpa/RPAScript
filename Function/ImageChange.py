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


# FLDテスト処理
# fileImage : 画像ファイルパス
#
def FastLineDetector(fileImage, lenth, disth, canth1, canth2, casize, dom):
    """
    概要: 画像の線形を検出
    @param lenth: 検出する最小の線分のピクセル数(int)
    @param disth: マージする線分の距離(float)
    @param canth1: Canny Edge Detectorの引数1(float)
    @param canth2: Canny Edge Detectorの引数2(float)
    @param casize: Canny Edge Detectorに使うSobelのサイズ(0ならCannyは適用しない)(int)
    @param dom: Trueなら線分をマージして出力する(boolean)
    @return boolean,検出ラインピクセル値配列,ライン描画後画像のcvインスタンス
    """
    colorimg = cv2.imread(fileImage, cv2.IMREAD_COLOR)  # 元画像
    if colorimg is None:
        return False, "", ""
    image = cv2.cvtColor(colorimg.copy(), cv2.COLOR_BGR2GRAY)

    # FLDパラメーター設定--------------------------------------------
    length_threshold = lenth
    distance_threshold = disth
    canny_th1 = canth1
    canny_th2 = canth2
    canny_aperture_size = casize
    do_merge = dom
    # -------------------------------------------------------------
    # 高速ライン検出器生成
    fld = cv2.ximgproc.createFastLineDetector(
        length_threshold,
        distance_threshold,
        canny_th1,
        canny_th2,
        canny_aperture_size,
        do_merge,
    )
    # fld = cv2.createLineSegmentDetector(cv2.LSD_REFINE_STD) # LSD

    # ライン取得
    lines = fld.detect(image)
    # lines, width, prec, nfa = fld.detect(image) # LSD
    # # ライン描画後画像のインスタンス作成
    out = fld.drawSegments(colorimg, lines)
    # # ウィンドウサイズ変更可能設定
    # cv2.namedWindow("Fast Line Detector(LINE)", cv2.WINDOW_NORMAL)
    # # ウィンドウ表示
    # cv2.imshow("Fast Line Detector(LINE)", out)
    # cv2.waitKey()
    # # 線形描画後画像の保存
    # cv2.imwrite(
    #     r"D:\PythonScript\RPAScript\RPAPhoto\PDFeTaxReadForList\\FLDTESTOUT.png", out
    # )
    return True, lines, out


def trimImageSave(URL, img, lPix, tPix, rPix, bPix, imgurl):
    """
    概要: 画像をトリミングして上書き
    @param URL: 画像フォルダ(str)
    @param img: cv2で開いた画像(obj)
    @param Lefthigh: 左上角のy,x値(list)
    @param Righthigh: 右上角のy,x値(list)
    @param Leftunder: 左下角のy,x値(list)
    @param Rightunder: 右下角のy,x値(list)
    @param imgurl: 保存ファイルURL(str)
    @return 保存ファイルURL(str)
    """
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
