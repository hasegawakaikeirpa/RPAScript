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


def trimImageSave(URL, img, left, upper, right, lower, imgurl):
    """
    概要: 画像をトリミングして上書き
    @param URL: 画像フォルダ(str)
    @param img: cv2で開いた画像(obj)
    @param left: 左のy値(list)
    @param upper: 上のx値(list)
    @param right: 右のy値(list)
    @param lower: 下のx値(list)
    @param imgurl: 保存ファイルURL(str)
    @return 保存ファイルURL(str)
    """
    try:
        trimImageFile = img.crop((left, upper, right, lower))  # トリミング
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
    AutoTrimming(URL, imgurl)
    img = Image.open(img)
    img = img.resize(size=(1920, 1920), resample=Image.BILINEAR)
    img.save(imgurl)
    return imgurl


def AutoTrimming(URL, imgurl):
    """
    概要: 画像からデータ集合部を検出し、自動トリミング
    @param URL: 画像フォルダ(str)
    @param imgurl: 画像URL(str)
    @return boolean
    """
    try:
        img = cv2.imread(imgurl)
        size = img.shape  # 画像のサイズ x,y
        Pix = int(size[0] / 400)  # 検出ピクセル数
        if Pix <= 0:
            Pix = 1
        # FLDインスタンス生成
        FLDs = FastLineDetector(
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
        trimImageSave(
            URL,
            img,
            int(LeftHigh[0]),
            int(LeftHigh[1]),
            int(RightLow[0]),
            int(RightLow[1]),
            imgurl,
        )
        return True
    except:
        return False
