import SQLConnect as SQ
import pandas as pd
#関与先データベースをCSVアウト-------------------------------------------------------
sql = 'SELECT * FROM m_kkanyo'
URL = "\\Sv05121a\e\C 作業台\RPA\ALLDataBase\m_kkanyo.csv"
URL = URL.replace("\\","/")
URL = "/" + URL
SQDF = SQ.MySQLHeaderTo_df('ws77','SYSTEM','SYSTEM',3306,'test_db','utf8',sql)[1]
SQDF.to_csv(URL, index = False)
#HeidiデータベースをCSVアウト-------------------------------------------------------
sql = 'SELECT * FROM kanyodb'
URL = "\\Sv05121a\e\C 作業台\RPA\ALLDataBase\Heidi関与先DB.csv"
URL = URL.replace("\\","/")
URL = "/" + URL
SQDF = SQ.MySQLHeaderTo_df('ws77','SYSTEM','SYSTEM',3306,'kanyodb','utf8',sql)[1]
SQDF.to_csv(URL, index = False)
#部門情報をCSVアウト----------------------------------------------------------------
sql = 'SELECT * FROM m_bmn'
URL = "\\Sv05121a\e\C 作業台\RPA\ALLDataBase\m_bmn.csv"
URL = URL.replace("\\","/")
URL = "/" + URL
SQDF = SQ.MySQLHeaderTo_df('ws77','SYSTEM','SYSTEM',3306,'test_db','utf8',sql)[1]
SQDF.to_csv(URL, index = False)
# #社員情報をCSVアウト----------------------------------------------------------------
# sql = 'SELECT * FROM m_syain'
# URL = "\\Sv05121a\e\C 作業台\RPA\ALLDataBase\m_syain.csv"
# URL = URL.replace("\\","/")
# URL = "/" + URL
# SQDF = SQ.MySQLHeaderTo_df('ws77','SYSTEM','SYSTEM',3306,'test_db','utf8',sql)[1]
# SQDF.to_csv(URL, index = False)
#FMSMAILLISTをCSVアウト------------------------------------------------------------
WithA = "WITH SubFMS AS (SELECT * FROM m_kfmsmail WHERE cr_RecKbn = '0' GROUP BY vc_FMSKnrCd),"
WithB = "SubKan AS (SELECT * FROM m_kkanyo WHERE cr_RecKbn = '0' GROUP BY vc_KnrCd),"
WithC = "Subido AS (SELECT * FROM d_jnjido WHERE cr_RecKbn = '0' GROUP BY vc_SyainCd_pk),"
WithD = "Subbmn AS (SELECT * FROM m_bmn WHERE cr_RecKbn = '0' GROUP BY vc_BmnCd_pk),"
WithE = "SubKrireki AS (SELECT t1.vc_gyou,MAX(t1.in_RrkNo_pk) AS in_RrkNo_pk,t1.vc_FMSKnrCd,t1.vc_Name,t1.vc_KName,\
        t1.vc_Hakkou,t1.vc_SousinK,t1.vc_Mail,t1.vc_BmnCd_pk,t1.vc_BmnNm,t1.vc_KansaTantouNo,\
        t1.vc_KansaTantou,t1.vc_SubTantouNo,t1.vc_SubTantou,t1.vc_Sub_SubTantouNo,t1.vc_Sub_SubTantou,\
        t1.vc_SousinK2,t1.vc_Mail2,t1.vc_SousinK3,t1.vc_Mail3,t1.vc_SousinK4,t1.vc_Mail4,t1.vc_SousinK5,\
        t1.vc_Mail5,t1.cr_RecKbn,t1.dt_InstDT,t1.dt_UpdtDT,t1.vc_inputuser,t1.vc_beforeadd FROM m_kfmsrireki AS t1 \
        JOIN (SELECT vc_gyou,MAX(in_RrkNo_pk) AS in_RrkNo_pk,vc_FMSKnrCd,vc_Name,vc_KName,vc_Hakkou,vc_SousinK,vc_Mail,vc_BmnCd_pk,vc_BmnNm,vc_KansaTantouNo,\
        vc_KansaTantou,vc_SubTantouNo,vc_SubTantou,vc_Sub_SubTantouNo,vc_Sub_SubTantou,vc_SousinK2,vc_Mail2,vc_SousinK3,vc_Mail3,vc_SousinK4,vc_Mail4,vc_SousinK5,\
        vc_Mail5,cr_RecKbn,dt_InstDT,dt_UpdtDT,vc_inputuser,vc_beforeadd FROM m_kfmsrireki GROUP BY vc_FMSKnrCd) AS t2 ON t1.vc_FMSKnrCd = t2.vc_FMSKnrCd \
        AND t1.in_RrkNo_pk = t2.in_RrkNo_pk GROUP BY vc_FMSKnrCd ORDER BY vc_FMSKnrCd)"
SelectStr = "SELECT F.vc_KnrCd,F.vc_KanKojinNo_pk,F.vc_FMSKnrCd,F.vc_Name,K.vc_Name AS 'Yago',\
        CASE WHEN R.vc_BmnCd_pk IS NOT NULL THEN R.vc_BmnCd_pk ELSE I.vc_BmnCd END AS vc_BmnCd,\
        CASE WHEN R.vc_BmnNm IS NOT NULL THEN R.vc_BmnNm ELSE M.vc_BmnNm END AS vc_BmnNm,\
        CASE WHEN R.vc_KansaTantouNo IS NOT NULL THEN R.vc_KansaTantouNo ELSE K.vc_KansaTantouNo END AS vc_KansaTantouNo,\
        CASE WHEN R.vc_KansaTantou IS NOT NULL THEN R.vc_KansaTantou ELSE K.vc_KansaTantou END AS vc_KansaTantou,\
        CASE WHEN R.vc_SubTantouNo IS NOT NULL THEN R.vc_SubTantouNo ELSE K.vc_SubTantouNo END AS vc_SubTantouNo,\
        CASE WHEN R.vc_SubTantou IS NOT NULL THEN R.vc_SubTantou ELSE K.vc_SubTantou END AS vc_SubTantou,\
        CASE WHEN R.vc_Sub_SubTantouNo IS NOT NULL THEN R.vc_Sub_SubTantouNo ELSE K.vc_Sub_SubTantouNo END AS vc_Sub_SubTantouNo,\
        CASE WHEN R.vc_Sub_SubTantou IS NOT NULL THEN R.vc_Sub_SubTantou ELSE K.vc_Sub_SubTantou END AS vc_Sub_SubTantou,\
        F.vc_Hakkou,\
        CASE WHEN R.vc_SousinK IS NOT NULL THEN R.vc_SousinK ELSE F.vc_SousinK END AS vc_SousinK,\
        CASE WHEN R.vc_Mail IS NOT NULL THEN R.vc_Mail ELSE F.vc_Mail END AS vc_Mail,\
        CASE WHEN R.vc_SousinK2 IS NOT NULL THEN R.vc_SousinK2 ELSE F.vc_SousinK2 END AS vc_SousinK2,\
        CASE WHEN R.vc_Mail2 IS NOT NULL THEN R.vc_Mail2 ELSE F.vc_Mail2 END AS vc_Mail2,\
        CASE WHEN R.vc_SousinK3 IS NOT NULL THEN R.vc_SousinK3 ELSE F.vc_SousinK3 END AS vc_SousinK3,\
        CASE WHEN R.vc_Mail3 IS NOT NULL THEN R.vc_Mail3 ELSE F.vc_Mail3 END AS vc_Mail3,\
        CASE WHEN R.vc_SousinK4 IS NOT NULL THEN R.vc_SousinK4 ELSE F.vc_SousinK4 END AS vc_SousinK4,\
        CASE WHEN R.vc_Mail4 IS NOT NULL THEN R.vc_Mail4 ELSE F.vc_Mail4 END AS vc_Mail4,\
        CASE WHEN R.vc_SousinK5 IS NOT NULL THEN R.vc_SousinK5 ELSE F.vc_SousinK5 END AS vc_SousinK5,\
        CASE WHEN R.vc_Mail5 IS NOT NULL THEN R.vc_Mail5 ELSE F.vc_Mail5 END AS vc_Mail5 \
        FROM SubFMS F INNER JOIN SubKan K ON F.vc_KnrCd = K.vc_KnrCd \
        LEFT JOIN Subido I ON K.vc_KansaTantouNo = I.vc_SyainCd_pk \
        LEFT JOIN Subbmn M ON I.vc_BmnCd = M.vc_BmnCd_pk \
        LEFT JOIN SubKrireki R ON F.vc_FMSKnrCd = R.vc_FMSKnrCd GROUP BY F.vc_FMSKnrCd ORDER BY F.vc_KnrCd"
sql = WithA + WithB + WithC + WithD + WithE + SelectStr
URL = "\\Sv05121a\e\C 作業台\RPA\ALLDataBase\m_kfmsmail.csv"
URL = URL.replace("\\","/")
URL = "/" + URL
SQDF = SQ.MySQLHeaderTo_df('ws77','SYSTEM','SYSTEM',3306,'test_db','utf8',sql)[1]
SQDF.to_csv(URL, index = False)
#人事異動をCSVアウト--------------------------------------------------------------
sql = 'SELECT * FROM d_jnjido'
URL = "\\Sv05121a\e\C 作業台\RPA\ALLDataBase\d_jnjido.csv"
URL = URL.replace("\\","/")
URL = "/" + URL
SQDF = SQ.MySQLHeaderTo_df('ws77','SYSTEM','SYSTEM',3306,'test_db','utf8',sql)[1]
SQDF.to_csv(URL, index = False)
#人事異動を考慮した社員情報一覧をCSVアウト------------------------------------------
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
URL = "\\Sv05121a\e\C 作業台\RPA\ALLDataBase\Joinm_bmn.csv"
URL = URL.replace("\\","/")
URL = "/" + URL
SQDF = SQ.MySQLHeaderTo_df('ws77','SYSTEM','SYSTEM',3306,'test_db','utf8',sql)[1]
SQDF.to_csv(URL, index = False)