import MySQLdb
import pandas as pd
import numpy as np
import datetime
import Function.SQLCSVOUTFunction as SQC

# loggerインポート
from logging import getLogger

logger = getLogger()
# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def MySQLGet(
    str_host, str_user, str_passwd, int_port, str_database, str_charset, sql
):  # host='ws77',user='SYSTEM',passwd='SYSTEM',port='3306',database='test_db',charset='utf8'
    # SQL文を送信し、結果を返す
    try:
        conn = MySQLdb.connect(
            host=str_host,
            user=str_user,
            passwd=str_passwd,
            port=int_port,
            database=str_database,
            charset=str_charset,
        )
        cursor = conn.cursor()
        cursor.execute(sql)  # select文を実行
        conn.commit()
        SqlData = cursor.fetchall()
        cursor.close()
        conn.close()
        logger.debug("MySQLGet(SQL文を送信し、結果を返す)完了: debug level log")
        return True, SqlData
    except:
        cursor.close()
        conn.close()
        logger.debug("MySQLGet(SQL文を送信し、結果を返す)失敗: debug level log")
        return False, "取得失敗"


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def MySQLHeaderTo_df(
    str_host, str_user, str_passwd, int_port, str_database, str_charset, sql
):  # host='ws77',user='SYSTEM',passwd='SYSTEM',port='3306',database='test_db',charset='utf8'
    # SQL文を送信し、結果をDFに格納
    try:
        conn = MySQLdb.connect(
            host=str_host,
            user=str_user,
            passwd=str_passwd,
            port=int_port,
            database=str_database,
            charset=str_charset,
        )
        cursor = conn.cursor()
        SqlData = pd.read_sql(sql, conn)
        cursor.close()
        conn.close()
        logger.debug("MySQLHeaderTo_df(SQL文を送信し、結果をDFに格納)完了: debug level log")
        return True, SqlData
    except:
        cursor.close()
        conn.close()
        logger.debug("MySQLHeaderTo_df(SQL文を送信し、結果をDFに格納)失敗: debug level log")
        return False, "取得失敗"


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def MySQLAct(
    str_host, str_user, str_passwd, int_port, str_database, str_charset, sql
):  # host='ws77',user='SYSTEM',passwd='SYSTEM',port='3306',database='test_db',charset='utf8'
    # SQL文を送信、結果をBooleanで返す
    try:
        conn = MySQLdb.connect(
            host=str_host,
            user=str_user,
            passwd=str_passwd,
            port=int_port,
            database=str_database,
            charset=str_charset,
        )
        cursor = conn.cursor()
        cursor.execute(sql)  # select文を実行
        conn.commit()
        cursor.close()
        conn.close()
        logger.debug("MySQLAct(SQL文を送信、結果をBooleanで返す)完了: debug level log")
        return True
    except:
        cursor.close()
        conn.close()
        logger.debug("MySQLAct(SQL文を送信、結果をBooleanで返す)失敗: debug level log")
        return False


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def MysqlColumnCheck(
    str_host, str_user, str_passwd, int_port, str_database, str_charset, TB, ColN
):  # host='ws77',user='SYSTEM',passwd='SYSTEM',port='3306',database='test_db',charset='utf8',テーブル名,列名
    # 引数のカラム名(ColN)と一致する引数テーブル(TB)のカラムのデータ型を返す
    try:
        sql = "show columns from " + TB
        conn = MySQLdb.connect(
            host=str_host,
            user=str_user,
            passwd=str_passwd,
            port=int_port,
            database=str_database,
            charset=str_charset,
        )
        cursor = conn.cursor()
        cursor.execute(sql)  # select文を実行
        conn.commit()
        SqlColumn = cursor.fetchall()
        cursor.close()
        conn.close()
        for SqlColumnItem in SqlColumn:
            if SqlColumnItem[0] == ColN:
                logger.debug(
                    "MysqlColumnCheck(引数のカラム名(ColN)と一致する引数テーブル(TB)のカラムのデータ型を返す)完了: debug level log"
                )
                return True, SqlColumnItem[1]
    except:
        cursor.close()
        conn.close()
        logger.debug(
            "MysqlColumnCheck(引数のカラム名(ColN)と一致する引数テーブル(TB)のカラムのデータ型を返す)失敗: debug level log"
        )
        return False, ""


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def MysqlColumnPic(
    str_host, str_user, str_passwd, int_port, str_database, str_charset, TB
):  # host='ws77',user='SYSTEM',passwd='SYSTEM',port='3306',database='test_db',charset='utf8',テーブル名,列名
    # テーブルのカラム情報をタプルで返す
    try:
        sql = "show columns from " + TB
        conn = MySQLdb.connect(
            host=str_host,
            user=str_user,
            passwd=str_passwd,
            port=int_port,
            database=str_database,
            charset=str_charset,
        )
        cursor = conn.cursor()
        cursor.execute(sql)  # select文を実行
        conn.commit()
        SqlColumn = cursor.fetchall()
        cursor.close()
        conn.close()
        logger.debug("MysqlColumnPic(テーブルのカラム情報をタプルで返す)完了: debug level log")
        return True, SqlColumn
    except:
        cursor.close()
        conn.close()
        logger.debug("MysqlColumnPic(テーブルのカラム情報をタプルで返す)失敗: debug level log")
        return False, ""


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def ChangeData(ColN, ParList, UDRowItem, TB):  # 列名,列名リスト,行データ,テーブル名
    # データ型に合わせて値を変更する。
    try:
        ColP = MysqlColumnCheck(
            "ws77", "SYSTEM", "SYSTEM", 3306, "test_db", "utf8", TB, ColN
        )
        if ColP[0] is True:
            SQLColP = ColP[1]
            TypeItem = str(type(UDRowItem))
            # データ型に合わせて値を変更----------------------------------------------------------------
            if "datetime" in SQLColP:
                if UDRowItem is None:  # Timestamp('2022-03-09 00:00:00')
                    FDATE = datetime.datetime.now()
                    FDATE = str(FDATE.strftime("%Y-%m-%d %H:%M:%S"))
                    # FDATE = "Timestamp('" + FDATE + "')"
                    ParList.append(FDATE)
                else:
                    if ColN == "dt_UpdtDT":
                        FDATE = datetime.datetime.now()
                        FDATE = str(FDATE.strftime("%Y-%m-%d %H:%M:%S"))
                        # FDATE = "Timestamp('" + FDATE + "')"
                        ParList.append(FDATE)
                    else:
                        ParList.append(UDRowItem)
            elif "char" in SQLColP:
                if UDRowItem == " ":
                    ParList.append("")
                elif UDRowItem == "　":
                    ParList.append("")
                elif UDRowItem == "  ":
                    ParList.append("")
                elif UDRowItem == "":
                    ParList.append("")
                elif UDRowItem == "":
                    ParList.append("")
                elif ColN == "vc_KnrCd":
                    ParList.append(UDRowItem.replace("  ", "").replace(" ", ""))
                elif ColN == "in_RrkNo_pk":
                    ParList.append(UDRowItem + 1)
                elif "int" in TypeItem:  # int判定で処理分け
                    ParList.append(
                        str(int(UDRowItem))
                        .replace("\u3000", "  ")
                        .replace("\u200b", " ")
                    )
                elif "float" in TypeItem:  # float判定で処理分け
                    if np.isnan(UDRowItem):  # nan判定で処理分け
                        ParList.append("")
                    else:
                        ParList.append(
                            str(int(UDRowItem))
                            .replace("\u3000", "  ")
                            .replace("\u200b", " ")
                            .replace(".0", "")
                        )
                else:
                    ParList.append(
                        str(UDRowItem).replace("\u3000", "  ").replace("\u200b", " ")
                    )

            elif "int" in SQLColP:
                if UDRowItem == " ":
                    ParList.append("")
                elif UDRowItem == "　":
                    ParList.append("")
                elif UDRowItem == "  ":
                    ParList.append("")
                elif ColN == "vc_KnrCd":
                    ParList.append(UDRowItem.replace("  ", "").replace(" ", ""))
                elif ColN == "in_RrkNo_pk":
                    ParList.append(UDRowItem + 1)
                elif "int" in TypeItem:  # int判定で処理分け
                    ParList.append(
                        str(int(UDRowItem))
                        .replace("\u3000", "  ")
                        .replace("\u200b", " ")
                    )
                elif "float" in TypeItem:  # float判定で処理分け
                    if np.isnan(UDRowItem):  # nan判定で処理分け
                        ParList.append("")
                    else:
                        ParList.append(
                            str(int(UDRowItem))
                            .replace("\u3000", "  ")
                            .replace("\u200b", " ")
                            .replace(".0", "")
                        )
                else:
                    ParList.append(int(UDRowItem))
            else:
                if UDRowItem == " ":
                    ParList.append("")
                elif UDRowItem == "　":
                    ParList.append("")
                elif UDRowItem == "  ":
                    ParList.append("")
                elif ColN == "vc_KnrCd":
                    ParList.append(UDRowItem.replace("  ", "").replace(" ", ""))
                elif ColN == "in_RrkNo_pk":
                    ParList.append(UDRowItem + 1)
                elif "int" in TypeItem:  # int判定で処理分け
                    ParList.append(
                        str(int(UDRowItem))
                        .replace("\u3000", "  ")
                        .replace("\u200b", " ")
                    )
                elif "float" in TypeItem:  # float判定で処理分け
                    if np.isnan(UDRowItem):  # nan判定で処理分け
                        ParList.append("")
                    else:
                        ParList.append(
                            str(int(UDRowItem))
                            .replace("\u3000", "  ")
                            .replace("\u200b", " ")
                            .replace(".0", "")
                        )
                else:
                    ParList.append(UDRowItem)
            logger.debug(
                "ChangeData(引数で渡したTBのカラムに応じたデータ型に合わせて値を変更する。)完了: debug level log"
            )
            return ParList
        else:
            logger.debug(
                "ChangeData(引数で渡したTBのカラムに応じたデータ型に合わせて値を変更する。)テーブルカラム取得失敗: debug level log"
            )
            print("テーブルカラム取得失敗")
            return False
    except:
        logger.debug(
            "ChangeData(引数で渡したTBのカラムに応じたデータ型に合わせて値を変更する。)exceptエラー: debug level log"
        )
        print("exceptエラー")
        return False


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def MysqlDiffUp(MTB, CTB, UDRow):  # 元TB名,履歴TB名,更新行データ
    try:
        # 履歴テーブルにコピー-------------------------------------------------------------------------------------------------------------------------------------
        sql = "SELECT * FROM " + MTB  # SELECT分を代入
        DFCol = MysqlColumnPic(
            "ws77", "SYSTEM", "SYSTEM", 3306, "test_db", "utf8", MTB
        )[
            1
        ]  # 関数でTB列情報取得
        ColList = []  # データ型変帝の為のカラムリストを作成
        ParList = []  # SQL結合用に行データ格納用のリスト作成
        for DFColItem in DFCol:  # Rowデータのデータ型に併せて値を変更
            ColList.append(DFColItem[0])  # DFから列名のみ抽出
        ColRow = 0  # カラムリストのRowIndex初期化
        for UDRowItem in UDRow:  # 行データひとつずつループ
            ColN = ColList[ColRow]  # カラムリストから列名取得
            ChangeData(ColN, ParList, UDRowItem, MTB)  # 列名,行データ格納用のリスト,行データ要素,TB名
            ColRow = ColRow + 1  # カラムリストのRowIndex加算
        FColList = str(ColList)  # SQL文用列名リストの作成
        FColList = FColList.replace("'", "")  # 不要なのでシングルコーテーション削除
        sql = (
            "INSERT INTO "
            + CTB
            + " SELECT * FROM "
            + MTB
            + " WHERE vc_KnrCd='"
            + UDRow["vc_KnrCd"].replace("  ", "").replace(" ", "")
            + "'"
        )  # 変更対象を履歴DBにコピー
        MySQLAct(
            "ws77", "SYSTEM", "SYSTEM", 3306, "test_db", "utf8", sql
        )  # 引数8=親TB名,引数9=履歴数列名
        sql = (
            "SELECT * FROM "
            + MTB
            + " WHERE vc_KnrCd="
            + UDRow["vc_KnrCd"].replace("  ", "").replace(" ", "")
        )  # 変更対象を履歴DBにコピー
        # -------------------------------------------------------------------------------------------------------------------------------------------------------
        # マスターテーブルを差分更新--------------------------------------------------------------------------------------------------------------------------------
        SQLData = MySQLHeaderTo_df(
            "ws77", "SYSTEM", "SYSTEM", 3306, "test_db", "utf8", sql
        )[
            1
        ]  # マスターの最新レコードをDF化
        SQLDataRow = np.array(SQLData).shape[0]  # DF行数取得
        if SQLDataRow == 1:
            SQLDataSingle = SQLData.iloc[0, :]  # DF行データ取得
            ColRow = 0  # カラムリストのRowIndex初期化
            for ColListItem in ColList:  # 行データひとつずつループ
                ColN = ColList[ColRow]  # カラムリストから列名取得
                if SQLDataSingle[ColN] == ParList[ColRow]:
                    sql = ""
                else:
                    DataType = type(ParList[ColRow])  # 値の型検出
                    if ParList[ColRow] == "":
                        sql = (
                            "UPDATE "
                            + MTB
                            + " SET "
                            + ColN
                            + "=''"
                            + " WHERE vc_KnrCd='"
                            + UDRow["vc_KnrCd"].replace("  ", "").replace(" ", "")
                            + "'"
                        )  # 変更対象を履歴DBにコピー
                    else:
                        if "str" in str(DataType):
                            sql = (
                                "UPDATE "
                                + MTB
                                + " SET "
                                + ColN
                                + "='"
                                + str(ParList[ColRow])
                                + "' WHERE vc_KnrCd='"
                                + UDRow["vc_KnrCd"].replace("  ", "").replace(" ", "")
                                + "'"
                            )  # 変更対象を履歴DBにコピー
                        else:
                            sql = (
                                "UPDATE "
                                + MTB
                                + " SET "
                                + ColN
                                + "="
                                + str(ParList[ColRow])
                                + " WHERE vc_KnrCd='"
                                + UDRow["vc_KnrCd"].replace("  ", "").replace(" ", "")
                                + "'"
                            )  # 変更対象を履歴DBにコピー
                    sql = sql.replace("[", "").replace("]", "")
                    MySQLAct(
                        "ws77", "SYSTEM", "SYSTEM", 3306, "test_db", "utf8", sql
                    )  # 引数8=親TB名,引数9=履歴数列名
                    sql = ""
                ColRow = ColRow + 1
            return True
        else:
            print("マスターに重複があります。")
            return False
    except:
        return False


# -------------------------------------------------------------------------------------------------------------------
def SQLIn(ws):  # Excelデータを履歴テーブルにインサート
    try:
        LenRow = np.array(ws).shape[0]  # dfインスタンスの行数取得
        ColNS = MysqlColumnPic(
            "ws77", "SYSTEM", "SYSTEM", 3306, "test_db", "utf8", "m_kfmsrireki"
        )
        ColN = []
        NewColNS = MysqlColumnPic(
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
            DBSQL = MySQLGet("ws77", "SYSTEM", "SYSTEM", 3306, "test_db", "utf8", sql)
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
            MaxRrkNo = MySQLGet(
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
                ChangeData("vc_gyou", ParList, "", "m_kfmsrireki")
                ParList.append(MaxRrkNo)
                ChangeData("vc_FMSKnrCd", ParList, wscd, "m_kfmsrireki")
                ChangeData("vc_Name", ParList, wsRow["個人名"], "m_kfmsrireki")
                ChangeData("vc_KName", ParList, wsRow["関与先名"], "m_kfmsrireki")
                ChangeData("vc_Hakkou", ParList, wsRow["発送方法"], "m_kfmsrireki")
                ChangeData("vc_SousinK", ParList, wsRow["送信方法"], "m_kfmsrireki")
                ChangeData("vc_Mail", ParList, wsRow["アドレス"], "m_kfmsrireki")
                ChangeData("vc_BmnCd_pk", ParList, wsRow["課No"], "m_kfmsrireki")
                ChangeData("vc_BmnNm", ParList, wsRow["課"], "m_kfmsrireki")
                ChangeData("vc_KansaTantouNo", ParList, wsRow["監査担当No"], "m_kfmsrireki")
                ChangeData("vc_KansaTantou", ParList, wsRow["監査担当"], "m_kfmsrireki")
                ChangeData("vc_SubTantouNo", ParList, wsRow["サブNo"], "m_kfmsrireki")
                ChangeData("vc_SubTantou", ParList, wsRow["サブ"], "m_kfmsrireki")
                ChangeData(
                    "vc_Sub_SubTantouNo", ParList, wsRow["サブ2No"], "m_kfmsrireki"
                )
                ChangeData("vc_Sub_SubTantou", ParList, wsRow["サブ2"], "m_kfmsrireki")
                ChangeData("vc_SousinK2", ParList, wsRow["送信方法2"], "m_kfmsrireki")
                ChangeData("vc_Mail2", ParList, wsRow["アドレス2"], "m_kfmsrireki")
                ChangeData("vc_SousinK3", ParList, wsRow["送信方法3"], "m_kfmsrireki")
                ChangeData("vc_Mail3", ParList, wsRow["アドレス3"], "m_kfmsrireki")
                ChangeData("vc_SousinK4", ParList, wsRow["送信方法4"], "m_kfmsrireki")
                ChangeData("vc_Mail4", ParList, wsRow["アドレス4"], "m_kfmsrireki")
                ChangeData("vc_SousinK5", ParList, wsRow["送信方法5"], "m_kfmsrireki")
                ChangeData("vc_Mail5", ParList, wsRow["アドレス5"], "m_kfmsrireki")
                ChangeData("cr_RecKbn", ParList, 0, "m_kfmsrireki")
                ChangeData("dt_InstDT", ParList, wsRow["入力日時"], "m_kfmsrireki")
                ChangeData("dt_UpdtDT", ParList, "", "m_kfmsrireki")
                ChangeData("vc_inputuser", ParList, wsRow["入力ユーザー"], "m_kfmsrireki")
                ChangeData("vc_beforeadd", ParList, wsRow["変更前アドレス"], "m_kfmsrireki")
                # ----------------------------------------------------------------------------------------------------------
            else:
                # テーブルのデータ型に合わせて値を格納したリストを作成---------------------------------------------------------------
                ChangeData("vc_KnrCd", NewParList, Leftwscd, "m_kfmsmail")
                if len(Rightwscd) == 0:
                    ChangeData("vc_KanKojinNo_pk", NewParList, "", "m_kfmsmail")
                else:
                    ChangeData("vc_KanKojinNo_pk", NewParList, Rightwscd, "m_kfmsmail")
                NewParList.append(MaxRrkNo)
                ChangeData("vc_FMSKnrCd", NewParList, wscd, "m_kfmsmail")
                NewParList.append("")  # ｶﾅ不要なので空白
                ChangeData("vc_Name", NewParList, wsRow["個人名"], "m_kfmsmail")
                ChangeData("vc_KName", NewParList, wsRow["関与先名"], "m_kfmsmail")
                ChangeData("vc_Hakkou", NewParList, wsRow["発送方法"], "m_kfmsmail")
                if wsRow["発送方法"] == "メール":
                    ChangeData("vc_PDFName", NewParList, "締日_請求元名_今回請求額", "m_kfmsmail")
                else:
                    ChangeData(
                        "vc_PDFName", NewParList, "締日_関与先ｺｰﾄﾞ_請求元ｺｰﾄﾞ", "m_kfmsmail"
                    )
                ChangeData("vc_SousinK", NewParList, wsRow["送信方法"], "m_kfmsmail")
                ChangeData("vc_Mail", NewParList, wsRow["アドレス"], "m_kfmsmail")
                ChangeData("vc_SousinK2", NewParList, wsRow["送信方法2"], "m_kfmsmail")
                ChangeData("vc_Mail2", NewParList, wsRow["アドレス2"], "m_kfmsmail")
                ChangeData("vc_SousinK3", NewParList, wsRow["送信方法3"], "m_kfmsmail")
                ChangeData("vc_Mail3", NewParList, wsRow["アドレス3"], "m_kfmsmail")
                ChangeData("vc_SousinK4", NewParList, wsRow["送信方法4"], "m_kfmsmail")
                ChangeData("vc_Mail4", NewParList, wsRow["アドレス4"], "m_kfmsmail")
                ChangeData("vc_SousinK5", NewParList, wsRow["送信方法5"], "m_kfmsmail")
                ChangeData("vc_Mail5", NewParList, wsRow["アドレス5"], "m_kfmsmail")
                ChangeData("cr_RecKbn", NewParList, 0, "m_kfmsmail")
                ChangeData("dt_InstDT", NewParList, wsRow["入力日時"], "m_kfmsmail")
                ChangeData("dt_UpdtDT", NewParList, "", "m_kfmsmail")
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
                MySQLAct("ws77", "SYSTEM", "SYSTEM", 3306, "test_db", "utf8", Newsql)
                SQC.MailRirekiUp()
                SQC.MailListUp()
                NewParList = []
            MySQLAct("ws77", "SYSTEM", "SYSTEM", 3306, "test_db", "utf8", sql)
            SQC.MailRirekiUp()
            SQC.MailListUp()
            ParList = []
        return True
    except:
        return False


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# MysqlDiffUp(MTB,CTB,UDRow):の使い方↓

# sql = 'SELECT * FROM m_kfmsmail'#SELECT分を代入
# KFM = MySQLHeaderTo_df('ws77','SYSTEM','SYSTEM',3306,'test_db','utf8',sql)[1]#関数でクエリ結果をDF化
# KFMRow = np.array(KFM).shape[0]#DF行数取得
# for x in range(KFMRow):#DF分ループ
#     KFMData = KFM.iloc[x,:]#DF行データ取得
#     ITB = 'm_kfmsmailrireki'#テーブル名を代入
#     ColRow = 0
#     MysqlDiffUp('m_kfmsmail',ITB,KFMData) #元TB名,履歴TB名,更新行データ
