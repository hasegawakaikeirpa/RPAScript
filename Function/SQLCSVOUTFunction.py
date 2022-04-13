import SQLConnect as SQ

# loggerインポート
from logging import getLogger

logger = getLogger()


def KanyoUp():
    # 関与先データベースをCSVアウト-------------------------------------------------------
    sql = "SELECT * FROM m_kkanyo"
    URL = r"\\Sv05121a\e\C 作業台\RPA\ALLDataBase\m_kkanyo.csv"
    URL = URL.replace("\\", "/")

    SQDF = SQ.MySQLHeaderTo_df(
        "ws77", "SYSTEM", "SYSTEM", 3306, "test_db", "utf8", sql
    )[1]
    SQDF.to_csv(URL, index=False)
    logger.debug("関与先データベースをCSVアウト: debug level log")


def SyainUp():
    # 社員情報をCSVアウト----------------------------------------------------------------
    sql = "SELECT * FROM m_syain"
    URL = r"\\Sv05121a\e\C 作業台\RPA\ALLDataBase\m_syain.csv"
    URL = URL.replace("\\", "/")

    SQDF = SQ.MySQLHeaderTo_df(
        "ws77", "SYSTEM", "SYSTEM", 3306, "test_db", "utf8", sql
    )[1]
    SQDF.to_csv(URL, index=False)
    logger.debug("社員情報をCSVアウト: debug level log")


def MailListUp():
    # FMSMAILLISTをCSVアウト------------------------------------------------------------
    WithA = "WITH MAIN AS (SELECT * FROM m_kfmsmail),"
    WithB = "RIREKI AS (SELECT * FROM m_kfmsrireki AS m WHERE NOT EXISTS \
    (SELECT * FROM m_kfmsrireki AS s WHERE m.vc_FMSKnrCd = s.vc_FMSKnrCd AND m.in_RrkNo_pk < s.in_RrkNo_pk)),"
    WithC = "SubFMS AS (SELECT * FROM m_kfmsmail WHERE cr_RecKbn = '0' GROUP BY vc_FMSKnrCd),"
    WithD = (
        "SubKan AS (SELECT * FROM m_kkanyo WHERE cr_RecKbn = '0' GROUP BY vc_KnrCd),"
    )
    WithE = "SubMix AS (SELECT F.vc_KnrCd,F.vc_KanKojinNo_pk,F.vc_FMSKnrCd,F.vc_Name,K.vc_Name AS 'Yago',\
    K.vc_HaizokuNo,K.vc_Haizoku,K.vc_KansaTantouNo,K.vc_KansaTantou,\
    K.vc_SubTantouNo,K.vc_SubTantou,K.vc_Sub_SubTantouNo,K.vc_Sub_SubTantou,\
    F.vc_Hakkou,F.vc_PDFName,F.vc_SousinK,F.vc_Mail,F.vc_SousinK2,F.vc_Mail2,\
    F.vc_SousinK3,F.vc_Mail3,F.vc_SousinK4,F.vc_Mail4,F.vc_SousinK5,F.vc_Mail5 FROM SubFMS F \
    INNER JOIN SubKan K ON F.vc_KnrCd = K.vc_KnrCd)"
    SelectStr = " SELECT SM.vc_KnrCd,SM.vc_KanKojinNo_pk,SM.vc_FMSKnrCd,\
    CASE WHEN R.vc_Name IS NOT NULL THEN R.vc_Name ELSE SM.vc_Name END AS vc_Name,\
    SM.Yago,SM.vc_HaizokuNo,SM.vc_Haizoku,\
    CASE WHEN R.vc_KansaTantouNo IS NOT NULL THEN R.vc_KansaTantouNo ELSE SM.vc_KansaTantouNo END AS vc_KansaTantouNo,\
    CASE WHEN R.vc_KansaTantou IS NOT NULL THEN R.vc_KansaTantou ELSE SM.vc_KansaTantou END AS vc_KansaTantou,\
    CASE WHEN R.vc_SubTantouNo IS NOT NULL THEN R.vc_SubTantouNo ELSE SM.vc_SubTantouNo END AS vc_SubTantouNo,\
    CASE WHEN R.vc_SubTantou IS NOT NULL THEN R.vc_SubTantou ELSE SM.vc_SubTantou END AS vc_SubTantou,\
    CASE WHEN R.vc_Sub_SubTantouNo IS NOT NULL THEN R.vc_Sub_SubTantouNo ELSE SM.vc_Sub_SubTantouNo END AS vc_Sub_SubTantouNo,\
    CASE WHEN R.vc_Sub_SubTantou IS NOT NULL THEN R.vc_Sub_SubTantou ELSE SM.vc_Sub_SubTantou END AS vc_Sub_SubTantou,\
    CASE WHEN R.vc_Hakkou IS NOT NULL THEN R.vc_Hakkou ELSE SM.vc_Hakkou END AS vc_Hakkou,\
    SM.vc_PDFName,\
    CASE WHEN R.vc_SousinK IS NOT NULL THEN R.vc_SousinK ELSE SM.vc_SousinK END AS vc_SousinK,\
    CASE WHEN R.vc_Mail IS NOT NULL THEN R.vc_Mail ELSE SM.vc_Mail END AS vc_Mail,\
    CASE WHEN R.vc_SousinK2 IS NOT NULL THEN R.vc_SousinK2 ELSE SM.vc_SousinK2 END AS vc_SousinK2,\
    CASE WHEN R.vc_Mail2 IS NOT NULL THEN R.vc_Mail2 ELSE SM.vc_Mail2 END AS vc_Mail2,\
    CASE WHEN R.vc_SousinK3 IS NOT NULL THEN R.vc_SousinK3 ELSE SM.vc_SousinK3 END AS vc_SousinK3,\
    CASE WHEN R.vc_Mail3 IS NOT NULL THEN R.vc_Mail3 ELSE SM.vc_Mail3 END AS vc_Mail3,\
    CASE WHEN R.vc_SousinK4 IS NOT NULL THEN R.vc_SousinK4 ELSE SM.vc_SousinK4 END AS vc_SousinK4,\
    CASE WHEN R.vc_Mail4 IS NOT NULL THEN R.vc_Mail4 ELSE SM.vc_Mail4 END AS vc_Mail4,\
    CASE WHEN R.vc_SousinK5 IS NOT NULL THEN R.vc_SousinK5 ELSE SM.vc_SousinK5 END AS vc_SousinK5,\
    CASE WHEN R.vc_Mail5 IS NOT NULL THEN R.vc_Mail5 ELSE SM.vc_Mail5 END AS vc_Mail5\
    FROM SubMix SM LEFT JOIN RIREKI R ON SM.vc_FMSKnrCd = R.vc_FMSKnrCd;"
    sql = WithA + WithB + WithC + WithD + WithE + SelectStr
    URL = r"\\Sv05121a\e\C 作業台\RPA\ALLDataBase\m_kfmsmail.csv"
    URL = URL.replace("\\", "/")

    SQDF = SQ.MySQLHeaderTo_df(
        "ws77", "SYSTEM", "SYSTEM", 3306, "test_db", "utf8", sql
    )[1]
    SQDF.to_csv(URL, index=False)
    logger.debug("FMSMAILLISTをCSVアウト完了: debug level log")


def MailRirekiUp():
    # メアド変更履歴をCSVアウト---------------------------------------------------------
    sql = "SELECT * FROM m_kfmsrireki AS m WHERE NOT EXISTS (SELECT * FROM m_kfmsrireki AS s WHERE m.vc_FMSKnrCd = s.vc_FMSKnrCd AND m.in_RrkNo_pk < s.in_RrkNo_pk);"
    URL = r"\\Sv05121a\e\C 作業台\RPA\ALLDataBase\m_kfmsrireki.csv"
    URL = URL.replace("\\", "/")

    SQDF = SQ.MySQLHeaderTo_df(
        "ws77", "SYSTEM", "SYSTEM", 3306, "test_db", "utf8", sql
    )[1]
    SQDF.columns = [
        "行",
        "in_RrkNo_pk",
        "コード",
        "個人名",
        "関与先名",
        "発送方法",
        "送信方法",
        "アドレス",
        "課No",
        "課",
        "監査担当No",
        "監査担当",
        "サブNo",
        "サブ",
        "サブ2No",
        "サブ2",
        "送信方法2",
        "アドレス2",
        "送信方法3",
        "アドレス3",
        "送信方法4",
        "アドレス4",
        "送信方法5",
        "アドレス5",
        "cr_RecKbn",
        "dt_InstDT",
        "入力日時",
        "入力ユーザー",
        "変更前アドレス",
    ]
    SQDF.to_csv(URL, index=False)
    logger.debug("メアド変更履歴をCSVアウト: debug level log")


def JinjiIdo():
    # 人事異動をCSVアウト--------------------------------------------------------------
    sql = "SELECT * FROM d_jnjido"
    URL = r"\\Sv05121a\e\C 作業台\RPA\ALLDataBase\d_jnjido.csv"
    URL = URL.replace("\\", "/")

    SQDF = SQ.MySQLHeaderTo_df(
        "ws77", "SYSTEM", "SYSTEM", 3306, "test_db", "utf8", sql
    )[1]
    SQDF.to_csv(URL, index=False)
    logger.debug("人事異動をCSVアウト: debug level log")


def JinjiIdoSyain():
    # 人事異動を考慮した社員情報一覧をCSVアウト------------------------------------------
    WithA = "WITH SubMax AS (SELECT vc_SyainCd_pk ,MAX(in_IdoNo_pk) As MaxIdoNo,Max(d_jnjido.in_RrkNo_pk) As MaxRrkNo \
                FROM d_jnjido WHERE cr_RecKbn = '0' AND (dy_TkyEndD >= CURDATE() OR dy_TkyEndD = '0000-00-00' OR dy_TkyEndD IS NULL) GROUP BY vc_SyainCd_pk),"
    WithB = "Submn AS (SELECT * FROM m_bmn),"
    WithC = "SubIdo AS (SELECT Ido.vc_SyainCd_pk,Ido.in_IdoNo_pk,Ido.cr_IdoKbn,DATE_FORMAT(Ido.dy_JComD,'%Y/%m/%d') AS dy_JComYmd,DATE_FORMAT(Ido.dy_LComD,'%Y/%m/%d') AS dy_LComYmd \
                ,DATE_FORMAT(Ido.dy_TkyStrD,'%Y/%m/%d') AS dy_TkyStrYmd,DATE_FORMAT(Ido.dy_TkyEndD,'%Y/%m/%d') AS dy_TkyEndYmd\
                ,Ido.cr_SyainKbn,Ido.vc_BmnCd,Ido.cr_YakuCd,Ido.vc_GrpCd,Ido.vc_Biko FROM d_JnjIdo Ido \
                INNER JOIN SubMax Sub ON Ido.vc_SyainCd_pk = Sub.vc_SyainCd_pk AND Ido.in_IdoNo_pk = Sub.MaxIdoNo WHERE Ido.cr_RecKbn = '0'),"
    SelectStr = "SubTotal AS (SELECT Mst.vc_SyainCd_pk,Mst.in_RrkNo_pk,Mst.vc_UsrID,Mst.vc_Name,Mst.vc_NameR,Mst.vc_Kana,Mst.vc_RealName,DATE_FORMAT(Mst.dy_BirthD,'%Y/%m/%d') AS dy_BirthYmd\
                ,Mst.vc_Sex,Mst.vc_BLTyp,Mst.vc_Zipcd,Mst.vc_Addr1,Mst.vc_Addr2,Mst.vc_Addr3,Mst.vc_Tel,Mst.vc_Mobile,Mst.vc_Mail,Mst.vc_ComMail,Mst.vc_NenkinNo,Mst.vc_KoyoHknNo\
                ,Mst.vc_KenkHknNo,Mst.vc_Acdmc,Mst.vc_Dptmt,Mst.vc_Eto,Mst.vc_Seiza,Mst.vc_Biko As vc_MstBiko,Ido.in_IdoNo_pk,Ido.cr_IdoKbn,Ido.dy_JComYmd,Ido.dy_LComYmd,Ido.dy_TkyStrYmd,Ido.dy_TkyEndYmd\
                ,Ido.cr_SyainKbn,Ido.vc_BmnCd,Ido.cr_YakuCd,Ido.vc_GrpCd,Ido.vc_Biko As vc_IdoBiko FROM m_Syain Mst LEFT JOIN SubIdo Ido ON Mst.vc_SyainCd_pk = Ido.vc_SyainCd_pk WHERE Mst.cr_RecKbn = '0' ORDER BY Mst.vc_SyainCd_pk)"
    LastSelect = "SELECT sbt.vc_SyainCd_pk,sbt.in_RrkNo_pk,sbt.vc_Name,sbt.vc_ComMail,sbt.vc_BmnCd,sbm.vc_BmnNm FROM SubTotal sbt INNER JOIN Submn sbm ON sbt.vc_BmnCd = sbm.vc_BmnCd_pk"
    sql = WithA + WithB + WithC + SelectStr + LastSelect
    URL = r"\\Sv05121a\e\C 作業台\RPA\ALLDataBase\m_bmn.csv"
    URL = URL.replace("\\", "/")

    SQDF = SQ.MySQLHeaderTo_df(
        "ws77", "SYSTEM", "SYSTEM", 3306, "test_db", "utf8", sql
    )[1]
    SQDF.to_csv(URL, index=False)
    logger.debug("人事異動を考慮した社員情報一覧をCSVアウト: debug level log")
