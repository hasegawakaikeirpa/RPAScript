import argparse
from enum import Enum
import io
import os
from google.cloud import vision
from google.oauth2 import service_account
from PIL import Image, ImageDraw
import pandas as pd
import numpy as np
from collections import OrderedDict

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
        """Returns document bounds given an image."""
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
    idx = np.abs(nnlist - num).argmin()
    nearVol = list[idx]
    if nearVol - num > (near * -1) and nearVol - num < (near * 1):
        nlist = np.where(nlist == nearVol, num, nlist)

    nnlist = np.where(nlist == num, 0, nlist)
    idx = np.abs(nnlist - num).argmin()
    nearVol = list[idx]
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


def Dfchange(YDicList, KeyX, KeyY, XYList, YList, strList, near, LabelX, Label, Flag):
    try:
        strs = ""
        for YDicListItem in YDicList:
            YList = getNearestValue(YList, YDicListItem, near)
        print(YList)
        Ys = 0
        for YListItem in YList:
            XYList[Ys][3] = YListItem
            Ys += 1
        dfXYList = pd.DataFrame(XYList)
        dfXYList.columns = ["No", "テキスト", "X軸", "Y軸"]
        npXYList = ChangeList(dfXYList, "Y軸")  # pram1:リスト,pram2:str"Y軸"
        if npXYList[0] is True:
            dfnp = list(npXYList[1])
            # CSVDF = pd.DataFrame(dfnp)
            # CSVDF.to_csv(
            #     r"\\Sv05121a\e\電子ファイル\メッセージボックス\TEST\XYList.csv", encoding="cp932"
            # )
        dfRow = len(dfnp)
        for lb in range(dfRow):
            # if lb == 460:
            #     print(460)
            btxt = dfnp[lb][1]
            bjsonX = dfnp[lb][2]  # 現在の文字の横軸
            bjsonY = dfnp[lb][3]  # 現在の文字の縦軸
            if not lb == dfRow - 1:
                NextbjsonX = dfnp[lb + 1][2]  # 次の文字の横軸
                NextbjsonY = dfnp[lb + 1][3]  # 次の文字の縦軸
                diffparX = NextbjsonX - bjsonX  # 次の文字との横軸間隔
                diffparY = NextbjsonY - bjsonY  # 次の文字との縦軸間隔
                if diffparX > KeyX:  # 次の文字との横軸間隔が指定値以上なら
                    strs = strs + btxt
                    strList.append(strs)
                    strs = ""
                elif diffparY > KeyY:  # 次の文字との縦軸間隔が指定値以上なら
                    strs = strs + btxt
                    if Flag == "eltax" and len(strList) == 0:
                        strList.append("発行元::" + strs)
                    else:
                        strList.append(strs)
                    strs = ""
                else:
                    if diffparX > LabelX:  # 次の文字との横軸間隔がラベル指定値以上なら
                        strs = strs + btxt
                        if Flag == "eltax" and len(strList) == 2:
                            strList.append("発行元部署::" + strs)
                            strs = ""
                        elif Flag == "eltax" and "発行日時::" in strs:
                            strList.append(strs)
                            strs = ""
                        else:
                            strs = strs + Label
                    else:
                        strs = strs + btxt
            else:  # 最終行の処理
                strs = strs + btxt
                strList.append(strs)
                strs = ""
        return True, strList
    except:
        return False, ""


def rentxtver(
    filein, KeyX, KeyY, LabelX, etaxKeyX, etaxKeyY, etaxLabelX, Label, near, Flag
):  # 自作関数一文字づつの軸間を指定値を元に切り分け文章作成
    try:
        bounds = get_document_bounds(
            filein, FeatureType.PARA, Flag
        )  # Vision結果を一文字とverticesに分けリスト格納
        Flag = bounds[2]
        bounds = bounds[1]
        if not len(bounds) == 0:
            lbound = len(bounds)
            strList = []
            XYList = []  # テキストの位置情報格納リスト
            YList = []
            for lb in range(lbound):
                btxt = bounds[lb][0]
                bjson = bounds[lb][1].vertices
                bjsonX = bjson[0].x  # 現在の文字の横軸
                bjsonY = bjson[0].y  # 現在の文字の縦軸
                XYList.append([lb, btxt, bjsonX, bjsonY])
                YList.append(bjsonY)
            YDicList = list(OrderedDict.fromkeys(YList))  # 抽出リストの重複削除
            if Flag == "etax":  # OCRでeTaxと判定されたら
                Xd = len(XYList) - 1  # XYList最終行インデックス
                # XYListで600より上の情報を削除---------------------------------
                for XYListItem in reversed(XYList):  # XYListで600より上の情報を削除
                    if XYListItem[3] <= 600 or XYListItem[3] >= 5500:
                        XYList.pop(Xd)
                    Xd -= 1
                # -------------------------------------------------------------
                YList = []  # Y軸のリストを初期化
                Xd = len(XYList)  # XYList要素数分
                # 600より上の情報を削除したXYListからY軸のリストを作成-------------
                for lb in range(Xd):
                    bjsonY = XYList[lb][3]  # 現在の文字の縦軸
                    YList.append(bjsonY)
                # -------------------------------------------------------------
                DC = Dfchange(
                    YDicList,
                    etaxKeyX,
                    etaxKeyY,
                    XYList,
                    YList,
                    strList,
                    near,
                    etaxLabelX,
                    Label,
                    Flag,
                )
                if DC[0] is True:
                    logger.debug("rentxtver(OCR結果を整形eTax)成功: debug level log")
                    return True, DC[1]
                else:
                    logger.debug("rentxtver(OCR結果を整形eTax)失敗: debug level log")
                    return False, "eTaxDfchangeエラー"
            elif Flag == "eltax":  # OCRでelTaxと判定されたら
                Xd = len(XYList) - 1  # XYList最終行インデックス
                # XYListで600より上の情報を削除---------------------------------
                for XYListItem in reversed(XYList):  # XYListで600より上の情報を削除
                    if XYListItem[3] <= 600 or XYListItem[3] >= 5500:
                        XYList.pop(Xd)
                    Xd -= 1
                # -------------------------------------------------------------
                YList = []  # Y軸のリストを初期化
                Xd = len(XYList)  # XYList要素数分
                # 600より上の情報を削除したXYListからY軸のリストを作成-------------
                for lb in range(Xd):
                    bjsonY = XYList[lb][3]  # 現在の文字の縦軸
                    YList.append(bjsonY)
                # -------------------------------------------------------------
                DC = Dfchange(
                    YDicList,
                    etaxKeyX,
                    etaxKeyY,
                    XYList,
                    YList,
                    strList,
                    near,
                    etaxLabelX,
                    Label,
                    Flag,
                )
                if DC[0] is True:
                    logger.debug("rentxtver(OCR結果を整形eTax)成功: debug level log")
                    return True, DC[1]
                else:
                    logger.debug("rentxtver(OCR結果を整形eTax)失敗: debug level log")
                    return False, "eTaxDfchangeエラー"

            else:  # OCRでeTax以外なら
                DC = Dfchange(
                    YDicList,
                    KeyX,
                    KeyY,
                    XYList,
                    YList,
                    strList,
                    near,
                    LabelX,
                    Label,
                    Flag,
                )
                if DC[0] is True:
                    logger.debug("rentxtver(OCR結果を整形eTax以外)成功: debug level log")
                    return True, DC[1]
                else:
                    logger.debug("rentxtver(OCR結果を整形eTax以外)失敗: debug level log")
                    return False, "eTaxじゃないDfchangeエラー"
        else:  # Vision取得が空なら
            logger.debug("rentxtver(OCR結果を整形)失敗Vision取得が空: debug level log")
            return False, "Vision取得が空"
    except Exception as e:
        logger.debug("rentxtver(OCR結果を整形)失敗Exception: debug level log")
        return False, e


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("detect_file", help="The image for text detection.")
    parser.add_argument("-out_file", help="Optional output file", default=0)
    args = parser.parse_args()

    render_doc_text(args.detect_file, args.out_file)
