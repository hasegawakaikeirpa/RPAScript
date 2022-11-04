###########################################################################################################
# 稼働設定：解像度 1920*1080 表示スケール125%
###########################################################################################################
# モジュールインポート
import pyautogui as pg
import time
import MJSOpen

# pandasインポート
import pandas as pd

# 配列計算関数numpyインポート
import numpy as np

# osインポート
import os

# 例外処理判定の為のtracebackインポート
import traceback

# pandas(pd)で関与先データCSVを取得
import pyautogui
import pyperclip  # クリップボードへのコピーで使用
import ExcelFileAction as EFA

import MJSSPOPDFMarge as PDFM
import datetime
import openpyxl
import re

import WarekiHenkan as WH
import RPA_Function as RPA
import Control
import Sub_GenkasyoukyakuUpdate as GenkasyoukyakuUpdate
import Sub_HoujinzeiUpdate as HoujinzeiUpdate
import Sub_KaikeiUpDate as KaikeiUpDate
import Sub_KessanUpDate as KessanUpDate
import Sub_DensisinkokuUpDate as DensisinkokuUpDate

# logger設定------------------------------------------------------------------------------------------------------------
import logging.config

logging.config.fileConfig(r"LogConf\loggingMJSSysUp.conf")
logger = logging.getLogger(__name__)
LURL = r"\\NAS-SV\B_監査etc\B2_電子ﾌｧｲﾙ\RPA_ミロクシステム次年更新\一括更新申請\MJSLog\初回起動_"
# ----------------------------------------------------------------------------------------------------------------------
# #######################################################################################################################
# 一括更新処理の該当年度はThisYearKey.pngなので、年度が変わったらスクリーンショットしなおす事
# #######################################################################################################################

# ------------------------------------------------------------------------------------------------
class Job:
    """
    処理全体(class)
    """

    def __init__(self, **kw):
        log_out("Jobクラス読込開始")
        # 自分のDir(str)
        self.dir = RPA.My_Dir("MJS_SystemPrintOut")
        # 画像のDir(str)
        self.Img_dir = self.dir + r"\\img"
        # コントロール(class)
        self.control = Control.control()

        self.FolURL = os.getcwd().replace("\\", "/")  # 先
        # 当年(int)
        self.Start_Year = WH.Wareki.from_ad(datetime.datetime.today().year).year
        # RPA用画像フォルダの作成
        self.PrintOut_url = self.Img_dir + r"\\MJS_SystemPrintOut"  # 先
        self.All_url = self.PrintOut_url + r"\\All"  # 先
        self.NextCreate_url = self.Img_dir + r"\\MJS_SystemNextCreate"  # 先
        self.XLSDir = r"\\NAS-SV\B_監査etc\B2_電子ﾌｧｲﾙ\RPA_ミロクシステム次年更新\製本・電子ファイル印刷申請"
        self.first_csv = self.XLSDir + r"\MJSLog\MJSSysUpLog.txt"  # 処理状況CSVのURL
        self.BatUrl = (
            os.getcwd() + r"\\bat\\AWADriverOpen.bat"
        )  # 4724ポート指定でappiumサーバー起動バッチを開く
        self.driver = MJSOpen.MainFlow(
            self.BatUrl, self.FolURL, self.Img_dir
        )  # MJSを起動しログイン後インスタンス化
        log_out("Jobクラス読込終了")

    def MainFlow(self, Exc):

        """
        概要: プリントメイン処理
        @param FolURL : ミロク起動関数のフォルダ(str)
        @param TFolURL : このpyファイルのフォルダ(str)
        @param Exlsx : Excel指示シート(obj)
        @return : bool
        """
        try:
            log_out("xlsxをDataFrameに")
            open(LURL, "w").close()
            for Exc.sheet_name in Exc.input_sheet_name:
                # DataFrameとしてsheetのデータ読込み
                if "印刷申請" in Exc.sheet_name:
                    Exc.Read_sheet(Exc.sheet_name, self.first_csv)
                    MainStarter(
                        self,
                        Exc,
                    )  # データ送信画面までの関数
                    print("")
        except Exception as e:
            log_out(e)


# ------------------------------------------------------------------------------------------------
class Sheet:
    """
    エクセルブック(class)
    """

    def __init__(self, XLSURL, **kw):
        log_out("_Excelブック読込開始")
        self.mybook_url = XLSURL
        Ex_file = EFA.XlsmRead(XLSURL)
        if Ex_file[0] is True:
            # エクセルブック
            self.book = Ex_file[1]
            # 全シート
            self.input_sheet_name = self.book.sheet_names
            # 全シート数
            self.num_sheet = len(self.input_sheet_name)
            log_out("_Excelブック読込終了")
        else:
            log_out("_Excelブック読込失敗")

    def Read_sheet(self, sheet_name, first_csv, **kw):
        log_out("_Excelシート読込開始")
        self.sheet_header = []
        ExSheet = ""
        NameSheet = ""
        ExSheet = self.book.parse(sheet_name, skiprows=0)
        NameSheet = self.book.parse("関与先一覧")
        print(ExSheet)
        # 初回読込時の保存--------------------------
        dt_s = datetime.datetime.now()
        dt_s = dt_s.strftime("%Y-%m-%d %H-%M-%S")
        self.sheet_df = pd.DataFrame(ExSheet)
        self.name_df = pd.DataFrame(NameSheet)
        self.sheet_df.to_csv(
            first_csv + dt_s + ".csv",
            encoding="cp932",
            index=False,
        )
        # 列名整理--------------------------------
        self.sheet_column_count = self.sheet_df.shape[1]  # 列数
        for Ex in range(self.sheet_column_count):
            ExRow = ExSheet.iloc[0]  # 列名
            ExSecondRow = ExSheet.iloc[2]  # 列名2
            if ExRow[Ex] == ExRow[Ex]:  # nan判定
                # nanでない場合
                Txt = ExRow[Ex]
                if ExSecondRow[Ex] == ExSecondRow[Ex]:  # nan判定
                    # nanでない場合
                    self.sheet_header.append(ExRow[Ex] + "_" + ExSecondRow[Ex])
                else:
                    # nanの場合
                    self.sheet_header.append(ExRow[Ex])
            else:
                # nanの場合
                if ExSecondRow[Ex] == ExSecondRow[Ex]:  # nan判定
                    # nanでない場合
                    self.sheet_header.append(Txt + "_" + ExSecondRow[Ex])
                else:
                    # nanの場合
                    self.sheet_header.append(Txt)
        # データ整理--------------------------------
        # Df作成
        ExDf = pd.DataFrame(self.sheet_df.values[3:, :], columns=self.sheet_header)
        # Dfnan処理
        ExDf.dropna(how="all", inplace=True)
        print(ExDf)
        self.sheet_df = ExDf
        self.sheet_column_count = self.sheet_df.shape[1]  # 列数
        self.sheet_row_count = self.sheet_df.shape[0]  # 行数

        log_out("_Excelシート読込完了")

    def WriteExcel(self, txt):
        """
        エクセルシート入力
        """
        dt_now = datetime.datetime.now()
        dt_now = dt_now.strftime("%Y/%m/%d %H:%M:%S")
        WriteEx = openpyxl.load_workbook(self.mybook_url, keep_vba=True)
        WriteExSheet = WriteEx[self.sheet_name]
        if txt == "○":
            WriteExSheet.cell(
                row=self.this_row_count + 5, column=self.this_col_count + 1
            ).value = dt_now
        else:
            WriteExSheet.cell(
                row=self.this_row_count + 5, column=self.this_col_count + 1
            ).value = txt
        print("シート書き込み完了")
        print(WriteEx)
        WriteEx.save(XLSURL)
        WriteEx.close


# ------------------------------------------------------------------------------------------------
def log_out(txt):
    """
    logger出力
    """
    dt_s = datetime.datetime.now()
    dt_s = dt_s.strftime("%Y-%m-%d %H:%M:%S")
    logger.debug(dt_s + txt)


# ------------------------------------------------------------------------------------------------
def logcsv_out(txt):
    """
    loggercsv出力
    """
    dt_s = datetime.datetime.now()
    dt_s = dt_s.strftime("%Y-%m-%d %H:%M:%S")
    with open(LURL, "a") as f:
        print([dt_s, txt], file=f)


# ------------------------------------------------------------------------------------------------
def NameSearch(NameDF, Rno):
    """
    顧問先名称の検索
    """
    try:
        NameDFColumn = np.array(NameDF.columns)
        NameDF = np.array(NameDF)
        NC = np.where(NameDFColumn == "コード")
        KC = np.where(NameDFColumn == "顧問先名称")
        NameDFIndex = NameDF[:, NC]
        NR = np.where(NameDFIndex == Rno)
        N_L = NameDF[NR, KC]
        N_L = (
            str(N_L[0])
            .replace("[", "")
            .replace("]", "")
            .replace("'", "")
            .replace('"', "")
            .replace("\u3000", "")
        )
        print(N_L)
        return N_L
    except:
        return "NameErr"


# ------------------------------------------------------------------------------------------------------------------
def ChildFlow_sub(Job, Exc, txt):
    """
    シート列名に応じて処理分岐サブ
    """
    # Log---------------------------------------------------------------------------------------
    msg = "_関与先番号:" + str(Exc.row_kanyo_no) + ":" + str(Exc.row_kanyo_name) + txt + "開始"
    log_out(msg)
    logcsv_out(msg)
    # ------------------------------------------------------------------------------------------
    if "会計大将" == Exc.Title:

        # 会計大将のアイコンを探す
        ImgList = [r"\K_TaisyouIcon.png", r"\K_TaisyouIcon2.png"]
        ICFL = RPA.ImgCheckForList(Job.All_url, ImgList, 0.9, 10)
        if ICFL[0] is True:  # 会計大将のアイコンがあれば
            RPA.ImgClick(Job.All_url, ICFL[1], 0.9, 10)  # 会計大将のアイコンをクリック
            ret = KaikeiUpDate.KaikeiUpDate(Job, Exc)
            return ret
    elif "決算内訳書" == Exc.Title:

        # 決算内訳書のアイコンを探す-------------------------------------------------
        ImgList = [r"\K_Uchiwake.png", r"\K_Uchiwake2.png"]
        ICFL = RPA.ImgCheckForList(Job.All_url, ImgList, 0.9, 10)
        if ICFL[0] is True:  # 決算内訳書のアイコンがあれば
            RPA.ImgClick(Job.All_url, ICFL[1], 0.9, 10)  # 決算内訳書のアイコンをクリック
            ret = KessanUpDate.KessanUpDate(Job, Exc)
            return ret
    elif "減価償却" == Exc.Title:

        # 減価償却のアイコンを探す-------------------------------------------------
        ImgList = [r"\G_Syoukyaku.png", r"\G_Syoukyaku2.png"]
        ICFL = RPA.ImgCheckForList(Job.All_url, ImgList, 0.9, 10)
        if ICFL[0] is True:  # 減価償却のアイコンがあれば
            RPA.ImgClick(Job.All_url, ICFL[1], 0.9, 10)  # 減価償却のアイコンをクリック
            ret = GenkasyoukyakuUpdate.GenkasyoukyakuUpdate(Job, Exc)
            return ret
    elif "法人税申告書" == Exc.Title:
        # 法人税のアイコンを探す-------------------------------------------------
        ImgList = [r"\Houjinzei.png", r"\Houjinzei2.png"]
        ICFL = RPA.ImgCheckForList(Job.All_url, ImgList, 0.9, 10)
        if ICFL[0] is True:  # 法人税のアイコンがあれば
            RPA.ImgClick(Job.All_url, ICFL[1], 0.9, 10)  # 法人税のアイコンをクリック
            ret = HoujinzeiUpdate.HoujinzeiUpdate(Job, Exc)
            return ret
    elif "電子申告" == Exc.Title:
        # 電子申告のアイコンを探す-------------------------------------------------
        ImgList = [r"\DensiIcon.png", r"\DensiIcon2.png"]
        ICFL = RPA.ImgCheckForList(Job.All_url, ImgList, 0.9, 10)
        if ICFL[0] is True:  # 電子申告のアイコンがあれば
            RPA.ImgClick(Job.All_url, ICFL[1], 0.9, 10)  # 電子申告のアイコンをクリック
            pg.keyDown("alt")
            pg.press("a")
            pg.keyUp("alt")
            ret = DensisinkokuUpDate.DensisinkokuUpDate(Job, Exc)
            return ret

    # Log--------------------y-------------------------------------------------------------------
    msg = "_関与先番号:" + str(Exc.row_kanyo_no) + ":" + str(Exc.row_kanyo_name) + txt + "終了"
    log_out(msg)
    logcsv_out(msg)
    # ------------------------------------------------------------------------------------------


# ------------------------------------------------------------------------------------------------------------------
def ChildFlow(Job, Exc):
    """
    シート列名に応じて処理分岐サブ
    """
    try:
        if "会計大将" == Exc.Title:
            Exc.Fname = Job.Img_dir + r"\PDF\\" + Exc.PN + ".pdf"
            # 処理
            SystemUp = ChildFlow_sub(Job, Exc, Exc.Title + Exc.PN + "_印刷処理")
            if SystemUp[0] is True:
                Exc.WriteExcel("○")  # シート書き込み
                # Log
                msg = (
                    "_関与先番号:"
                    + str(Exc.row_kanyo_no)
                    + ":"
                    + str(Exc.row_kanyo_name)
                    + Exc.Title
                    + Exc.PN
                    + "_印刷処理完了"
                )
                log_out(msg)
                logcsv_out(msg)
            elif SystemUp[1] == "要消費税基本情報登録":
                Exc.WriteExcel("要消費税基本情報登録")  # シート書き込み
                # Log
                msg = (
                    "_関与先番号:"
                    + str(Exc.row_kanyo_no)
                    + ":"
                    + str(Exc.row_kanyo_name)
                    + Exc.Title
                    + Exc.PN
                    + "_要消費税基本情報登録"
                )
                log_out(msg)
                logcsv_out(msg)
            elif SystemUp[1] == "出力履歴なし":
                Exc.WriteExcel("要消費税基本情報登録")  # シート書き込み
                # Log
                msg = (
                    "_関与先番号:"
                    + str(Exc.row_kanyo_no)
                    + ":"
                    + str(Exc.row_kanyo_name)
                    + Exc.Title
                    + Exc.PN
                    + "_出力履歴なし"
                )
                log_out(msg)
                logcsv_out(msg)
            elif SystemUp[1] == "決算順序未設定":
                Exc.WriteExcel("決算順序未設定")  # シート書き込み
                # Log
                msg = (
                    "_関与先番号:"
                    + str(Exc.row_kanyo_no)
                    + ":"
                    + str(Exc.row_kanyo_name)
                    + Exc.Title
                    + Exc.PN
                    + "_決算順序未設定"
                )
                log_out(msg)
                logcsv_out(msg)
            elif SystemUp[1] == "T_Err":
                Exc.WriteExcel("貸借バランスエラー")  # シート書き込み
                # Log
                msg = (
                    "_関与先番号:"
                    + str(Exc.row_kanyo_no)
                    + ":"
                    + str(Exc.row_kanyo_name)
                    + Exc.Title
                    + Exc.PN
                    + "_貸借バランスエラー"
                )
                log_out(msg)
                logcsv_out(msg)
            elif SystemUp[0] is False:
                Exc.WriteExcel("計算エラー")  # シート書き込み
                # Log
                msg = (
                    "_関与先番号:"
                    + str(Exc.row_kanyo_no)
                    + ":"
                    + str(Exc.row_kanyo_name)
                    + Exc.Title
                    + Exc.PN
                    + "_計算エラー"
                )
                log_out(msg)
                logcsv_out(msg)
        elif "決算内訳書" == Exc.Title:
            Exc.Fname = Job.Img_dir + r"\PDF\\" + Exc.PN + ".pdf"
            # 処理
            SystemUp = ChildFlow_sub(Job, Exc, Exc.Title + Exc.PN + "_印刷処理")
            if SystemUp[0] is True:
                Exc.WriteExcel("○")  # シート書き込み
                # Log
                msg = (
                    "_関与先番号:"
                    + str(Exc.row_kanyo_no)
                    + ":"
                    + str(Exc.row_kanyo_name)
                    + Exc.Title
                    + Exc.PN
                    + "_印刷処理完了"
                )
                log_out(msg)
                logcsv_out(msg)
            elif SystemUp[1] == "印刷様式未設定":
                Exc.WriteExcel("印刷様式未設定処理終了")  # シート書き込み
                # Log
                msg = (
                    "_関与先番号:"
                    + str(Exc.row_kanyo_no)
                    + ":"
                    + str(Exc.row_kanyo_name)
                    + Exc.Title
                    + Exc.PN
                    + "_印刷様式未設定処理終了"
                )
                log_out(msg)
                logcsv_out(msg)

        elif "減価償却" == Exc.Title:
            Exc.Fname = Job.Img_dir + r"\PDF\\" + Exc.PN + ".pdf"
            # 処理
            SystemUp = ChildFlow_sub(Job, Exc, Exc.Title + Exc.PN + "_印刷処理")
            if SystemUp[0] is True:
                Exc.WriteExcel("○")  # シート書き込み
                # Log
                msg = (
                    "_関与先番号:"
                    + str(Exc.row_kanyo_no)
                    + ":"
                    + str(Exc.row_kanyo_name)
                    + Exc.Title
                    + Exc.PN
                    + "_印刷処理完了"
                )
                log_out(msg)
                logcsv_out(msg)
            elif SystemUp[1] == "物件無し":
                Exc.WriteExcel("物件無し")  # シート書き込み
                # Log
                msg = (
                    "_関与先番号:"
                    + str(Exc.row_kanyo_no)
                    + ":"
                    + str(Exc.row_kanyo_name)
                    + Exc.Title
                    + Exc.PN
                    + "_物件無し"
                )
                log_out(msg)
                logcsv_out(msg)
            elif SystemUp[0] is False:
                Exc.WriteExcel("資産無し")  # シート書き込み
                # Log
                msg = (
                    "_関与先番号:"
                    + str(Exc.row_kanyo_no)
                    + ":"
                    + str(Exc.row_kanyo_name)
                    + Exc.Title
                    + Exc.PN
                    + "_資産無し"
                )
                log_out(msg)
                logcsv_out(msg)

        elif "法人税申告書" == Exc.Title:
            Exc.Fname = Job.Img_dir + r"\PDF\\" + Exc.PN + ".pdf"
            # 処理
            SystemUp = ChildFlow_sub(Job, Exc, Exc.Title + Exc.PN + "_印刷処理")
            if SystemUp[0] is True:
                Exc.WriteExcel("○")  # シート書き込み
                # Log
                msg = (
                    "_関与先番号:"
                    + str(Exc.row_kanyo_no)
                    + ":"
                    + str(Exc.row_kanyo_name)
                    + Exc.Title
                    + Exc.PN
                    + "_印刷処理完了"
                )
                log_out(msg)
                logcsv_out(msg)
            else:
                Exc.WriteExcel("失敗")  # シート書き込み
                # Log
                msg = (
                    "_関与先番号:"
                    + str(Exc.row_kanyo_no)
                    + ":"
                    + str(Exc.row_kanyo_name)
                    + Exc.Title
                    + Exc.PN
                    + "_印刷処理失敗"
                )
                log_out(msg)
                logcsv_out(msg)
                # ------------------------------------------------------------------------------------------
        elif "電子申告" == Exc.Title:
            Exc.Fname = Job.Img_dir + r"\PDF\\" + Exc.PN + ".pdf"
            # 処理
            SystemUp = ChildFlow_sub(Job, Exc, Exc.Title + Exc.PN + "_印刷処理")
            if SystemUp[0] is True:
                Exc.WriteExcel("○")  # シート書き込み
                # Log
                msg = (
                    "_関与先番号:"
                    + str(Exc.row_kanyo_no)
                    + ":"
                    + str(Exc.row_kanyo_name)
                    + Exc.Title
                    + Exc.PN
                    + "_印刷処理完了"
                )
                log_out(msg)
                logcsv_out(msg)
            else:
                Exc.WriteExcel("失敗")  # シート書き込み
                # Log
                msg = (
                    "_関与先番号:"
                    + str(Exc.row_kanyo_no)
                    + ":"
                    + str(Exc.row_kanyo_name)
                    + Exc.Title
                    + Exc.PN
                    + "_印刷処理失敗"
                )
                log_out(msg)
                logcsv_out(msg)
    except:
        print("")


# ------------------------------------------------------------------------------------------------------------------
def OpenSystem(Job, Exc):
    try:
        Exc.this_col_count = 0
        # 列名からMJSシステムリストを作成------------------------------------------------
        Exc.SystemList = []
        for Exc.this_col_name in Exc.sheet_header:
            # エクセルシートの値が1(str)なら
            if Exc.row_data[Exc.this_col_name] == "1":
                if Exc.this_col_count < (len(Exc.sheet_header) - 1):
                    if "_" in Exc.this_col_name:
                        SP = Exc.this_col_name.split("_")
                        Exc.Title = SP[0]  # MJS出力帳表名
                        Exc.PN = SP[1]  # MJS出力帳表名
                        Exc.SystemList.append(SP[1])
                        # Log---------------------------------------------------------------------------------------
                        msg = (
                            "_関与先番号:"
                            + str(Exc.row_kanyo_no)
                            + ":"
                            + str(Exc.row_kanyo_name)
                            + Exc.Title
                            + Exc.PN
                            + "_プリントメイン処理開始"
                        )
                        log_out(msg)
                        logcsv_out(msg)
                        # ------------------------------------------------------------------------------------------
                        if (
                            Exc.Title != "なし"
                            and Exc.Title != "決算フォルダ"
                            and Exc.Title != "繰越対象"
                            and "::" not in Exc.Title
                        ):
                            # ChildFFlag = True
                            CF = ChildFlow(Job, Exc)
                            if CF is True:
                                print("")
            Exc.this_col_count += 1
        return True
    except:
        print("TEST")
        return False

    # try:
    #     Eh = 0
    #     # 列名からMJSシステムリストを作成------------------------------------------------
    #     SystemList = []
    #     CountList = []
    #     for r in range(len(ExrcHeader)):
    #         if ExrcHeader[r] == ExrcHeader[r]:
    #             print(ExrcHeader[r])
    #         else:
    #             ExrcHeader.pop(r)
    #     for ExrcHeaderItem in ExrcHeader:
    #         if "_" in ExrcHeaderItem:
    #             SP = ExrcHeaderItem.split("_")
    #             SystemList.append(SP[0])
    #     for SystemListItem in SystemList:
    #         CountList.append(int(SystemList.count(SystemListItem)))
    #     SL = np.array(SystemList)
    #     CL = np.array(CountList)
    #     FMaxSystemList = SL[CL.argsort(axis=0)[::-1]]
    #     FMaxSystemList = list(dict.fromkeys(FMaxSystemList))
    #     print(FMaxSystemList)
    #     ChildFFlag = False
    #     # ----------------------------------------------------------------------------
    #     for ExrcHeaderItem in ExrcHeader:
    #         if Eh < (len(ExrcHeader) - 1):
    #             for FMaxSystemListItem in FMaxSystemList:
    #                 if FMaxSystemListItem in ExrcHeaderItem:
    #                     Title = FMaxSystemListItem  # MJSSytem名
    #                     PN = ExrcHeaderItem.split("_")[1]  # MJS出力帳表名
    #                     # nanの場合
    #                     # Log--------------------------------------------
    #                     dt_s = datetime.datetime.now()
    #                     dt_s = dt_s.strftime("%Y-%m-%d %H:%M:%S")
    #                     Rno = Exc.row_data["関与先番号_関与先番号"]
    #                     Rn = NameSearch(NameDF, Rno)
    #                     Rn = Rn.replace("\u3000", " ")
    #                     NumList = [1, 2, 3, 4, 5]
    #                     strNumList = ["1", "2", "3", "4", "5"]
    #                     if (
    #                         Exc.row_data[ExrcHeaderItem] in NumList
    #                         or Exc.row_data[ExrcHeaderItem] in strNumList
    #                     ):
    #                         logger.debug(
    #                             dt_s
    #                             + "_関与先番号:"
    #                             + str(Rno)
    #                             + ":"
    #                             + str(Rn)
    #                             + "_プリントメイン処理開始"
    #                         )
    #                         with open(LURL, "a") as f:
    #                             print(
    #                                 [dt_s, "関与先番号:" + str(Rno), str(Rn), "プリントメイン処理開始"],
    #                                 file=f,
    #                             )
    #                         # -----------------------------------------------
    #                         if (
    #                             not Title == "なし" or not Title == "決算フォルダ"
    #                         ) and "::" not in Title:
    #                             ChildFFlag = True
    #                             CF = ChildFlow(Job, Exc, txt)
    #                             if CF is True:
    #                                 print("")
    #             Eh += 1

    #     if ChildFFlag is True:
    #         return True
    #     else:
    #         return False
    # except:
    #     print("TEST")
    #     return False


# ------------------------------------------------------------------------------------------------------------------
def MainStarter(Job, Exc):
    try:
        for Exc.this_row_count in range(Exc.sheet_row_count):
            if Exc.this_row_count != 0:
                Exc.row_data = Exc.sheet_df.iloc[Exc.this_row_count]
                if Exc.row_data["関与先番号_関与先番号"] == Exc.row_data["関与先番号_関与先番号"]:  # nan判定
                    # nanでない場合
                    Exc.row_kanyo_no = Exc.row_data["関与先番号_関与先番号"]
                    Exc.row_kanyo_name = NameSearch(Exc.name_df, Exc.row_kanyo_no)
                    Exc.row_savedir = Exc.row_data["年度_(保管フォルダ名)"]
                    # マージPDFの保存先・対象システム年度をエクセルから抽出
                    if "_" in Exc.row_savedir:
                        sd = Exc.row_savedir.split("_")
                        Exc.row_savedir = sd[0]
                        Exc.year = re.sub(r"\D", "", sd[1])
                    else:
                        Exc.year = 0
                    OpenSystem(Job, Exc)
                    print("")
                else:
                    # nanの場合
                    print("nan")
        return True, ""
    except:
        return False, ""


# ------------------------------------------------------------------------------------------------------------------
# def MainFlow(FolURL, TFolURL, Job.Img_dir, SerchURL, XLSDir, LURL, Exlsx, driver, XLSURL):
#     """
#     概要: プリントメイン処理
#     @param FolURL : ミロク起動関数のフォルダ(str)
#     @param TFolURL : このpyファイルのフォルダ(str)
#     @param Exlsx : Excel指示シート(obj)
#     @return : bool
#     """
#     try:
#         # ----------------------------------------------------------------------------------------------------------------------
#         logger.debug("xlsxをDataFrameに")
#         # sheet_namesメソッドでExcelブック内の各シートの名前をリストで取得できる
#         input_sheet_name = Exlsx.sheet_names
#         # lenでシートの総数を確認
#         num_sheet = len(input_sheet_name)
#         # シートの数とシートの名前のリストの表示
#         print("Sheet の数:", num_sheet)
#         print(input_sheet_name)
#         for isnItem in input_sheet_name:
#             Exlsx = EFA.XlsmRead(XLSURL)[1]
#             # DataFrameとしてsheetのデータ読込み
#             if isnItem == "印刷申請":
#                 ExSheet = ""
#                 NameSheet = ""
#                 ExSheet = Exlsx.parse(isnItem, skiprows=0)
#                 NameSheet = Exlsx.parse("関与先一覧")
#                 print(ExSheet)
#                 # 初回読込時の保存--------------------------
#                 dt_s = datetime.datetime.now()
#                 dt_s = dt_s.strftime("%Y-%m-%d %H-%M-%S")
#                 DF = pd.DataFrame(ExSheet)
#                 NameDF = pd.DataFrame(NameSheet)
#                 DF.to_csv(
#                     r"\\NAS-SV\B_監査etc\B2_電子ﾌｧｲﾙ\RPA_ミロクシステム次年更新\製本・電子ファイル印刷申請\MJSLog\初回起動_プリント"
#                     + dt_s
#                     + ".csv",
#                     encoding="cp932",
#                     index=False,
#                 )
#                 # ----------------------------------------
#                 Exrc = np.array(ExSheet).shape[1]  # 列数
#                 ExrcHeader = []
#                 for Ex in range(Exrc):
#                     Exc.row_data = ExSheet.iloc[0]
#                     ExSecondRow = ExSheet.iloc[2]
#                     if Exc.row_data[Ex] == Exc.row_data[Ex]:  # nan判定
#                         # nanでない場合
#                         Txt = Exc.row_data[Ex]
#                         if ExSecondRow[Ex] == ExSecondRow[Ex]:  # nan判定
#                             # nanでない場合
#                             ExrcHeader.append(Exc.row_data[Ex] + "_" + ExSecondRow[Ex])
#                         else:
#                             # nanの場合
#                             ExrcHeader.append(Exc.row_data[Ex])
#                     else:
#                         # nanの場合
#                         if ExSecondRow[Ex] == ExSecondRow[Ex]:  # nan判定
#                             # nanでない場合
#                             ExrcHeader.append(Txt + "_" + ExSecondRow[Ex])
#                         else:
#                             # nanの場合
#                             ExrcHeader.append(Txt)
#                 # Log--------------------------------------------
#                 dt_s = datetime.datetime.now()
#                 dt_s = dt_s.strftime("%Y-%m-%d %H:%M:%S")
#                 logger.debug(dt_s + "_Excelシート読込完了")
#                 with open(LURL, "a") as f:
#                     print([dt_s, "Excelシート読込完了"], file=f)
#                 # -----------------------------------------------
#                 MainStarter(
#                     FolURL,
#                     TFolURL,
#                     Job.Img_dir,
#                     SerchURL,
#                     XLSDir,
#                     LURL,
#                     NameDF,
#                     ExSheet,
#                     ExrcHeader,
#                     isnItem,
#                     driver,
#                 )  # データ送信画面までの関数
#         print("MainStarter終了")
#         return True
#     except Exception as e:
#         logger.debug(e)
#         return False


def Main(self, Exc):
    try:
        # Log--------------------------------------------
        dt_s = datetime.datetime.now()
        dt_s = dt_s.strftime("%Y-%m-%d %H:%M:%S")
        logger.debug(dt_s + "_MJSシステム更新開始")
        # -----------------------------------------------
        BatUrl = FolURL + "/bat/AWADriverOpen.bat"  # 4724ポート指定でappiumサーバー起動バッチを開く
        driver = MJSOpen.MainFlow(
            BatUrl, FolURL, "RPAPhoto/MJS_DensiSinkoku"
        )  # MJSを起動しログイン後インスタンス化
        # driver = []
        FolURL = FolURL + "/RPAPhoto/MJS_DensiSinkoku"
        for fd_path, sb_folder, sb_file in os.walk(XLSDir):
            FDP = fd_path
            if not len(sb_folder) == 0:
                for sb_fileItem in sb_file:
                    print(sb_fileItem)
                    if (
                        "製本・電子ファイル印刷申請ミロク" in sb_fileItem
                        and not "製本・電子ファイル印刷申請ミロク(原本).xlsm" == sb_fileItem
                    ):
                        XLSURL = (
                            FDP + r"\\" + sb_fileItem.replace("~", "").replace("$", "")
                        )
                        MoveXLSURL = (
                            FDP
                            + r"\\MJSLog\\"
                            + sb_fileItem.replace("~", "").replace("$", "")
                        )
                        os.rename(XLSURL, MoveXLSURL)
                        MoveXLSURL = (
                            FDP + r"\\" + sb_fileItem.replace("~", "").replace("$", "")
                        )
                        XLSURL = (
                            FDP
                            + r"\\MJSLog\\"
                            + sb_fileItem.replace("~", "").replace("$", "")
                        )
                        open(LURL, "w").close()
                        Exlsx = EFA.XlsmRead(XLSURL)
                        if Exlsx[0] is True:
                            try:
                                MainFlow(
                                    FolURL,
                                    TFolURL,
                                    Job.Img_dir,
                                    SerchURL,
                                    XLSDir,
                                    LURL,
                                    Exlsx[1],
                                    driver,
                                    XLSURL,
                                )
                            except:
                                traceback.print_exc()
                            Exlsx = "閉じろや"
                            os.rename(XLSURL, MoveXLSURL)
                        else:
                            print("Excel読み込みエラー")
                            logger.debug("Excel読み込みエラー")
        return True
    except:
        return False


if __name__ == "__main__":
    global Start_Year  # 当年
    j = Job()

    # Log--------------------------------------------
    dt_s = datetime.datetime.now()
    dt_s = dt_s.strftime("%Y-%m-%d %H:%M:%S")
    logger.debug(dt_s + "_MJS決算書印刷開始")
    # -----------------------------------------------
    for fd_path, sb_folder, sb_file in os.walk(j.XLSDir):
        FDP = fd_path
        if not len(sb_folder) == 0:
            for sb_fileItem in sb_file:
                print(sb_fileItem)
                if (
                    "製本・電子ファイル印刷申請ミロク" in sb_fileItem
                    and not "製本・電子ファイル印刷申請ミロク(原本).xlsm" == sb_fileItem
                ):
                    XLSURL = FDP + r"\\" + sb_fileItem.replace("~", "").replace("$", "")
                    MoveXLSURL = (
                        FDP
                        + r"\\MJSLog\\"
                        + sb_fileItem.replace("~", "").replace("$", "")
                    )
                    os.rename(XLSURL, MoveXLSURL)
                    MoveXLSURL = (
                        FDP + r"\\" + sb_fileItem.replace("~", "").replace("$", "")
                    )
                    XLSURL = (
                        FDP
                        + r"\\MJSLog\\"
                        + sb_fileItem.replace("~", "").replace("$", "")
                    )
                    Ex_File = Sheet(XLSURL)
                    try:
                        j.MainFlow(Ex_File)
                    except:
                        traceback.print_exc()
                    print("stop")
                    os.rename(XLSURL, MoveXLSURL)
