import os
import numpy as np
from pdfminer.high_level import extract_text
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from PIL import Image
import pyocr
import ContextTimeOut as CTO
import Function.CSVOut as FCSV
import Function.FolderCreate as FC

# logger設定------------------------------------------------------------------------------
import logging.config

logging.config.fileConfig(r"LogConf\logging_debug.conf")
logger = logging.getLogger(__name__)
# ----------------------------------------------------------------------------------------
def SerchdirFolders(URL):  # 指定URL配下のサブフォルダを取得
    List = []
    for fd_path, sb_folder, sb_file in os.walk(URL):
        for fol in sb_folder:
            # print(fd_path + '\\' + fol)
            List.append([fd_path, fol])
    return List


# ----------------------------------------------------------------------------------------
def SerchdirFiles(URL):  # 指定URL配下のファイルを取得
    List = []
    for fd_path, sb_folder, sb_file in os.walk(URL):
        for fil in sb_file:
            # print(fd_path + '\\' + fil)
            List.append([fd_path, fil])
    return List


# ----------------------------------------------------------------------------------------
def PDFOCRRead():
    # インストールしたTesseract-OCRのパスを環境変数「PATH」へ追記する。
    # OS自体に設定してあれば以下の2行は不要
    path = "C:\\Program Files\\Tesseract-OCR"
    os.environ["PATH"] = os.environ["PATH"] + path
    # pyocrへ利用するOCRエンジンをTesseractに指定する。
    tools = pyocr.get_available_tools()
    print(tools[0].get_name())
    tool = tools[0]
    # OCR対象の画像ファイルを読み込む
    img = Image.open("test2.jpg")
    # 画像を読みやすいように加工。
    img = img.convert("RGB")
    size = img.size
    img2 = Image.new("RGB", size)
    border = 110
    for x in range(size[0]):
        for y in range(size[1]):
            r, g, b = img.getpixel((x, y))
            if r > border or g > border or b > border:
                r = 255
                g = 255
                b = 255
            img2.putpixel((x, y), (r, g, b))
    # 画像から文字を読み込む
    builder = pyocr.builders.TextBuilder(tesseract_layout=3)
    text = tool.image_to_string(img2, lang="jpn", builder=builder)
    return text


# ----------------------------------------------------------------------------------------
def PDFSetting(
    dfIndexdata,
    SinkokuCSV,
    SinkokuCSV2,
    SinkokuCSV3,
    SinkokuCSV4,
    SyotokuCSV,
    SyotokuCSV2,
    SyotokuCSV3,
    SyotokuCSV4,
    SyouhiCSV,
    SyouhiCSV2,
    SyouhiCSV3,
    SyouhiCyukanCSV,
    YoteiCSV,
    HoujinCSV,
    SyoukyakuCSV,
    SyoukyakuCSV2,
    ZouyoCSV,
    ZaisanCSV,
    SinkokuUkeCSV,
    ImageCSV,
):
    # 確定申告リストと突合------------------------------------------------------
    IndexFlags = SinkokuCSV == dfIndexdata
    FolseC = IndexFlags.sum(axis=1) - np.array(dfIndexdata).shape[0]
    if FolseC[0] >= -2:
        PDFFlag = "確定申告"
    # ------------------------------------------------------------------------
    # 確定申告リスト2と突合------------------------------------------------------
    IndexFlags = SinkokuCSV2 == dfIndexdata
    FolseC = IndexFlags.sum(axis=1) - np.array(dfIndexdata).shape[0]
    if FolseC[0] >= -2:
        PDFFlag = "確定申告2"
    # ------------------------------------------------------------------------
    # 確定申告リスト3と突合------------------------------------------------------
    IndexFlags = SinkokuCSV3 == dfIndexdata
    FolseC = IndexFlags.sum(axis=1) - np.array(dfIndexdata).shape[0]
    if FolseC[0] >= -2:
        PDFFlag = "確定申告3"
    # ------------------------------------------------------------------------
    # 確定申告リスト4と突合------------------------------------------------------
    IndexFlags = SinkokuCSV4 == dfIndexdata
    FolseC = IndexFlags.sum(axis=1) - np.array(dfIndexdata).shape[0]
    if FolseC[0] >= -2:
        PDFFlag = "確定申告4"
    # ------------------------------------------------------------------------
    # 所得税リストと突合--------------------------------------------------------
    IndexFlags = SyotokuCSV == dfIndexdata
    FolseC = IndexFlags.sum(axis=1) - np.array(dfIndexdata).shape[0]
    if FolseC[0] >= -2:
        PDFFlag = "所得税"
    # ------------------------------------------------------------------------
    # 所得税2リストと突合--------------------------------------------------------
    IndexFlags = SyotokuCSV2 == dfIndexdata
    FolseC = IndexFlags.sum(axis=1) - np.array(dfIndexdata).shape[0]
    if FolseC[0] >= -2:
        PDFFlag = "所得税2"
    # ------------------------------------------------------------------------
    # 所得税3リストと突合--------------------------------------------------------
    IndexFlags = SyotokuCSV3 == dfIndexdata
    FolseC = IndexFlags.sum(axis=1) - np.array(dfIndexdata).shape[0]
    if FolseC[0] >= -2:
        PDFFlag = "所得税3"
    # ------------------------------------------------------------------------
    # 所得税4リストと突合--------------------------------------------------------
    IndexFlags = SyotokuCSV4 == dfIndexdata
    FolseC = IndexFlags.sum(axis=1) - np.array(dfIndexdata).shape[0]
    if FolseC[0] >= -2:
        PDFFlag = "所得税4"
    # ------------------------------------------------------------------------
    # 消費税リストと突合--------------------------------------------------------
    IndexFlags = SyouhiCSV == dfIndexdata
    FolseC = IndexFlags.sum(axis=1) - np.array(dfIndexdata).shape[0]
    if FolseC[0] >= -2:
        PDFFlag = "消費税"
    # ------------------------------------------------------------------------
    # 消費税リストと突合--------------------------------------------------------
    IndexFlags = SyouhiCSV2 == dfIndexdata
    FolseC = IndexFlags.sum(axis=1) - np.array(dfIndexdata).shape[0]
    if FolseC[0] >= -2:
        PDFFlag = "消費税2"
    # ------------------------------------------------------------------------
    # 消費税リストと突合--------------------------------------------------------
    IndexFlags = SyouhiCSV3 == dfIndexdata
    FolseC = IndexFlags.sum(axis=1) - np.array(dfIndexdata).shape[0]
    if FolseC[0] >= -2:
        PDFFlag = "消費税3"
    # ------------------------------------------------------------------------
    # 消費税中間リストと突合--------------------------------------------------------
    IndexFlags = SyouhiCyukanCSV == dfIndexdata
    FolseC = IndexFlags.sum(axis=1) - np.array(dfIndexdata).shape[0]
    if FolseC[0] >= -2:
        PDFFlag = "消費税中間申告"
    # ------------------------------------------------------------------------
    # 予定申告リストと突合------------------------------------------------------
    IndexFlags = YoteiCSV == dfIndexdata
    FolseC = IndexFlags.sum(axis=1) - np.array(dfIndexdata).shape[0]
    if FolseC[0] >= -2:
        PDFFlag = "予定申告"
    # ------------------------------------------------------------------------
    # 法人税リストと突合--------------------------------------------------------
    IndexFlags = HoujinCSV == dfIndexdata
    FolseC = IndexFlags.sum(axis=1) - np.array(dfIndexdata).shape[0]
    if FolseC[0] >= -2:
        PDFFlag = "法人税"
    # ------------------------------------------------------------------------
    # 贈与税リストと突合--------------------------------------------------------
    IndexFlags = ZouyoCSV == dfIndexdata
    FolseC = IndexFlags.sum(axis=1) - np.array(dfIndexdata).shape[0]
    if FolseC[0] >= -2:
        PDFFlag = "贈与税"
    # ------------------------------------------------------------------------
    # 財産債務リストと突合--------------------------------------------------------
    IndexFlags = ZaisanCSV == dfIndexdata
    FolseC = IndexFlags.sum(axis=1) - np.array(dfIndexdata).shape[0]
    if FolseC[0] >= -2:
        PDFFlag = "財産債務"
    # ------------------------------------------------------------------------
    # 申告受付リストと突合--------------------------------------------------------
    IndexFlags = SinkokuUkeCSV == dfIndexdata
    FolseC = IndexFlags.sum(axis=1) - np.array(dfIndexdata).shape[0]
    if FolseC[0] >= -2:
        PDFFlag = "申告受付通知"
    # ------------------------------------------------------------------------
    # イメージ添付書類リストと突合--------------------------------------------------------
    IndexFlags = ImageCSV == dfIndexdata
    FolseC = IndexFlags.sum(axis=1) - np.array(dfIndexdata).shape[0]
    if FolseC[0] >= -2:
        PDFFlag = "イメージ添付書類"
    # ------------------------------------------------------------------------
    # 償却資産リストと突合------------------------------------------------------
    IndexFlags = SyoukyakuCSV == dfIndexdata
    FolseC = IndexFlags.sum(axis=1) - np.array(dfIndexdata).shape[0]
    if FolseC[0] >= -2:
        try:
            PDFFlag
            if PDFFlag == "法人税":
                if "課税所在地" in dfIndexdata:
                    PDFFlag = "償却資産"
                else:
                    PDFFlag = "法人税"
            else:
                PDFFlag = "償却資産"
        except:
            PDFFlag = "償却資産"
    # ------------------------------------------------------------------------
    # 償却資産2リストと突合------------------------------------------------------
    IndexFlags = SyoukyakuCSV2 == dfIndexdata
    FolseC = IndexFlags.sum(axis=1) - np.array(dfIndexdata).shape[0]
    if FolseC[0] >= -2:
        try:
            PDFFlag
            if PDFFlag == "法人税":
                if "課税所在地" in dfIndexdata:
                    PDFFlag = "償却資産2"
                else:
                    PDFFlag = "法人税"
            else:
                PDFFlag = "償却資産2"
        except:
            PDFFlag = "償却資産2"
    # ------------------------------------------------------------------------
    return PDFFlag


# ----------------------------------------------------------------------------------------
def ReadAction(
    SCode,
    path_pdf,
    PDFFlag,
    y,
    PDFdfRow,
    PDFdf,
    SinkokuCSVList,
    SinkokuCSV2List,
    SinkokuCSV3List,
    SinkokuCSV4List,
    SyouhiCSVList,
    SyouhiCSV2List,
    SyouhiCSV3List,
    SyouhiCyukanCSVList,
    SyotokuCSVList,
    SyotokuCSV2List,
    SyotokuCSV3List,
    SyotokuCSV4List,
    YoteiCSVList,
    SyoukyakuCSVList,
    SyoukyakuCSV2List,
    ZouyoCSVList,
    ZaisanCSVList,
    SinkokuUkeCSVList,
    HoujinCSVList,
    ImageCSVList,
    CSVBadList,
    SubPDFdf,
):
    try:
        if PDFFlag == "確定申告":
            for z in range(PDFdfRow):  # PDFのテーブル行数分ループ
                dfdatarow = PDFdf.iloc[z]  # PDFのテーブル行データ1
                if dfdatarow[0] == "手続名":
                    PDFTitle = str(dfdatarow[1])
                elif dfdatarow[0] == "氏名又は名称":
                    PDFName = str(dfdatarow[1])
                elif dfdatarow[0] == "受付日時":
                    PDFDate = str(dfdatarow[1])
                elif dfdatarow[0] == "種目":
                    PDFSyumoku = str(dfdatarow[1])
                elif dfdatarow[0] == "事業年度　自":
                    PDFJigyouNendo = str(dfdatarow[1])
                elif dfdatarow[0] == "事業年度　至":
                    PDFJigyouNendo = PDFJigyouNendo + "-" + str(dfdatarow[1])
                elif dfdatarow[0] == "税目":
                    if z == 10:
                        PDFZeimoku = str(dfdatarow[1])
                    elif z == 16:
                        PDFZeimoku2 = str(dfdatarow[1])
                elif dfdatarow[0] == "申告の種類":
                    if z == 11:
                        PDFSinkokuSyu = str(dfdatarow[1])
                    elif z == 17:
                        PDFSinkokuSyu2 = str(dfdatarow[1])
                elif dfdatarow[0] == "所得金額又は欠損金額":
                    PDFSyotokuAndKesson = str(dfdatarow[1])
                elif dfdatarow[0] == "差引確定法人税額":
                    PDFKakuteiHoujingaku = str(dfdatarow[1])
                elif "欠損金又は災害損失金等の当期" in dfdatarow[0]:
                    PDFKessonAndSaigai = str(dfdatarow[1])
                elif "翌期へ繰り越す欠損金又は災害" in dfdatarow[0]:
                    PDFKuriketusai = str(dfdatarow[1])
                elif dfdatarow[0] == "課税標準法人税額":
                    PDFKazeiHyoujyun = str(dfdatarow[1])
                elif dfdatarow[0] == "差引確定地方法人税額":
                    PDFSasihiki = str(dfdatarow[1])
            OutputList = [
                SCode,
                path_pdf.replace("/", "\\"),
                str(y + 1) + "ページ目",
                PDFTitle,
                PDFName,
                PDFDate,
                PDFSyumoku,
                PDFJigyouNendo,
                PDFZeimoku,
                PDFSinkokuSyu,
                PDFSyotokuAndKesson,
                PDFKakuteiHoujingaku,
                PDFKessonAndSaigai,
                PDFKuriketusai,
                PDFZeimoku2,
                PDFSinkokuSyu2,
                PDFKazeiHyoujyun,
                PDFSasihiki,
            ]
            SinkokuCSVList.append(OutputList)
        # ------------------------------------------------------------------------
        elif PDFFlag == "確定申告2":
            for z in range(PDFdfRow):  # PDFのテーブル行数分ループ
                dfdatarow = PDFdf.iloc[z]  # PDFのテーブル行データ1
                if dfdatarow[0] == "手続名":
                    PDFTitle = str(dfdatarow[1])
                elif dfdatarow[0] == "氏名又は名称":
                    PDFName = str(dfdatarow[1])
                elif dfdatarow[0] == "受付日時":
                    PDFDate = str(dfdatarow[1])
                elif dfdatarow[0] == "種目":
                    PDFSyumoku = str(dfdatarow[1])
                elif dfdatarow[0] == "事業年度　自":
                    PDFJigyouNendo = str(dfdatarow[1])
                elif dfdatarow[0] == "事業年度　至":
                    PDFJigyouNendo = PDFJigyouNendo + "-" + str(dfdatarow[1])
                elif dfdatarow[0] == "税目":
                    if z == 10:
                        PDFZeimoku = str(dfdatarow[1])
                    elif z == 16:
                        PDFZeimoku2 = str(dfdatarow[1])
                elif dfdatarow[0] == "申告の種類":
                    if z == 11:
                        PDFSinkokuSyu = str(dfdatarow[1])
                    elif z == 17:
                        PDFSinkokuSyu2 = str(dfdatarow[1])
                elif dfdatarow[0] == "所得金額又は欠損金額":
                    PDFSyotokuAndKesson = str(dfdatarow[1])
                elif dfdatarow[0] == "この申告による還付金額":
                    if z == 13:
                        PDFSinkokuKanpu = str(dfdatarow[1])
                    elif z == 19:
                        PDFSinkokuKanpu2 = str(dfdatarow[1])
                elif "欠損金又は災害損失金等の当期" in dfdatarow[0]:
                    PDFKessonAndSaigai = str(dfdatarow[1])
                elif "翌期へ繰り越す欠損金又は災害" in dfdatarow[0]:
                    PDFKuriketusai = str(dfdatarow[1])
                elif dfdatarow[0] == "課税標準法人税額":
                    PDFKazeiHyoujyun = str(dfdatarow[1])
            OutputList = [
                SCode,
                path_pdf.replace("/", "\\"),
                str(y + 1) + "ページ目",
                PDFTitle,
                PDFName,
                PDFDate,
                PDFSyumoku,
                PDFJigyouNendo,
                PDFZeimoku,
                PDFSinkokuSyu,
                PDFSyotokuAndKesson,
                PDFSinkokuKanpu,
                PDFKessonAndSaigai,
                PDFKuriketusai,
                PDFZeimoku2,
                PDFSinkokuSyu2,
                PDFKazeiHyoujyun,
                PDFSinkokuKanpu2,
            ]
            SinkokuCSV2List.append(OutputList)
        # ------------------------------------------------------------------------
        elif PDFFlag == "確定申告3":
            for z in range(PDFdfRow):  # PDFのテーブル行数分ループ
                dfdatarow = PDFdf.iloc[z]  # PDFのテーブル行データ1
                if dfdatarow[0] == "手続名":
                    PDFTitle = str(dfdatarow[1])
                elif dfdatarow[0] == "氏名又は名称":
                    PDFName = str(dfdatarow[1])
                elif dfdatarow[0] == "受付日時":
                    PDFDate = str(dfdatarow[1])
                elif dfdatarow[0] == "種目":
                    PDFSyumoku = str(dfdatarow[1])
                elif dfdatarow[0] == "事業年度　自":
                    PDFJigyouNendo = str(dfdatarow[1])
                elif dfdatarow[0] == "事業年度　至":
                    PDFJigyouNendo = PDFJigyouNendo + "-" + str(dfdatarow[1])
                elif dfdatarow[0] == "税目":
                    if z == 10:
                        PDFZeimoku = str(dfdatarow[1])
                    elif z == 16:
                        PDFZeimoku2 = str(dfdatarow[1])
                elif dfdatarow[0] == "申告の種類":
                    if z == 11:
                        PDFSinkokuSyu = str(dfdatarow[1])
                    elif z == 17:
                        PDFSinkokuSyu2 = str(dfdatarow[1])
                elif dfdatarow[0] == "所得金額又は欠損金額":
                    PDFSyotokuAndKesson = str(dfdatarow[1])
                elif dfdatarow[0] == "この申告による還付金額":
                    if z == 13:
                        PDFSinkokuKanpu = str(dfdatarow[1])
                elif "欠損金又は災害損失金等の当期" in dfdatarow[0]:
                    PDFKessonAndSaigai = str(dfdatarow[1])
                elif "翌期へ繰り越す欠損金又は災害" in dfdatarow[0]:
                    PDFKuriketusai = str(dfdatarow[1])
                elif dfdatarow[0] == "課税標準法人税額":
                    PDFKazeiHyoujyun = str(dfdatarow[1])
                elif dfdatarow[0] == "差引確定地方法人税額":
                    PDFSasihiki = str(dfdatarow[1])
            OutputList = [
                SCode,
                path_pdf.replace("/", "\\"),
                str(y + 1) + "ページ目",
                PDFTitle,
                PDFName,
                PDFDate,
                PDFSyumoku,
                PDFJigyouNendo,
                PDFZeimoku,
                PDFSinkokuSyu,
                PDFSyotokuAndKesson,
                PDFSinkokuKanpu,
                PDFKessonAndSaigai,
                PDFKuriketusai,
                PDFZeimoku2,
                PDFSinkokuSyu2,
                PDFKazeiHyoujyun,
                PDFSasihiki,
            ]
            SinkokuCSV3List.append(OutputList)
        # ------------------------------------------------------------------------
        elif PDFFlag == "確定申告4":
            for z in range(PDFdfRow):  # PDFのテーブル行数分ループ
                dfdatarow = PDFdf.iloc[z]  # PDFのテーブル行データ1
                if dfdatarow[0] == "手続名":
                    PDFTitle = str(dfdatarow[1])
                elif dfdatarow[0] == "氏名又は名称":
                    PDFName = str(dfdatarow[1])
                elif dfdatarow[0] == "受付日時":
                    PDFDate = str(dfdatarow[1])
                elif dfdatarow[0] == "種目":
                    PDFSyumoku = str(dfdatarow[1])
                elif dfdatarow[0] == "事業年度　自":
                    PDFJigyouNendo = str(dfdatarow[1])
                elif dfdatarow[0] == "事業年度　至":
                    PDFJigyouNendo = PDFJigyouNendo + "-" + str(dfdatarow[1])
                elif dfdatarow[0] == "税目":
                    if z == 10:
                        PDFZeimoku = str(dfdatarow[1])
                    elif z == 16:
                        PDFZeimoku2 = str(dfdatarow[1])
                elif dfdatarow[0] == "申告の種類":
                    if z == 11:
                        PDFSinkokuSyu = str(dfdatarow[1])
                    elif z == 17:
                        PDFSinkokuSyu2 = str(dfdatarow[1])
                elif dfdatarow[0] == "所得金額又は欠損金額":
                    PDFSyotokuAndKesson = str(dfdatarow[1])
                elif dfdatarow[0] == "差引確定法人税額":
                    PDFSasihikih = str(dfdatarow[1])
                elif "欠損金又は災害損失金等の当期" in dfdatarow[0]:
                    PDFKessonAndSaigai = str(dfdatarow[1])
                elif "翌期へ繰り越す欠損金又は災害" in dfdatarow[0]:
                    PDFKuriketusai = str(dfdatarow[1])
                elif dfdatarow[0] == "課税標準法人税額":
                    PDFKazeiHyoujyun = str(dfdatarow[1])
                elif dfdatarow[0] == "差引確定地方法人税額":
                    PDFSasihiki = str(dfdatarow[1])
            OutputList = [
                SCode,
                path_pdf.replace("/", "\\"),
                str(y + 1) + "ページ目",
                PDFTitle,
                PDFName,
                PDFDate,
                PDFSyumoku,
                PDFJigyouNendo,
                PDFZeimoku,
                PDFSinkokuSyu,
                PDFSyotokuAndKesson,
                PDFSasihikih,
                PDFKessonAndSaigai,
                PDFKuriketusai,
                PDFZeimoku2,
                PDFSinkokuSyu2,
                PDFKazeiHyoujyun,
                PDFSasihiki,
            ]
            SinkokuCSV4List.append(OutputList)
        # ------------------------------------------------------------------------
        elif PDFFlag == "所得税":
            for z in range(PDFdfRow):  # PDFのテーブル行数分ループ
                dfdatarow = PDFdf.iloc[z]  # PDFのテーブル行データ1
                if dfdatarow[0] == "手続名":
                    PDFTitle = str(dfdatarow[1])
                elif dfdatarow[0] == "氏名又は名称":
                    PDFName = str(dfdatarow[1])
                elif dfdatarow[0] == "受付日時":
                    PDFDate = str(dfdatarow[1])
                elif dfdatarow[0] == "年分":
                    PDFNendo = str(dfdatarow[1])
                elif dfdatarow[0] == "種目":
                    PDFSyumoku = str(dfdatarow[1])
                elif dfdatarow[0] == "所得金額":
                    PDFSyotoku = str(dfdatarow[1])
                elif "納める税金" in dfdatarow[0]:
                    PDFNouzeigaku = str(dfdatarow[1])
                elif "還付される税金" in dfdatarow[0]:
                    PDFKanpugaku = str(dfdatarow[1])
            OutputList = [
                SCode,
                path_pdf.replace("/", "\\"),
                str(y + 1) + "ページ目",
                PDFTitle,
                PDFName,
                PDFDate,
                PDFNendo,
                PDFSyumoku,
                PDFSyotoku,
                PDFNouzeigaku,
                PDFKanpugaku,
            ]
            SyotokuCSVList.append(OutputList)
        # ------------------------------------------------------------------------
        elif PDFFlag == "所得税2":
            for z in range(PDFdfRow):  # PDFのテーブル行数分ループ
                dfdatarow = PDFdf.iloc[z]  # PDFのテーブル行データ1
                if dfdatarow[0] == "氏名又は名称":
                    PDFName = str(dfdatarow[1])
                elif dfdatarow[0] == "受付日時":
                    PDFDate = str(dfdatarow[1])
                elif dfdatarow[0] == "年分":
                    PDFNendo = str(dfdatarow[1])
                elif dfdatarow[0] == "種目":
                    PDFSyumoku = str(dfdatarow[1])
                elif dfdatarow[0] == "所得金額":
                    PDFSyotoku = str(dfdatarow[1])
                elif "納める税金" in dfdatarow[0]:
                    PDFNouzeigaku = str(dfdatarow[1])
                elif "還付される税金" in dfdatarow[0]:
                    PDFKanpugaku = str(dfdatarow[1])
                elif dfdatarow[0] == "「所得金額」欄について":
                    PDFSyotokuCom = str(dfdatarow[1])
            OutputList = [
                SCode,
                path_pdf.replace("/", "\\"),
                str(y + 1) + "ページ目",
                PDFName,
                PDFDate,
                PDFNendo,
                PDFSyumoku,
                PDFSyotoku,
                PDFNouzeigaku,
                PDFKanpugaku,
                PDFSyotokuCom,
            ]
            SyotokuCSV2List.append(OutputList)
        # ------------------------------------------------------------------------
        elif PDFFlag == "所得税3":
            for z in range(PDFdfRow):  # PDFのテーブル行数分ループ
                dfdatarow = PDFdf.iloc[z]  # PDFのテーブル行データ1
                if dfdatarow[0] == "手続名":
                    PDFTitle = str(dfdatarow[1])
                elif dfdatarow[0] == "氏名又は名称":
                    PDFName = str(dfdatarow[1])
                elif dfdatarow[0] == "受付日時":
                    PDFDate = str(dfdatarow[1])
                elif dfdatarow[0] == "年分":
                    PDFNendo = str(dfdatarow[1])
                elif dfdatarow[0] == "種目":
                    PDFSyumoku = str(dfdatarow[1])
                elif dfdatarow[0] == "所得金額":
                    PDFSyotoku = str(dfdatarow[1])
                elif "納める税金" in dfdatarow[0]:
                    PDFNouzeigaku = str(dfdatarow[1])
                elif "還付される税金" in dfdatarow[0]:
                    PDFKanpugaku = str(dfdatarow[1])
                elif dfdatarow[0] == "「所得金額」欄について":
                    PDFSyotokuCom = str(dfdatarow[1])
            OutputList = [
                SCode,
                path_pdf.replace("/", "\\"),
                str(y + 1) + "ページ目",
                PDFTitle,
                PDFName,
                PDFDate,
                PDFNendo,
                PDFSyumoku,
                PDFSyotoku,
                PDFNouzeigaku,
                PDFKanpugaku,
                PDFSyotokuCom,
            ]
            SyotokuCSV3List.append(OutputList)
        # ------------------------------------------------------------------------
        elif PDFFlag == "所得税4":
            for z in range(PDFdfRow):  # PDFのテーブル行数分ループ
                dfdatarow = PDFdf.iloc[z]  # PDFのテーブル行データ1
                if dfdatarow[0] == "手続名":
                    PDFTitle = str(dfdatarow[1])
                elif dfdatarow[0] == "氏名又は名称":
                    PDFName = str(dfdatarow[1])
                elif dfdatarow[0] == "受付日時":
                    PDFDate = str(dfdatarow[1])
                elif dfdatarow[0] == "年分":
                    PDFNendo = str(dfdatarow[1])
                elif dfdatarow[0] == "種目":
                    PDFSyumoku = str(dfdatarow[1])
                elif dfdatarow[0] == "所得金額":
                    PDFSyotoku = str(dfdatarow[1])
                elif "納める税金" in dfdatarow[0]:
                    PDFNouzeigaku = str(dfdatarow[1])
                elif "還付される税金" in dfdatarow[0]:
                    PDFKanpugaku = str(dfdatarow[1])
                elif dfdatarow[0] == "「所得金額」欄について":
                    PDFSyotokuCom = str(dfdatarow[1])
            OutputList = [
                SCode,
                path_pdf.replace("/", "\\"),
                str(y + 1) + "ページ目",
                PDFTitle,
                PDFName,
                PDFDate,
                PDFNendo,
                PDFSyumoku,
                PDFSyotoku,
                PDFNouzeigaku,
                PDFKanpugaku,
                PDFSyotokuCom,
            ]
            SyotokuCSV4List.append(OutputList)
        # ------------------------------------------------------------------------
        elif PDFFlag == "消費税":
            for z in range(PDFdfRow):  # PDFのテーブル行数分ループ
                dfdatarow = PDFdf.iloc[z]  # PDFのテーブル行データ1
                if dfdatarow[0] == "手続名":
                    PDFTitle = str(dfdatarow[1])
                elif dfdatarow[0] == "氏名又は名称":
                    PDFName = str(dfdatarow[1])
                elif dfdatarow[0] == "受付日時":
                    PDFDate = str(dfdatarow[1])
                elif dfdatarow[0] == "種目":
                    PDFSyumoku = str(dfdatarow[1])
                elif dfdatarow[0] == "申告の種類":
                    PDFSyurui = str(dfdatarow[1])
                elif dfdatarow[0] == "課税標準額":
                    PDFKazeigaku = str(dfdatarow[1])
                elif "消費税及び地方消費税の合計" in dfdatarow[0]:
                    PDFGoukeigaku = str(dfdatarow[1])
                elif dfdatarow[0] == "課税期間　自":
                    PDFKazeikikan = str(dfdatarow[1])
                elif dfdatarow[0] == "課税期間　至":
                    PDFKazeikikan = PDFKazeikikan + "-" + str(dfdatarow[1])
            OutputList = [
                SCode,
                path_pdf.replace("/", "\\"),
                str(y + 1) + "ページ目",
                PDFTitle,
                PDFName,
                PDFDate,
                PDFSyumoku,
                PDFSyurui,
                PDFKazeigaku,
                PDFGoukeigaku,
                PDFKazeikikan,
            ]
            SyouhiCSVList.append(OutputList)
        # ------------------------------------------------------------------------
        elif PDFFlag == "消費税2":
            for z in range(PDFdfRow):  # PDFのテーブル行数分ループ
                dfdatarow = PDFdf.iloc[z]  # PDFのテーブル行データ1
                if dfdatarow[0] == "手続名":
                    PDFTitle = str(dfdatarow[1])
                elif dfdatarow[0] == "氏名又は名称":
                    PDFName = str(dfdatarow[1])
                elif dfdatarow[0] == "受付日時":
                    PDFDate = str(dfdatarow[1])
                elif dfdatarow[0] == "種目":
                    PDFSyumoku = str(dfdatarow[1])
                elif dfdatarow[0] == "課税標準額":
                    PDFKazeigaku = str(dfdatarow[1])
                elif "消費税及び地方消費税の合計" in dfdatarow[0]:
                    PDFGoukeigaku = str(dfdatarow[1])
                elif dfdatarow[0] == "課税期間　自":
                    PDFKazeikikan = str(dfdatarow[1])
                elif dfdatarow[0] == "課税期間　至":
                    PDFKazeikikan = PDFKazeikikan + "-" + str(dfdatarow[1])
            OutputList = [
                SCode,
                path_pdf.replace("/", "\\"),
                str(y + 1) + "ページ目",
                PDFTitle,
                PDFName,
                PDFDate,
                PDFSyumoku,
                PDFKazeigaku,
                PDFGoukeigaku,
                PDFKazeikikan,
            ]
            SyouhiCSV2List.append(OutputList)
        # ------------------------------------------------------------------------
        elif PDFFlag == "消費税3":
            for z in range(PDFdfRow):  # PDFのテーブル行数分ループ
                dfdatarow = PDFdf.iloc[z]  # PDFのテーブル行データ1
                if dfdatarow[0] == "氏名又は名称":
                    PDFName = str(dfdatarow[1])
                elif dfdatarow[0] == "受付日時":
                    PDFDate = str(dfdatarow[1])
                elif dfdatarow[0] == "種目":
                    PDFSyumoku = str(dfdatarow[1])
                elif dfdatarow[0] == "課税標準額":
                    PDFKazeigaku = str(dfdatarow[1])
                elif "消費税及び地方消費税の合計" in dfdatarow[0]:
                    PDFGoukeigaku = str(dfdatarow[1])
                elif dfdatarow[0] == "課税期間　自":
                    PDFKazeikikan = str(dfdatarow[1])
                elif dfdatarow[0] == "課税期間　至":
                    PDFKazeikikan = PDFKazeikikan + "-" + str(dfdatarow[1])
            OutputList = [
                SCode,
                path_pdf.replace("/", "\\"),
                str(y + 1) + "ページ目",
                PDFName,
                PDFDate,
                PDFSyumoku,
                PDFKazeigaku,
                PDFGoukeigaku,
                PDFKazeikikan,
            ]
            SyouhiCSV3List.append(OutputList)
        # ------------------------------------------------------------------------
        elif PDFFlag == "消費税中間申告":
            for z in range(PDFdfRow):  # PDFのテーブル行数分ループ
                dfdatarow = PDFdf.iloc[z]  # PDFのテーブル行データ1
                if dfdatarow[0] == "手続名":
                    PDFTitle = str(dfdatarow[1])
                elif dfdatarow[0] == "氏名又は名称":
                    PDFName = str(dfdatarow[1])
                elif dfdatarow[0] == "受付日時":
                    PDFDate = str(dfdatarow[1])
                elif dfdatarow[0] == "種目":
                    PDFSyumoku = str(dfdatarow[1])
                elif "消費税及び地方消費税の合計" in dfdatarow[0]:
                    PDFGoukeigaku = str(dfdatarow[1])
                elif dfdatarow[0] == "課税期間　自":
                    PDFKazeikikan = str(dfdatarow[1])
                elif dfdatarow[0] == "課税期間　至":
                    PDFKazeikikan = PDFKazeikikan + "-" + str(dfdatarow[1])
            OutputList = [
                SCode,
                path_pdf.replace("/", "\\"),
                str(y + 1) + "ページ目",
                PDFTitle,
                PDFName,
                PDFDate,
                PDFSyumoku,
                PDFGoukeigaku,
                PDFKazeikikan,
            ]
            SyouhiCyukanCSVList.append(OutputList)
        # ------------------------------------------------------------------------
        elif PDFFlag == "予定申告":
            for z in range(PDFdfRow):  # PDFのテーブル行数分ループ
                dfdatarow = PDFdf.iloc[z]  # PDFのテーブル行データ1
                if dfdatarow[0] == "手続名":
                    PDFTitle = str(dfdatarow[1])
                elif dfdatarow[0] == "氏名又は名称":
                    PDFName = str(dfdatarow[1])
                elif dfdatarow[0] == "受付日時":
                    PDFDate = str(dfdatarow[1])
                elif dfdatarow[0] == "種目":
                    PDFSyumoku = str(dfdatarow[1])
                elif dfdatarow[0] == "事業年度　自":
                    PDFJigyouNendo = str(dfdatarow[1])
                elif dfdatarow[0] == "事業年度　至":
                    PDFJigyouNendo = PDFJigyouNendo + "-" + str(dfdatarow[1])
                elif dfdatarow[0] == "税目":
                    if z == 10:
                        PDFZeimoku = str(dfdatarow[1])
                    elif z == 12:
                        PDFZeimoku2 = str(dfdatarow[1])
                elif dfdatarow[0] == "納付すべき法人税額":
                    PDFNouhuHoujin = str(dfdatarow[1])
                elif dfdatarow[0] == "納付すべき地方法人税額":
                    PDFNouhuTihou = str(dfdatarow[1])
            OutputList = [
                SCode,
                path_pdf.replace("/", "\\"),
                str(y + 1) + "ページ目",
                PDFTitle,
                PDFName,
                PDFDate,
                PDFSyumoku,
                PDFJigyouNendo,
                PDFZeimoku,
                PDFNouhuHoujin,
                PDFZeimoku2,
                PDFNouhuTihou,
            ]
            YoteiCSVList.append(OutputList)
        # ------------------------------------------------------------------------
        elif PDFFlag == "償却資産":
            for z in range(PDFdfRow):  # PDFのテーブル行数分ループ
                dfdatarow = PDFdf.iloc[z]  # PDFのテーブル行データ1
                if dfdatarow[0] == "手続名":
                    PDFTitle = str(dfdatarow[1])
                elif dfdatarow[0] == "氏名又は名称":
                    PDFName = str(dfdatarow[1])
                elif dfdatarow[0] == "発行元名":
                    PDFHakkou = str(dfdatarow[1])
                elif dfdatarow[0] == "発行元所属名":
                    PDFHakkouSyozoku = str(dfdatarow[1])
                elif dfdatarow[0] == "受付日時":
                    PDFDate = str(dfdatarow[1])
                elif dfdatarow[0] == "提出先":
                    PDFTeisyutu = str(dfdatarow[1])
                elif dfdatarow[0] == "年度・期別":
                    PDFNendo = str(dfdatarow[1])
                elif dfdatarow[0] == "課税所在地":
                    PDFSyozaiti = str(dfdatarow[1])
            OutputList = [
                SCode,
                path_pdf.replace("/", "\\"),
                str(y + 1) + "ページ目",
                PDFTitle,
                PDFName,
                PDFHakkou,
                PDFHakkouSyozoku,
                PDFDate,
                PDFTeisyutu,
                PDFNendo,
                PDFSyozaiti,
            ]
            SyoukyakuCSVList.append(OutputList)
        # ------------------------------------------------------------------------
        elif PDFFlag == "償却資産2":
            for z in range(PDFdfRow):  # PDFのテーブル行数分ループ
                dfdatarow = PDFdf.iloc[z]  # PDFのテーブル行データ1
                if dfdatarow[0] == "手続名":
                    PDFTitle = str(dfdatarow[1])
                elif dfdatarow[0] == "氏名又は名称":
                    PDFName = str(dfdatarow[1])
                elif dfdatarow[0] == "発行元名":
                    PDFHakkou = str(dfdatarow[1])
                elif dfdatarow[0] == "受付日時":
                    PDFDate = str(dfdatarow[1])
                elif dfdatarow[0] == "提出先":
                    PDFTeisyutu = str(dfdatarow[1])
                elif dfdatarow[0] == "年度・期別":
                    PDFNendo = str(dfdatarow[1])
                elif dfdatarow[0] == "課税所在地":
                    PDFSyozaiti = str(dfdatarow[1])
            OutputList = [
                SCode,
                path_pdf.replace("/", "\\"),
                str(y + 1) + "ページ目",
                PDFTitle,
                PDFName,
                PDFHakkou,
                PDFDate,
                PDFTeisyutu,
                PDFNendo,
                PDFSyozaiti,
            ]
            SyoukyakuCSV2List.append(OutputList)
        # ------------------------------------------------------------------------
        elif PDFFlag == "贈与税":
            for z in range(PDFdfRow):  # PDFのテーブル行数分ループ
                dfdatarow = PDFdf.iloc[z]  # PDFのテーブル行データ1
                if dfdatarow[0] == "手続名":
                    PDFTitle = str(dfdatarow[1])
                elif dfdatarow[0] == "氏名又は名称":
                    PDFName = str(dfdatarow[1])
                elif dfdatarow[0] == "受付日時":
                    PDFDate = str(dfdatarow[1])
                elif dfdatarow[0] == "年分":
                    PDFNendo = str(dfdatarow[1])
                elif dfdatarow[0] == "種目":
                    PDFSyumoku = str(dfdatarow[1])
                elif dfdatarow[0] == "課税価格の合計額":
                    PDFKazeigaku = str(dfdatarow[1])
                elif dfdatarow[0] == "申告期限までに納付すべき税額":
                    PDFNouhuZeigaku = str(dfdatarow[1])
            OutputList = [
                SCode,
                path_pdf.replace("/", "\\"),
                str(y + 1) + "ページ目",
                PDFTitle,
                PDFName,
                PDFDate,
                PDFNendo,
                PDFSyumoku,
                PDFKazeigaku,
                PDFNouhuZeigaku,
            ]
            ZouyoCSVList.append(OutputList)
        # ------------------------------------------------------------------------
        elif PDFFlag == "財産債務":
            for z in range(PDFdfRow):  # PDFのテーブル行数分ループ
                dfdatarow = PDFdf.iloc[z]  # PDFのテーブル行データ1
                if dfdatarow[0] == "手続名":
                    PDFTitle = str(dfdatarow[1])
                elif dfdatarow[0] == "氏名又は名称":
                    PDFName = str(dfdatarow[1])
                elif dfdatarow[0] == "受付日時":
                    PDFDate = str(dfdatarow[1])
                elif dfdatarow[0] == "種目":
                    PDFSyumoku = str(dfdatarow[1])
            OutputList = [
                SCode,
                path_pdf.replace("/", "\\"),
                str(y + 1) + "ページ目",
                PDFTitle,
                PDFName,
                PDFDate,
                PDFSyumoku,
            ]
            ZaisanCSVList.append(OutputList)
        # ------------------------------------------------------------------------
        elif PDFFlag == "申告受付通知":
            for z in range(PDFdfRow):  # PDFのテーブル行数分ループ
                dfdatarow = PDFdf.iloc[z]  # PDFのテーブル行データ1
                if dfdatarow[0] == "手続名":
                    PDFTitle = str(dfdatarow[1])
                elif dfdatarow[0] == "氏名又は名称":
                    PDFName = str(dfdatarow[1])
                elif dfdatarow[0] == "発行元名":
                    PDFHakkou = str(dfdatarow[1])
                elif dfdatarow[0] == "発行元所属名":
                    PDFHakkouSyozoku = str(dfdatarow[1])
                elif dfdatarow[0] == "発行元電話番号":
                    PDFHakkouTel = str(dfdatarow[1])
                elif dfdatarow[0] == "受付日時":
                    PDFDate = str(dfdatarow[1])
                elif dfdatarow[0] == "提出先":
                    PDFTeisyutu = str(dfdatarow[1])
                elif dfdatarow[0] == "年度・期別":
                    PDFNendo = str(dfdatarow[1])
                elif dfdatarow[0] == "課税所在地":
                    PDFSyozaiti = str(dfdatarow[1])
            OutputList = [
                SCode,
                path_pdf.replace("/", "\\"),
                str(y + 1) + "ページ目",
                PDFTitle,
                PDFName,
                PDFHakkou,
                PDFHakkouSyozoku,
                PDFHakkouTel,
                PDFDate,
                PDFTeisyutu,
                PDFNendo,
                PDFSyozaiti,
            ]
            SinkokuUkeCSVList.append(OutputList)
        # ------------------------------------------------------------------------
        elif PDFFlag == "イメージ添付書類":
            for z in range(PDFdfRow):  # PDFのテーブル行数分ループ
                dfdatarow = PDFdf.iloc[z]  # PDFのテーブル行データ1
                if dfdatarow[0] == "手続名":
                    PDFTitle = str(dfdatarow[1])
                elif dfdatarow[0] == "氏名又は名称":
                    PDFName = str(dfdatarow[1])
                elif dfdatarow[0] == "受付番号":
                    PDFUkeNo = str(dfdatarow[1])
                elif dfdatarow[0] == "受付日時":
                    PDFDate = str(dfdatarow[1])
                elif dfdatarow[0] == "元の申告・申請書の受付番号":
                    PDFMotoNo = str(dfdatarow[1])
            OutputList = [
                SCode,
                path_pdf.replace("/", "\\"),
                str(y + 1) + "ページ目",
                PDFTitle,
                PDFName,
                PDFUkeNo,
                PDFDate,
                PDFMotoNo,
            ]
            ImageCSVList.append(OutputList)
        # ------------------------------------------------------------------------
        elif PDFFlag == "法人税":
            for z in range(PDFdfRow):  # PDFのテーブル行数分ループ
                dfdatarow = PDFdf.iloc[z]  # PDFのテーブル行データ1
                if dfdatarow[0] == "手続名":
                    PDFTitle = str(dfdatarow[1])
                elif dfdatarow[0] == "氏名又は名称":
                    PDFName = str(dfdatarow[1])
                elif dfdatarow[0] == "発行元名":
                    PDFHakkou = str(dfdatarow[1])
                elif dfdatarow[0] == "発行元所属名":
                    PDFHakkouSyozoku = str(dfdatarow[1])
                elif dfdatarow[0] == "受付日時":
                    PDFDate = str(dfdatarow[1])
                elif dfdatarow[0] == "提出先":
                    PDFTeisyutu = str(dfdatarow[1])
                elif dfdatarow[0] == "年度・期別":
                    PDFNendo = str(dfdatarow[1])
                elif dfdatarow[0] == "納税者氏名":
                    PDFNouzeiName = str(dfdatarow[1])
            # 表外データがあった場合の処理---------------------------------------------------------------------
            SPDList = []
            SPDRow = np.array(SubPDFdf).shape[0]
            for zz in range(SPDRow):
                Spdatarow = SubPDFdf.iloc[zz]  # PDFのテーブル行データ1
                if "円" in Spdatarow[0]:
                    SPDList.append(Spdatarow[0].replace("\u3000", "").replace(" ", ""))
            SPDstr = "\n".join(SPDList)
            # ----------------------------------------------------------------------------------------------
            OutputList = [
                SCode,
                path_pdf.replace("/", "\\"),
                str(y + 1) + "ページ目",
                PDFTitle,
                PDFName,
                PDFHakkou,
                PDFHakkouSyozoku,
                PDFDate,
                PDFTeisyutu,
                PDFNendo,
                PDFNouzeiName,
                SPDstr,
            ]
            HoujinCSVList.append(OutputList)
        # ------------------------------------------------------------------------
        else:
            logger.debug(path_pdf + "_" + str(y + 1) + "ページ目取得失敗書式登録なし")
            OutputList = [
                SCode,
                path_pdf.replace("/", "\\"),
                str(y + 1) + "ページ目取得失敗書式登録なし",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
            ]
            CSVBadList.append(OutputList)
            print("書式登録されていません。")
    except Exception as e:
        logger.debug(path_pdf + "_" + str(y + 1) + "ページ目ReadActionエラー")
        OutputList = [
            SCode,
            path_pdf.replace("/", "\\"),
            str(y + 1) + "ページ目ReadActionエラー",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
        ]
        CSVBadList.append(OutputList)
        print(e)


# ----------------------------------------------------------------------------------------
def ReadActionTKC(
    SCode,
    path_pdf,
    PDFFlag,
    y,
    TKCListSinsei,
    TKCListHTS,
    TKCListHTPDF,
    TKCListSyouhi,
    TKCListSyouhiPDF,
    TKCListTodouhu,
    TKCListSityou,
    PDFtext,
):
    ########################################################################
    ########################################################################
    SinseiJyusin = False
    HoujinTIhouJyusin = False
    HoujinTIhouTenpu = False
    SyouhizeiJyusin = False
    SyouhizeiJyusinPDF = False
    TdouhuJyusin = False
    SityouJyusin = False
    Prow = 0  # テキストデータの行数カウント変数
    FRow = 0  # メッセージ本文内の金額記載欄の先頭行数格納用
    ERow = 0  # メッセージ本文内の金額記載欄の末尾行数格納用
    # 検索キー一致で値を変数格納----------------------------------
    for PDFtextItem in PDFtext:
        print(PDFtextItem)
        if PDFFlag == "国税の電子申請・届出完了報告書":
            if PDFtextItem == "【申請・届出の受信通知】":
                SinseiJyusin = True
            if "提出先：" in PDFtextItem and SinseiJyusin is True:
                PTKCTeisyutu = PDFtextItem.replace("提出先：", "")
            elif "利用者識別番号：" in PDFtextItem and SinseiJyusin is True:
                PTKCRiyouNo = PDFtextItem.replace("利用者識別番号：", "")
            elif "氏名又は名称：" in PDFtextItem and SinseiJyusin is True:
                PTKCName = PDFtextItem.replace("氏名又は名称：", "")
            elif "代表者等氏名：" in PDFtextItem and SinseiJyusin is True:
                PTKCDaihyouName = PDFtextItem.replace("代表者等氏名：", "")
            elif "受付番号：" in PDFtextItem and SinseiJyusin is True:
                PTKCUketukeNo = PDFtextItem.replace("受付番号：", "")
            elif "受付日時：" in PDFtextItem and SinseiJyusin is True:
                PTKCDateTime = PDFtextItem.replace("受付日時：", "")
            elif "種目：" in PDFtextItem and SinseiJyusin is True:
                PTKCSyumoku = PDFtextItem.replace("種目：", "")
                SinseiJyusin = False
                OutputList = [
                    SCode,
                    path_pdf.replace("/", "\\"),
                    "ページ情報無",
                    PTKCTeisyutu,
                    PTKCRiyouNo,
                    PTKCName,
                    PTKCDaihyouName,
                    PTKCUketukeNo,
                    PTKCDateTime,
                    PTKCSyumoku,
                ]
                TKCListSinsei.append(OutputList)
            # ----------------------------------------------------------------------
        elif PDFFlag == "法人税・地方法人税・消費税の電子申告完了報告書":
            if PDFtextItem == "【法人税・地方法人税の受信通知】":
                HoujinTIhouJyusin = True
            if "提出先：" in PDFtextItem and HoujinTIhouJyusin is True:
                PTKCTeisyutu = PDFtextItem.replace("提出先：", "")
            elif "利用者識別番号：" in PDFtextItem and HoujinTIhouJyusin is True:
                PTKCRiyouNo = PDFtextItem.replace("利用者識別番号：", "")
            elif "氏名又は名称：" in PDFtextItem and HoujinTIhouJyusin is True:
                PTKCName = PDFtextItem.replace("氏名又は名称：", "")
            elif "代表者等氏名：" in PDFtextItem and HoujinTIhouJyusin is True:
                PTKCDaihyouName = PDFtextItem.replace("代表者等氏名：", "")
            elif "受付番号：" in PDFtextItem and HoujinTIhouJyusin is True:
                PTKCUketukeNo = PDFtextItem.replace("受付番号：", "")
            elif "受付日時：" in PDFtextItem and HoujinTIhouJyusin is True:
                PTKCDateTime = PDFtextItem.replace("受付日時：", "")
            elif "種目：" in PDFtextItem and HoujinTIhouJyusin is True:
                PTKCSyumoku = PDFtextItem.replace("種目：", "")
            elif "事業年度自：" in PDFtextItem and HoujinTIhouJyusin is True:
                PTKCNendo = PDFtextItem.replace("事業年度自：", "")
            elif "事業年度至：" in PDFtextItem and HoujinTIhouJyusin is True:
                PTKCNendo = PTKCNendo + "-" + PDFtextItem.replace("事業年度至：", "")
            elif "税目：" in PDFtextItem and HoujinTIhouJyusin is True:
                try:
                    PTKCZeimoku
                    PTKCZeimoku2 = PDFtextItem.replace("税目：", "")
                except NameError:
                    PTKCZeimoku = PDFtextItem.replace("税目：", "")
            elif "申告の種類：" in PDFtextItem and HoujinTIhouJyusin is True:
                try:
                    PTKCSyurui
                    PTKCSyurui2 = PDFtextItem.replace("申告の種類：", "")
                except NameError:
                    PTKCSyurui = PDFtextItem.replace("申告の種類：", "")
            elif "所得金額又は欠損金額：" in PDFtextItem and HoujinTIhouJyusin is True:
                PTKCSyotokuKesson = PDFtextItem.replace("所得金額又は欠損金額：", "")
            elif "この申告による還付金額：" in PDFtextItem and HoujinTIhouJyusin is True:
                PTKCSinKanpu = PDFtextItem.replace("この申告による還付金額：", "")
            elif "欠損金又は災害損失金等の当期控除額：" in PDFtextItem and HoujinTIhouJyusin is True:
                PTKCKessonKoujyo = PDFtextItem.replace("欠損金又は災害損失金等の当期控除額：", "")
            elif "翌期へ繰り越す欠損金又は災害損失金：" in PDFtextItem and HoujinTIhouJyusin is True:
                PTKCKuriketu = PDFtextItem.replace("翌期へ繰り越す欠損金又は災害損失金：", "")
            elif "課税標準法人税額：" in PDFtextItem and HoujinTIhouJyusin is True:
                PTKCKazei = PDFtextItem.replace("課税標準法人税額：", "")
            elif "差引確定地方法人税額：" in PDFtextItem and HoujinTIhouJyusin is True:
                PTKCSasihikiTihou = PDFtextItem.replace("差引確定地方法人税額：", "")
                HoujinTIhouJyusin = False
                OutputList = [
                    SCode,
                    path_pdf.replace("/", "\\"),
                    "ページ情報無",
                    PTKCTeisyutu,
                    PTKCRiyouNo,
                    PTKCName,
                    PTKCDaihyouName,
                    PTKCUketukeNo,
                    PTKCDateTime,
                    PTKCSyumoku,
                    PTKCNendo,
                    PTKCZeimoku,
                    PTKCSyurui,
                    PTKCSyotokuKesson,
                    PTKCSinKanpu,
                    PTKCKessonKoujyo,
                    PTKCKuriketu,
                    PTKCZeimoku2,
                    PTKCSyurui2,
                    PTKCKazei,
                    PTKCSasihikiTihou,
                ]
                TKCListHTS.append(OutputList)
            # ----------------------------------------------------------------------
            if PDFtextItem == "【法人税・地方法人税の添付書類(PDF)の受信通知】":
                HoujinTIhouTenpu = True
            if "提出先：" in PDFtextItem and HoujinTIhouTenpu is True:
                PTKCTeisyutu = PDFtextItem.replace("提出先：", "")
            elif "利用者識別番号：" in PDFtextItem and HoujinTIhouTenpu is True:
                PTKCRiyouNo = PDFtextItem.replace("利用者識別番号：", "")
            elif "元の申告・申請書の受付番号：" in PDFtextItem and HoujinTIhouTenpu is True:
                PTKCMotoSin = PDFtextItem.replace("元の申告・申請書の受付番号：", "")
            elif "氏名又は名称：" in PDFtextItem and HoujinTIhouTenpu is True:
                PTKCName = PDFtextItem.replace("氏名又は名称：", "")
            elif "代表者等氏名：" in PDFtextItem and HoujinTIhouTenpu is True:
                PTKCDaihyouName = PDFtextItem.replace("代表者等氏名：", "")
            elif "受付番号：" in PDFtextItem and HoujinTIhouTenpu is True:
                PTKCUketukeNo = PDFtextItem.replace("受付番号：", "")
            elif "受付日時：" in PDFtextItem and HoujinTIhouTenpu is True:
                PTKCDateTime = PDFtextItem.replace("受付日時：", "")
                HoujinTIhouTenpu = False
                OutputList = [
                    SCode,
                    path_pdf.replace("/", "\\"),
                    "ページ情報無",
                    PTKCTeisyutu,
                    PTKCRiyouNo,
                    PTKCMotoSin,
                    PTKCName,
                    PTKCDaihyouName,
                    PTKCUketukeNo,
                    PTKCDateTime,
                ]
                TKCListHTPDF.append(OutputList)
            # ----------------------------------------------------------------------
            if PDFtextItem == "【消費税の受信通知】":
                SyouhizeiJyusin = True
            if "提出先：" in PDFtextItem and SyouhizeiJyusin is True:
                PTKCTeisyutu = PDFtextItem.replace("提出先：", "")
            elif "利用者識別番号：" in PDFtextItem and SyouhizeiJyusin is True:
                PTKCRiyouNo = PDFtextItem.replace("利用者識別番号：", "")
            elif "氏名又は名称：" in PDFtextItem and SyouhizeiJyusin is True:
                PTKCName = PDFtextItem.replace("氏名又は名称：", "")
            elif "代表者等氏名：" in PDFtextItem and SyouhizeiJyusin is True:
                PTKCDaihyouName = PDFtextItem.replace("代表者等氏名：", "")
            elif "受付番号：" in PDFtextItem and SyouhizeiJyusin is True:
                PTKCUketukeNo = PDFtextItem.replace("受付番号：", "")
            elif "受付日時：" in PDFtextItem and SyouhizeiJyusin is True:
                PTKCDateTime = PDFtextItem.replace("受付日時：", "")
            elif "種目：" in PDFtextItem and SyouhizeiJyusin is True:
                PTKCSyumoku = PDFtextItem.replace("種目：", "")
            elif "申告の種類：" in PDFtextItem and SyouhizeiJyusin is True:
                PTKCSyurui = PDFtextItem.replace("申告の種類：", "")
            elif "課税期間自：" in PDFtextItem and SyouhizeiJyusin is True:
                PTKCNendo = PDFtextItem.replace("課税期間自：", "")
            elif "課税期間至：" in PDFtextItem and SyouhizeiJyusin is True:
                PTKCNendo = PTKCNendo + "-" + PDFtextItem.replace("課税期間至：", "")
            elif "課税標準額：" in PDFtextItem and SyouhizeiJyusin is True:
                PTKCKazei = PDFtextItem.replace("課税標準額：", "")
            elif "消費税及び地方消費税の合計（納付又は還付）税額：" in PDFtextItem and SyouhizeiJyusin is True:
                PTKCGoukei = PDFtextItem.replace("消費税及び地方消費税の合計（納付又は還付）税額：", "")
                SyouhizeiJyusin = False
                OutputList = [
                    SCode,
                    path_pdf.replace("/", "\\"),
                    "ページ情報無",
                    PTKCTeisyutu,
                    PTKCRiyouNo,
                    PTKCName,
                    PTKCDaihyouName,
                    PTKCUketukeNo,
                    PTKCDateTime,
                    PTKCSyumoku,
                    PTKCSyurui,
                    PTKCNendo,
                    PTKCKazei,
                    PTKCGoukei,
                ]
                TKCListSyouhi.append(OutputList)
            # ----------------------------------------------------------------------
            if PDFtextItem == "【消費税の添付書類(PDF)の受信通知】":
                SyouhizeiJyusinPDF = True
            if "提出先：" in PDFtextItem and SyouhizeiJyusinPDF is True:
                PTKCTeisyutu = PDFtextItem.replace("提出先：", "")
            elif "利用者識別番号：" in PDFtextItem and SyouhizeiJyusinPDF is True:
                PTKCRiyouNo = PDFtextItem.replace("利用者識別番号：", "")
            elif "氏名又は名称：" in PDFtextItem and SyouhizeiJyusinPDF is True:
                PTKCName = PDFtextItem.replace("氏名又は名称：", "")
            elif "代表者等氏名：" in PDFtextItem and SyouhizeiJyusinPDF is True:
                PTKCDaihyouName = PDFtextItem.replace("代表者等氏名：", "")
            elif "受付番号：" in PDFtextItem and SyouhizeiJyusinPDF is True:
                PTKCUketukeNo = PDFtextItem.replace("受付番号：", "")
            elif "受付日時：" in PDFtextItem and SyouhizeiJyusinPDF is True:
                PTKCDateTime = PDFtextItem.replace("受付日時：", "")
                SyouhizeiJyusinPDF = False
                OutputList = [
                    SCode,
                    path_pdf.replace("/", "\\"),
                    "ページ情報無",
                    PTKCTeisyutu,
                    PTKCRiyouNo,
                    PTKCName,
                    PTKCDaihyouName,
                    PTKCUketukeNo,
                    PTKCDateTime,
                ]
                TKCListSyouhiPDF.append(OutputList)
            # ----------------------------------------------------------------------
            if PDFtextItem == "【都道府県民税･事業税･特別法人事業税の受付通知】":
                TdouhuJyusin = True
            if "納税者の氏名又は名称：" in PDFtextItem and TdouhuJyusin is True:
                PTKCDaihyouName = PDFtextItem.replace("納税者の氏名又は名称：", "")
            elif "発行元：" in PDFtextItem and TdouhuJyusin is True:
                PTKCHakkoumoto = PDFtextItem.replace("発行元：", "") + PDFtext[
                    Prow + 1
                ].replace(
                    "\u3000", ""
                )  # 2段なので1行下も結合
            elif "電話番号：" in PDFtextItem and TdouhuJyusin is True:
                PTKCTelNo = PDFtextItem.replace("電話番号：", "")
            elif "発行日時：" in PDFtextItem and TdouhuJyusin is True:
                PTKCHakkouDay = PDFtextItem.replace("発行日時：", "")
            elif "件名：" in PDFtextItem and TdouhuJyusin is True:
                PTKCTitle = PDFtextItem.replace("件名：", "")
            elif "(MUD002I)" in PDFtextItem and TdouhuJyusin is True:
                FRow = Prow + 1
            elif "受付日時：" in PDFtextItem and TdouhuJyusin is True:
                ERow = Prow
                PTKCUketukeDay = PDFtextItem.replace("受付日時：", "")
            elif "受付番号：" in PDFtextItem and TdouhuJyusin is True:
                PTKCUketukeNo = PDFtextItem.replace("受付番号：", "")
            elif "手続名：" in PDFtextItem and TdouhuJyusin is True:
                PTKCTetutuki = PTKCNendo + "-" + PDFtextItem.replace("手続名：", "")
            elif "事業年度(期別)：" in PDFtextItem and TdouhuJyusin is True:
                PTKCNendo = PDFtextItem.replace("事業年度(期別)：", "")
            elif "提出先：" in PDFtextItem and TdouhuJyusin is True:
                PTKCTeisyutu = PDFtextItem.replace("提出先：", "")
                # メッセージ本文内の金額一覧を取得し文字列に変換---------------------------------------
                if not FRow == 0 and not ERow == 0:
                    TKCSPDList = []
                    for yy in range(FRow, ERow):
                        if "円" in PDFtext[yy]:
                            TKCSPDList.append(
                                PDFtext[yy].replace("\u3000", "").replace(" ", "")
                            )
                    TKCSPDstr = "\n".join(TKCSPDList)
                    FRow = 0
                    ERow = 0
                else:
                    TKCSPDstr = ""
                TdouhuJyusin = False
                OutputList = [
                    SCode,
                    path_pdf.replace("/", "\\"),
                    "ページ情報無",
                    PTKCDaihyouName,
                    PTKCHakkoumoto,
                    PTKCTelNo,
                    PTKCHakkouDay,
                    PTKCTitle,
                    TKCSPDstr,
                    PTKCUketukeDay,
                    PTKCUketukeNo,
                    PTKCTetutuki,
                    PTKCNendo,
                    PTKCTeisyutu,
                ]
                TKCListTodouhu.append(OutputList)
            # ----------------------------------------------------------------------
            if PDFtextItem == "【市町村民税の受付通知】":
                SityouJyusin = True
            if "納税者の氏名又は名称：" in PDFtextItem and SityouJyusin is True:
                PTKCDaihyouName = PDFtextItem.replace("納税者の氏名又は名称：", "")
            elif "発行元：" in PDFtextItem and SityouJyusin is True:
                PTKCHakkoumoto = PDFtextItem.replace("発行元：", "") + PDFtext[
                    Prow + 1
                ].replace(
                    "\u3000", ""
                )  # 2段なので1行下も結合
            elif "電話番号：" in PDFtextItem and SityouJyusin is True:
                PTKCTelNo = PDFtextItem.replace("電話番号：", "")
            elif "発行日時：" in PDFtextItem and SityouJyusin is True:
                PTKCHakkouDay = PDFtextItem.replace("発行日時：", "")
            elif "件名：" in PDFtextItem and SityouJyusin is True:
                PTKCTitle = PDFtextItem.replace("件名：", "")
            elif "(MUD002I)" in PDFtextItem and SityouJyusin is True:
                FRow = Prow + 1
            elif "受付日時：" in PDFtextItem and SityouJyusin is True:
                ERow = Prow
                PTKCUketukeDay = PDFtextItem.replace("受付日時：", "")
            elif "受付番号：" in PDFtextItem and SityouJyusin is True:
                PTKCUketukeNo = PDFtextItem.replace("受付番号：", "")
            elif "手続名：" in PDFtextItem and SityouJyusin is True:
                PTKCTetutuki = PTKCNendo + "-" + PDFtextItem.replace("手続名：", "")
            elif "事業年度(期別)：" in PDFtextItem and SityouJyusin is True:
                PTKCNendo = PDFtextItem.replace("事業年度(期別)：", "")
            elif "提出先：" in PDFtextItem and SityouJyusin is True:
                PTKCTeisyutu = PDFtextItem.replace("提出先：", "")
                # メッセージ本文内の金額一覧を取得し文字列に変換---------------------------------------
                if not FRow == 0 and not ERow == 0:
                    TKCSPDList = []
                    for yy in range(FRow, ERow):
                        if "円" in PDFtext[yy]:
                            TKCSPDList.append(
                                PDFtext[yy].replace("\u3000", "").replace(" ", "")
                            )
                    TKCSPDstr = "\n".join(TKCSPDList)
                    FRow = 0
                    ERow = 0
                else:
                    TKCSPDstr = ""
                SityouJyusin = False
                OutputList = [
                    SCode,
                    path_pdf.replace("/", "\\"),
                    "ページ情報無",
                    PTKCDaihyouName,
                    PTKCHakkoumoto,
                    PTKCTelNo,
                    PTKCHakkouDay,
                    PTKCTitle,
                    TKCSPDstr,
                    PTKCUketukeDay,
                    PTKCUketukeNo,
                    PTKCTetutuki,
                    PTKCNendo,
                    PTKCTeisyutu,
                ]
                TKCListSityou.append(OutputList)
            # ----------------------------------------------------------------------
        Prow += 1


# ----------------------------------------------------------------------------------------------
def CSVIndexSort(
    SCode,
    path_pdf,
    SinkokuCSVList,
    SinkokuCSV2List,
    SinkokuCSV3List,
    SinkokuCSV4List,
    SyotokuCSVList,
    SyotokuCSV2List,
    SyotokuCSV3List,
    SyotokuCSV4List,
    SyouhiCSVList,
    SyouhiCSV2List,
    SyouhiCSV3List,
    SyouhiCyukanCSVList,
    HoujinCSVList,
    YoteiCSVList,
    SyoukyakuCSVList,
    SyoukyakuCSV2List,
    ZouyoCSVList,
    ZaisanCSVList,
    SinkokuUkeCSVList,
    TKCListSinsei,
    TKCListHTS,
    TKCListHTPDF,
    TKCListSyouhi,
    TKCListSyouhiPDF,
    TKCListTodouhu,
    TKCListSityou,
    ImageCSVList,
    CSVBadList,
    SinkokuCSV,
    SinkokuCSV2,
    SinkokuCSV3,
    SinkokuCSV4,
    SyotokuCSV,
    SyotokuCSV2,
    SyotokuCSV3,
    SyotokuCSV4,
    SyouhiCSV,
    SyouhiCSV2,
    SyouhiCSV3,
    SyouhiCyukanCSV,
    HoujinCSV,
    YoteiCSV,
    SyoukyakuCSV,
    SyoukyakuCSV2,
    ZouyoCSV,
    ZaisanCSV,
    SinkokuUkeCSV,
    ImageCSV,
):
    # PDFから抽出したリストと形式があわないので、税目リストを行列入替---------------------------
    SinkokuCSV = SinkokuCSV.transpose()  # 行列入替
    SinkokuCSV2 = SinkokuCSV2.transpose()  # 行列入替
    SinkokuCSV3 = SinkokuCSV3.transpose()  # 行列入替
    SinkokuCSV4 = SinkokuCSV4.transpose()  # 行列入替
    SyotokuCSV = SyotokuCSV.transpose()  # 行列入替
    SyotokuCSV2 = SyotokuCSV2.transpose()  # 行列入替
    SyotokuCSV3 = SyotokuCSV3.transpose()
    SyotokuCSV4 = SyotokuCSV4.transpose()  # 行列入替
    SyouhiCSV = SyouhiCSV.transpose()  # 行列入替
    SyouhiCSV2 = SyouhiCSV2.transpose()  # 行列入替
    SyouhiCSV3 = SyouhiCSV3.transpose()  # 行列入替
    SyouhiCyukanCSV = SyouhiCyukanCSV.transpose()  # 行列入替
    HoujinCSV = HoujinCSV.transpose()  # 行列入替
    YoteiCSV = YoteiCSV.transpose()  # 行列入替
    SyoukyakuCSV = SyoukyakuCSV.transpose()  # 行列入替
    SyoukyakuCSV2 = SyoukyakuCSV2.transpose()  # 行列入替
    ZouyoCSV = ZouyoCSV.transpose()  # 行列入替
    ZaisanCSV = ZaisanCSV.transpose()  # 行列入替
    SinkokuUkeCSV = SinkokuUkeCSV.transpose()  # 行列入替
    ImageCSV = ImageCSV.transpose()  # 行列入替
    # ------------------------------------------------------------------------------------
    fp = open(path_pdf, "rb")  # PDFファイルを読み込み
    parser = PDFParser(fp)  # PDFperserを作成。
    document = PDFDocument(parser)  # PDFperserを格納。
    num_pages = 0  # ページ数格納変数を初期化
    num_pagesList = []
    for page in PDFPage.create_pages(document):  # ページオブジェ分ループ
        num_pages += 1  # ページ数カウント
        num_pagesList.append(num_pages - 1)
    print(num_pages)  # ページ数確認
    # ------------------------------------------------------------------------------------
    try:
        for y in range(num_pages):
            # TX = extract_text(path_pdf,page_numbers=y,codec='utf-8') テキストのみ取得できる
            # print(TX)
            PageVol = str(y + 1)
            TO = True  # TimeOut判定変数
            # TimeOutを加味したPDFRead処理TimeOut設定時間はContextTimeOut.pyにコンテキストで設定する
            TKCFlag = False  # TKC出力PDF判定フラグ
            try:
                # 第三引数に'stream'を渡すと表外の値を抽出できる
                tables = CTO.camelotTimeOut(path_pdf, PageVol, "")
                PDFdf = tables[0].df  # PDFテーブルをdf化
            except:  # TimeOut処理を記述
                TO = False  # TimeOut判定変数
                pass
            # 検索キー一致で種目分岐--------------------------------------
            Notext = False  # テキスト判定フラグ
            try:
                # PDFtext = extract_text(path_pdf,page_numbers=y,maxpages=1)
                PDFtext = extract_text(
                    path_pdf, page_numbers=num_pagesList, maxpages=num_pages
                )
                print(PDFtext)
                PDFtext = (
                    PDFtext.replace("\u3000", "").replace(" ", "").split("\n")
                )  # 改行コードでSplit
                print(PDFtext)
                for PDFtextItem in PDFtext:
                    if "国税の電子申請・届出完了報告書" in PDFtextItem:
                        PDFFlag = "国税の電子申請・届出完了報告書"
                        TKCFlag = True
                        break
                    elif "法人税・地方法人税・消費税の電子申告完了報告書" in PDFtextItem:
                        PDFFlag = "法人税・地方法人税・消費税の電子申告完了報告書"
                        TKCFlag = True
                        break
            except:
                Notext = True  # テキスト判定フラグ
            # ---------------------------------------------------------
            if TO is not False:
                t_count = len(tables)  # PDFのテーブル数を格納
                if t_count >= 2:
                    # 第三引数に'stream'を渡すと表外の値を抽出できる
                    Subtables = CTO.camelotTimeOut(path_pdf, PageVol, "stream")
                    SubPDFdf = Subtables[0].df  # PDFテーブルをdf化
                    print(SubPDFdf)
                    for x in range(t_count):  # PDFテーブル数分ループ
                        PDFdf = tables[x].df  # PDFテーブルをdf化
                        print(PDFdf)
                        dfIndexdata = PDFdf.iloc[:, 0]  # PDFのインデックス
                        # print(dfIndexdata)
                        if TKCFlag is True:
                            OutputList = []
                            # 表のインデックスを元に値を格納-----------------------------------------------------------
                            ReadActionTKC(
                                SCode,
                                path_pdf,
                                PDFFlag,
                                y,
                                TKCListSinsei,
                                TKCListHTS,
                                TKCListHTPDF,
                                TKCListSyouhi,
                                TKCListSyouhiPDF,
                                TKCListTodouhu,
                                TKCListSityou,
                                PDFtext,
                            )
                            break
                            # --------------------------------------------------------------------------------------
                        else:
                            PDFFlag = PDFSetting(
                                dfIndexdata,
                                SinkokuCSV,
                                SinkokuCSV2,
                                SinkokuCSV3,
                                SinkokuCSV4,
                                SyotokuCSV,
                                SyotokuCSV2,
                                SyotokuCSV3,
                                SyotokuCSV4,
                                SyouhiCSV,
                                SyouhiCSV2,
                                SyouhiCSV3,
                                SyouhiCyukanCSV,
                                YoteiCSV,
                                HoujinCSV,
                                SyoukyakuCSV,
                                SyoukyakuCSV2,
                                ZouyoCSV,
                                ZaisanCSV,
                                SinkokuUkeCSV,
                                ImageCSV,
                            )  # PDFから抽出した表のインデックスを元に表のタイプを判別
                            PDFdfRow = np.array(PDFdf).shape[0]  # 配列行数取得
                            OutputList = []
                            # 表のインデックスを元に値を格納-----------------------------------------------------------
                            ReadAction(
                                SCode,
                                path_pdf,
                                PDFFlag,
                                y,
                                PDFdfRow,
                                PDFdf,
                                SinkokuCSVList,
                                SinkokuCSV2List,
                                SinkokuCSV3List,
                                SinkokuCSV4List,
                                SyouhiCSVList,
                                SyouhiCSV2List,
                                SyouhiCSV3List,
                                SyouhiCyukanCSVList,
                                SyotokuCSVList,
                                SyotokuCSV2List,
                                SyotokuCSV3List,
                                SyotokuCSV4List,
                                YoteiCSVList,
                                SyoukyakuCSVList,
                                SyoukyakuCSV2List,
                                ZouyoCSVList,
                                ZaisanCSVList,
                                SinkokuUkeCSVList,
                                HoujinCSVList,
                                ImageCSVList,
                                CSVBadList,
                                SubPDFdf,
                            )
                            # --------------------------------------------------------------------------------------
                else:
                    for x in range(t_count):  # PDFテーブル数分ループ
                        PDFdf = tables[x].df  # PDFテーブルをdf化
                        print(PDFdf)
                        dfIndexdata = PDFdf.iloc[:, 0]  # PDFのインデックス
                        # print(dfIndexdata)
                        PDFFlag = PDFSetting(
                            dfIndexdata,
                            SinkokuCSV,
                            SinkokuCSV2,
                            SinkokuCSV3,
                            SinkokuCSV4,
                            SyotokuCSV,
                            SyotokuCSV2,
                            SyotokuCSV3,
                            SyotokuCSV4,
                            SyouhiCSV,
                            SyouhiCSV2,
                            SyouhiCSV3,
                            SyouhiCyukanCSV,
                            YoteiCSV,
                            HoujinCSV,
                            SyoukyakuCSV,
                            SyoukyakuCSV2,
                            ZouyoCSV,
                            ZaisanCSV,
                            SinkokuUkeCSV,
                            ImageCSV,
                        )  # PDFから抽出した表のインデックスを元に表のタイプを判別
                        PDFdfRow = np.array(PDFdf).shape[0]  # 配列行数取得
                        OutputList = []
                        SubPDFdf = []
                        # 表のインデックスを元に値を格納-----------------------------------------------------------
                        ReadAction(
                            SCode,
                            path_pdf,
                            PDFFlag,
                            y,
                            PDFdfRow,
                            PDFdf,
                            SinkokuCSVList,
                            SinkokuCSV2List,
                            SinkokuCSV3List,
                            SinkokuCSV4List,
                            SyouhiCSVList,
                            SyouhiCSV2List,
                            SyouhiCSV3List,
                            SyouhiCyukanCSVList,
                            SyotokuCSVList,
                            SyotokuCSV2List,
                            SyotokuCSV3List,
                            SyotokuCSV4List,
                            YoteiCSVList,
                            SyoukyakuCSVList,
                            SyoukyakuCSV2List,
                            ZouyoCSVList,
                            ZaisanCSVList,
                            SinkokuUkeCSVList,
                            HoujinCSVList,
                            ImageCSVList,
                            CSVBadList,
                            SubPDFdf,
                        )
                        # --------------------------------------------------------------------------------------
            else:
                if TKCFlag is True:
                    OutputList = []
                    # 表のインデックスを元に値を格納-----------------------------------------------------------
                    ReadActionTKC(
                        SCode,
                        path_pdf,
                        PDFFlag,
                        y,
                        TKCListSinsei,
                        TKCListHTS,
                        TKCListHTPDF,
                        TKCListSyouhi,
                        TKCListSyouhiPDF,
                        TKCListTodouhu,
                        TKCListSityou,
                        PDFtext,
                    )
                    break
                    # --------------------------------------------------------------------------------------
                elif Notext is True:
                    logger.debug(path_pdf + "_" + str(y + 1) + "ページ目PDFテキスト情報なし")
                    OutputList = [
                        SCode,
                        path_pdf.replace("/", "\\"),
                        str(y + 1) + "ページ目PDFテキスト情報なし",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                    ]
                    CSVBadList.append(OutputList)
                else:
                    logger.debug(path_pdf + "_" + str(y + 1) + "ページ目タイムアウトエラー")
                    OutputList = [
                        SCode,
                        path_pdf.replace("/", "\\"),
                        str(y + 1) + "ページ目タイムアウトエラー",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                        "",
                    ]
                    CSVBadList.append(OutputList)
                    print("タイムアウトエラー")
    except Exception as e:
        if TO is not False:
            logger.debug(path_pdf + "_" + str(y + 1) + "ページ目取得失敗")
            OutputList = [
                SCode,
                path_pdf.replace("/", "\\"),
                str(y + 1) + "ページ目取得失敗",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
            ]
            print(e)
            CSVBadList.append(OutputList)


# ----------------------------------------------------------------------------------------
def PDFRead(URL):
    MeUrl = os.getcwd().replace("\\", "/")  # 自分のパス
    # 各税目のインデックスリストを加工して格納------------------------------------------------
    SinkokuCSV = FCSV.CsvReadHeaderless(
        MeUrl + "/RPAPhoto/PDFReadForList/確定申告.CSV"
    )  # 内国法人確定申告のインデックスリスト
    SinkokuCSV2 = FCSV.CsvReadHeaderless(
        MeUrl + "/RPAPhoto/PDFReadForList/確定申告2.CSV"
    )  # 内国法人確定申告のインデックスリスト
    SinkokuCSV3 = FCSV.CsvReadHeaderless(
        MeUrl + "/RPAPhoto/PDFReadForList/確定申告3.CSV"
    )  # 内国法人確定申告のインデックスリスト
    SinkokuCSV4 = FCSV.CsvReadHeaderless(
        MeUrl + "/RPAPhoto/PDFReadForList/確定申告4.CSV"
    )  # 内国法人確定申告のインデックスリスト
    SyotokuCSV = FCSV.CsvReadHeaderless(
        MeUrl + "/RPAPhoto/PDFReadForList/所得税.CSV"
    )  # 所得税のインデックスリスト
    SyotokuCSV2 = FCSV.CsvReadHeaderless(
        MeUrl + "/RPAPhoto/PDFReadForList/所得税2.CSV"
    )  # 所得税のインデックスリスト
    SyotokuCSV3 = FCSV.CsvReadHeaderless(
        MeUrl + "/RPAPhoto/PDFReadForList/所得税3.CSV"
    )  # 所得税のインデックスリスト
    SyotokuCSV4 = FCSV.CsvReadHeaderless(
        MeUrl + "/RPAPhoto/PDFReadForList/所得税4.CSV"
    )  # 所得税のインデックスリスト
    SyouhiCSV = FCSV.CsvReadHeaderless(
        MeUrl + "/RPAPhoto/PDFReadForList/消費税.CSV"
    )  # 消費税のインデックスリスト
    SyouhiCSV2 = FCSV.CsvReadHeaderless(
        MeUrl + "/RPAPhoto/PDFReadForList/消費税2.CSV"
    )  # 消費税のインデックスリスト
    SyouhiCSV3 = FCSV.CsvReadHeaderless(
        MeUrl + "/RPAPhoto/PDFReadForList/消費税3.CSV"
    )  # 消費税のインデックスリスト
    SyouhiCyukanCSV = FCSV.CsvReadHeaderless(
        MeUrl + "/RPAPhoto/PDFReadForList/消費税中間申告.CSV"
    )  # 消費税のインデックスリスト
    HoujinCSV = FCSV.CsvReadHeaderless(
        MeUrl + "/RPAPhoto/PDFReadForList/法人税.CSV"
    )  # 法人税のインデックスリスト
    YoteiCSV = FCSV.CsvReadHeaderless(
        MeUrl + "/RPAPhoto/PDFReadForList/予定申告.CSV"
    )  # 予定申告のインデックスリスト
    SyoukyakuCSV = FCSV.CsvReadHeaderless(
        MeUrl + "/RPAPhoto/PDFReadForList/償却資産.CSV"
    )  # 償却資産のインデックスリスト
    SyoukyakuCSV2 = FCSV.CsvReadHeaderless(
        MeUrl + "/RPAPhoto/PDFReadForList/償却資産2.CSV"
    )  # 償却資産のインデックスリスト
    ZouyoCSV = FCSV.CsvReadHeaderless(
        MeUrl + "/RPAPhoto/PDFReadForList/贈与税.CSV"
    )  # 償却資産のインデックスリスト
    ZaisanCSV = FCSV.CsvReadHeaderless(
        MeUrl + "/RPAPhoto/PDFReadForList/財産債務調書.CSV"
    )  # 償却資産のインデックスリスト
    SinkokuUkeCSV = FCSV.CsvReadHeaderless(
        MeUrl + "/RPAPhoto/PDFReadForList/申告受付通知.CSV"
    )  # 償却資産のインデックスリスト
    ImageCSV = FCSV.CsvReadHeaderless(
        MeUrl + "/RPAPhoto/PDFReadForList/イメージ添付書類.CSV"
    )  # 償却資産のインデックスリスト
    # ------------------------------------------------------------------------------------
    SinkokuCSVList = []  # 成功リスト初期化
    SinkokuCSV2List = []  # 成功リスト初期化
    SinkokuCSV3List = []  # 成功リスト初期化
    SinkokuCSV4List = []  # 成功リスト初期化
    SyotokuCSVList = []  # 成功リスト初期化
    SyotokuCSV2List = []  # 成功リスト初期化
    SyotokuCSV3List = []  # 成功リスト初期化
    SyotokuCSV4List = []  # 成功リスト初期化
    SyouhiCSVList = []  # 成功リスト初期化
    SyouhiCSV2List = []  # 成功リスト初期化
    SyouhiCSV3List = []  # 成功リスト初期化
    SyouhiCyukanCSVList = []
    HoujinCSVList = []  # 成功リスト初期化
    YoteiCSVList = []  # 成功リスト初期化
    SyoukyakuCSVList = []  # 成功リスト初期化
    SyoukyakuCSV2List = []  # 成功リスト初期化
    ZouyoCSVList = []  # 成功リスト初期化
    ZaisanCSVList = []  # 成功リスト初期化
    SinkokuUkeCSVList = []
    TKCListSinsei = []  # 成功リスト初期化
    TKCListHTS = []
    TKCListHTPDF = []
    TKCListSyouhi = []
    TKCListSyouhiPDF = []
    TKCListTodouhu = []
    TKCListSityou = []
    ImageCSVList = []
    CSVBadList = []  # 失敗リスト初期化
    # ------------------------------------------------------------------------------------
    # FCSV.CsvSaveEnc(URL.replace("\\","/") + "/PDFDataSuccess.csv",CSVList,"shiftjis")
    dir_List = SerchdirFolders(URL)  # 指定URL配下のサブフォルダを取得
    print(dir_List)
    for dir_ListItem in dir_List:
        Serchd = dir_ListItem[0] + "\\" + dir_ListItem[1]  # サブフォルダ名
        dir_Files = SerchdirFiles(Serchd)  # サブフォルダ配下のサブフォルダを取得
        print(dir_Files)
        for dir_FilesItem in dir_Files:
            if Serchd == dir_FilesItem[0]:
                dif = dir_FilesItem[0] + "\\" + dir_FilesItem[1]  # ファイル名
                dirsplit = dir_FilesItem[1].split("_")
                dirsplit = dirsplit[0].split(".")
                SCode = dirsplit[0]
                try:
                    if ".xdw" not in dif:  # Docuファイルじゃなければ
                        path_pdf = dif.replace("\\", "/")  # PDFパスを代入
                        CSVIndexSort(
                            SCode,
                            path_pdf,
                            SinkokuCSVList,
                            SinkokuCSV2List,
                            SinkokuCSV3List,
                            SinkokuCSV4List,
                            SyotokuCSVList,
                            SyotokuCSV2List,
                            SyotokuCSV3List,
                            SyotokuCSV4List,
                            SyouhiCSVList,
                            SyouhiCSV2List,
                            SyouhiCSV3List,
                            SyouhiCyukanCSVList,
                            HoujinCSVList,
                            YoteiCSVList,
                            SyoukyakuCSVList,
                            SyoukyakuCSV2List,
                            ZouyoCSVList,
                            ZaisanCSVList,
                            SinkokuUkeCSVList,
                            TKCListSinsei,
                            TKCListHTS,
                            TKCListHTPDF,
                            TKCListSyouhi,
                            TKCListSyouhiPDF,
                            TKCListTodouhu,
                            TKCListSityou,
                            ImageCSVList,
                            CSVBadList,
                            SinkokuCSV[1],
                            SinkokuCSV2[1],
                            SinkokuCSV3[1],
                            SinkokuCSV4[1],
                            SyotokuCSV[1],
                            SyotokuCSV2[1],
                            SyotokuCSV3[1],
                            SyotokuCSV4[1],
                            SyouhiCSV[1],
                            SyouhiCSV2[1],
                            SyouhiCSV3[1],
                            SyouhiCyukanCSV[1],
                            HoujinCSV[1],
                            YoteiCSV[1],
                            SyoukyakuCSV[1],
                            SyoukyakuCSV2[1],
                            ZouyoCSV[1],
                            ZaisanCSV[1],
                            SinkokuUkeCSV[1],
                            ImageCSV[1],
                        )
                    else:
                        print("xdw")
                except Exception as e:
                    print(e)
    # ------------------------------------------------------------------------------------
    ListURL = FC.CreFol("//Sv05121a/e/電子ファイル/メッセージボックス/TEST", "受信通知CSV")
    for f in os.listdir(ListURL):
        if os.path.isfile(os.path.join(ListURL, f)):
            if ".csv" in f:
                try:
                    # os.remove(os.path.join(ListURL, f))
                    osurl = ListURL + "/" + f
                    os.remove(osurl)
                except:
                    print("OSREMOVEError")
    if not np.array(SinkokuCSVList).shape[0] == 0:
        FCSV.CsvSaveEnc(
            ListURL + "/内国法人確定申告受信通知リスト.csv",
            SinkokuCSVList,
            "cp932",
            [
                "コード",
                "URL",
                "ページ",
                "手続名",
                "氏名又は名称",
                "受付日時",
                "種目",
                "事業年度",
                "税目",
                "申告の種類",
                "所得金額又は欠損金額",
                "差引確定法人税額",
                "欠損金又は災害損失金等の当期控除額",
                "翌期へ繰り越す欠損金又は災害損失金",
                "税目2",
                "申告の種類2",
                "課税標準法人税額",
                "差引確定地方法人税額",
            ],
        )
    if not np.array(SinkokuCSV2List).shape[0] == 0:
        FCSV.CsvSaveEnc(
            ListURL + "/内国法人確定申告受信通知リスト2.csv",
            SinkokuCSV2List,
            "cp932",
            [
                "コード",
                "URL",
                "ページ",
                "手続名",
                "氏名又は名称",
                "受付日時",
                "種目",
                "事業年度",
                "税目",
                "申告の種類",
                "所得金額又は欠損金額",
                "この申告による還付金額",
                "欠損金又は災害損失金等の当期控除額",
                "翌期へ繰り越す欠損金又は災害損失金",
                "税目2",
                "申告の種類2",
                "課税標準法人税額",
                "この申告による還付金額2",
            ],
        )
    if not np.array(SinkokuCSV3List).shape[0] == 0:
        FCSV.CsvSaveEnc(
            ListURL + "/内国法人確定申告受信通知リスト3.csv",
            SinkokuCSV3List,
            "cp932",
            [
                "コード",
                "URL",
                "ページ",
                "手続名",
                "氏名又は名称",
                "受付日時",
                "種目",
                "事業年度",
                "税目",
                "申告の種類",
                "所得金額又は欠損金額",
                "この申告による還付金額",
                "欠損金又は災害損失金等の当期控除額",
                "翌期へ繰り越す欠損金又は災害損失金",
                "税目2",
                "申告の種類2",
                "課税標準法人税額",
                "差引確定地方法人税額",
            ],
        )
    if not np.array(SinkokuCSV4List).shape[0] == 0:
        FCSV.CsvSaveEnc(
            ListURL + "/内国法人確定申告受信通知リスト4.csv",
            SinkokuCSV4List,
            "cp932",
            [
                "コード",
                "URL",
                "ページ",
                "手続名",
                "氏名又は名称",
                "受付日時",
                "種目",
                "事業年度",
                "税目",
                "申告の種類",
                "所得金額又は欠損金額",
                "差引確定法人税額",
                "欠損金又は災害損失金等の当期控除額",
                "翌期へ繰り越す欠損金又は災害損失金",
                "税目2",
                "申告の種類2",
                "課税標準法人税額",
                "差引確定地方法人税額",
            ],
        )
    if not np.array(SyotokuCSVList).shape[0] == 0:
        FCSV.CsvSaveEnc(
            ListURL + "/所得税受信通知リスト.csv",
            SyotokuCSVList,
            "cp932",
            [
                "コード",
                "URL",
                "ページ",
                "手続名",
                "氏名又は名称",
                "受付日時",
                "年分",
                "種目",
                "所得金額",
                "納める税金",
                "還付される税金",
            ],
        )

    if not np.array(SyotokuCSV2List).shape[0] == 0:
        FCSV.CsvSaveEnc(
            ListURL + "/所得税2受信通知リスト.csv",
            SyotokuCSV2List,
            "cp932",
            [
                "コード",
                "URL",
                "ページ",
                "氏名又は名称",
                "受付日時",
                "年分",
                "種目",
                "所得金額",
                "納める税金",
                "還付される税金",
                "「所得金額」欄について",
            ],
        )
    if not np.array(SyotokuCSV3List).shape[0] == 0:
        FCSV.CsvSaveEnc(
            ListURL + "/所得税3受信通知リスト.csv",
            SyotokuCSV3List,
            "cp932",
            [
                "コード",
                "URL",
                "ページ",
                "手続名",
                "氏名又は名称",
                "受付日時",
                "年分",
                "種目",
                "所得金額",
                "納める税金",
                "還付される税金",
                "「所得金額」欄について",
            ],
        )
    if not np.array(SyotokuCSV4List).shape[0] == 0:
        FCSV.CsvSaveEnc(
            ListURL + "/所得税4受信通知リスト.csv",
            SyotokuCSV4List,
            "cp932",
            [
                "コード",
                "URL",
                "ページ",
                "手続名",
                "氏名又は名称",
                "受付日時",
                "年分",
                "種目",
                "所得金額",
                "納める税金",
                "還付される税金",
                "「所得金額」欄について",
            ],
        )

    if not np.array(SyouhiCSVList).shape[0] == 0:
        FCSV.CsvSaveEnc(
            ListURL + "/消費税受信通知リスト.csv",
            SyouhiCSVList,
            "cp932",
            [
                "コード",
                "URL",
                "ページ",
                "手続名",
                "氏名又は名称",
                "受付日時",
                "種目",
                "申告の種類",
                "課税標準額",
                "消費税及び地方消費税の合計",
                "課税期間",
            ],
        )
    if not np.array(SyouhiCSV2List).shape[0] == 0:
        FCSV.CsvSaveEnc(
            ListURL + "/消費税2受信通知リスト.csv",
            SyouhiCSV2List,
            "cp932",
            [
                "コード",
                "URL",
                "ページ",
                "手続名",
                "氏名又は名称",
                "受付日時",
                "種目",
                "課税標準額",
                "消費税及び地方消費税の合計",
                "課税期間",
            ],
        )

    if not np.array(SyouhiCSV3List).shape[0] == 0:
        FCSV.CsvSaveEnc(
            ListURL + "/消費税2受信通知リスト.csv",
            SyouhiCSV3List,
            "cp932",
            [
                "コード",
                "URL",
                "ページ",
                "氏名又は名称",
                "受付日時",
                "種目",
                "課税標準額",
                "消費税及び地方消費税の合計",
                "課税期間",
            ],
        )

    if not np.array(SyouhiCyukanCSVList).shape[0] == 0:
        FCSV.CsvSaveEnc(
            ListURL + "/消費税中間申告受信通知リスト.csv",
            SyouhiCyukanCSVList,
            "cp932",
            [
                "コード",
                "URL",
                "ページ",
                "手続名",
                "氏名又は名称",
                "受付日時",
                "種目",
                "消費税及び地方消費税の合計",
                "課税期間",
            ],
        )

    if not np.array(HoujinCSVList).shape[0] == 0:
        FCSV.CsvSaveEnc(
            ListURL + "/法人税受信通知リスト.csv",
            HoujinCSVList,
            "cp932",
            [
                "コード",
                "URL",
                "ページ",
                "手続名",
                "氏名又は名称",
                "発行元名",
                "発行元所属名",
                "受付日時",
                "提出先",
                "年度・期別",
                "納税者氏名",
                "表外表示金額",
            ],
        )
    if not np.array(YoteiCSVList).shape[0] == 0:
        FCSV.CsvSaveEnc(
            ListURL + "/予定納税受信通知リスト.csv",
            YoteiCSVList,
            "cp932",
            [
                "コード",
                "URL",
                "ページ",
                "手続名",
                "氏名又は名称",
                "受付日時",
                "種目",
                "事業年度",
                "税目",
                "納付すべき法人税額",
                "税目2",
                "納付すべき地方法人税額",
            ],
        )
    if not np.array(SyoukyakuCSVList).shape[0] == 0:
        FCSV.CsvSaveEnc(
            ListURL + "/償却資産受信通知リスト.csv",
            SyoukyakuCSVList,
            "cp932",
            [
                "コード",
                "URL",
                "ページ",
                "手続名",
                "氏名又は名称",
                "発行元名",
                "発行元所属名",
                "受付日時",
                "提出先",
                "年度・期別",
                "課税所在地",
            ],
        )
    if not np.array(SyoukyakuCSV2List).shape[0] == 0:
        FCSV.CsvSaveEnc(
            ListURL + "/償却資産2受信通知リスト.csv",
            SyoukyakuCSV2List,
            "cp932",
            [
                "コード",
                "URL",
                "ページ",
                "手続名",
                "氏名又は名称",
                "発行元名",
                "受付日時",
                "提出先",
                "年度・期別",
                "課税所在地",
            ],
        )
    if not np.array(ZouyoCSVList).shape[0] == 0:
        FCSV.CsvSaveEnc(
            ListURL + "/贈与税受信通知リスト.csv",
            ZouyoCSVList,
            "cp932",
            [
                "コード",
                "URL",
                "ページ",
                "手続名",
                "氏名又は名称",
                "受付日時",
                "年分",
                "種目",
                "課税価格の合計額",
                "申告期限までに納付すべき税額",
            ],
        )
    if not np.array(ZaisanCSVList).shape[0] == 0:
        FCSV.CsvSaveEnc(
            ListURL + "/贈与税受信通知リスト.csv",
            ZaisanCSVList,
            "cp932",
            ["コード", "URL", "ページ", "手続名", "氏名又は名称", "受付日時", "種目"],
        )
    if not np.array(SinkokuUkeCSVList).shape[0] == 0:
        FCSV.CsvSaveEnc(
            ListURL + "/申告受付通知リスト.csv",
            SinkokuUkeCSVList,
            "cp932",
            [
                "コード",
                "URL",
                "ページ",
                "手続名",
                "氏名又は名称",
                "発行元名",
                "発行元所属名",
                "発行元電話番号",
                "受付日時",
                "提出先",
                "年度・期別",
                "課税所在地",
            ],
        )
    if not np.array(TKCListSinsei).shape[0] == 0:
        FCSV.CsvSaveEnc(
            ListURL + "/TKC受信通知リスト.csv",
            TKCListSinsei,
            "cp932",
            [
                "コード",
                "URL",
                "ページ",
                "提出先",
                "利用者識別番号",
                "氏名又は名称",
                "代表者等氏名",
                "受付番号",
                "受付日時",
                "種目",
            ],
        )
    if not np.array(TKCListHTS).shape[0] == 0:
        FCSV.CsvSaveEnc(
            ListURL + "/TKC法人税の受信通知リスト.csv",
            TKCListHTS,
            "cp932",
            [
                "コード",
                "URL",
                "ページ",
                "提出先",
                "利用者識別番号",
                "氏名又は名称",
                "代表者等氏名",
                "受付番号",
                "受付日時",
                "種目",
                "事業年度",
                "税目",
                "申告の種類",
                "所得金額又は欠損金額",
                "この申告による還付金額",
                "欠損金又は災害損失金等の当期控除額",
                "翌期へ繰り越す欠損金又は災害損失金",
                "税目2",
                "申告の種類2",
                "課税標準法人税額",
                "差引確定地方法人税額",
            ],
        )
    if not np.array(TKCListHTPDF).shape[0] == 0:
        FCSV.CsvSaveEnc(
            ListURL + "/TKC法人税の添付書類の受信通知.csv",
            TKCListHTPDF,
            "cp932",
            [
                "コード",
                "URL",
                "ページ",
                "提出先",
                "利用者識別番号",
                "元の申告・申請書の受付番号",
                "氏名又は名称",
                "代表者等氏名",
                "受付番号",
                "受付日時",
            ],
        )
    if not np.array(TKCListSyouhi).shape[0] == 0:
        FCSV.CsvSaveEnc(
            ListURL + "/TKC消費税の受信通知.csv",
            TKCListSyouhi,
            "cp932",
            [
                "コード",
                "URL",
                "ページ",
                "提出先",
                "利用者識別番号",
                "氏名又は名称",
                "代表者等氏名",
                "受付番号",
                "受付日時",
                "種目",
                "申告の種類",
                "課税期間",
                "課税標準額",
                "消費税合計税額",
            ],
        )
    if not np.array(TKCListSyouhiPDF).shape[0] == 0:
        FCSV.CsvSaveEnc(
            ListURL + "/TKC消費税の受信通知.csv",
            TKCListSyouhiPDF,
            "cp932",
            ["コード", "URL", "ページ", "提出先", "利用者識別番号", "氏名又は名称", "代表者等氏名", "受付番号", "受付日時"],
        )
    if not np.array(TKCListTodouhu).shape[0] == 0:
        FCSV.CsvSaveEnc(
            ListURL + "/TKC都道府県民税の受信通知.csv",
            TKCListTodouhu,
            "cp932",
            [
                "コード",
                "URL",
                "ページ",
                "納税者の氏名又は名称",
                "発行元",
                "電話番号",
                "発行日時",
                "件名",
                "メッセージ本文金額",
                "受付日時",
                "受付番号",
                "手続名",
                "事業年度",
                "提出先",
            ],
        )
    if not np.array(TKCListSityou).shape[0] == 0:
        FCSV.CsvSaveEnc(
            ListURL + "/TKC市町村民税の受信通知.csv",
            TKCListSityou,
            "cp932",
            [
                "コード",
                "URL",
                "ページ",
                "納税者の氏名又は名称",
                "発行元",
                "電話番号",
                "発行日時",
                "件名",
                "メッセージ本文金額",
                "受付日時",
                "受付番号",
                "手続名",
                "事業年度",
                "提出先",
            ],
        )
    if not np.array(ImageCSVList).shape[0] == 0:
        FCSV.CsvSaveEnc(
            ListURL + "/イメージ取得リスト.csv",
            ImageCSVList,
            "cp932",
            ["コード", "URL", "ページ", "手続名", "氏名又は名称", "受付番号", "受付日時", "元の申告・申請書の受付番号"],
        )
    if not np.array(CSVBadList).shape[0] == 0:
        FCSV.CsvSaveEnc(
            ListURL + "/受信通知取得失敗リスト.csv",
            CSVBadList,
            "cp932",
            [
                "コード",
                "URL",
                "ページ",
                "手続名",
                "氏名又は名称",
                "発行元名",
                "発行元所属名",
                "受付日時",
                "提出先",
                "年度・期別",
                "納税者氏名",
            ],
        )
    # ------------------------------------------------------------------------------------


# URL = "\\\\Sv05121a\\e\\電子ファイル\\メッセージボックス\\2022-2\\送信分受信通知"
URL = "\\\\Sv05121a\\e\\電子ファイル\\メッセージボックス\\TEST"
try:
    logger.debug(URL + "内のPDF抽出開始")
    PDFRead(URL)
    logger.debug(URL + "内のPDF抽出完了")
except Exception as e:
    logger.debug("エラー終了" + e)
