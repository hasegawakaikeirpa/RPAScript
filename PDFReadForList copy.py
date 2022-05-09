from datetime import datetime
import os
import numpy as np
from pdfminer.high_level import extract_text
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from PIL import Image
from collections import OrderedDict
import ContextTimeOut as CTO
import Function.CSVOut as FCSV
import Function.FolderCreate as FC
import Function.MiniStrChange as MSC
import toml
import RPAPhoto.PDFReadForList.CSVSetting as CSVSet  # CSVの設定ファイルの読込
import Function.PDFCellsImport as FPDF

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


# -------------------------------------------------------------------------------------------------------
def DiffListPlus(ColList, ScrList, Ers):
    try:
        LNList = Settingtoml["MASTER"]["ListNameList"]  # tomlから各種設定リスト名を抽出
        NewColList = []
        for LNListItem in LNList:
            NewColList = Settingtoml["CsvSaveEnc"][LNListItem]
            SColA = set(ColList) - set(NewColList)
            SColB = set(NewColList) - set(ColList)
            if len(SColA) == 0 and len(SColB) == 0:
                CDict[LNListItem].append(ScrList)
                return True, LNListItem
        print(ColList)
        print(
            "========================================================================================"
        )
        print(ScrList)
        if Ers == "Sub":
            print("サブテーブル取得エラー")
            CDict["SubErrList"].append(ScrList)
            return False, "SubErrList"
        else:
            print("指定列名での設定項目がありませんでした。")
            CDict["ErrList"].append(ScrList)
            return False, "ErrList"
    except:
        print(ColList)
        print(
            "========================================================================================"
        )
        print(ScrList)
        if Ers == "Sub":
            print("サブテーブル取得エラー")
            CDict["SubErrList"].append(ScrList)
            return False, "SubErrList"
        else:
            print("指定列名での設定項目がありませんでした。")
            CDict["ErrList"].append(ScrList)
            return False, "ErrList"


# -------------------------------------------------------------------------------------------------------
def DiffListCSVOUT(ListURL, ColN):
    ListURL = ListURL.replace("\\", "/")
    FCSV.CsvSaveEnc(
        ListURL + "/" + ColN + ".csv",
        CDict[ColN],
        "cp932",
        Settingtoml["CsvSaveEnc"][ColN],
    )


# ----------------------------------------------------------------------------------------------
def CamelotSerch(CDict, path_pdf, PageVol, Settingtoml, SCode, y, engine, DLCList):
    try:
        NextFlag = False
        TO = True  # TimeOut判定変数
        # 第三引数に'stream'を渡すと表外の値を抽出できる
        if engine == "stream":
            tables = CTO.camelotTimeOut(path_pdf, PageVol, engine)
        else:
            tables = CTO.camelotTimeOut(path_pdf, PageVol, "")
        # t = tables._tables[0].data
        # Sbtext = "".join([str(_) for _ in t])
        mp = []
        mp.append(y)
        Sbtext = extract_text(
            path_pdf, page_numbers=mp, maxpages=1, codec="utf-8"
        )  # テキストのみ取得できる
        Sbtext = Sbtext.replace("\n\n", ":")
        # =================================================================
        if "申告のお知らせ" in Sbtext:
            if "課税期間分の中間申告について" in Sbtext:
                TaxType = "etaxsyouhicyuukan"
            elif "事業年度等分中間（予定）申告について" in Sbtext:
                TaxType = "etaxjigyounendo"
            else:
                TaxType = "etaxosirase"
        elif "「消費税の納税義務者でなくなった旨の届出書」を提出していない場合には" in Sbtext:
            TaxType = "etaxsyouhi"
        elif "消費税簡易課税制度選択不適⽤届出" in Sbtext:
            TaxType = "etaxsyouhitodoke"
        elif "源泉所得税及復興特別所得税" in Sbtext:
            if "徴収⾼計算書の送付の要否" in Sbtext:
                TaxType = "etaxsyotoku2"
            else:
                TaxType = "etaxsyotoku"
        elif "前事業年度等" in Sbtext:
            TaxType = "etaxjigyounendo"
        elif "Copyright(C) TKC" in Sbtext:
            if "税務届出書類等作成支援システム(e-DMS)による電子申請・届出が完了しましたので、ご報告いたします。" in Sbtext:
                if "地 方 税 の 電 子 申 請・届 出 完 了 報 告 書" in Sbtext:
                    TaxType = "TKC2"
                else:
                    TaxType = "TKC"
            elif "ＴＫＣ電子申告システム" in Sbtext:
                TaxType = "TKC3"
                tables = CTO.camelotTimeOut(path_pdf, PageVol, "stream")
            elif "地 方 税 ポ ー タ ル シ ス テ ム ( e L T A X ) の" in Sbtext:
                TaxType = "TKC10"
                tables = CTO.camelotTimeOut(path_pdf, PageVol, "stream")
        else:
            if "送信された申告データを受付けました。" in Sbtext:
                MOUTList = Settingtoml["OUTLIST"]["MJSOutList"]
                Sbt = Sbtext.replace("\u3000", "").replace("\n", "")
                for MOUTListItem in MOUTList:
                    if MOUTListItem in Sbt:
                        TaxType = "MJSOutList"
                        break
                    else:
                        TaxType = "MJS"
            elif "（e-Tax）" in Sbtext:
                TaxType = "etaxList"
            else:
                TaxType = "eltaxList"
        # =================================================================
        try:
            CSbtext = Sbtext.split("\n")
            SBR = len(CSbtext) - 1
            for CSbtextItem in reversed(CSbtext):
                if CSbtextItem == "":
                    CSbtext.pop(SBR)
                elif "国税受付システムからの「受信通知」の内容" in CSbtextItem:
                    Relist = CSbtextItem.split("国税受付システムからの「受信通知」の内容")
                    CSbtext[SBR] = CSbtext[SBR].replace(Relist[0], "")
                SBR -= 1
            SBR = len(CSbtext) - 1
            for SBRP in range(SBR - 10, SBR):
                if "ファイル名称" in CSbtext[SBRP]:
                    print("1ページ")
                    NextFlag = False
                    break
                else:
                    print("続き有")
                    NextFlag = True
            # もしページで--------------------------------------------------
            if NextFlag is True:
                yy = int(PageVol)
                mp = []
                mp.append(yy)
                NSbtext = extract_text(
                    path_pdf, page_numbers=mp, maxpages=1, codec="utf-8"
                )  # テキストのみ取得できる
                NSbtext = NSbtext.replace("\n\n", ":")
                Sbtext = Sbtext + "\n" + NSbtext
                print(Sbtext)

            # -------------------------------------------------------------
            tCells = FPDF.CellsImport(
                CDict,
                Settingtoml,
                SCode,
                path_pdf,
                tables,
                y,
                TaxType,
                Sbtext,
                DLCList,
                NextFlag,
            )
            if tCells[0] is False:
                TO = False
            return True, TO, tables, tCells, TaxType, NextFlag
            # tCells = FPDF.CellsImport(Settingtoml,SCode, path_pdf, tables, y)
        except:
            # -------------------------------------------------------------
            tCells = FPDF.CellsImport(
                CDict,
                Settingtoml,
                SCode,
                path_pdf,
                tables,
                y,
                TaxType,
                Sbtext,
                DLCList,
                NextFlag,
            )
            if tCells[0] is False:
                TO = False
            return True, TO, tables, tCells, TaxType, NextFlag
    except:  # TimeOut処理を記述
        TO = False  # TimeOut判定変数
        return False, TO, tables, tCells, TaxType, NextFlag


# ----------------------------------------------------------------------------------------------


def CSVIndexSort(SCode, path_pdf, DLCList):
    # # ------------------------------------------------------------------------------------
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
            if y == 0:
                NF = False
            if NF is True:
                NF = False
                continue
            else:
                # TX = extract_text(path_pdf,page_numbers=y,codec='utf-8') テキストのみ取得できる
                # print(TX)
                PageVol = str(y + 1)
                # TimeOutを加味したPDFRead処理TimeOut設定時間はContextTimeOut.pyにコンテキストで設定する
                # 一回目の処理-----------------------------------------------
                # PDFテキスト内容で税目処理分け
                TO = CamelotSerch(
                    CDict, path_pdf, PageVol, Settingtoml, SCode, y, "", DLCList
                )  # return True, TO,tables, tCells
                try:
                    NF = TO[5]
                except:
                    NF = False
                # ---------------------------------------------------------
                if "TKC" not in TO[4]:  # 一回目処理結果がTKCじゃなければ
                    if NF is False:
                        if TO[1] is not False:  # 一回目処理がTimeOutしなかったら
                            tables = TO[2]
                            tCells = TO[3]
                            t_count = len(tables)  # PDFのテーブル数を格納
                            # PDFのテーブル数をが二つ以上なら----------------------------------
                            if t_count >= 2:
                                # 既に取得済みの初めのページを格納
                                DLP = DiffListPlus(tCells[1], tCells[2], "")  # 抽出リストに格納
                                DLCList.append(DLP[1])  # できあがった抽出リストを保管
                                # 二回目の処理第六引数に'stream'を渡すと表外の値を抽出できる------
                                # PDFテキスト内容で税目処理分け
                                SB = CamelotSerch(
                                    CDict,
                                    path_pdf,
                                    PageVol,
                                    Settingtoml,
                                    SCode,
                                    y,
                                    "stream",
                                )  # return True, TO,tables, tCells
                                # ---------------------------------------------------------
                                Subtables = SB[2]
                                SubtCells = SB[3]
                                SubtCells[2][1] = str(SubtCells[2][1]) + "サブテーブル失敗"
                                DLP = DiffListPlus(
                                    SubtCells[1], SubtCells[2], "Sub"
                                )  # 抽出リストに格納
                                DLCList.append(DLP[1])  # できあがった抽出リストを保管
                                # TKCPDFの表外テキスト抽出処理------------------------------
                                # PDFテキスト内容で税目処理分け
                                SB = CamelotSerch(
                                    CDict,
                                    path_pdf,
                                    PageVol,
                                    Settingtoml,
                                    SCode,
                                    y,
                                    "stream",
                                )  # return True, TO,tables, tCells
                                # ---------------------------------------------------------
                            else:
                                # 既に取得済みの初めのページを格納
                                # 二回目の処理第六引数に'stream'を渡すと表外の値を抽出できる------
                                # PDFテキスト内容で税目処理分け
                                if "TKC" in TO[4]:
                                    SB = CamelotSerch(
                                        CDict,
                                        path_pdf,
                                        PageVol,
                                        Settingtoml,
                                        SCode,
                                        y,
                                        "stream",
                                    )  # return True, TO,tables, tCells
                                # ---------------------------------------------------------

                                DLP = DiffListPlus(tCells[1], tCells[2], "")  # 抽出リストに格納
                                DLCList.append(DLP[1])  # できあがった抽出リストを保管
                            # ------------------------------------------------------------
                        else:
                            # 二回目の処理第六引数に'stream'を渡すと表外の値を抽出できる------
                            # PDFテキスト内容で税目処理分け
                            SB = CamelotSerch(
                                CDict,
                                path_pdf,
                                PageVol,
                                Settingtoml,
                                SCode,
                                y,
                                "stream",
                            )  # return True, TO,tables, tCells
                            # ---------------------------------------------------------
                            if SB[1] is not False:  # 一回目処理がTimeOutしなかったら
                                Subtables = SB[2]
                                SubtCells = SB[3]
                                DLP = DiffListPlus(
                                    SubtCells[1], SubtCells[2], ""
                                )  # 抽出リストに格納
                                DLCList.append(DLP[1])  # できあがった抽出リストを保管
                            else:
                                logger.debug(path_pdf + "_" + str(y + 1) + "ページ目タイムアウト")
                                OutputList = [
                                    path_pdf.replace("/", "\\"),
                                    str(y + 1) + "ページ目タイムアウト",
                                    SCode,
                                    "",
                                    "",
                                    "",
                                    "",
                                    "",
                                    "",
                                    "",
                                    "",
                                    "",
                                    "",
                                    "",
                                    "",
                                    "",
                                    "",
                                    "",
                                    "",
                                    "",
                                ]
                                DLP = DiffListPlus(
                                    Settingtoml["CsvSaveEnc"]["ErrList"], OutputList, ""
                                )  # 抽出リストに格納
                                DLCList.append(DLP[1])  # できあがった抽出リストを保管
                    else:
                        tables = TO[2]
                        tCells = TO[3]
                        # 既に取得済みの初めのページを格納
                        if len(tCells[2]) == 3:
                            OutputList = [
                                path_pdf.replace("/", "\\"),
                                str(y + 1) + "ページ目NFエラー取得失敗",
                                SCode,
                                "",
                                "",
                                "",
                                "",
                                "",
                                "",
                                "",
                                "",
                                "",
                                "",
                                "",
                                "",
                                "",
                                "",
                                "",
                                "",
                                "",
                            ]
                            DLP = DiffListPlus(
                                Settingtoml["CsvSaveEnc"]["ErrList"], OutputList, ""
                            )  # 抽出リストに格納
                            DLCList.append(DLP[1])  # できあがった抽出リストを保管
                        else:
                            DLP = DiffListPlus(tCells[1], tCells[2], "")  # 抽出リストに格納
                            DLCList.append(DLP[1])  # できあがった抽出リストを保管
                else:  # 一回目処理結果がTKCだったら
                    if not TO[4] == "TKC3":
                        tables = TO[2]
                        tCells = TO[3]
                        # 既に取得済みの初めのページを格納
                        DLP = DiffListPlus(tCells[1], tCells[2], "")  # 抽出リストに格納
                        DLCList.append(DLP[1])  # できあがった抽出リストを保管
                    else:
                        print("TKCテキスト完了")
                        NF = TO[5]
    except Exception as e:
        if TO[0] is not False:
            logger.debug(path_pdf + "_" + str(y + 1) + "ページ目取得失敗")
            OutputList = [
                path_pdf.replace("/", "\\"),
                str(y + 1) + "ページ目取得失敗",
                SCode,
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
            ]
            DLP = DiffListPlus(
                Settingtoml["CsvSaveEnc"]["ErrList"], OutputList, ""
            )  # 抽出リストに格納
            if DLP[0] is True:
                DLCList.append(DLP[1])  # できあがった抽出リストを保管
            print(e)
        elif e.args[0] == "local variable 'tables' referenced before assignment":
            logger.debug(path_pdf + "_" + str(y + 1) + "ページ目取得失敗")
            OutputList = [
                path_pdf.replace("/", "\\"),
                str(y + 1) + "ページ目取得失敗",
                SCode,
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
                "",
            ]
            DLP = DiffListPlus(
                Settingtoml["CsvSaveEnc"]["ErrList"], OutputList, ""
            )  # 抽出リストに格納
            if DLP[0] is True:
                DLCList.append(DLP[1])  # できあがった抽出リストを保管
            print(e)


# ----------------------------------------------------------------------------------------
def PDFRead(URL, Settingtoml):
    # ------------------------------------------------------------------------------------
    # FCSV.CsvSaveEnc(URL.replace("\\","/") + "/PDFDataSuccess.csv",CSVList,"shiftjis")
    DLCList = []
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
                    if dif.endswith(".pdf") is True:  # pdfファイルのみ
                        path_pdf = dif.replace("\\", "/")  # PDFパスを代入
                        CSVIndexSort(SCode, path_pdf, DLCList)
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
    DLCDiplicated = list(OrderedDict.fromkeys(DLCList))  # 抽出リストの重複削除
    for DItem in DLCDiplicated:
        try:
            DiffListCSVOUT(ListURL, DItem)  # 抽出リストをCSV書出し
        except:
            continue


# ------------------------------------------------------------------------------------
def CSVLog(URL, LogURL):
    URL = URL + "\\受信通知CSV"
    now = datetime.now()
    DY = "{0:%Y-%m-%d %H:%M:%S}".format(now)
    DY = DY.replace(":", "-")
    List = []
    ALLList = []
    for fd_path, sb_folder, sb_file in os.walk(URL):
        for fil in sb_file:
            if fil.endswith(".csv") is True:
                List.append([fd_path, fil])
    for ListItem in List:
        CURL = ListItem[0] + "\\" + ListItem[1]
        DFCSV = FCSV.CsvReadDtypeDict(CURL, str)
        DFCSVRow = np.array(DFCSV[1]).shape[0]
        for DI in range(DFCSVRow):
            AR = DFCSV[1].iloc[DI]
            ALLList.append(AR)
        # print(ALLList)
    LogURL = LogURL.replace("\\", "/") + "/" + DY + "_Log.csv"
    FCSV.CsvSaveNoHeader(LogURL, ALLList, "cp932")


# ------------------------------------------------------------------------------------

MeUrl = os.getcwd().replace("\\", "/")  # 自分のパス
# toml読込------------------------------------------------------------------------------
with open(MeUrl + r"/RPAPhoto/PDFReadForList/Setting.toml", encoding="utf-8") as f:
    Settingtoml = toml.load(f)
    print(Settingtoml)
# ----------------------------------------------------------------------------------------
CDict = CSVSet.CSVIndexSortFuncArray  # 外部よりdict変数取得
# URL = "\\\\Sv05121a\\e\\電子ファイル\\メッセージボックス\\2022-2\\送信分受信通知"
URL = "\\\\Sv05121a\\e\\電子ファイル\\メッセージボックス\\TEST"
LogURL = "\\\\Sv05121a\\e\\電子ファイル\\メッセージボックス\\PDFREADLog"
try:
    logger.debug(URL + "内のPDF抽出開始")
    PDFRead(URL, Settingtoml)
    CSVLog(URL, LogURL)
    logger.debug(URL + "内のPDF抽出完了")
except Exception as e:
    logger.debug("エラー終了" + e)
