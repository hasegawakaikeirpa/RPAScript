﻿# import argparse
from argparse import ArgumentParser
from enum import Enum
import io
import os
from google.cloud import vision
from google.oauth2 import service_account
from PIL import Image, ImageDraw

# import pandas as pd
from pandas import DataFrame
import numpy as np

# from collections import OrderedDict


# loggerインポート
from logging import getLogger

logger = getLogger()


class FeatureType(Enum):
    PAGE = 1
    BLOCK = 2
    PARA = 3
    WORD = 4
    SYMBOL = 5


def draw_boxes(image, bounds, color):
    """Draw a border around the image using the hints in the vector list."""
    draw = ImageDraw.Draw(image)

    for bound in bounds:
        draw.polygon(
            [
                bound.vertices[0].x,
                bound.vertices[0].y,
                bound.vertices[1].x,
                bound.vertices[1].y,
                bound.vertices[2].x,
                bound.vertices[2].y,
                bound.vertices[3].x,
                bound.vertices[3].y,
            ],
            None,
            color,
        )
    return image


def get_document_bounds(image_file, feature, Flag):
    try:
        """GoovleVisionAPIでOCR"""
        logger.debug("get_document_bounds(GoogleVisionAPI)開始: debug level log")
        credentials = service_account.Credentials.from_service_account_file(
            os.getcwd() + "/key.json"
        )  # GAPIキーのURL
        client = vision.ImageAnnotatorClient(credentials=credentials)
        # client = vision.ImageAnnotatorClient()
        verList = []
        bounds = []

        with io.open(image_file, "rb") as image_file:
            content = image_file.read()

        image = vision.Image(content=content)

        response = client.document_text_detection(image=image)
        document = response.full_text_annotation
        if "国税電子申告・納税システム(e-Tax)" in document.text:
            Flag = "etax"
        elif "フリコミ" in document.text or "CD" in document.text:
            Flag = "通帳"
        else:
            if not Flag == "eltax":
                Flag = "MJS"
        # Collect specified feature bounds by enumerating all document features
        for page in document.pages:
            for block in page.blocks:
                for paragraph in block.paragraphs:
                    for word in paragraph.words:
                        for symbol in word.symbols:
                            verList.append([symbol.text, symbol.bounding_box])
                            if feature == FeatureType.SYMBOL:
                                bounds.append(symbol.bounding_box)

                        if feature == FeatureType.WORD:
                            bounds.append(word.bounding_box)

                    if feature == FeatureType.PARA:
                        bounds.append(paragraph.bounding_box)

                if feature == FeatureType.BLOCK:
                    bounds.append(block.bounding_box)

        # The list `bounds` contains the coordinates of the bounding boxes.
        logger.debug("get_document_bounds(GoogleVisionAPI)終了: debug level log")
        return bounds, verList, Flag
    except:
        return "boundsなし", "verListなし", "Flagなし"


def get_document_bounds_BANK(image_file, feature):
    try:
        """GoovleVisionAPIでOCR"""
        logger.debug("get_document_bounds(GoogleVisionAPI)開始: debug level log")
        print("GoogleVisionAPI開始")
        credentials = service_account.Credentials.from_service_account_file(
            os.getcwd() + "/key.json"
        )  # GAPIキーのURL
        client = vision.ImageAnnotatorClient(credentials=credentials)
        # client = vision.ImageAnnotatorClient()
        verList = []
        bounds = []

        with io.open(image_file, "rb") as image_file:
            content = image_file.read()

        image = vision.Image(content=content)

        response = client.document_text_detection(image=image)
        document = response.full_text_annotation
        print("GoogleVisionAPIclient接続完了")
        # Collect specified feature bounds by enumerating all document features
        for page in document.pages:
            for block in page.blocks:
                for paragraph in block.paragraphs:
                    for word in paragraph.words:
                        for symbol in word.symbols:
                            verList.append([symbol.text, symbol.bounding_box])
                            if feature == FeatureType.SYMBOL:
                                bounds.append(symbol.bounding_box)

                        if feature == FeatureType.WORD:
                            bounds.append(word.bounding_box)

                    if feature == FeatureType.PARA:
                        bounds.append(paragraph.bounding_box)

                if feature == FeatureType.BLOCK:
                    bounds.append(block.bounding_box)

        # The list `bounds` contains the coordinates of the bounding boxes.
        logger.debug("get_document_bounds(GoogleVisionAPI)終了: debug level log")
        return bounds, verList
    except:
        return "boundsなし", "verListなし"


def render_doc_text(filein, fileout):
    logger.debug("render_doc_text(Visionテキスト識別エリアに色塗り)開始: debug level log")
    image = Image.open(filein)
    bounds = get_document_bounds(filein, FeatureType.BLOCK)[0]
    draw_boxes(image, bounds, "blue")
    bounds = get_document_bounds(filein, FeatureType.PARA)[0]
    draw_boxes(image, bounds, "red")
    bounds = get_document_bounds(filein, FeatureType.WORD)[0]
    draw_boxes(image, bounds, "yellow")

    if fileout != 0:
        image.save(fileout)
    else:
        image.show()
    logger.debug("render_doc_text(Visionテキスト識別エリアに色塗り)終了: debug level log")


def getNearestValuePar(list, num):
    """
    概要: リストからある値に最も近い値を返却する関数
    @param list: データ配列
    @param num: 対象値
    @return 対象値に最も近い値
    """

    # リスト要素と対象値の差分を計算し最小値のインデックスを取得
    array = np.asarray(list)
    idx = (np.abs(array - num)).argmin()
    return array[idx]


def getNearestValue(list, num, near):
    """
    概要: リストからある値に最も近い値を返却する関数
    @param list: データ配列
    @param num: 対象値
    @return 対象値に最も近い値
    """

    # リスト要素と対象値の差分を計算し最小値のインデックスを取得
    nlist = np.array(list)
    nnlist = np.where(nlist == num, 0, nlist)
    NmiVol = 0
    while NmiVol < near and NmiVol > (near * -1):
        idx = np.abs(nnlist - num).argmin()
        nearVol = list[idx]
        if nearVol == num:
            break
        else:
            NmiVol = nearVol - near
            if nearVol - num > (near * -1) and nearVol - num < (near * 1):
                nlist = np.where(nlist == nearVol, num, nlist)

            nnlist = np.where(nlist == num, 0, nlist)
            idx = np.abs(nnlist - num).argmin()
            nearVol = list[idx]
            if nearVol - num > (near * -1) and nearVol - num < (near * 1):
                nlist = np.where(nlist == nearVol, num, nlist)
    return nlist


def ChangeList(dflist, Fname):
    """
    概要: リストの並び替え
    @param dflist: データ配列
    @param Fname: 初めに並び替えする列
    @param Sname: 次に並び替えする列
    @return 対象値に最も近い値
    """
    try:
        npdf = np.array(dflist)  # numpy配列に格納
        npT = npdf[:, 0]  # numpy列切出
        npS = npdf[:, 1]  # numpy列切出
        npX = npdf[:, 2]  # numpy列切出
        npY = npdf[:, 3]  # numpy列切出
        # numpy配列で並替
        if Fname == "Y軸":
            lex_ind = np.lexsort((npT, npS, npX, npY))
        else:
            lex_ind = np.lexsort((npT, npS, npY, npX))
        NEWA = [npdf[i] for i in lex_ind]

        return True, NEWA
    except:
        return False, ""


def DfTuuchou(
    XYList,
    YokoList,
    TateList,
):
    """
    概要: OCR結果の文字位置調整
    @param XYList: OCR結果データ
    @param YokoList: 横直線のピクセル値配列
    @param TateList: 縦直線のピクセル値配列
    @return 並び替え後の配列
    """
    try:
        strs = ""  # テキスト代入変数
        strList = []
        FstrList = []
        # ---------------------------------------------------------------------------
        dfXYList = DataFrame(XYList)  # XYListをデータフレーム化
        dfXYList.columns = ["No", "テキスト", "X軸", "Y軸"]  # XYListデータフレームのヘッダー設定
        # XYListデータフレームの並び替え(行の順番)--------------------------------------
        npXYList = ChangeList(dfXYList, "Y軸")  # pram1:リスト,pram2:str"Y軸"
        # ---------------------------------------------------------------------------
        if npXYList[0] is True:
            dfnp = list(npXYList[1])  # 並び替えたDFをList化(高速化の為)
        # ####################################################################################
        dfRow = len(dfnp)
        InputRetu = 0  # 現在の編集列番号
        GyouList = []
        # 縦軸Listループ処理----------------------------------------------------------------
        for TL in range(len(TateList)):
            # if not TL == len(TateList) - 1:

            for lb in range(dfRow):
                btxt = str(dfnp[lb][1])  # 現在の文字
                bjsonX = int(dfnp[lb][3])  # 現在の文字の縦軸
                bjsonY = int(dfnp[lb][2])  # 現在の文字の横軸
                # 行のみを抽出-------------------------------------------------------------
                if not TL == len(TateList) - 1:
                    if (
                        int(TateList[TL][1]) <= bjsonX
                        and int(TateList[TL + 1][1]) > bjsonX
                    ):
                        GyouList.append([btxt, bjsonX, bjsonY])
                else:
                    L_t = int(TateList[TL][1]) + 5
                    if L_t <= bjsonX:
                        GyouList.append([btxt, bjsonX, bjsonY])
                # ------------------------------------------------------------------------
            GyouList = sorted(GyouList, key=lambda x: x[2])  # 行List並び替え
            NowRets = 0
            # 行Listループ処理-------------------------------------------------------------
            for GyouListItem in GyouList:
                # 今の列位置を判定---------------------------------------------------------
                for IRC in range(len(YokoList)):
                    if not IRC == len(YokoList) - 1:  # 行List最終要素じゃなければ
                        if (
                            int(YokoList[IRC][0]) <= GyouListItem[2]
                            and int(YokoList[IRC + 1][0]) > GyouListItem[2]
                        ):
                            NowRets = IRC
                            break
                    else:
                        if int(YokoList[IRC][0]) < GyouListItem[2]:
                            NowRets = IRC
                            break
                # ------------------------------------------------------------------------
                if not InputRetu == len(YokoList) - 1:  # 行List最終要素じゃなければ
                    # 今の行の縦軸が今の行の縦軸以上かつ次の行の縦軸未満なら------------------
                    if (
                        int(YokoList[InputRetu][0]) <= GyouListItem[2]
                        and int(YokoList[InputRetu + 1][0]) > GyouListItem[2]
                    ):
                        strs += GyouListItem[0]
                    elif int(YokoList[InputRetu + 1][0]) <= GyouListItem[2]:
                        if not NowRets == InputRetu:
                            NI = NowRets - InputRetu
                            if NI > 0:
                                while NowRets != InputRetu:
                                    strList.append(strs)
                                    strs = ""
                                    InputRetu += 1
                                    if NowRets == InputRetu:
                                        strs += GyouListItem[0]
                            else:
                                while NowRets != InputRetu:
                                    strList.append("")
                                    NowRets += 1
                                    if NowRets == InputRetu:
                                        strs += GyouListItem[0]
                        else:
                            strList.append(strs)
                            strs = ""
                            strs += GyouListItem[0]
                            InputRetu += 1
                    # ---------------------------------------------------------------------
                else:
                    if int(YokoList[InputRetu][0]) <= GyouListItem[2]:
                        strs += GyouListItem[0]
                    # ---------------------------------------------------------------------
            # -----------------------------------------------------------------------------
            YDiff = (len(YokoList) - 1) - InputRetu
            if YDiff == 0:
                strList.append(strs)
                strs = ""
                FstrList.append(strList)
                strList = []
                GyouList = []
                InputRetu = 0
            else:
                while YDiff != 0:
                    strList.append(strs)
                    strs = ""
                    YDiff -= 1
                strList.append(strs)
                strs = ""
                FstrList.append(strList)
                strList = []
                GyouList = []
                InputRetu = 0
        return True, FstrList
    except:
        return False, ""


def Bankrentxtver(filein, YokoList, TateList):  # 自作関数一文字づつの軸間を指定値を元に切り分け文章作成
    """
    概要: OCR呼出関数
    @param filein: 画像ファイル
    @param YokoList: 横直線のピクセル値配列
    @param TateList: 縦直線のピクセル値配列
    @return bool,並び替え後の配列
    """
    try:
        # cmap = os.getcwd() + r"\TKInterGUI\cmapchange.csv"
        # cmapdata = np.loadtxt(
        #     cmap,  # 読み込みたいファイルのパス
        #     delimiter=",",  # ファイルの区切り文字
        #     skiprows=0,  # 先頭の何行を無視するか（指定した行数までは読み込まない）
        #     usecols=(0, 1, 2, 3),  # 読み込みたい列番号
        # )
        print("get_document_bounds_BANK開始")
        bounds = get_document_bounds_BANK(
            filein, FeatureType.PARA
        )  # Vision結果を一文字とverticesに分けリスト格納

        bounds = bounds[1]
        if not len(bounds) == 0:
            lbound = len(bounds)
            XYList = []  # テキストの位置情報格納リスト
            for lb in range(lbound):
                btxt = bounds[lb][0]
                # cp932不可の文字を変換##############################################################
                # np.where(cmapdata == "ㄉ",
                # ##################################################################################
                bjson = bounds[lb][1].vertices
                bjsonX = bjson[0].x  # 現在の文字の横軸
                bjsonY = bjson[0].y  # 現在の文字の縦軸
                XYList.append([lb, btxt, bjsonX, bjsonY])

            # df = pd.DataFrame(XYList)
            # with open(
            #     r"D:\PythonScript\RPAScript\RPAPhoto\PDFeTaxReadForList\XYList.csv",
            #     mode="w",
            #     encoding="shiftjis",
            #     errors="ignore",
            #     newline="",
            # ) as f:
            #     # pandasでファイルオブジェクトに書き込む
            #     df.to_csv(f, index=False)
            print("DfTuuchou開始")
            DC = DfTuuchou(
                XYList,
                YokoList,
                TateList,
            )
            print("DfTuuchou完了")
            if DC[0] is True:
                logger.debug("rentxtver(OCR結果を整形eTax以外)成功: debug level log")
                print("rentxtver(OCR結果を整形eTax以外)成功")
                return True, DC[1]
            else:
                logger.debug("rentxtver(OCR結果を整形eTax以外)失敗: debug level log")
                print("rentxtver(OCR結果を整形eTax以外)失敗")
                return False, "Dfchangeエラー"
        else:  # Vision取得が空なら
            logger.debug("rentxtver(OCR結果を整形)失敗Vision取得が空: debug level log")
            print("rentxtver(OCR結果を整形)失敗Vision取得が空")
            return False, "Vision取得が空"
    except Exception as e:
        print("rentxtver(OCR結果を整形)失敗Exception")
        logger.debug("rentxtver(OCR結果を整形)失敗Exception: debug level log")
        return False, e


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("detect_file", help="The image for text detection.")
    parser.add_argument("-out_file", help="Optional output file", default=0)
    args = parser.parse_args()

    render_doc_text(args.detect_file, args.out_file)
