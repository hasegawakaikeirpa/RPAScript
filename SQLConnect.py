def MySQLGet(str_host,str_user,str_passwd,int_port,str_database,str_charset,sql):#host='ws77',user='SYSTEM',passwd='SYSTEM',port='3306',database='test_db',charset='utf8'
    try:
        conn = MySQLdb.connect(host=str_host,user=str_user,passwd=str_passwd,port=int_port,database=str_database,charset=str_charset)
        cursor = conn.cursor()
        cursor.execute(sql)  # select文を実行
        conn.commit()
        SqlData = cursor.fetchall() 
        cursor.close()
        conn.close()
        return True,SqlData
    except:
        return False,"取得失敗"
def MySQLHeaderTo_df(str_host,str_user,str_passwd,int_port,str_database,str_charset,sql):#host='ws77',user='SYSTEM',passwd='SYSTEM',port='3306',database='test_db',charset='utf8'
    try:
        conn = MySQLdb.connect(host=str_host,user=str_user,passwd=str_passwd,port=int_port,database=str_database,charset=str_charset)
        cursor = conn.cursor()
        SqlData = pd.read_sql(sql, conn)
        cursor.close()
        conn.close()
        return True,SqlData
    except:
        return False,"取得失敗"

import MySQLdb
import pandas as pd
import CSVOut as co
import numpy as np
from tqdm import tqdm
# sqlstr = 'SELECT * FROM m_kkanyo'
# Sqldf = MySQLHeaderTo_df('ws77','SYSTEM','SYSTEM',3306,'test_db','utf8',sqlstr)[1]
# Sqldf.to_csv("//Sv05121a/e/C 作業台/RPA/ALLDataBase/TBCopyCopy.csv",index=None)
# CSVList = co.CsvRead("//Sv05121a/e/C 作業台/RPA/ALLDataBase/TB.csv")
# MasRow = np.array(Sqldf.shape[0])#配列行数取得
# for x in range(MasRow):
#     Sqldfrow = Sqldf.iloc[x,:]
#     SyanaiCode = Sqldfrow['vc_KnrCd']
#     CsvRow = co.CsvSortArray("//Sv05121a/e/C 作業台/RPA/ALLDataBase/TB.csv","SyanaiCode",int(SyanaiCode),"int")
#     if CsvRow[0] == True:
#         CsvRowRow = CsvRow[1]
#         try:
#             Siki = str(int(CsvRowRow['（国税）利用者識別番号']))
#         except:
#             Siki = str(CsvRowRow['（国税）利用者識別番号'])
#         ID = str(CsvRowRow['（地方税）利用者ID'])
#         #'vc_Msikibetu','vc_Mid'
#         sql = "UPDATE m_kkanyo SET vc_Msikibetu = '" + Siki + "',vc_Mid = '" + ID + "' WHERE vc_KnrCd = '" + SyanaiCode + "'"
#         #sql = 'UPDATE m_kkanyo SET vc_Msikibetu = ' + '12345678910' + ',vc_Mid = ' + 'hsaaha123456798' + ' WHERE vc_KnrCd = ' + SyanaiCode
#         MSGet = MySQLGet('ws77','SYSTEM','SYSTEM',3306,'test_db','utf8',sql) #host='ws77',user='SYSTEM',passwd='SYSTEM',port='3306',database='test_db',charset='utf8'
#         if MSGet[0] == True:
#             print(SyanaiCode + "成功")
#         else:
#             print(SyanaiCode + "失敗")
