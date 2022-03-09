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
        cursor.close()
        conn.close()
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
        cursor.close()
        conn.close()
        return False,"取得失敗"
def MySQLAct(str_host,str_user,str_passwd,int_port,str_database,str_charset,sql):#host='ws77',user='SYSTEM',passwd='SYSTEM',port='3306',database='test_db',charset='utf8'
    try:
        conn = MySQLdb.connect(host=str_host,user=str_user,passwd=str_passwd,port=int_port,database=str_database,charset=str_charset)
        cursor = conn.cursor()
        cursor.execute(sql)  # select文を実行
        conn.commit()
        cursor.close()
        conn.close()
        return True
    except:
        cursor.close()
        conn.close()
        return False

import MySQLdb
import pandas as pd
import CSVOut as co
import numpy as np
import os
from datetime import datetime as dt
from tqdm import tqdm
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String
import datetime

def ChangeData(ColN,ParList,UDRowItem):#列名,列名リスト,行データ
    #データ型に合わせて値を変更----------------------------------------------------------------
    if 'dt_' in ColN:
        if UDRowItem == None:#Timestamp('2022-03-09 00:00:00')
            FDATE = datetime.datetime.now()
            FDATE = str(FDATE.strftime('%Y-%m-%d %H:%M:%S'))
            # FDATE = "Timestamp('" + FDATE + "')"
            ParList.append(FDATE)
        else:
            ParList.append(UDRowItem)
    else:
        if UDRowItem == " ":
            ParList.append("")
        elif UDRowItem == "　":
            ParList.append("")
        elif UDRowItem == "  ":
            ParList.append("")
        elif ColN == 'vc_KnrCd':
            ParList.append(UDRowItem.replace("  ","").replace(" ",""))
        elif ColN == 'in_RrkNo_pk':
            ParList.append(UDRowItem + 1)
        elif ColN == 'cr_RecKbn':
            ParList.append('1')
        else:
            ParList.append(UDRowItem)
    ColRow = ColRow + 1
    #---------------------------------------------------------------------------------------
def MysqlDiffUp(MTB,CTB,UDRow):#元TB名,履歴TB名,更新行データ
    try:
        sql = 'SELECT * FROM ' + MTB #SELECT分を代入
        KFM = MySQLHeaderTo_df('ws77','SYSTEM','SYSTEM',3306,'test_db','utf8',sql)[1]#関数でクエリ結果をDF化
        DFCol = KFM.columns#DF列名を取得
        ColList = []
        ParList = []
        for DFColItem in DFCol:#Rowデータのデータ型に併せて値を変更
            ColList.append(DFColItem)
        ColRow = 0
        for UDRowItem in UDRow:
            ColN = ColList[ColRow]
            ChangeData(ColN,ParList,UDRowItem)#列名,列名リスト,行データ
        FColList = str(ColList)#SQL文用列名リストの作成
        FColList = FColList.replace("'","")#不要なのでシングルコーテーション削除
        sql = 'INSERT INTO ' + ITB + ' SELECT * FROM ' + MTB + ' WHERE vc_KnrCd=' + KFMData['vc_KnrCd'].replace("  ","").replace(" ","")#変更対象を履歴DBにコピー
        MySQLAct('ws77','SYSTEM','SYSTEM',3306,'test_db','utf8',sql)#引数8=親TB名,引数9=履歴数列名   
        sql = 'insert into ' + ITB + ' (' + str(FColList) + ') values (' + str(ParList) + ')'
        sql = sql.replace("[","").replace("]","")
        MySQLAct('ws77','SYSTEM','SYSTEM',3306,'test_db','utf8',sql)#引数8=親TB名,引数9=履歴数列名       
        sql = 'SELECT * FROM m_kfmsmail WHERE vc_KnrCd=' + KFMData['vc_KnrCd'].replace("  ","").replace(" ","")
        MFM = MySQLHeaderTo_df('ws77','SYSTEM','SYSTEM',3306,'test_db','utf8',sql)[1]#関数でクエリ結果をDF化
        sql = 'SELECT * FROM m_kfmsmailrireki AS m WHERE NOT EXISTS (SELECT 1 FROM m_kfmsmailrireki AS s WHERE m.vc_KnrCd = s.vc_KnrCd AND m.in_RrkNo_pk < s.in_RrkNo_pk)'
        KFMKFM = MySQLHeaderTo_df('ws77','SYSTEM','SYSTEM',3306,'test_db','utf8',sql)[1]#関数でクエリ結果をDF化
        print(MFM)
        print(KFMKFM)
        print(KFMKFM[~KFMKFM.isin(MFM.to_dict(orient='list')).all(1)])
        sql = ''
        return True
    except:
        return False
sql = 'SELECT * FROM m_kfmsmail'#SELECT分を代入
KFM = MySQLHeaderTo_df('ws77','SYSTEM','SYSTEM',3306,'test_db','utf8',sql)[1]#関数でクエリ結果をDF化
KFMRow = np.array(KFM).shape[0]#DF行数取得

for x in range(KFMRow):#DF分ループ
    KFMData = KFM.iloc[x,:]#DF行データ取得
    ITB = 'm_kfmsmailrireki'#テーブル名を代入
    ColRow = 0
    MysqlDiffUp('m_kfmsmail',ITB,KFMData) #元TB名,履歴TB名,更新行データ