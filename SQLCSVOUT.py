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
WithD = "Subbmn AS (SELECT * FROM m_bmn WHERE cr_RecKbn = '0' GROUP BY vc_BmnCd_pk)"
SelectStr = "SELECT F.vc_KnrCd,F.vc_KanKojinNo_pk,F.vc_FMSKnrCd,F.vc_Name,K.vc_Name AS 'Yago',I.vc_BmnCd,M.vc_BmnNm,K.vc_KansaTantouNo,K.vc_KansaTantou,\
            K.vc_SubTantouNo,K.vc_SubTantou,K.vc_Sub_SubTantouNo,K.vc_Sub_SubTantou,F.vc_Hakkou,F.vc_PDFName,F.vc_SousinK,F.vc_Mail,F.vc_SousinK2,F.vc_Mail2,\
            F.vc_SousinK3,F.vc_Mail3,F.vc_SousinK4,F.vc_Mail4,F.vc_SousinK5,F.vc_Mail5 FROM SubFMS F INNER JOIN SubKan K ON F.vc_KnrCd = K.vc_KnrCd\
                LEFT JOIN Subido I ON K.vc_KansaTantouNo = I.vc_SyainCd_pk LEFT JOIN Subbmn M ON I.vc_BmnCd = M.vc_BmnCd_pk"
sql = WithA + WithB + WithC + WithD + SelectStr
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