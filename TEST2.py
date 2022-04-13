<<<<<<< HEAD
﻿from PIL import Image
import os
import sys
import pyocr
import pyocr.builders
import pdf2image

purl = r"\\Sv05121a\e\電子ファイル\メッセージボックス\TESTe-Tax\eTAX\12_有限会社 広島シティサービス\12_有限会社 広島シティサービス_消費税及び地方消費税の中間申告について_20220401 123212.pdf"
TESTURL = r"C:\Users\soumu\Desktop\RPAScript\RPAPhoto\PDFeTaxReadForList"
Mydir = os.getcwd()
pppath = Mydir + r"\poppler-22.01.0\Library\bin"
tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)

# The tools are returned in the recommended order of usage
tool = tools[0]
print("Will use tool '%s'" % (tool.get_name()))
# Ex: Will use tool 'libtesseract'


# pdfから画像オブジェクトに
images = pdf2image.convert_from_path(
    purl, dpi=200, output_folder=TESTURL, fmt="png", poppler_path=pppath
)
lang = "jpn"
# lang = 'jpn'
# 画像オブジェクトからテキストに
for image in images:
    txt = tool.image_to_string(image, lang=lang, builder=pyocr.builders.TextBuilder())
    print(txt)
=======
﻿import numpy as np
import math

wsAd = np.nan
if math.isnan(wsAd) is True:
    print("nan")
>>>>>>> 8ef8bf93830227b51cbdcae8ed5541e63a829791
