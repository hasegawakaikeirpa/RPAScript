# モジュールインポート
# 配列計算関数numpyインポート
import numpy as np

# osインポート
import os

# datetimeインポート
from datetime import datetime as dt

# 例外処理判定の為のtracebackインポート
import traceback

# pandas(pd)で関与先データCSVを取得
import Function.ExcelFileAction as EF
import calendar
import Function.SQLConnect as SQ
import Function.SQLCSVOUTFunction as FSQC

# logger設定------------------------------------------------------------------------------------------------------------
import logging.config

logging.config.fileConfig(r"LogConf\logging_debug.conf")
logger = logging.getLogger(__name__)
# ----------------------------------------------------------------------------------------------------------------------
def CSVOutFind(wsRow, LogList):  # 登録ログに同一データがないかチェック
    try:
        # 行データから変数格納----------------------------------------------------------------------------------------
        wscd = wsRow["コード"]
        wsAd = wsRow["アドレス"]
        wsNyuu = wsRow["入力日時"]

        # ----------------------------------------------------------------------------------------------------------
        CSVLenRow = np.array(LogList).shape[0]  # dfインスタンスの行数取得
        for x in range(CSVLenRow):
            CSVRow = LogList.iloc[x]  # dfインスタンスの行データ
            # 行データから変数格納----------------------------------------------------------------------------------------
            CSVcd = CSVRow["コード"]
            CSVAd = CSVRow["アドレス"]
            CSVNyuu = CSVRow["入力日時"]
            # 文字列日付をDate格納----------------------------------------------------------------------------------------
            try:
                CSVNyuu = dt.strptime(CSVNyuu, "%Y/%m/%d %H:%M")
            except:
                try:
                    CSVNyuu = dt.strptime(CSVNyuu, "%Y/%m/%d %H:%M:%S")
                except:
                    try:
                        CSVNyuu = dt.strptime(CSVNyuu, "%Y-%m-%d %H:%M:%S")
                    except:
                        CSVNyuu = dt.strptime(CSVNyuu, "%Y-%m-%d %H:%M")
            # ----------------------------------------------------------------------------------------------------------
            if wscd == CSVcd:  # 登録済みリストに同一コードがあったら
                if wsAd == CSVAd:  # 登録済みリストに同一アドレスがあったら
                    if wsNyuu == CSVNyuu:  # 登録済みリストと同一の登録日時なら
                        return True
                else:
                    if wsNyuu > CSVNyuu:  # 登録済みリストより後の登録日時なら
                        return False
        return False
    except:
        return False


# ----------------------------------------------------------------------------------------------------------------------
def SQLIn(ws):  # Excelデータを履歴テーブルにインサート
    try:
        LenRow = np.array(ws).shape[0]  # dfインスタンスの行数取得
        ColNS = SQ.MysqlColumnPic(
            "ws77", "SYSTEM", "SYSTEM", 3306, "test_db", "utf8", "m_kfmsrireki"
        )
        ColN = []
        NewColNS = SQ.MysqlColumnPic(
            "ws77", "SYSTEM", "SYSTEM", 3306, "test_db", "utf8", "m_kfmsmail"
        )
        NewColN = []
        # テーブルのカラム情報より列名リスト作成-------------------------------------------------------------------------
        for ColNSItem in ColNS[1]:
            ColN.append(ColNSItem[0])
        for NewColNSSItem in NewColNS[1]:
            NewColN.append(NewColNSSItem[0])
        # -----------------------------------------------------------------------------------------------------------
        ParList = []
        NewParList = []
        for x in range(LenRow):
            wsRow = ws.iloc[x]  # dfインスタンスの行データ
            wscd = str(wsRow["コード"])
            wscdType = type(wscd)
            wscdFlag = False
            if int(wscd) < 100:
                wscdFlag = True
                if wscdType is str:
                    wscd = f"{int(wscd):03}"
            # 元DBへの存在チェック-----------------------------------------------------------------------------------------
            sql = "SELECT * FROM m_kfmsmail WHERE vc_FMSKnrCd = '" + wscd + "';"
            DBSQL = SQ.MySQLGet(
                "ws77", "SYSTEM", "SYSTEM", 3306, "test_db", "utf8", sql
            )
            if len(DBSQL[1]) == 0:
                DBCHECK = False
            else:
                DBCHECK = True
            # -----------------------------------------------------------------------------------------------------------
            # WHERE社内コードでDBよりMAX(履歴No)を抽出-------------------------------------------------------------------------
            if wscdFlag is False:
                Maxsql = (
                    "SELECT MAX(in_RrkNo_pk) FROM m_kfmsrireki WHERE vc_FMSKnrCd = "
                    + str(wscd)
                    + ";"
                )
            else:
                Maxsql = (
                    "SELECT MAX(in_RrkNo_pk) FROM m_kfmsrireki WHERE vc_FMSKnrCd = "
                    + wscd
                    + ";"
                )
            MaxRrkNo = SQ.MySQLGet(
                "ws77", "SYSTEM", "SYSTEM", 3306, "test_db", "utf8", Maxsql
            )
            if MaxRrkNo[0] is True:
                print(MaxRrkNo[1])
                if MaxRrkNo[1] == ((None,),):
                    MaxRrkNo = 1
                else:
                    Mstr = str(MaxRrkNo[1]).replace("((", "").replace(",),)", "")
                    MaxRrkNo = int(Mstr) + 1
            else:
                MaxRrkNo = 1
            wscdLen = len(wscd)
            wscdType = type(wscd)
            if wscdLen == 3:
                if wscdType is str:
                    Fwscd = f"{int(wscd):04}"
                else:
                    Fwscd = f"{wscd:04}"
                Leftwscd = Fwscd[:4]
            elif wscdLen == 5:
                if wscdType is str:
                    Fwscd = f"{int(wscd):06}"
                else:
                    Fwscd = f"{wscd:06}"
                Leftwscd = Fwscd[:4]
                Rightwscd = Fwscd[4:]
            if DBCHECK is True:
                # テーブルのデータ型に合わせて値を格納したリストを作成---------------------------------------------------------------
                SQ.ChangeData("vc_gyou", ParList, "", "m_kfmsrireki")
                ParList.append(MaxRrkNo)
                SQ.ChangeData("vc_FMSKnrCd", ParList, wscd, "m_kfmsrireki")
                SQ.ChangeData("vc_Name", ParList, wsRow["個人名"], "m_kfmsrireki")
                SQ.ChangeData("vc_KName", ParList, wsRow["関与先名"], "m_kfmsrireki")
                SQ.ChangeData("vc_Hakkou", ParList, wsRow["発送方法"], "m_kfmsrireki")
                SQ.ChangeData("vc_SousinK", ParList, wsRow["送信方法"], "m_kfmsrireki")
                SQ.ChangeData("vc_Mail", ParList, wsRow["アドレス"], "m_kfmsrireki")
                SQ.ChangeData("vc_BmnCd_pk", ParList, wsRow["課No"], "m_kfmsrireki")
                SQ.ChangeData("vc_BmnNm", ParList, wsRow["課"], "m_kfmsrireki")
                SQ.ChangeData(
                    "vc_KansaTantouNo", ParList, wsRow["監査担当No"], "m_kfmsrireki"
                )
                SQ.ChangeData("vc_KansaTantou", ParList, wsRow["監査担当"], "m_kfmsrireki")
                SQ.ChangeData("vc_SubTantouNo", ParList, wsRow["サブNo"], "m_kfmsrireki")
                SQ.ChangeData("vc_SubTantou", ParList, wsRow["サブ"], "m_kfmsrireki")
                SQ.ChangeData(
                    "vc_Sub_SubTantouNo", ParList, wsRow["サブ2No"], "m_kfmsrireki"
                )
                SQ.ChangeData("vc_Sub_SubTantou", ParList, wsRow["サブ2"], "m_kfmsrireki")
                SQ.ChangeData("vc_SousinK2", ParList, wsRow["送信方法2"], "m_kfmsrireki")
                SQ.ChangeData("vc_Mail2", ParList, wsRow["アドレス2"], "m_kfmsrireki")
                SQ.ChangeData("vc_SousinK3", ParList, wsRow["送信方法3"], "m_kfmsrireki")
                SQ.ChangeData("vc_Mail3", ParList, wsRow["アドレス3"], "m_kfmsrireki")
                SQ.ChangeData("vc_SousinK4", ParList, wsRow["送信方法4"], "m_kfmsrireki")
                SQ.ChangeData("vc_Mail4", ParList, wsRow["アドレス4"], "m_kfmsrireki")
                SQ.ChangeData("vc_SousinK5", ParList, wsRow["送信方法5"], "m_kfmsrireki")
                SQ.ChangeData("vc_Mail5", ParList, wsRow["アドレス5"], "m_kfmsrireki")
                SQ.ChangeData("cr_RecKbn", ParList, 0, "m_kfmsrireki")
                SQ.ChangeData("dt_InstDT", ParList, wsRow["入力日時"], "m_kfmsrireki")
                SQ.ChangeData("dt_UpdtDT", ParList, "", "m_kfmsrireki")
                SQ.ChangeData("vc_inputuser", ParList, wsRow["入力ユーザー"], "m_kfmsrireki")
                SQ.ChangeData("vc_beforeadd", ParList, wsRow["変更前アドレス"], "m_kfmsrireki")
                # ----------------------------------------------------------------------------------------------------------
            else:
                # テーブルのデータ型に合わせて値を格納したリストを作成---------------------------------------------------------------
                SQ.ChangeData("vc_KnrCd", NewParList, Leftwscd, "m_kfmsmail")
                if len(Rightwscd) == 0:
                    SQ.ChangeData("vc_KanKojinNo_pk", NewParList, "", "m_kfmsmail")
                else:
                    SQ.ChangeData(
                        "vc_KanKojinNo_pk", NewParList, Rightwscd, "m_kfmsmail"
                    )
                NewParList.append(MaxRrkNo)
                SQ.ChangeData("vc_FMSKnrCd", NewParList, wscd, "m_kfmsmail")
                NewParList.append("")  # ｶﾅ不要なので空白
                SQ.ChangeData("vc_Name", NewParList, wsRow["個人名"], "m_kfmsmail")
                SQ.ChangeData("vc_KName", NewParList, wsRow["関与先名"], "m_kfmsmail")
                SQ.ChangeData("vc_Hakkou", NewParList, wsRow["発送方法"], "m_kfmsmail")
                if wsRow["発送方法"] == "メール":
                    SQ.ChangeData(
                        "vc_PDFName", NewParList, "締日_請求元名_今回請求額", "m_kfmsmail"
                    )
                else:
                    SQ.ChangeData(
                        "vc_PDFName", NewParList, "締日_関与先ｺｰﾄﾞ_請求元ｺｰﾄﾞ", "m_kfmsmail"
                    )
                SQ.ChangeData("vc_SousinK", NewParList, wsRow["送信方法"], "m_kfmsmail")
                SQ.ChangeData("vc_Mail", NewParList, wsRow["アドレス"], "m_kfmsmail")
                SQ.ChangeData("vc_SousinK2", NewParList, wsRow["送信方法2"], "m_kfmsmail")
                SQ.ChangeData("vc_Mail2", NewParList, wsRow["アドレス2"], "m_kfmsmail")
                SQ.ChangeData("vc_SousinK3", NewParList, wsRow["送信方法3"], "m_kfmsmail")
                SQ.ChangeData("vc_Mail3", NewParList, wsRow["アドレス3"], "m_kfmsmail")
                SQ.ChangeData("vc_SousinK4", NewParList, wsRow["送信方法4"], "m_kfmsmail")
                SQ.ChangeData("vc_Mail4", NewParList, wsRow["アドレス4"], "m_kfmsmail")
                SQ.ChangeData("vc_SousinK5", NewParList, wsRow["送信方法5"], "m_kfmsmail")
                SQ.ChangeData("vc_Mail5", NewParList, wsRow["アドレス5"], "m_kfmsmail")
                SQ.ChangeData("cr_RecKbn", NewParList, 0, "m_kfmsmail")
                SQ.ChangeData("dt_InstDT", NewParList, wsRow["入力日時"], "m_kfmsmail")
                SQ.ChangeData("dt_UpdtDT", NewParList, "", "m_kfmsmail")
                # ----------------------------------------------------------------------------------------------------------
            ParList = str(ParList).replace("[", "").replace("]", "").replace("nan", "")
            NewParList = (
                str(ParList).replace("[", "").replace("]", "").replace("nan", "")
            )
            ColN = str(ColN).replace("[", "").replace("]", "").replace("'", "")
            NewColN = str(NewColN).replace("[", "").replace("]", "").replace("'", "")
            if DBCHECK is True:
                sql = "INSERT INTO m_kfmsrireki (" + ColN + ") VALUES(" + ParList + ");"
            else:
                sql = (
                    "INSERT INTO m_kfmsmail ("
                    + NewColN
                    + ") VALUES("
                    + NewParList
                    + ");"
                )
                Newsql = (
                    "INSERT INTO m_kfmsrireki (" + ColN + ") VALUES(" + ParList + ");"
                )
                SQ.MySQLAct("ws77", "SYSTEM", "SYSTEM", 3306, "test_db", "utf8", Newsql)
                FSQC.MailRirekiUp()
                FSQC.MailListUp()
                NewParList = []
            SQ.MySQLAct("ws77", "SYSTEM", "SYSTEM", 3306, "test_db", "utf8", sql)
            FSQC.MailRirekiUp()
            FSQC.MailListUp()
            ParList = []
        return True
    except:
        return False


# ----------------------------------------------------------------------------------------------------------------------
def MainFlow(FolURL2, Lday):
    FolURL2 = FolURL2 + "/RPAPhoto/TKCCDBMailAddressUpdate"  # RPA用画像保管フォルダを指定
    # XlsmURL = r"\\Sv05121a\e\C 作業台\請求書メールアドレス収集\アドレス新規登録シート.xlsm"  # アドレス登録シートを指定
    XlsmURL = r"D:\アドレス新規登録シート.xlsm"  # アドレス登録シートを指定
    XlsmURL = XlsmURL.replace("\\", "/")  # URLリネーム
    # エクセルブックを読込------------------------------------------------------------------------------------------------
    logger.debug("エクセルブックを読込")
    XlsmList = EF.XlsmRead(XlsmURL)
    input_book = XlsmList[1]
    # sheet_namesメソッドでExcelブック内の各シートの名前をリストで取得できる
    input_sheet_name = input_book.sheet_names
    # lenでシートの総数を確認
    num_sheet = len(input_sheet_name)
    # シートの数とシートの名前のリストの表示
    print("Sheet の数:", num_sheet)
    print(input_sheet_name)
    x = 0
    for isnItem in input_sheet_name:
        if isnItem == "アドレス登録":
            ws = input_book.parse(input_sheet_name[x], dtype=str)
            print(ws)
            break
        x = x + 1
    ws = ws.sort_values("入力日時", ascending=False)  # 入力日時順に並び替え
    ws = ws.drop_duplicates(subset="コード")  # コードで重複削除
    print(ws)
    logger.debug("Excelデータを履歴テーブルにインサート")
    SQLIn(ws)
    # ----------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------
# RPA用画像フォルダの作成-----------------------------------------------------------
Lday = calendar.monthrange(dt.today().year, dt.today().month)
FolURL2 = os.getcwd().replace("\\", "/")  # 先
# --------------------------------------------------------------------------------
try:
    MF = MainFlow(FolURL2, Lday)
except:
    traceback.print_exc()
