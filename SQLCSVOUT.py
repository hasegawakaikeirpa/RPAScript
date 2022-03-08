import SQLConnect as SQ
import pandas as pd
#関与先データベースをCSVアウト-------------------------------------------------------
sql = 'SELECT * FROM m_kkanyo'
URL = "\\Sv05121a\e\C 作業台\RPA\ALLDataBase\m_kkanyo.csv"
URL = URL.replace("\\","/")
URL = "/" + URL
SQDF = SQ.MySQLHeaderTo_df('ws77','SYSTEM','SYSTEM',3306,'test_db','utf8',sql)[1]
SQDF.to_csv(URL, index = False)
#社員情報をCSVアウト----------------------------------------------------------------
sql = 'SELECT * FROM m_syain'
URL = "\\Sv05121a\e\C 作業台\RPA\ALLDataBase\m_syain.csv"
URL = URL.replace("\\","/")
URL = "/" + URL
SQDF = SQ.MySQLHeaderTo_df('ws77','SYSTEM','SYSTEM',3306,'test_db','utf8',sql)[1]
SQDF.to_csv(URL, index = False)