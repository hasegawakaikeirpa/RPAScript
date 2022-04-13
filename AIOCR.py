# モジュールインポート
# osインポート
import os

from google.cloud import vision
from google.oauth2 import service_account
import io

# ﻿from PIL import Image
import os
import sys
import pyocr
import pyocr.builders
import pdf2image


def ChangePDF(purl, TESTURL, fmtt):
    Mydir = os.getcwd()
    pppath = Mydir + r"\poppler-22.01.0\Library\bin"

    # pdfから画像オブジェクトに
    images = pdf2image.convert_from_path(
        purl, dpi=200, output_folder=TESTURL, fmt=fmtt, poppler_path=pppath
    )


def APIRead(
    FolURL, tar, ele
):  # Arg1 = 画像ファイルのdir,Arg2 = 読取画像,Arg3 = 比較画像 Arg2 - Arg3 のテキストを返す
    # GoogleAPI身元証明書のjson読み込み--------------------------------------------------------------------
    credentials = service_account.Credentials.from_service_account_file(
        FolURL2 + "/key.json"
    )  # GAPIキーのURL
    client = vision.ImageAnnotatorClient(credentials=credentials)
    # client = vision.ImageAnnotatorClient()PCにPath通してるならこっちでも認証可能
    # 画像を読込んでテキストを返す
    path = FolURL + "\\" + tar
    with io.open(path, "rb") as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    # OT = '\n"{}"'.format(texts.description)
    x = 0
    for text in texts:
        # OT = '\n"{}"'.format(text.description)
        if x == 0:
            OT = '\n"{}"'.format(text.description)
        x = x + 1
        # vertices = (['({},{})'.format(vertex.x, vertex.y)
        #             for vertex in text.bounding_poly.vertices])
        # print('bounds: {}'.format(','.join(vertices)))

    path = FolURL + "\\" + ele
    with io.open(path, "rb") as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    x = 0
    for text in texts:
        if x == 0:
            ET = '\n"{}"'.format(text.description)
        x = x + 1
    #     print('\n"{}"'.format(text.description))
    # vertices = (['({},{})'.format(vertex.x, vertex.y)
    #             for vertex in text.bounding_poly.vertices])
    # print('bounds: {}'.format(','.join(vertices)))

    if response.error.message:
        raise Exception(
            "{}\nFor more info on error messages, check: "
            "https://cloud.google.com/apis/design/errors".format(response.error.message)
        )
    OT = OT.split("\n")
    ET = ET.split("\n")
    print(OT)
    print(ET)
    Final = []
    for OTItem in OT:
        OTT = (
            OTItem.replace(" ", "")
            .replace("\u3000", "")
            .replace("'", "")
            .replace('"', "")
        )
        for ETItem in ET:
            ETT = (
                ETItem.replace(" ", "")
                .replace("\u3000", "")
                .replace("'", "")
                .replace('"', "")
            )
            OTT = OTT.replace(ETT, "")
        Final.append(OTT)
    print(Final)
    return OT, ET, Final


# RPA用画像フォルダの作成---------------------------------------------------------
FolURL = r"C:\Users\soumu\Desktop\RPAScript\RPAPhoto\PDFeTaxReadForList"  # 元
# FolURL = FolURL.replace('\\','/')#先
FolURL2 = os.getcwd().replace("\\", "/")  # 先
# --------------------------------------------------------------------------------
tar = "TEST.png"
ele = "TEST2.png"
PDFDir = r"\\Sv05121a\e\電子ファイル\メッセージボックス\TESTe-Tax\eTAX\12_有限会社 広島シティサービス\12_有限会社 広島シティサービス_給与所得・退職所得等の所得税徴収高計算書(一般)_20220228 114427.pdf"
ChangePDF(PDFDir, FolURL, "png")
APIRead(FolURL, tar, ele)
