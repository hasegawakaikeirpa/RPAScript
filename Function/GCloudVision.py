import argparse
from enum import Enum
import io
import os
from google.cloud import vision
from google.oauth2 import service_account
from PIL import Image, ImageDraw, ImageOps
import pandas as pd
import numpy as np
from collections import OrderedDict
from dateutil.parser import parse
import cv2
import matplotlib.pyplot as plt

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


def get_document_bounds_BANK(image_file, feature, Flag):
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

        Flag = "通帳"

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


def Dfchange(YDicList, KeyX, KeyY, XYList, YList, strList, near, LabelX, Label, Flag):
    try:
        strs = ""  # テキスト代入変数
        YD = len(YList)
        # Y軸リストを閾値(near)で統一し置換(行を揃える)----------------------------------
        for YDN in range(YD):
            if not YDN == YD - 1:
                key = YList[YDN]
                for YDNN in range(YD):
                    key2 = YList[YDNN]
                    Sa = key - key2
                    if Sa < 0:
                        if Sa >= (near * -1):
                            YList[YDNN] = key
                    else:
                        if Sa <= near:
                            YList[YDNN] = key
        # ---------------------------------------------------------------------------
        Ys = 0
        # 行を揃えたY軸リストを元にXYListを作成-----------------------------------------
        for YListItem in YList:
            XYList[Ys][3] = YListItem
            Ys += 1
        # ---------------------------------------------------------------------------
        dfXYList = pd.DataFrame(XYList)  # XYListをデータフレーム化
        dfXYList.columns = ["No", "テキスト", "X軸", "Y軸"]  # XYListデータフレームのヘッダー設定
        # XYListデータフレームの並び替え(行の順番)--------------------------------------
        npXYList = ChangeList(dfXYList, "Y軸")  # pram1:リスト,pram2:str"Y軸"
        # ---------------------------------------------------------------------------
        if npXYList[0] is True:
            dfnp = list(npXYList[1])  # 並び替えたDFをList化(高速化の為)
            # CSVDF = pd.DataFrame(dfnp)
            # CSVDF.to_csv(
            #     r"D:\PythonScript\RPAScript\RPAPhoto\PDFeTaxReadForList\XYList.csv",
            #     encoding="cp932",
            # )
        dfRow = len(dfnp)
        # 並び替えたListにループ処理---------------------------------------------------
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


# def DfTuuchou(
#     YDicList, KeyX, KeyY, XYList, YList, strList, near, LabelX, Label, Flag, Banktoml
# ):
#     try:
#         strs = ""  # テキスト代入変数
#         FstrList = []
#         YD = len(YList)
#         NpYlist = []
#         # Y軸リストを閾値(near)で統一し置換(行を揃える)----------------------------------
#         for YDN in range(YD):
#             if not YDN == YD - 1:
#                 key = YList[YDN]
#                 if key not in NpYlist:
#                     for YDNN in range(YD):
#                         key2 = YList[YDNN]
#                         Sa = key - key2
#                         if Sa < 0:
#                             if Sa >= (near * -1):
#                                 YList[YDNN] = key
#                                 if key not in NpYlist:
#                                     NpYlist.append(key)
#                         else:
#                             if Sa <= near:
#                                 YList[YDNN] = key
#                                 if key not in NpYlist:
#                                     NpYlist.append(key)

#         # # DataFrame作成
#         # df = pd.DataFrame(YList)
#         # with open(
#         #     r"D:\PythonScript\RPAScript\RPAPhoto\PDFeTaxReadForList\YList.csv",
#         #     mode="w",
#         #     encoding="shiftjis",
#         #     errors="ignore",
#         #     newline="",
#         # ) as f:
#         #     # pandasでファイルオブジェクトに書き込む
#         #     df.to_csv(f, index=False)
#         # ---------------------------------------------------------------------------
#         Ys = 0
#         # 行を揃えたY軸リストを元にXYListを作成-----------------------------------------
#         for YListItem in YList:
#             XYList[Ys][3] = YListItem
#             Ys += 1
#         # ---------------------------------------------------------------------------
#         dfXYList = pd.DataFrame(XYList)  # XYListをデータフレーム化
#         dfXYList.columns = ["No", "テキスト", "X軸", "Y軸"]  # XYListデータフレームのヘッダー設定
#         # XYListデータフレームの並び替え(行の順番)--------------------------------------
#         npXYList = ChangeList(dfXYList, "Y軸")  # pram1:リスト,pram2:str"Y軸"
#         # ---------------------------------------------------------------------------
#         if npXYList[0] is True:
#             dfnp = list(npXYList[1])  # 並び替えたDFをList化(高速化の為)
#             # DataFrame作成
#             df = pd.DataFrame(dfnp)
#             with open(
#                 r"D:\PythonScript\RPAScript\RPAPhoto\PDFeTaxReadForList\XYList3.csv",
#                 mode="w",
#                 encoding="shiftjis",
#                 errors="ignore",
#                 newline="",
#             ) as f:
#                 # pandasでファイルオブジェクトに書き込む
#                 df.to_csv(f, index=False)

#         dfRow = len(dfnp)
#         InputCount = 0  # テキスト代入変数に代入した回数
#         InputSlide = 1  # 現在の編集列番号
#         YeqXlistTrrigeer = False
#         FontSize = 0
#         # 並び替えたListにループ処理---------------------------------------------------
#         for lb in range(dfRow):
#             if lb == 257:
#                 print("")
#             btxt = dfnp[lb][1]  # 現在の文字
#             bjsonX = dfnp[lb][3]  # 現在の文字の縦軸
#             bjsonY = dfnp[lb][2]  # 現在の文字の横軸
#             # テキスト代入変数に代入した回数がtomlの値以外なら---------------------------
#             if not InputCount == Banktoml[str(InputSlide) + "Col"]:
#                 if YeqXlistTrrigeer is False:
#                     # 横軸値のリスト作成-------------------------------------------------
#                     YeqXlist = []  # 行範囲リスト
#                     bjsonYMinXRange = []  # 行範囲代入リスト
#                     Gyou = bjsonX  # 現在の行の縦軸
#                     Yav = []
#                     for Yeq in range(len(dfnp)):  # 同行の横軸リスト作成
#                         if dfnp[Yeq][3] == bjsonX:
#                             YeqXlist.append(dfnp[Yeq][2])
#                             if not Yeq == len(dfnp) - 1:
#                                 # ----------------------------
#                                 thisT = dfnp[Yeq][1]
#                                 NextT = dfnp[Yeq + 1][1]
#                                 if (
#                                     thisT.isdecimal() is True
#                                     and NextT.isdecimal() is True
#                                 ):
#                                     this = dfnp[Yeq][2]
#                                     Next = dfnp[Yeq + 1][2]
#                                     sa = Next - this
#                                     if len(Yav) == 0:
#                                         if not sa <= 0:
#                                             Yav.append(sa)
#                                     else:
#                                         hei = sum(Yav) / len(Yav)
#                                         if not sa <= 0:
#                                             if not hei - sa >= (hei / 2):
#                                                 Yav.append(sa)
#                                 # ----------------------------
#                     if FontSize == 0:
#                         if len(Yav) == 0:
#                             FontSize = 30
#                         else:
#                             # FontSize = sum(Yav) / len(Yav)
#                             FontSize = 30
#                     for bj in range(Banktoml["ColCount"]):

#                         if bj == 0:
#                             PlusStr = FontSize * Banktoml[str(bj + 1) + "Col"]
#                             # Fval = min(YeqXlist)  # 行範囲始点
#                             Fval = Banktoml["StartPos"]  # 行範囲始点
#                             Lval = PlusStr + Fval  # 行範囲終点
#                             # Lnear = getNearestValuePar(YeqXlist, (Lval - FontSize))
#                             bjsonYMinXRange.append([round(Fval), round(Lval)])
#                         else:
#                             PlusStr = FontSize * Banktoml[str(bj + 1) + "Col"]
#                             Fval = FontSize + bjsonYMinXRange[bj - 1][1]  # 行範囲始点
#                             Lval = PlusStr + Fval  # 行範囲終点
#                             bjsonYMinXRange.append([round(Fval), round(Lval)])
#                             # Fnear = getNearestValuePar(YeqXlist, Fval)
#                             # Fx = 0
#                             # if Fnear <= bjsonYMinXRange[bj - 1][1]:
#                             #     while Fnear <= bjsonYMinXRange[bj - 1][1]:
#                             #         Fx += 1
#                             #         Fnear = getNearestValuePar(
#                             #             YeqXlist, Fval + (FontSize * Fx)
#                             #         )
#                             #         if Fx >= 100:
#                             #             break
#                             # Lval = PlusStr + bjsonYMinXRange[bj - 1][1]  # 行範囲終点
#                             # # Lnear = getNearestValuePar(YeqXlist, (Lval - FontSize))
#                             # bjsonYMinXRange.append([round(Fnear), round(Lval)])
#                     YeqXlistTrrigeer = True
#                     # -----------------------------------------------------------------
#                 if len(YeqXlist) >= 8:
#                     # リスト先頭軸とリスト最終軸の計算
#                     try:
#                         bjDiff = (
#                             bjsonYMinXRange[InputSlide - 1][1]
#                             - bjsonYMinXRange[InputSlide - 1][0]
#                         )
#                     except:
#                         bjDiff = 0
#                     if bjDiff > 0:
#                         # 現在の文字位置が行範囲内ならテキスト代入変数に代入
#                         if (
#                             bjsonY >= bjsonYMinXRange[InputSlide - 1][0]
#                             and bjsonY <= bjsonYMinXRange[InputSlide - 1][1]
#                         ):
#                             if Gyou == bjsonX:  # 現在の文字縦軸が現在の行の縦軸と一致する場合
#                                 if InputSlide == Banktoml["HidukeColNo"]:
#                                     # 文字列内に不要な文字があれば置換---------------------
#                                     for p in reversed(range(len(strs))):
#                                         if (
#                                             strs[p].isdecimal() is False
#                                             and not strs[p] == "."
#                                         ):  # 文字が数字と,.で無かった場合
#                                             print(strs[p])
#                                             strs = strs.replace(strs[p], "")
#                                             if not InputCount == 0:
#                                                 InputCount -= 1
#                                     # -------------------------------------------------
#                                     if (
#                                         btxt.isdecimal() is True
#                                         or btxt == ","
#                                         or btxt == "."
#                                     ):  # 文字が数字と,.だった場合
#                                         strs = strs + btxt
#                                         InputCount += 1
#                                 else:  # 現在のスライドが日付設定列番と一致しない場合
#                                     strs = strs + btxt
#                                     InputCount += 1
#                                 # 文字列代入変数に指定回数分代入していた場合
#                                 if InputCount == Banktoml[str(InputSlide) + "Col"]:
#                                     # 現在のスライドが通貨設定列番と一致する場合
#                                     if InputSlide in Banktoml["MoneyCol"]:
#                                         strList.append(
#                                             strs.replace(".", "")
#                                             .replace(",", "")
#                                             .replace("*", "")
#                                             .replace("'", "")
#                                             .replace("-", "")
#                                             .replace("✓", "")
#                                         )
#                                     else:  # 現在のスライドが通貨設定列番と一致する場合
#                                         strList.append(strs)
#                                     InputSlide += 1
#                                     InputCount = 0
#                                     strs = ""
#                                     # 現在のスライドが最大行設定と一致する場合
#                                     if InputSlide - 1 == Banktoml["ColCount"]:
#                                         FstrList.append(strList)
#                                         YeqXlistTrrigeer = False
#                                         InputSlide = 1
#                                         strList = []
#                                 elif lb == dfRow - 1:
#                                     strList.append(strs)
#                                     FstrList.append(strList)
#                                     YeqXlistTrrigeer = False
#                                     InputSlide = 1
#                                     InputCount = 0
#                                     strs = ""
#                                     strList = []
#                             else:  # 現在の文字縦軸が現在の行の縦軸と一致しない場合
#                                 strList.append(strs)
#                                 InputSlide += 1
#                                 InputCount = 0
#                                 strs = ""
#                                 # 現在のスライドが最大行設定と一致する場合
#                                 if InputSlide - 1 == Banktoml["ColCount"]:
#                                     FstrList.append(strList)
#                                     YeqXlistTrrigeer = False
#                                     InputSlide = 1
#                                     strList = []
#                                 elif lb == dfRow - 1:
#                                     FstrList.append(strList)
#                                     YeqXlistTrrigeer = False
#                                     InputSlide = 1
#                                     strList = []
#                         else:  # 現在の文字位置が行範囲外の場合
#                             if (
#                                 InputSlide == Banktoml["HidukeColNo"]
#                             ):  # 現在のスライドが日付設定列番と一致する場合
#                                 # 文字列内に不要な文字があれば置換---------------------
#                                 for p in reversed(range(len(strs))):
#                                     if (
#                                         strs[p].isdecimal() is False
#                                         and not strs[p] == "."
#                                     ):
#                                         strs = strs.replace(strs[p], "")
#                                         if not InputCount == 0:
#                                             InputCount -= 1
#                                 # -------------------------------------------------
#                                 wn = 0  # 指定範囲外取得の為の加算変数
#                                 if not len(strs) == Banktoml["HidukeCount"]:
#                                     while not (
#                                         len(strs) == Banktoml["HidukeCount"]
#                                     ):  # 文字列が指定文字数になるまでループ
#                                         btxt = btxt = dfnp[lb + wn][1]
#                                         if (
#                                             btxt.isdecimal() is True
#                                             or btxt == ","
#                                             or btxt == "."
#                                         ):  # 文字が数字と,.で無かった場合
#                                             strs = strs + btxt
#                                             InputCount += 1
#                                         wn += 1
#                                 else:
#                                     strList.append(strs)
#                                     InputSlide += 1
#                                     InputCount = 0
#                                     strs = ""
#                                     strs = strs + btxt
#                                     InputCount += 1
#                             else:  # 現在のスライドが日付設定列番と一致しない場合
#                                 # 現在のスライドが通貨設定列番と一致する場合
#                                 if InputSlide in Banktoml["MoneyCol"]:
#                                     strList.append(
#                                         strs.replace(".", "")
#                                         .replace(",", "")
#                                         .replace("*", "")
#                                         .replace("'", "")
#                                         .replace("-", "")
#                                         .replace("✓", "")
#                                     )
#                                     InputSlide += 1
#                                     InputCount = 0
#                                     strs = ""
#                                     strs = strs + btxt
#                                     InputCount += 1
#                                 else:  # 現在のスライドが通貨設定列番と一致しない場合
#                                     if not InputSlide - 1 == Banktoml["ColCount"]:
#                                         if InputSlide == len(
#                                             bjsonYMinXRange
#                                         ):  # 行範囲内リスト最終行なら
#                                             # 現在の文字位置が次の行範囲内ならテキスト代入変数に代入
#                                             if (
#                                                 bjsonY
#                                                 >= bjsonYMinXRange[InputSlide - 1][0]
#                                                 and bjsonY
#                                                 <= bjsonYMinXRange[InputSlide - 1][1]
#                                             ):
#                                                 strList.append(strs)
#                                                 InputSlide += 1
#                                                 InputCount = 0
#                                                 strs = ""
#                                                 strs = strs + btxt
#                                                 InputCount += 1
#                                             else:
#                                                 strList.append(strs)
#                                                 InputSlide += 1
#                                                 InputCount = 0
#                                                 strs = ""
#                                                 strs = strs + btxt
#                                                 InputCount += 1
#                                         else:
#                                             # 現在の文字位置が次の行範囲内ならテキスト代入変数に代入
#                                             if (
#                                                 bjsonY >= bjsonYMinXRange[InputSlide][0]
#                                                 and bjsonY
#                                                 <= bjsonYMinXRange[InputSlide][1]
#                                             ):
#                                                 strList.append(strs)
#                                                 InputSlide += 1
#                                                 InputCount = 0
#                                                 strs = ""
#                                                 strs = strs + btxt
#                                                 InputCount += 1
#                                             else:
#                                                 InputCount = 0
#                                     else:
#                                         InputCount = 0
#                                 # 現在のスライドが最大行設定と一致する場合
#                                 if InputSlide - 1 == Banktoml["ColCount"]:
#                                     FstrList.append(strList)
#                                     YeqXlistTrrigeer = False
#                                     InputSlide = 1
#                                     strList = []
#                                 elif lb == dfRow - 1:
#                                     FstrList.append(strList)
#                                     YeqXlistTrrigeer = False
#                                     InputSlide = 1
#                                     strList = []
#                     else:
#                         print("NobjDiff")
#                         strList.append("")
#                         InputSlide += 1
#                         InputCount = 0
#                         strs = strs + btxt
#                         InputCount += 1
#                 else:  # 抽出行情報が8個未満の場合
#                     print("抽出行情報が8個未満")
#                     InputCount = 0
#                     strs = ""
#                     strs = strs + btxt
#                     YeqXlistTrrigeer = False
#                     InputSlide = 1
#                     strList = []
#             # ------------------------------------------------------------------
#             else:
#                 if InputSlide == Banktoml["HidukeColNo"]:
#                     # 文字列内に不要な文字があれば置換---------------------
#                     for p in reversed(range(len(strs))):
#                         if (
#                             strs[p].isdecimal() is False and not strs[p] == "."
#                         ):  # 文字が数字と,.で無かった場合
#                             print(strs[p])
#                             strs = strs.replace(strs[p], "")
#                             if not InputCount == 0:
#                                 InputCount -= 1
#                     # -------------------------------------------------
#                     if (
#                         btxt.isdecimal() is True or btxt == "," or btxt == "."
#                     ):  # 文字が数字と,.だった場合
#                         strs = strs + btxt
#                         InputCount += 1
#                 else:  # 現在のスライドが日付設定列番と一致しない場合
#                     strs = strs + btxt
#                     InputCount += 1
#                 # 文字列代入変数に指定回数分代入していた場合
#                 if InputCount == Banktoml[str(InputSlide) + "Col"]:
#                     # 現在のスライドが通貨設定列番と一致する場合
#                     if InputSlide in Banktoml["MoneyCol"]:
#                         strList.append(
#                             strs.replace(".", "")
#                             .replace(",", "")
#                             .replace("*", "")
#                             .replace("'", "")
#                             .replace("-", "")
#                             .replace("✓", "")
#                         )
#                     else:  # 現在のスライドが通貨設定列番と一致する場合
#                         strList.append(strs)
#                     InputSlide += 1
#                     InputCount = 0
#                     strs = ""
#                     # 現在のスライドが最大行設定と一致する場合
#                     if InputSlide - 1 == Banktoml["ColCount"]:
#                         FstrList.append(strList)
#                         YeqXlistTrrigeer = False
#                         InputSlide = 1
#                         strList = []
#                 elif lb == dfRow - 1:
#                     strList.append(strs)
#                     FstrList.append(strList)
#                     YeqXlistTrrigeer = False
#                     InputSlide = 1
#                     InputCount = 0
#                     strs = ""
#                     strList = []
#         return True, FstrList
#     except:
#         return False, ""


def DfTuuchou(
    YDicList, KeyX, KeyY, XYList, YList, strList, near, LabelX, Label, Flag, Banktoml
):
    try:
        strs = ""  # テキスト代入変数
        FstrList = []
        YD = len(YList)
        NpYlist = []
        # Y軸リストを閾値(near)で統一し置換(行を揃える)----------------------------------
        for YDN in range(YD):
            if not YDN == YD - 1:
                key = YList[YDN]
                if key not in NpYlist:
                    for YDNN in range(YD):
                        key2 = YList[YDNN]
                        Sa = key - key2
                        if Sa < 0:
                            if Sa >= (near * -1):
                                YList[YDNN] = key
                                if key not in NpYlist:
                                    NpYlist.append(key)
                        else:
                            if Sa <= near:
                                YList[YDNN] = key
                                if key not in NpYlist:
                                    NpYlist.append(key)
        # ---------------------------------------------------------------------------
        Ys = 0
        # 行を揃えたY軸リストを元にXYListを作成-----------------------------------------
        for YListItem in YList:
            XYList[Ys][3] = YListItem
            Ys += 1
        # ---------------------------------------------------------------------------
        dfXYList = pd.DataFrame(XYList)  # XYListをデータフレーム化
        dfXYList.columns = ["No", "テキスト", "X軸", "Y軸"]  # XYListデータフレームのヘッダー設定
        # XYListデータフレームの並び替え(行の順番)--------------------------------------
        npXYList = ChangeList(dfXYList, "Y軸")  # pram1:リスト,pram2:str"Y軸"
        # ---------------------------------------------------------------------------
        if npXYList[0] is True:
            dfnp = list(npXYList[1])  # 並び替えたDFをList化(高速化の為)
            # # DataFrame作成
            # df = pd.DataFrame(dfnp)
            # with open(
            #     r"D:\PythonScript\RPAScript\RPAPhoto\PDFeTaxReadForList\XYList3.csv",
            #     mode="w",
            #     encoding="shiftjis",
            #     errors="ignore",
            #     newline="",
            # ) as f:
            #     # pandasでファイルオブジェクトに書き込む
            #     df.to_csv(f, index=False)

        dfRow = len(dfnp)
        InputCount = 0  # テキスト代入変数に代入した回数
        InputSlide = 1  # 現在の編集列番号
        YeqXlistTrrigeer = False
        FontSize = Banktoml["FontSize"]
        # 並び替えたListにループ処理---------------------------------------------------
        for lb in range(dfRow):
            btxt = dfnp[lb][1]  # 現在の文字
            bjsonX = dfnp[lb][3]  # 現在の文字の縦軸
            bjsonY = dfnp[lb][2]  # 現在の文字の横軸
            NeDiff = FontSize * Banktoml[str(InputSlide) + "Col"]
            FS = int(dfnp[lb][2])
            LS = int(dfnp[lb - 1][2])
            NextYDiff = FS - LS  # 前の文字との横軸差
            # テキスト代入変数に代入した回数がtomlの値以外なら---------------------------
            if not InputCount == Banktoml[str(InputSlide) + "Col"]:
                if YeqXlistTrrigeer is False:
                    # 横軸値のリスト作成-------------------------------------------------
                    YeqXlist = []  # 行範囲リスト
                    bjsonYMinXRange = []  # 行範囲代入リスト
                    Gyou = bjsonX  # 現在の行の縦軸
                    Yav = []
                    for Yeq in range(len(dfnp)):  # 同行の横軸リスト作成
                        if dfnp[Yeq][3] == bjsonX:
                            YeqXlist.append(dfnp[Yeq][2])
                            if not Yeq == len(dfnp) - 1:
                                # ----------------------------
                                thisT = dfnp[Yeq][1]
                                NextT = dfnp[Yeq + 1][1]
                                if (
                                    thisT.isdecimal() is True
                                    and NextT.isdecimal() is True
                                ):
                                    this = dfnp[Yeq][2]
                                    Next = dfnp[Yeq + 1][2]
                                    sa = Next - this
                                    if len(Yav) == 0:
                                        if not sa <= 0:
                                            Yav.append(sa)
                                    else:
                                        hei = sum(Yav) / len(Yav)
                                        if not sa <= 0:
                                            if not hei - sa >= (hei / 2):
                                                Yav.append(sa)
                                # ----------------------------
                    for bj in range(Banktoml["ColCount"]):
                        if bj == 0:
                            if (bj + 1) == Banktoml["SmallTXTCol"]:
                                PlusStr = (
                                    FontSize * Banktoml["SmallTXTMag"]
                                ) * Banktoml[str(bj + 1) + "Col"]
                            else:
                                PlusStr = FontSize * Banktoml[str(bj + 1) + "Col"]
                            Fval = min(YeqXlist)  # 行範囲始点
                            # Fval = Banktoml["StartPos"]  # 行範囲始点
                            Lval = PlusStr + Fval  # 行範囲終点
                            bjsonYMinXRange.append([round(Fval), round(Lval)])
                        else:
                            try:
                                KVal = bjsonYMinXRange[bj - 1][1]
                                KValList = []
                                for YeqXlistItem in YeqXlist:
                                    if KVal < YeqXlistItem:
                                        KValList.append(YeqXlistItem)
                                Fval = min(KValList)  # 行範囲始点
                                if (Fval - KVal) > (FontSize * 4):
                                    Fval = FontSize + bjsonYMinXRange[bj - 1][1]
                                if (bj + 1) == Banktoml["SmallTXTCol"]:
                                    PlusStr = (
                                        FontSize * Banktoml["SmallTXTMag"]
                                    ) * Banktoml[str(bj + 1) + "Col"]
                                else:
                                    PlusStr = FontSize * Banktoml[str(bj + 1) + "Col"]
                                # Fval = FontSize + bjsonYMinXRange[bj - 1][1]  # 行範囲始点
                                Lval = PlusStr + Fval  # 行範囲終点
                                bjsonYMinXRange.append([round(Fval), round(Lval)])
                            except:
                                print("文章分けテーブル作成失敗")
                    YeqXlistTrrigeer = True
                    # -----------------------------------------------------------------
                if len(YeqXlist) >= 8:
                    # リスト先頭軸とリスト最終軸の計算
                    try:
                        bjDiff = (
                            bjsonYMinXRange[InputSlide - 1][1]
                            - bjsonYMinXRange[InputSlide - 1][0]
                        )
                    except:
                        bjDiff = 0
                    if bjDiff > 0:
                        # 現在の文字位置が行範囲内ならテキスト代入変数に代入
                        if (
                            bjsonY >= bjsonYMinXRange[InputSlide - 1][0]
                            and bjsonY <= bjsonYMinXRange[InputSlide - 1][1]
                        ):
                            if Gyou == bjsonX:  # 現在の文字縦軸が現在の行の縦軸と一致する場合
                                strs = strs + btxt
                                InputCount += 1
                        else:
                            if NextYDiff > NeDiff:
                                strList.append(strs)
                                strs = ""
                                InputSlide += 1
                                NeDiff = FontSize * Banktoml[str(InputSlide) + "Col"]
                                if NextYDiff > NeDiff:
                                    strList.append("")
                                    InputSlide += 1
                                    InputCount = 0
                                    strs = strs + btxt
                                    InputCount += 1
                                else:
                                    strs = strs + btxt
                                    InputCount += 1
                            else:
                                if InputSlide == Banktoml["HidukeColNo"]:
                                    # 文字列内に不要な文字があれば置換---------------------
                                    for p in reversed(range(len(strs))):
                                        if (
                                            strs[p].isdecimal() is False
                                            and not strs[p] == "."
                                            and not strs[p] == "-"
                                        ):  # 文字が数字と-.で無かった場合
                                            print(strs[p])
                                            strs = strs.replace(strs[p], "")
                                    # -------------------------------------------------
                                    strList.append(strs)
                                elif InputSlide in Banktoml["MoneyCol"]:
                                    strList.append(
                                        strs.replace(".", "")
                                        .replace(",", "")
                                        .replace("*", "")
                                        .replace("'", "")
                                        .replace("-", "")
                                        .replace("✓", "")
                                        .replace("$", "")
                                    )
                                else:  # 現在のスライドが通貨設定列番と一致する場合
                                    strList.append(strs)
                                strs = ""
                                InputSlide += 1
                                # if not dfnp[lb][3] == dfnp[lb - 1][3]:
                                #     InputSlide += 1
                                InputCount = 0
                                strs = strs + btxt
                                InputCount += 1
                            # 現在のスライドが最大行設定と一致する場合
                            if InputSlide - 1 == Banktoml["ColCount"]:
                                FstrList.append(strList)
                                YeqXlistTrrigeer = False
                                InputSlide = 1
                                strList = []
                            elif InputSlide - 2 == Banktoml["ColCount"]:
                                FstrList.append(strList)
                                YeqXlistTrrigeer = False
                                InputSlide = 1
                                strList = []
                else:
                    # 横軸リストのデータ数が不足していれば読まずにリセット
                    YeqXlistTrrigeer = False
            else:
                if InputSlide == Banktoml["HidukeColNo"]:
                    # 文字列内に不要な文字があれば置換---------------------
                    for p in reversed(range(len(strs))):
                        if (
                            strs[p].isdecimal() is False
                            and not strs[p] == "."
                            and not strs[p] == "-"
                        ):  # 文字が数字と-.で無かった場合
                            print(strs[p])
                            strs = strs.replace(strs[p], "")
                    # -------------------------------------------------
                    strList.append(strs)
                elif InputSlide in Banktoml["MoneyCol"]:
                    strList.append(
                        strs.replace(".", "")
                        .replace(",", "")
                        .replace("*", "")
                        .replace("'", "")
                        .replace("-", "")
                        .replace("✓", "")
                        .replace("$", "")
                    )
                else:  # 現在のスライドが通貨設定列番と一致する場合
                    strList.append(strs)
                InputSlide += 1
                InputCount = 0
                strs = ""
                # 現在の文字位置が次の行範囲内ならテキスト代入変数に代入
                if bjsonY >= bjsonYMinXRange[InputSlide][1]:
                    strList.append(strs)
                    InputSlide += 1
                    InputCount = 0
                    strs = ""
                    strs = strs + btxt
                    InputCount += 1
                else:
                    strs = strs + btxt
                    InputCount += 1
                # 現在のスライドが最大行設定と一致する場合
                if InputSlide - 1 == Banktoml["ColCount"]:
                    FstrList.append(strList)
                    YeqXlistTrrigeer = False
                    InputSlide = 1
                    strList = []
                elif lb == dfRow - 1:
                    strList.append(strs)
                    FstrList.append(strList)
                    YeqXlistTrrigeer = False
                    InputSlide = 1
                    InputCount = 0
                    strs = ""
                    strList = []
        return True, FstrList
    except:
        return False, ""


def Bankrentxtver(
    filein,
    KeyX,
    KeyY,
    LabelX,
    etaxKeyX,
    etaxKeyY,
    etaxLabelX,
    Label,
    near,
    Flag,
    Banktoml,
):  # 自作関数一文字づつの軸間を指定値を元に切り分け文章作成
    try:
        bounds = get_document_bounds_BANK(
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

            df = pd.DataFrame(XYList)
            with open(
                r"D:\PythonScript\RPAScript\RPAPhoto\PDFeTaxReadForList\XYList.csv",
                mode="w",
                encoding="shiftjis",
                errors="ignore",
                newline="",
            ) as f:
                # pandasでファイルオブジェクトに書き込む
                df.to_csv(f, index=False)
            if Flag == "通帳":  # OCRで通帳と判定されたら
                DC = DfTuuchou(
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
                    Banktoml,
                )
                if DC[0] is True:
                    logger.debug("rentxtver(OCR結果を整形eTax以外)成功: debug level log")
                    return True, DC[1]
                else:
                    logger.debug("rentxtver(OCR結果を整形eTax以外)失敗: debug level log")
                    return False, "eTaxじゃないDfchangeエラー"
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
