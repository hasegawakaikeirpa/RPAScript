import os
import numpy as np
import cv2

import camelot

# import camelot.io as camelot
from PIL import Image
from google.cloud import vision
from google.oauth2 import service_account
from reportlab.pdfgen import canvas
from reportlab.lib.colors import Color
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


def get_word_info(response):  # google cloud visionから送られる結果の処理
    document = response.full_text_annotation
    bounds_word = []
    words = []
    for page in document.pages:
        for block in page.blocks:
            for paragraph in block.paragraphs:
                for word in paragraph.words:
                    word_tmp = []
                    for symbol in word.symbols:
                        word_tmp.append(symbol.text)
                    bounds_word.append(word.bounding_box)
                    word_tmp = "".join(word_tmp)
                    words.append(word_tmp)

    left_bottoms = []  # reportlabが左下を基準点として文字をレンダリングするため、左下の座標を保存しておく
    heights = []
    for bound in bounds_word:
        temp_xs = []
        temp_ys = []
        for vertice in bound.vertices:
            temp_xs.append(vertice.x)
            temp_ys.append(vertice.y)
        left_bottoms.append({"x": min(temp_xs), "y": max(temp_ys)})
        heights.append(int(max(temp_ys) - min(temp_ys)))
    result = [
        {"text": text, "box": bounds_word, "vertic": vertic, "height": height}
        for (text, bound, vertic, height) in zip(
            words, bounds_word, left_bottoms, heights
        )
    ]

    return result


# # input_path = r"\\Sv05121a\e\電子ファイル\メッセージボックス\TESTe-Tax\eTAX\12_有限会社 広島シティサービス\12_有限会社 広島シティサービス_給与所得・退職所得等の所得税徴収高計算書(一般)_20220228 114427.pdf"

# input_path = os.getcwd() + r"\RPAPhoto\PDFeTaxReadForList\AIOCR2.png"
# output_path = os.getcwd() + r"\RPAPhoto\PDFeTaxReadForList\AIOCR2.pdf"  # 元
# pdfmetrics.registerFont(TTFont("ipaexg", "ipaexg.ttf"))
# pdfmetrics.registerFont(TTFont("ipaexm", "ipaexm.ttf"))

# # img = cv2.imread(str(input_path))
# img = cv2.imread(input_path)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# img_byte = cv2.imencode(".png", img)[1].tobytes()

# credentials = service_account.Credentials.from_service_account_file(
#     os.getcwd() + "/key.json"
# )  # GAPIキーのURL
# client = vision.ImageAnnotatorClient(credentials=credentials)
# # client = vision.ImageAnnotatorClient()PCにPath通してるならこっちでも認証可能

# img_gcv = vision.Image(content=img_byte)
# response = client.document_text_detection(image=img_gcv)  # ocr実行！
# results = get_word_info(response)  # 結果の処理

# small_fix_y = 0.25  # reportlabのレンダリング時に下にずれるのを補正する

# Y, X = img.shape[0], img.shape[1]
# cc = canvas.Canvas(output_path, pagesize=(X, Y))
# IFM = Image.fromarray(img)
# cc.drawImage(ImageReader(IFM), 0, 0, width=X, height=Y)
# # cc.drawImage(ImageReader(cv2pil(img)), 0, 0, width=X, height=Y)
# for result in results:
#     # cc.setFont("IPAexMintyou", result["height"] * 0.9)
#     cc.setFont("ipaexg", result["height"] * 0.9)
#     cc.setFillColor(Color(0, 0, 0, alpha=0))  # 色は透明にする
#     cc.drawString(
#         result["vertic"]["x"],
#         Y - result["vertic"]["y"] + small_fix_y * result["height"],
#         result["text"],
#     )
# cc.showPage()
# cc.save()

output_path = os.getcwd() + r"\RPAPhoto\PDFeTaxReadForList\AIOCR2.pdf"  # 元
lattice_tables = camelot.read_pdf(output_path, flavor="lattice", line_scale=110)
# lattice_tables = camelot.read_pdf(output_path, flavor="stream")
PDFdf = lattice_tables[0].df
print(PDFdf)
# lattice_tables.export(output_path, f='excel') # 今回はエクセルで出力しているがjson csv htmlでの出力も可能
