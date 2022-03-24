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
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def MySQLGet(str_host,str_user,str_passwd,int_port,str_database,str_charset,sql):#host='ws77',user='SYSTEM',passwd='SYSTEM',port='3306',database='test_db',charset='utf8'
#SQL文を送信し、結果を返す
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
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def MySQLHeaderTo_df(str_host,str_user,str_passwd,int_port,str_database,str_charset,sql):#host='ws77',user='SYSTEM',passwd='SYSTEM',port='3306',database='test_db',charset='utf8'
#SQL文を送信し、結果をDFに格納
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
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def MySQLAct(str_host,str_user,str_passwd,int_port,str_database,str_charset,sql):#host='ws77',user='SYSTEM',passwd='SYSTEM',port='3306',database='test_db',charset='utf8'
#SQL文を送信、結果をBooleanで返す
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
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def MysqlColumnCheck(str_host,str_user,str_passwd,int_port,str_database,str_charset,TB,ColN):#host='ws77',user='SYSTEM',passwd='SYSTEM',port='3306',database='test_db',charset='utf8',テーブル名,列名
#引数のカラム名(ColN)と一致する引数テーブル(TB)のカラムのデータ型を返す
    try:
        sql = "show columns from " + TB
        conn = MySQLdb.connect(host=str_host,user=str_user,passwd=str_passwd,port=int_port,database=str_database,charset=str_charset)
        cursor = conn.cursor()
        cursor.execute(sql)  # select文を実行
        conn.commit()
        SqlColumn = cursor.fetchall() 
        cursor.close()
        conn.close()
        for SqlColumnItem in SqlColumn:
            if SqlColumnItem[0] == ColN:
                return True,SqlColumnItem[1]
    except:
        cursor.close()
        conn.close()
        return False,""
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def MysqlColumnPic(str_host,str_user,str_passwd,int_port,str_database,str_charset,TB):#host='ws77',user='SYSTEM',passwd='SYSTEM',port='3306',database='test_db',charset='utf8',テーブル名,列名
#テーブルのカラム情報をタプルで返す
    try:
        sql = "show columns from " + TB
        conn = MySQLdb.connect(host=str_host,user=str_user,passwd=str_passwd,port=int_port,database=str_database,charset=str_charset)
        cursor = conn.cursor()
        cursor.execute(sql)  # select文を実行
        conn.commit()
        SqlColumn = cursor.fetchall() 
        cursor.close()
        conn.close()
        return True,SqlColumn
    except:
        cursor.close()
        conn.close()
        return False,""
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def ChangeData(ColN,ParList,UDRowItem,TB):#列名,列名リスト,行データ,テーブル名
#データ型に合わせて値を変更する。
    try:
        ColP = MysqlColumnCheck('ws77','SYSTEM','SYSTEM',3306,'test_db','utf8',TB,ColN)
        if ColP[0] == True:
            SQLColP = ColP[1]
            #データ型に合わせて値を変更----------------------------------------------------------------
            if 'datetime' in SQLColP:
                if UDRowItem == None:#Timestamp('2022-03-09 00:00:00')
                    FDATE = datetime.datetime.now()
                    FDATE = str(FDATE.strftime('%Y-%m-%d %H:%M:%S'))
                    # FDATE = "Timestamp('" + FDATE + "')"
                    ParList.append(FDATE)
                else:
                    if ColN == 'dt_UpdtDT':
                        FDATE = datetime.datetime.now()
                        FDATE = str(FDATE.strftime('%Y-%m-%d %H:%M:%S'))
                        # FDATE = "Timestamp('" + FDATE + "')"
                        ParList.append(FDATE)
                    else:
                        ParList.append(UDRowItem)
            elif 'char' in SQLColP:
                if UDRowItem == " ":
                    ParList.append("")
                elif UDRowItem == "　":
                    ParList.append("")
                elif UDRowItem == "  ":
                    ParList.append("")
                elif ColN == 'vc_KnrCd':
                    ParList.append(UDRowItem.replace("  ","").replace(" ",""))
                elif ColN == 'in_RrkNo_pk' or ColN == 'cr_RecKbn':
                    ParList.append(UDRowItem + 1)
                else:
                    ParList.append(str(UDRowItem).replace("\u3000"," ").replace("\u200b"," "))
            elif 'int' in SQLColP:
                if UDRowItem == " ":
                    ParList.append("")
                elif UDRowItem == "　":
                    ParList.append("")
                elif UDRowItem == "  ":
                    ParList.append("")
                elif ColN == 'vc_KnrCd':
                    ParList.append(UDRowItem.replace("  ","").replace(" ",""))
                elif ColN == 'in_RrkNo_pk' or ColN == 'cr_RecKbn':
                    ParList.append(UDRowItem + 1)
                else:
                    ParList.append(int(UDRowItem))
            else:
                if UDRowItem == " ":
                    ParList.append("")
                elif UDRowItem == "　":
                    ParList.append("")
                elif UDRowItem == "  ":
                    ParList.append("")
                elif ColN == 'vc_KnrCd':
                    ParList.append(UDRowItem.replace("  ","").replace(" ",""))
                elif ColN == 'in_RrkNo_pk' or ColN == 'cr_RecKbn':
                    ParList.append(UDRowItem + 1)
                else:
                    ParList.append(UDRowItem)
            return ParList
        else:
            print("テーブルカラム取得失敗")
            return False
    except:
        print("exceptエラー")
        return False
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def MysqlDiffUp(MTB,CTB,UDRow):#元TB名,履歴TB名,更新行データ
    try:
        #履歴テーブルにコピー-------------------------------------------------------------------------------------------------------------------------------------
        sql = 'SELECT * FROM ' + MTB #SELECT分を代入
        DFCol = MysqlColumnPic('ws77','SYSTEM','SYSTEM',3306,'test_db','utf8',MTB)[1]#関数でTB列情報取得
        ColList = []#データ型変帝の為のカラムリストを作成
        ParList = []#SQL結合用に行データ格納用のリスト作成
        for DFColItem in DFCol:#Rowデータのデータ型に併せて値を変更
            ColList.append(DFColItem[0])#DFから列名のみ抽出
        ColRow = 0#カラムリストのRowIndex初期化
        for UDRowItem in UDRow:#行データひとつずつループ
            ColN = ColList[ColRow]#カラムリストから列名取得
            ChangeData(ColN,ParList,UDRowItem,MTB)#列名,行データ格納用のリスト,行データ要素,TB名
            ColRow = ColRow + 1#カラムリストのRowIndex加算
        FColList = str(ColList)#SQL文用列名リストの作成
        FColList = FColList.replace("'","")#不要なのでシングルコーテーション削除
        sql = 'INSERT INTO ' + CTB + ' SELECT * FROM ' + MTB + " WHERE vc_KnrCd='" + UDRow['vc_KnrCd'].replace("  ","").replace(" ","") +"'" #変更対象を履歴DBにコピー
        MySQLAct('ws77','SYSTEM','SYSTEM',3306,'test_db','utf8',sql)#引数8=親TB名,引数9=履歴数列名
        sql = 'SELECT * FROM ' + MTB + ' WHERE vc_KnrCd=' + UDRow['vc_KnrCd'].replace("  ","").replace(" ","") #変更対象を履歴DBにコピー
        #-------------------------------------------------------------------------------------------------------------------------------------------------------
        #マスターテーブルを差分更新--------------------------------------------------------------------------------------------------------------------------------
        SQLData = MySQLHeaderTo_df('ws77','SYSTEM','SYSTEM',3306,'test_db','utf8',sql)[1]#マスターの最新レコードをDF化
        SQLDataRow = np.array(SQLData).shape[0]#DF行数取得
        if SQLDataRow == 1:
            SQLDataSingle = SQLData.iloc[0,:]#DF行データ取得
            ColRow = 0#カラムリストのRowIndex初期化
            for ColListItem in ColList:#行データひとつずつループ
                ColN = ColList[ColRow]#カラムリストから列名取得
                if SQLDataSingle[ColN] == ParList[ColRow]:     
                    sql = ''
                else:
                    DataType = type(ParList[ColRow]) #値の型検出
                    if ParList[ColRow] == '':
                        sql = 'UPDATE ' + MTB + ' SET ' + ColN + "=''" + " WHERE vc_KnrCd='" + UDRow['vc_KnrCd'].replace("  ","").replace(" ","") + "'"#変更対象を履歴DBにコピー
                    else:
                        if 'str' in str(DataType):
                            sql = 'UPDATE ' + MTB + ' SET ' + ColN + "='" + str(ParList[ColRow]) + "' WHERE vc_KnrCd='" + UDRow['vc_KnrCd'].replace("  ","").replace(" ","") + "'"#変更対象を履歴DBにコピー
                        else:
                            sql = 'UPDATE ' + MTB + ' SET ' + ColN + "=" + str(ParList[ColRow]) + " WHERE vc_KnrCd='" + UDRow['vc_KnrCd'].replace("  ","").replace(" ","") + "'"#変更対象を履歴DBにコピー
                    sql = sql.replace("[","").replace("]","")
                    MySQLAct('ws77','SYSTEM','SYSTEM',3306,'test_db','utf8',sql)#引数8=親TB名,引数9=履歴数列名       
                    sql = ''
                ColRow = ColRow + 1 
            return True
        else:
            print("マスターに重複があります。")
            return False
    except:
        return False
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#MysqlDiffUp(MTB,CTB,UDRow):の使い方↓

# sql = 'SELECT * FROM m_kfmsmail'#SELECT分を代入
# KFM = MySQLHeaderTo_df('ws77','SYSTEM','SYSTEM',3306,'test_db','utf8',sql)[1]#関数でクエリ結果をDF化
# KFMRow = np.array(KFM).shape[0]#DF行数取得
# for x in range(KFMRow):#DF分ループ
#     KFMData = KFM.iloc[x,:]#DF行データ取得
#     ITB = 'm_kfmsmailrireki'#テーブル名を代入
#     ColRow = 0
#     MysqlDiffUp('m_kfmsmail',ITB,KFMData) #元TB名,履歴TB名,更新行データ