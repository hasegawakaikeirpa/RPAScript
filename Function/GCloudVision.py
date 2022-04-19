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


def get_document_bounds(image_file, feature):
    """Returns document bounds given an image."""
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
    return bounds, verList


def render_doc_text(filein, fileout):
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


def getNearestValue(list, num):
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
    if nearVol - num > -10 and nearVol - num < 10:
        nlist = np.where(nlist == nearVol, num, nlist)
    return nlist


def rentxtver(filein, KeyX, KeyY, LabelX, Label):  # 自作関数一文字づつの軸間を指定値を元に切り分け文章作成
    try:
        bounds = get_document_bounds(filein, FeatureType.PARA)[
            1
        ]  # Vision結果を一文字とverticesに分けリスト格納
        lbound = len(bounds)
        strs = ""
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
        for YDicListItem in YDicList:
            YList = getNearestValue(YList, YDicListItem)
        print(YList)
        Ys = 0
        for YListItem in YList:
            XYList[Ys][3] = YListItem
            Ys += 1
        dfXYList = pd.DataFrame(XYList)
        dfXYList.columns = ["No", "テキスト", "X軸", "Y軸"]
        dfXYList.sort_values("Y軸")
        dfXYList.sort_values("X軸")
        print(dfXYList)
        dfXYList.to_csv(
            r"\\Sv05121a\e\電子ファイル\メッセージボックス\TEST\XYList.csv", encoding="cp932"
        )
        dfRow = len(dfXYList)
        for d in range(dfRow):
            dfRowData = dfXYList.iloc[d]
            dtxt = dfRowData["テキスト"]
            dtxt = dfRowData["X軸"]
            dtxt = dfRowData["Y軸"]
        # for lb in range(lbound):
        #     # if lb == 460:
        #     #     print(460)
        #     btxt = bounds[lb][0]
        #     bjson = bounds[lb][1].vertices
        #     bjsonX = bjson[0].x  # 現在の文字の横軸
        #     bjsonY = bjson[0].y  # 現在の文字の縦軸
        #     if not lb == lbound - 1:
        #         Nextbjson = bounds[lb + 1][1].vertices
        #         NextbjsonX = Nextbjson[0].x  # 次の文字の横軸
        #         NextbjsonY = Nextbjson[0].y  # 次の文字の縦軸
        #         diffparX = NextbjsonX - bjsonX  # 次の文字との横軸間隔
        #         diffparY = NextbjsonY - bjsonY  # 次の文字との縦軸間隔
        #         if diffparX > KeyX:  # 次の文字との横軸間隔が指定値以上なら
        #             strs = strs + btxt
        #             strList.append(strs)
        #             strs = ""
        #         elif diffparY > KeyY:  # 次の文字との縦軸間隔が指定値以上なら
        #             strs = strs + btxt
        #             strList.append(strs)
        #             strs = ""
        #         else:
        #             if diffparX > LabelX:  # 次の文字との横軸間隔がラベル指定値以上なら
        #                 strs = strs + btxt
        #                 strs = strs + Label
        #             else:
        #                 strs = strs + btxt
        #     else:  # 最終行の処理
        #         strs = strs + btxt
        #         strList.append(strs)
        #         strs = ""
        return True, strList
    except Exception as e:
        return False, e


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("detect_file", help="The image for text detection.")
    parser.add_argument("-out_file", help="Optional output file", default=0)
    args = parser.parse_args()

    render_doc_text(args.detect_file, args.out_file)
