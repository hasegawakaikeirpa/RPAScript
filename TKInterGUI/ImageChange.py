from PIL import Image, ImageOps, ImageDraw
import numpy as np
import cv2
import matplotlib.pyplot as plt

# from numba import jit
import math
import pyocr
import os
from pathlib import Path
from pdf2image import convert_from_path

# loggerインポート
from logging import getLogger

logger = getLogger()


def pdf_image(pdf_file, fmtt, dpi):
    """
    概要: popplerでPDFを指定した画像形式に変換
    @param pdf_file : PDFURL(str)
    @param img_path : 画像フォルダURL(str)
    @param fmtt : 変換後の画像形式(str)
    @param dpi : 変換する際の解像度(int)
    @param PDFPage : 変換するPDFのページ番号(str)
    @return : bool
    @return : 変換後画像URLのリスト(list)
    """
    try:
        Mydir = os.getcwd()
        pppath = Mydir + r"\poppler-22.01.0\Library\bin"
        # pdf_file、img_pathをPathにする
        pdf_path = Path(pdf_file)
        image_dir = os.path.dirname(pdf_file)
        FileKey = os.path.basename(pdf_file)
        FileKey = FileKey.replace(".pdf", "").replace(".PDF", "")
        # 線形検出パラメータ設定########################################
        disth = 1.41421356
        canth1 = 50.0
        canth2 = 50.0
        casize = 3
        do = True
        # ############################################################
        # PDFをImage に変換(pdf2imageの関数)
        pages = convert_from_path(pdf_path, dpi, poppler_path=pppath)
        # 画像ファイルを１ページずつ保存
        for i, page in enumerate(pages):
            file_name = FileKey + "_" + str(i + 1) + "page." + fmtt
            image_path = image_dir + r"/" + file_name
            page.save(image_path, fmtt)
            PDFChange(image_dir, image_path, disth, canth1, canth2, casize, do)
        return True
    except:
        return False


def show_image(img, **kwargs):
    """
    Show an RGB numpy array of an image without any interpolation
    """
    plt.subplot()
    plt.axis("off")
    plt.imshow(X=img, interpolation="none", **kwargs)


def ColorInverter(imgurl):
    """
    概要: 画像白黒反転
    @param img: 画像URL(str)
    @return 白黒反転した画像(cv2)
    """
    img = Image.open(imgurl).convert("RGB")
    Inv_img = ImageOps.invert(img)
    return Inv_img


def NoiseRemoval(img):
    """
    概要: 画像ノイズ除去（収縮⇒膨張）
    @param img: cv2で開いた画像
    @return 画像ノイズ除去した画像(cv2)
    """
    kernel = np.ones((2, 2))
    Open_img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    ksize = 7
    # 中央値フィルタ
    Open_img = cv2.medianBlur(Open_img, ksize)
    return Open_img


# FLDテスト処理
# fileImage : 画像ファイルパス
#
def FastLineDetector(fileImage, lenth, disth, canth1, canth2, casize, dom):
    """
    概要: 画像の線形を検出
    @param fileImage: 画像URL(str)
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
    # FLDインスタンス化
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


def StraightLineDetection(URL, imgurl, disth, canth1, canth2, casize, do):
    """
    概要: 画像から直線を検出し、画像の傾きを調べる
    @param URL: 画像フォルダ(str)
    @param imgurl: 画像URL(str)
    @param disth: マージする線分の距離(float)
    @param canth1: Canny Edge Detectorの引数1(float)
    @param canth2: Canny Edge Detectorの引数2(float)
    @param casize: Canny Edge Detectorに使うSobelのサイズ(0ならCannyは適用しない)(int)
    @param dom: Trueなら線分をマージして出力する(boolean)
    @return 傾き値リスト(np配列)
    """
    try:
        img = cv2.imread(imgurl)
        size = img.shape  # 画像のサイズ x,y
        Pix = int(size[0] / 100)  # 検出ピクセル数
        LCheck = False  # ライン検出フラグ
        while LCheck is False:  # ライン検出フラグTrueまでループ
            FLStock = []
            if Pix <= 0:
                Pix = 1
            # FLDインスタンス生成
            FLDs = FastLineDetector(
                imgurl,
                Pix,
                disth,
                canth1,
                canth2,
                casize,
                do,
            )  # boolean,yx値
            if FLDs[0] is True:  # 連続ピクセルを検知したら
                FLDItem = len(FLDs[1])  # 配列要素数
                if FLDItem <= 3:  # 配列要素数0なら
                    print(str(FLDItem) + "要素なので終了")
                    FLStock = FLDs[1]
                    LCheck = True
                else:
                    print(str(FLDItem) + "要素取得")
                    FLStock = FLDs[1]
            PlPix = size[0] / 1000
            if PlPix < 1:
                Pix += 1
            else:
                Pix += int(PlPix)
        XLFlag = False
        for x in range(len(FLStock)):
            UpY = FLStock[x][0][0]
            UpX = FLStock[x][0][1]
            LoY = FLStock[x][0][2]
            LoX = FLStock[x][0][3]
            # if UpX != LoX:
            if XLFlag is False:
                XList = np.array([[UpY, UpX, LoY, LoX]])
                XLFlag = True
            else:
                XList = np.append(XList, [[UpY, UpX, LoY, LoX]], axis=0)
        return True, XList
    except:
        return False, ""


def AutoTrimming(URL, imgurl, disth, canth1, canth2, casize, do):
    """
    概要: 画像からデータ集合部を検出し、自動トリミング
    @param URL: 画像フォルダ(str)
    @param imgurl: 画像URL(str)
    @param disth: マージする線分の距離(float)
    @param canth1: Canny Edge Detectorの引数1(float)
    @param canth2: Canny Edge Detectorの引数2(float)
    @param casize: Canny Edge Detectorに使うSobelのサイズ(0ならCannyは適用しない)(int)
    @param dom: Trueなら線分をマージして出力する(boolean)
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
            disth,
            canth1,
            canth2,
            casize,
            do,
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
        # UnderYmin = np.min(FinalIn[:, 2])  # 検出文字下辺y値の最小値(下辺最左)
        # UnderYmax = np.max(FinalIn[:, 2])  # 検出文字下辺y値の最大値(下辺最右)
        # UnderXmin = np.min(FinalIn[:, 3])  # 検出文字下辺x値の最小値(下辺最上)
        # UnderXmax = np.max(FinalIn[:, 3])  # 検出文字下辺x値の最大値(下辺最下)

        LeftHigh = [TopYmin - size[1] / 100, TopXmin - size[0] / 100]
        # RightHigh = [TopYmax + size[1] / 100, TopXmin - size[0] / 100]
        # LeftLow = [TopYmin - size[1] / 100, TopXmax + size[0] / 100]
        RightLow = [TopYmax + size[1] / 100, TopXmax + size[0] / 100]

        img = Image.open(imgurl)
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


# @jit
def ImageColorChange(URL, img):
    """
    概要: 画像の黒以外を白く
    @param URL: 画像フォルダ(str)
    @param img: cv2で開いた画像
    @return boolean
    """
    size = img.shape
    # ピクセル操作
    for x in range(size[0]):
        for y in range(size[1]):
            r, g, b = img[x, y]
            # 色付きのピクセルかどうか（白もしくは白に近しい色を切り抜くため）
            if (r + g + b) < 600:
                print(img[x, y])
                img[x, y] = 0, 0, 0
            else:
                img[x, y] = 255, 255, 255
    cv2.imwrite(URL + r"\\ChangeColor.png", img)  # ノイズ除去保存(cv2)

    return True


def ImageLotate(URL, imgurl, disth, canth1, canth2, casize, do):
    """
    概要: 画像から直線を検出し、画像の傾きを調べ回転して上書き保存
    @param URL: 画像フォルダ(str)
    @param imgurl: 画像URL(str)
    @param disth: マージする線分の距離(float)
    @param canth1: Canny Edge Detectorの引数1(float)
    @param canth2: Canny Edge Detectorの引数2(float)
    @param casize: Canny Edge Detectorに使うSobelのサイズ(0ならCannyは適用しない)(int)
    @param dom: Trueなら線分をマージして出力する(boolean)
    @return 傾き値リスト(np配列)
    """
    try:
        img = cv2.imread(imgurl)
        # 回転-----------------------------------------------------------------------
        # StraightLineDetectionで最後の一つになるまで絞りだしたピクセル連続線から
        # 角度をmathアークタンジェントで計算し、degreesでラジアン→℃変換後画像を回転
        Kakuavg = StraightLineDetection(URL, imgurl, disth, canth1, canth2, casize, do)
        if Kakuavg[0] is True:
            x1 = Kakuavg[1][:, 1]
            y1 = Kakuavg[1][:, 0]
            x2 = Kakuavg[1][:, 3]
            y2 = Kakuavg[1][:, 2]
            # numpyとmathではy,x軸が反対なので入替--------------------------------------
            x = np.average(y1) - np.average(y2)
            y = np.average(x1) - np.average(x2)
            # ------------------------------------------------------------------------
            tan = math.degrees(math.atan2(y, x))
            img = Image.open(imgurl)
            img = img.rotate(tan, expand=True)
            img.save(imgurl)
        # ---------------------------------------------------------------------------
        else:
            return False
        return True
    except:
        return False


def TesseOCRLotate(URL, fileurl):
    """
    概要: TesseractOCRで画像回転
    @param URL: 画像フォルダ(str)
    @param fileurl: 画像URL(str)
    @return boolean
    """
    try:
        # インストールしたTesseract-OCRのパスを環境変数「PATH」へ追記する。
        # OS自体に設定してあれば以下の2行は不要
        path = "C:\\Program Files\\Tesseract-OCR"
        os.environ["PATH"] = os.environ["PATH"] + path

        # pyocrへ利用するOCRエンジンをTesseractに指定する。
        tools = pyocr.get_available_tools()
        tool = tools[0]

        # OCR対象の画像ファイルを読み込む
        lotateFiles = []
        MaxFile = []
        img = Image.open(fileurl)
        img = img.rotate(
            90,
            expand=True,
        )
        img.save(fileurl.replace(r".png", "") + "90c.png")
        lotateFiles.append(str(fileurl.replace(r".png", "")) + "90c.png")
        MaxFile.append(0)
        img = Image.open(fileurl.replace(r".png", "") + "90c.png")
        img = img.rotate(
            90,
            expand=True,
        )
        img.save(fileurl.replace(r".png", "") + "180c.png")
        lotateFiles.append(str(fileurl.replace(r".png", "")) + "180c.png")
        MaxFile.append(0)
        img = Image.open(fileurl.replace(r".png", "") + "180c.png")
        img = img.rotate(
            90,
            expand=True,
        )
        img.save(fileurl.replace(r".png", "") + "270c.png")
        lotateFiles.append(str(fileurl.replace(r".png", "")) + "270c.png")
        MaxFile.append(0)
        img = Image.open(fileurl.replace(r".png", "") + "270c.png")
        img = img.rotate(
            90,
            expand=True,
        )
        img.save(fileurl.replace(r".png", "") + "360c.png")
        lotateFiles.append(str(fileurl.replace(r".png", "")) + "360c.png")
        MaxFile.append(0)
        # 画像から文字を読み込む
        lf = 0
        for lotateFilesItem in lotateFiles:
            builder = pyocr.builders.TextBuilder(tesseract_layout=6)
            img = Image.open(lotateFilesItem)
            text = tool.image_to_string(img, lang="jpn", builder=builder)
            TC = 0
            for textItem in text:
                if textItem.isdecimal() is True:
                    TC += 1
            MaxFile[lf] = TC
            lf += 1
        MaxIn = MaxFile.index(max(MaxFile))
        print(lotateFiles[MaxIn])
        img = Image.open(lotateFiles[MaxIn])
        img.save(fileurl)
        return True
    except:
        return False


def StraightLineErase(URL, imgurl, disth, canth1, canth2, casize, do):
    """
    概要: 画像から直線を検出し、白で塗り潰す
    @param URL: 画像フォルダ(str)
    @param imgurl: 画像URL(str)
    @param disth: マージする線分の距離(float)
    @param canth1: Canny Edge Detectorの引数1(float)
    @param canth2: Canny Edge Detectorの引数2(float)
    @param casize: Canny Edge Detectorに使うSobelのサイズ(0ならCannyは適用しない)(int)
    @param dom: Trueなら線分をマージして出力する(boolean)
    @return 傾き値リスト(np配列)
    """
    try:
        img = cv2.imread(imgurl)
        size = img.shape  # 画像のサイズ 横,縦
        Pix = int(size[0] / 50)  # 検出ピクセル数
        LineWidth = int((size[0] / 2000))
        LCheck = False  # ライン検出フラグ
        while LCheck is False:  # ライン検出フラグTrueまでループ
            FLStock = []
            if Pix <= 0:
                Pix = 1
            # FLDインスタンス生成
            FLDs = FastLineDetector(
                imgurl,
                Pix,
                disth,
                canth1,
                canth2,
                casize,
                do,
            )  # boolean,yx値
            if FLDs[0] is True:  # 連続ピクセルを検知したら
                FLDItem = len(FLDs[1])  # 配列要素数
                FLStock = FLDs[1]
                LCheck = True
        ######################################################
        img = Image.open(imgurl)
        draw = ImageDraw.Draw(img)
        ######################################################
        for x in range(len(FLStock)):
            # UpY = int(FLStock[x][0][0])  # 縦
            # UpX = int(FLStock[x][0][1])  # 横
            # LoY = int(FLStock[x][0][2])  # 縦
            # LoX = int(FLStock[x][0][3])  # 横

            UpY = FLStock[x][0][0]  # 縦
            UpX = FLStock[x][0][1]  # 横
            LoY = FLStock[x][0][2]  # 縦
            LoX = FLStock[x][0][3]  # 横

            YDif = UpY - LoY
            if YDif < 0:
                YDif = YDif * -1
            XDif = UpX - LoX
            if XDif < 0:
                XDif = XDif * -1
            # 線を消す(白で線を引く)
            if YDif > XDif:
                # no_lines_img = cv2.line(
                #     img, (0, UpX), (size[1], LoX), (255, 255, 255), LineWidth
                # )
                draw.line([(0, UpX), (size[1], LoX)], fill="White", width=LineWidth)
            elif YDif < XDif:
                # no_lines_img = cv2.line(
                #     img, (UpY, 0), (LoY, size[0]), (255, 255, 255), LineWidth
                # )
                draw.line([(UpY, 0), (LoY, size[0])], fill="White", width=LineWidth)
            else:
                # no_lines_img = cv2.line(
                #     img, (UpY, UpX), (LoY, LoX), (255, 255, 255), LineWidth
                # )
                draw.line([(UpY, UpX), (LoY, LoX)], fill="White", width=LineWidth)
        # cv2.imwrite(URL + r"\NoLine.png", no_lines_img)
        # 画像の表示
        img.save(imgurl)
        # img.show()
        return True
    except:
        return False


def toneCurveDownContrast(frame, n=1):
    """
    概要: トーンカーブでコントラストを下げる
    @param frame: cv2.imread(path)(obj)
    @return cv2(obj) 戻り値をcv2.imwrite(cv2(obj),URL)等で保存できる
    """
    look_up_table = np.zeros((256, 1), dtype="uint8")
    for i in range(256):
        if i < 256 / n:
            look_up_table[i][0] = i * n
        else:
            look_up_table[i][0] = 255
    return cv2.LUT(frame, look_up_table)


def toneCurveUpContrast(frame, n=1):
    """
    概要: トーンカーブでコントラストを上げる
    @param frame: cv2.imread(path)(obj)
    @return cv2(obj) 戻り値をcv2.imwrite(cv2(obj),URL)等で保存できる
    """
    look_up_table = np.zeros((256, 1), dtype="uint8")
    for i in range(256):
        if i < 256 - 256 / n:
            look_up_table[i][0] = 0
        else:
            look_up_table[i][0] = i * n - 255 * (n - 1)
    return cv2.LUT(frame, look_up_table)


def FSDArray(imgurl, txt, th, mll, mlg):
    """
    概要: 引数指定の画像から指定方向の直線の軸リストを作成
    @param txt: 直線の方向(縦or横:str)
    @param th: 直線とみなすための閾値(int)
    @param mll: 直線とみなす最小の長さ(int)
    @param mlg: 同一直線とみなす点間隔の長さ(int)
    @return ReturnList(list) 指定方向の直線の軸リスト
    """
    try:
        # 画像の読み込み
        img = cv2.imread(imgurl)
        # グレースケールに変換します。
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # ネガポジ変換で反転
        edges = cv2.Canny(gray, 50, 150, apertureSize=3)
        # ハフ変換で直線検出
        lines = cv2.HoughLinesP(
            edges,
            rho=1,
            theta=np.pi / 360,
            threshold=th,
            minLineLength=mll,
            maxLineGap=mlg,
        )
        ReturnList = []
        #  直線検出して、指定方向の軸リスト作成
        for line in lines:
            x1, y1, x2, y2 = line[0]
            if txt == "縦":
                if x1 == x2:  # 縦の直線のみ
                    if len(ReturnList) == 0:
                        ReturnList.append([x1, y1, x2, y2])
                    else:
                        inFlag = True
                        for ReturnListItem in ReturnList:
                            if (
                                ReturnListItem[0] - x1 > 100
                                or ReturnListItem[0] - x1 < -100
                            ):
                                inFlag = True
                            else:
                                inFlag = False
                                break
                        if inFlag is True:
                            ReturnList.append([x1, y1, x2, y2])
            elif txt == "横":
                if y1 == y2:  # 横の直線のみ
                    if len(ReturnList) == 0:
                        ReturnList.append([x1, y1, x2, y2])
                    else:
                        inFlag = True
                        for ReturnListItem in ReturnList:
                            if (
                                ReturnListItem[1] - y1 > 100
                                or ReturnListItem[1] - y1 < -100
                            ):
                                inFlag = True
                            else:
                                inFlag = False
                                break
                        if inFlag is True:
                            ReturnList.append([x1, y1, x2, y2])
        ReturnList = sorted(ReturnList, key=lambda x: x[0])
        return True, ReturnList
    except:
        return False, ""


def PDFChange(URL, imgurl, disth, canth1, canth2, casize, do):
    """
    概要: OCR読込用に画像を自動編集
    @param URL: 画像フォルダ(str)
    @param imgurl: 画像URL(str)
    @param disth: マージする線分の距離(float)
    @param canth1: Canny Edge Detectorの引数1(float)
    @param canth2: Canny Edge Detectorの引数2(float)
    @param casize: Canny Edge Detectorに使うSobelのサイズ(0ならCannyは適用しない)(int)
    @param dom: Trueなら線分をマージして出力する(boolean)
    @return OCR読込用に画像を自動編集した画像URL(str)
    """
    Inv_img = ColorInverter(imgurl)  # 白黒反転(PIL)
    Inv_img.save(imgurl)  # 白黒反転保存(PIL)
    img = cv2.imread(imgurl)  # 白黒反転画像(cv2)
    CleanUp_img = NoiseRemoval(img)  # ノイズ除去(cv2)
    cv2.imwrite(imgurl, CleanUp_img)  # ノイズ除去保存(cv2)
    Inv_img = ColorInverter(imgurl)  # 白黒反転(PIL)
    Inv_img.save(imgurl)  # 白黒反転保存(PIL)
    # 画像から直線を検出し、画像の傾きを調べ回転して上書き保存
    ILT = ImageLotate(URL, imgurl, disth, canth1, canth2, casize, do)
    if ILT is True:
        img = cv2.imread(imgurl)
        # 画像リサイズ-----------------------------------------------
        IMGsize = [3840, 3840]
        h, w = img.shape[:2]
        ash = IMGsize[1] / h
        asw = IMGsize[0] / w
        if asw < ash:
            sizeas = (int(w * asw), int(h * asw))
        else:
            sizeas = (int(w * ash), int(h * ash))
        img = cv2.resize(img, dsize=sizeas)
        cv2.imwrite(imgurl, img)
        # ----------------------------------------------------------
        TesseOCRLotate(URL, imgurl)  # 無料OCRで回転
        img = cv2.imread(imgurl)
        TC = toneCurveUpContrast(img)  # トーンカーブ処理
        cv2.imwrite(imgurl, TC)
        # 直線を削除------------------------------------------------------
        StraightLineErase(URL, imgurl, disth, canth1, canth2, casize, do)
        # ---------------------------------------------------------------
        # ImageColorChange(URL, img)
        return imgurl
    else:
        return imgurl


def OCRIMGChange(URL, imgurl, disth, canth1, canth2, casize, do):
    """
    概要: OCR読込用に画像を自動編集
    @param URL: 画像フォルダ(str)
    @param imgurl: 画像URL(str)
    @param disth: マージする線分の距離(float)
    @param canth1: Canny Edge Detectorの引数1(float)
    @param canth2: Canny Edge Detectorの引数2(float)
    @param casize: Canny Edge Detectorに使うSobelのサイズ(0ならCannyは適用しない)(int)
    @param dom: Trueなら線分をマージして出力する(boolean)
    @return OCR読込用に画像を自動編集した画像URL(str)
    """
    Inv_img = ColorInverter(imgurl)  # 白黒反転(PIL)
    Inv_img.save(imgurl)  # 白黒反転保存(PIL)
    img = cv2.imread(imgurl)  # 白黒反転画像(cv2)
    CleanUp_img = NoiseRemoval(img)  # ノイズ除去(cv2)
    cv2.imwrite(imgurl, CleanUp_img)  # ノイズ除去保存(cv2)
    Inv_img = ColorInverter(imgurl)  # 白黒反転(PIL)
    Inv_img.save(imgurl)  # 白黒反転保存(PIL)
    # 画像から直線を検出し、画像の傾きを調べ回転して上書き保存
    ILT = ImageLotate(URL, imgurl, disth, canth1, canth2, casize, do)
    if ILT is True:
        # 画像からデータ集合体位置を算出し、トリミング
        AutoTrimming(URL, imgurl, disth, canth1, canth2, casize, do)
        img = cv2.imread(imgurl)
        # 画像リサイズ-----------------------------------------------
        IMGsize = [3840, 3840]
        h, w = img.shape[:2]
        ash = IMGsize[1] / h
        asw = IMGsize[0] / w
        if asw < ash:
            sizeas = (int(w * asw), int(h * asw))
        else:
            sizeas = (int(w * ash), int(h * ash))
        img = cv2.resize(img, dsize=sizeas)
        cv2.imwrite(imgurl, img)
        # ----------------------------------------------------------
        TesseOCRLotate(URL, imgurl)  # 無料OCRで回転
        img = cv2.imread(imgurl)
        TC = toneCurveUpContrast(img)  # トーンカーブ処理
        cv2.imwrite(imgurl, TC)
        # 直線を削除------------------------------------------------------
        StraightLineErase(URL, imgurl, disth, canth1, canth2, casize, do)
        # ---------------------------------------------------------------
        # ImageColorChange(URL, img)
        return imgurl
    else:
        return imgurl


def ShortChange(imgurl):

    # img = Image.open(imgurl)
    # img = img.rotate(90, expand=True)
    # img.save(imgurl)

    img = cv2.imread(imgurl)
    # 画像リサイズ-----------------------------------------------
    IMGsize = [3840, 3840]
    h, w = img.shape[:2]
    ash = IMGsize[1] / h
    asw = IMGsize[0] / w
    if asw < ash:
        sizeas = (int(w * asw), int(h * asw))
    else:
        sizeas = (int(w * ash), int(h * ash))
    img = cv2.resize(img, dsize=sizeas)
    cv2.imwrite(imgurl, img)


if __name__ == "__main__":
    URL = r"D:\Souzoku_JAPng"

    for fd_path, sb_folder, sb_file in os.walk(URL):
        for sb_fileItem in sb_file:
            imgurl = fd_path + "\\" + sb_fileItem
            ShortChange(imgurl)
