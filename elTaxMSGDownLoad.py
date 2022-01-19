﻿def eTaxWebCrawler(H_id,H_pass,H_fold,H_SC,H_TN):
    #作成した変数は頭にH_をつける事
    #ブラウザ閲覧時のオプションを指定するオブジェクト"options"を作成
    H_options= Options()
    appState = {
        "recentDestinations": [
            {
                "id": "Save as PDF",
                "origin": "local",
                "account": "",
            }
        ],
        "selectedDestinationId": "Save as PDF",
        "version": 2,
    }
    prefs = {'printing.print_preview_sticky_settings.appState':
    json.dumps(appState),
    "savefile.default_directory": H_fold#"D:/PythonScript"
    }
    H_options.add_experimental_option("prefs",prefs)
    #必要に応じてオプションを追加
    H_options.add_argument('--window-size=1024,768')
    H_options.add_argument("--kiosk-printing")
    #ドライバのpathを指定
    H_path = 'D:\PythonScript/chromedriver'
    #WEBURLの指定
    H_WEBurl = "https://www.portal.eltax.lta.go.jp/apa/web/webindexb#eLTAX"
    #ブラウザのウィンドウを表すオブジェクト"driver"を作成
    H_driver = webdriver.Chrome(executable_path=H_path, chrome_options=H_options)
    H_driver.get(H_WEBurl)
    WebDriverWait(H_driver, 30).until(EC.presence_of_all_elements_located)#要素が読み込まれるまで最大30秒待つ
    #初めの拡張機能ポップアップを閉じる
    time.sleep(2)
    H_PopupCheck_btn = H_driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/form/div/div[1]/input')
    H_driver.execute_script("arguments[0].click();", H_PopupCheck_btn)
    H_PopupClose_btn = H_driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/form/div/div[2]/div[1]/a')#閉じるボタンの要素指定
    H_PopupClose_btn.click()
    WebDriverWait(H_driver, 30).until(EC.presence_of_all_elements_located)#要素が読み込まれるまで最大30秒待つ
    #ログイン画面要素指定------------------------------------------------------------------------------------------------------
    #利用者識別番号入力欄をxpathで取得
    H_Sikibetu_box1 = H_driver.find_element_by_xpath("/html/body/div[2]/form/div/div/div[1]/div/ul[1]/li[1]/input")
    #ログインPASS入力欄をxpathで取得
    H_LogPassBox = H_driver.find_element_by_xpath("/html/body/div[2]/form/div/div/div[1]/div/ul[1]/li[2]/input")
    H_Log_btn = H_driver.find_element_by_xpath("/html/body/div[2]/form/div/div/div[1]/div/button") 
    #WEB操作--------------------------------------------------------------------------------------------------------------------
    H_Sikibetu_box1.send_keys(H_id)
    H_LogPassBox.send_keys(H_pass)
    H_Log_btn.click()
    WebDriverWait(H_driver, 30).until(EC.presence_of_all_elements_located)#要素が読み込まれるまで最大30秒待つ
    #---------------------------------------------------------------------------------------------------------------------------
    try:
        WebDriverWait(H_driver, 30).until(EC.presence_of_all_elements_located)#要素が読み込まれるまで最大30秒待つ
        time.sleep(2)
        H_H1 = H_driver.find_element_by_xpath("/html/body/div[3]/form/div/div/div[1]/div/p")#H1要素を取得
        return H_H1.text,H_driver
    except Exception:
        try:
            H_H1 = H_driver.find_element_by_xpath("/html/body/div[1]/div[2]/form/h1")#H1要素を取得
            return H_H1.text,H_driver
        except Exception:
            H_H1 = H_driver.find_element_by_xpath("/html/body/div[2]/form/div/div/div/div/div[1]/div[1]/ul/li[7]/a/p")#H1要素を取得
            return H_H1.text,H_driver
    else:
        pass
#-----------------------------------------------------------------------------------------------------------------------------------------------------
def LogOnOuter(H_driver):
    #ログイン成功の場合
    #WEB画面要素指定------------------------------------------------------------------------------------------------------
    try: 
        H_MSG_Table = H_driver.find_element_by_xpath("/html/body/div[2]/form/div/div/div[2]/div[2]/div[1]")#メッセージボックスのテーブルをxpath取得
                                                      #/html/body/div[2]/form/div/div/div[2]/div[2]/div[1]/div[2]/table
    except Exception:
        pass
    else:
        ListURL = H_driver.current_url#xpathで取得したテーブルがあるページのURLを取得
        dfs = pd.read_html(H_driver.page_source, encoding = 'cp932')#pandasにWEBURLをぶっこむ
        H_MSG_row = len(dfs[2]) #テーブル行数を代入 
        return H_driver,H_MSG_row
#-----------------------------------------------------------------------------------------------------------------------------------------------------
def ParGet(H_driver,H_MSG_rowItem,H_MSG_row):
            try:
                #WEBTable
                H_FirstMSG_Cbx = H_driver.find_element_by_xpath("/html/body/div[2]/form/div/div/div[2]/div[2]/div[1]/div[2]/table/tbody/tr[{}]/td[1]/div/label".format(H_MSG_rowItem))#一行上のチェックボックス
                H_MSG_Cbx = H_driver.find_element_by_xpath("/html/body/div[2]/form/div/div/div[2]/div[2]/div[1]/div[2]/table/tbody/tr[{}]/td[1]/div/label".format(H_MSG_rowItem + 1))#チェックボックス
                H_driver.execute_script("arguments[0].click();", H_FirstMSG_Cbx)#チェックボックスクリック
                H_driver.execute_script("arguments[0].click();", H_MSG_Cbx)#チェックボックスクリック
                WebDriverWait(H_driver, 30).until(EC.presence_of_all_elements_located)#要素が読み込まれるまで最大30秒待つ
                H_driver.execute_script("hyouziAction()")#Javaで表示
                WebDriverWait(H_driver, 30).until(EC.presence_of_all_elements_located)#要素が読み込まれるまで最大30秒待つ
            except Exception:
                H_MSG_Cbx = H_driver.find_element_by_xpath("/html/body/div[2]/form/div/div/div[2]/div[2]/div[1]/div[2]/table/tbody/tr[{}]/td[1]/div/label".format(H_MSG_rowItem + 1))#チェックボックス
                H_driver.execute_script("arguments[0].click();", H_MSG_Cbx)#チェックボックスクリック
                WebDriverWait(H_driver, 30).until(EC.presence_of_all_elements_located)#要素が読み込まれるまで最大30秒待つ
                H_driver.execute_script("hyouziAction()")#Javaで表示
                WebDriverWait(H_driver, 30).until(EC.presence_of_all_elements_located)#要素が読み込まれるまで最大30秒待つ       
            finally:
                #要素取得
                H_MSG_TableItem1 = H_driver.find_element_by_xpath("/html/body/div[2]/form/div/div/div[2]/section/table/tbody/tr[1]/td").text.replace('\u3000', ' ')#発行元
                H_MSG_TableItem2 = H_driver.find_element_by_xpath("/html/body/div[2]/form/div/div/div[2]/section/table/tbody/tr[2]/td[1]").text.replace('\u3000', ' ')#発行元2
                H_MSG_TableItem3 = H_driver.find_element_by_xpath("/html/body/div[2]/form/div/div/div[2]/section/table/tbody/tr[3]/td[1]").text.replace('\u3000', ' ')#発行日時            
                H_MSG_TableItem4 = H_driver.find_element_by_xpath("/html/body/div[2]/form/div/div/div[2]/section/table/tbody/tr[4]/td").text.replace('\u3000', ' ')#件名
                return H_MSG_TableItem1,H_MSG_TableItem2,H_MSG_TableItem3,H_MSG_TableItem4
#-----------------------------------------------------------------------------------------------------------------------------------------------------
def PrintIFS(H_Title,H_driver):
    H_driver.execute_script('window.print();')#開いたタブを印刷
    #time.sleep(4)
    WebDriverWait(H_driver, 30).until(EC.presence_of_all_elements_located)#要素が読み込まれるまで最大30秒待つ
    H_BackBtn = H_driver.find_element_by_xpath("/html/body/div[2]/form/footer/div[1]/div/div[1]/a")
    H_BackBtn.click()
    WebDriverWait(H_driver, 30).until(EC.presence_of_all_elements_located)#要素が読み込まれるまで最大30秒待つ
    return "印刷完了"
#-----------------------------------------------------------------------------------------------------------------------------------------------------
def LogReturn(LogAns,H_driver):
    if LogAns == 'ログインしている利用者あてのメッセージを照会します。':#ログイン成功の場合
        #WEB画面要素指定------------------------------------------------------------------------------------------------------
        try:
            H_MSG_OpenMyNo = H_driver.find_element_by_xpath("/html/body/div[2]/form/div/div/div/div/div[1]/div[1]/ul/li[7]/a")
            H_MSG_OpenMyNo.click()
            WebDriverWait(H_driver, 30).until(EC.presence_of_all_elements_located)#要素が読み込まれるまで最大30秒待つ
            H_Today = dt.today() + relativedelta(months=-1)
            H_dtToday = dt.today()
            Hj = str(H_dtToday.year)
            Hjj = str('{0:02}'.format(H_dtToday.month))
            H_Str = Hj + "/" + Hjj + "/01 01:01:01" 
            H_LT = dt.strptime(H_Str, '%Y/%m/%d %H:%M:%S')
            H_LastToday = H_LT + relativedelta(days=-1)
            H_FirstMonth = H_driver.find_element_by_xpath("/html/body/div[2]/form/div/div/div[2]/div[1]/div/div[2]/input[1]")
            H_EndMonth = H_driver.find_element_by_xpath("/html/body/div[2]/form/div/div/div[2]/div[1]/div/div[2]/input[4]") 
            H_FMon = '{0:04}'.format(H_Today.year) + '{0:02}'.format(H_Today.month) + '{0:02}'.format(1)
            H_EMon = '{0:04}'.format(H_LastToday.year) + '{0:02}'.format(H_LastToday.month) + '{0:02}'.format(H_LastToday.day)
            H_FirstMonth.send_keys(H_FMon)
            H_EndMonth.send_keys(H_EMon)
            H_KensakuBtn = H_driver.find_element_by_xpath("/html/body/div[2]/form/div/div/div[2]/div[1]/div/input")
            H_KensakuBtn.click()
            WebDriverWait(H_driver, 30).until(EC.presence_of_all_elements_located)#要素が読み込まれるまで最大30秒待つ
            return H_driver.find_element_by_xpath("/html/body/div[2]/form/div/div/div[2]/p[2]/span").text
        except:
            WebDriverWait(H_driver, 30).until(EC.presence_of_all_elements_located)#要素が読み込まれるまで最大30秒待つ
            return "データ有"
    elif LogAns == "認証エラー":#ログイン失敗の場合
        WebDriverWait(H_driver, 30).until(EC.presence_of_all_elements_located)#要素が読み込まれるまで最大30秒待つ
        return "認証エラー"
    elif LogAns == "ログインできませんでした。":#ログイン失敗の場合
        return "ログインできませんでした。"
    else:                        #その他の場合
        WebDriverWait(H_driver, 30).until(EC.presence_of_all_elements_located)#要素が読み込まれるまで最大30秒待つ
#-----------------------------------------------------------------------------------------------------------------------------------------------------
def RenamePDF(DownTime,MTitle,KanyoNo,KanyoName,Hakkoumoto,Hakkou):
    tdy = dt.strptime(DownTime, '%Y/%m/%d %H:%M:%S')#文字列を日付型に変換
    CfolName = str(tdy.year) + "-" + str(tdy.month)
    folders = glob.glob("//Sv05121a/e/電子ファイル/メッセージボックス/*-*")
    KanyoFolName = str(KanyoNo) + "_" + KanyoName
    for foldersItem in folders:
        if foldersItem == "//Sv05121a/e/電子ファイル/メッセージボックス\\" + CfolName:
            Subfolders = glob.glob(foldersItem + "/*") #フォルダーがあった場合
            if MTitle == 'プレ申告データに関するお知らせ':
                MotherFol = foldersItem + "\\eLTAX"
                for SubfoldersItem in Subfolders:
                    if SubfoldersItem.replace('\u3000', ' ') == MotherFol:
                        SubFFlag = 1
                        print(MotherFol + "あります")
                        break
                    else:
                        SubFFlag = 0
                if SubFFlag == 0:
                    os.mkdir(foldersItem + "/eLTAX")
                    print(MotherFol + "作りました。")
                    break
                Tfolders = glob.glob(foldersItem + "\\eLTAX" + "/*") #フォルダーがあった場合
                ChildFol = foldersItem + "\\eLTAX" + "\\" + KanyoFolName
                TFFlag = 0
                for TfoldersItem in Tfolders:
                    if TfoldersItem == ChildFol:
                        MovingFol = TfoldersItem
                        TFFlag = 1
                        CreFolURL = ChildFol
                        print(ChildFol + "あります")
                        break
                    else:
                        TFFlag = 0
                if TFFlag == 0:
                    os.mkdir(foldersItem + "/eLTAX" + "/" + KanyoFolName)
                    CreFolURL = ChildFol
                    print(ChildFol + "作りました。")
                    break
                break
            else:
                MotherFol = foldersItem + "\\eLTAX受信通知"
                for SubfoldersItem in Subfolders:
                    if SubfoldersItem.replace('\u3000', ' ') == MotherFol:
                        SubFFlag = 1
                        print(MotherFol + "あります")
                        ChildFol = MotherFol
                        break
                    else:
                        SubFFlag = 0
                if SubFFlag == 0:
                    os.mkdir(foldersItem + "/eLTAX受信通知")
                    print(MotherFol + "作りました。")
                    ChildFol = MotherFol
                    break
                else:
                    break
        else:
            print("ありません") #フォルダーがなかった場合
    PDFfolder = glob.glob("D:\PythonScript/" + "*.pdf") #フォルダーがあった場合
    for PDFfolderItem in PDFfolder:
        PDFSerch = "メッセージ照会_お知らせ" in PDFfolderItem
        PDFName = KanyoFolName + "_" + Hakkoumoto + "_" + Hakkou + "_" + MTitle  + ".pdf"
        PDFPath = "D:\PythonScript/" + PDFName
        PDFPath = PDFPath.replace("/","\\")

        try:
            if PDFSerch == True:
                os.rename(PDFfolderItem,PDFPath)
                MovePDFPath = ChildFol + "/" + PDFName
                MovePDFPath = MovePDFPath.replace("/","\\")
                shutil.move(PDFPath,MovePDFPath)
                OKstr = MovePDFPath + "成功"
                OKstr = OKstr.replace('\uff0d', '-').replace('\xa0', '')
                OKLog.append(OKstr)
            #'D:\\PythonScript\\国税電子申告・納税システム－SU00S100 メール詳細 (1).pdf'
            else:
                NGstr = MovePDFPath + "_リネーム失敗-メッセージ照会_お知らせが含まれないファイル名-"
                NGstr = NGstr.replace('\uff0d', '-').replace('\xa0', '')
                NGLog.append(NGstr)
        except:
            traceback.print_exc()
            NGstr = MovePDFPath + "_リネーム失敗-トレースバックエラー-"
            NGstr = NGstr.replace('\uff0d', '-').replace('\xa0', '')
            NGLog.append(NGstr)
#-----------------------------------------------------------------------------------------------------------------------------------------------------
def SortPDF(DownTime,MTitle,KanyoNo,KanyoName,Hakkoumoto,Hakkou):
    tdy = dt.strptime(DownTime, '%Y/%m/%d %H:%M:%S')#文字列を日付型に変換
    CfolName = str(tdy.year) + "-" + str(tdy.month)
    KanyoFolName = str(KanyoNo) + "_" + KanyoName
    s = tdy.day
    ss = '{0:02}'.format(s)
    DTime = '{0:04}'.format(tdy.year) + '{0:02}'.format(tdy.month) + '{0:02}'.format(tdy.day) + " " + '{0:02}'.format(tdy.hour) + '{0:02}'.format(tdy.minute) + '{0:02}'.format(tdy.second)
    PDFName = KanyoFolName + "_" + Hakkoumoto + "_" + Hakkou + "_" + MTitle + ".pdf"
    if MTitle == 'プレ申告データに関するお知らせ':
        dir_path = "//Sv05121a/e/電子ファイル/メッセージボックス/" + CfolName + "/eLTAX//" + KanyoFolName
    else:
        dir_path = "//Sv05121a/e/電子ファイル/メッセージボックス/" + CfolName + "/eLTAX受信通知"
    for current_dir, sub_dirs, files_list in os.walk(dir_path): 
      for file_name in files_list: 
        foldersItem = os.path.join(current_dir,file_name).replace('\u3000','')
        PDFSerch = PDFName in foldersItem
        try:
            if PDFSerch == True:
                return True
            else:
                print(foldersItem)
        except Exception:
            return False
#-----------------------------------------------------------------------------------------------------------------------------------------------------
def LoginLoop(H_SCode,H_TKCName,H_First,H_FirstP,H_SecondP):
    LogAns = eTaxWebCrawler(H_First,H_FirstP,"D:/PythonScript",H_SCode,H_TKCName)#Nanではない場合
    LogArray = LogAns[0].split("\n",1)
    H_LogAns = LogArray[0]#ログオン後のH1テキストを代入
    H_LogAnsOBJ = LogAns[1]#ログオン後のWEBドライバーを代入
    H_LogMSGAns = LogReturn(H_LogAns,H_LogAnsOBJ)#ログオン後のH1テキストをで処理分けしWEBテーブルページへ
    if not H_LogMSGAns == "ログインできませんでした。" and not H_LogMSGAns == "認証エラー" and not H_LogMSGAns == '該当するデータはありませんでした。':
        H_Lo = LogOnOuter(H_LogAnsOBJ)#WEBテーブル取得
        H_L_D = H_Lo[0]#WEBテーブルページ
        H_L_Row = H_Lo[1]#WEBテーブル行数
        for H_MSG_rowItem in range(H_L_Row):#WEBテーブル行数分ループ
            H_Parameters = ParGet(H_L_D,H_MSG_rowItem,H_L_Row)#WEBテーブルから要素取得
            H_P1 = H_Parameters[0]
            H_P2 = H_Parameters[1]
            H_P3 = H_Parameters[2]
            H_P4 = H_Parameters[3]
            SPDF = SortPDF(H_P3,H_P4,H_SCode,H_TKCName,H_P1,H_P2)

            if SPDF == False or SPDF == None:
                PrintIFS(H_P4,H_LogAnsOBJ)#メッセージボックスの内容に応じて処理分け
                RenamePDF(H_P3,H_P4,H_SCode,H_TKCName,H_P1,H_P2)#PDF保存先フォルダー作成後リネーム&移動 DownTime,MTitle,KanyoNo,KanyoName
                if H_MSG_rowItem == H_L_Row - 1:
                    H_LogAnsOBJ.quit()
                else:
                    H_LogAnsOBJ.switch_to.window(H_LogAnsOBJ.window_handles[0])#タブ移動する
                    WebDriverWait(H_LogAnsOBJ, 30).until(EC.presence_of_all_elements_located)#要素が読み込まれるまで最大30秒待つ
            else:
                print("ファイルが存在します。")
                if H_MSG_rowItem == H_L_Row - 1:
                    H_LogAnsOBJ.quit()
                else:
                    H_BackBtn = H_LogAnsOBJ.find_element_by_xpath("/html/body/div[2]/form/footer/div[1]/div/div[1]/a")
                    H_BackBtn.click()
    elif H_LogMSGAns == "ログインできませんでした。":
        NGstr = str(H_SCode) + "_" + H_TKCName + "_" + "ログインエラー1回目"
        NGstr = NGstr.replace('\uff0d', '-').replace('\xa0', '').replace('\u71c1','').replace('\u9348','').replace('\u9ad9','')
        NGLog.append(NGstr)
        H_LogAnsOBJ.quit()
        LogAns = eTaxWebCrawler(H_First,H_SecondP,"D:/PythonScript",H_SCode,H_TKCName)#Nanではない場合
        LogArray = LogAns[0].split("\n",1)
        H_LogAns = LogArray[0]#ログオン後のH1テキストを代入
        H_LogAnsOBJ = LogAns[1]#ログオン後のWEBドライバーを代入
        H_LogMSGAns = LogReturn(H_LogAns,H_LogAnsOBJ)#ログオン後のH1テキストをで処理分けしWEBテーブルページへ
        if H_LogMSGAns == "ログインできませんでした。":
            NGstr = str(H_SCode) + "_" + H_TKCName + "_" + "ログインエラー2回目"
            NGstr = NGstr.replace('\uff0d', '-').replace('\xa0', '').replace('\u71c1','').replace('\u9348','').replace('\u9ad9','')
            NGLog.append(NGstr)
            H_LogAnsOBJ.quit()
        elif H_LogMSGAns == "認証エラー":
            H_LogAnsOBJ.quit()
    elif H_LogMSGAns == "認証エラー":
        print(H_SCode + "_" + H_TKCName + "_" + "暗証番号の変更")
    elif H_LogMSGAns == '該当するデータはありませんでした。':
        NGstr = str(H_SCode) + "_" + H_TKCName + "_" + "データ無"
        NGstr = NGstr.replace('\uff0d', '-').replace('\xa0', '').replace('\u71c1','').replace('\u9348','').replace('\u9ad9','')
        NGLog.append(NGstr)
        H_LogAnsOBJ.quit()
    else:
        H_LogAnsOBJ.quit()
#-----------------------------------------------------------------------------------------------------------------------------------------------------
#lxmlインポート
import lxml.html
#pandasインポート
import pandas as pd
#配列計算関数numpyインポート
import numpy as np
#小数点切り捨ての為にmathをインポート
import math
#timeインポート
import time
#reインポート
import re
#seleniumインポート
from selenium import webdriver
from selenium.webdriver.chrome.options import Options#ブラウザオプションを与える
from selenium.webdriver.common.keys import Keys#センドキーコマンドを与える
from selenium.webdriver.common.action_chains import ActionChains#JavaScript実行の為にActionChainsコマンドを与える
from selenium.webdriver.support.ui import WebDriverWait#読込待機コマンドを与える
from selenium.webdriver.support import expected_conditions as EC#読込待機コマンドに条件式を与える
#jsonインポート
import json
#osインポート
import os
#datetimeインポート
from datetime import datetime as dt
#日付加減算インポート
from dateutil.relativedelta import relativedelta
#glob(フォルダファイルチェックコマンド)インポート
import glob
#shutil(フォルダファイル編集コマンド)インポート
import shutil
#例外処理判定の為のtracebackインポート
import traceback
#pandas(pd)で関与先データCSVを取得
H_url = '//Sv05121a/e/C 作業台/RPA/ALLDataBase/Heidi関与先DB.csv'
H_df = pd.read_csv(H_url,encoding='utf-8')
H_forCount = 0

H_dfRow = np.array(H_df).shape[0]#配列行数取得
H_dfCol = np.array(H_df).shape[1]#配列列数取得
OKLog = []
NGLog = []
for x in range(H_dfRow):
    try:
        if x > 119:
        #関与先DB配列をループして識別番号とPassを取得
            H_dfDataRow = H_df.loc[x]
            H_SCode = H_dfDataRow["SyanaiCode"]
            try:
                H_TKCName = H_dfDataRow["TKCName"].replace('\u3000', ' ')#空白\u3000を置換
            except:
                H_TKCName = H_dfDataRow["TKCName"]
            H_MSikibetu = H_dfDataRow["MirokuTihouzeiUserID"]
            H_TSikibetu = H_dfDataRow["TKCTihouzeiUserID"]
            try:
                H_ePass = H_dfDataRow["etaxPass"].replace('\u3000', ' ')#空白\u3000を置換
            except:
                H_ePass = H_dfDataRow["etaxPass"]
            try:
                H_elPass = H_dfDataRow["eltaxPass"].replace('\u3000', ' ')#空白\u3000を置換
            except:
                H_elPass = H_dfDataRow["eltaxPass"]

            if H_MSikibetu == H_MSikibetu:#自身比較のNan判定
                if H_ePass == H_ePass:#自身比較のNan判定
                    LoginLoop(H_SCode,H_TKCName,H_MSikibetu,H_ePass,H_elPass)
                    pd.DataFrame(OKLog).to_csv('//Sv05121a/e/電子ファイル/メッセージボックス/PyOKLog.csv', encoding = "shift-jis")
                    pd.DataFrame(NGLog).to_csv('//Sv05121a/e/電子ファイル/メッセージボックス/PyNGLog.csv', encoding = "shift-jis")
                else:
                    if H_elPass == H_elPass:#自身比較のNan判定
                        LoginLoop(H_SCode,H_TKCName,H_MSikibetu,H_ePass,H_elPass)
                        pd.DataFrame(OKLog).to_csv('//Sv05121a/e/電子ファイル/メッセージボックス/PyOKLog.csv', encoding = "shift-jis")
                        pd.DataFrame(NGLog).to_csv('//Sv05121a/e/電子ファイル/メッセージボックス/PyNGLog.csv', encoding = "shift-jis")
            elif H_TSikibetu == H_TSikibetu:
                if H_ePass == H_ePass:#自身比較のNan判定
                    LoginLoop(H_SCode,H_TKCName,H_TSikibetu,H_ePass,H_elPass)
                    pd.DataFrame(OKLog).to_csv('//Sv05121a/e/電子ファイル/メッセージボックス/PyOKLog.csv', encoding = "shift-jis")
                    pd.DataFrame(NGLog).to_csv('//Sv05121a/e/電子ファイル/メッセージボックス/PyNGLog.csv', encoding = "shift-jis")
                else:
                    if H_elPass == H_elPass:#自身比較のNan判定
                        LoginLoop(H_SCode,H_TKCName,H_TSikibetu,H_ePass,H_elPass)
                        pd.DataFrame(OKLog).to_csv('//Sv05121a/e/電子ファイル/メッセージボックス/PyOKLog.csv', encoding = "shift-jis")
                        pd.DataFrame(NGLog).to_csv('//Sv05121a/e/電子ファイル/メッセージボックス/PyNGLog.csv', encoding = "shift-jis")
                    else:
                        print("NoPassWord")
                        NGstr = str(H_SCode) + "_" + H_TKCName + "_" + "パスワードエラー"
                        NGstr = NGstr.replace('\uff0d', '-').replace('\xa0', '')
                        NGLog.append(NGstr)
                        pd.DataFrame(NGLog).to_csv('//Sv05121a/e/電子ファイル/メッセージボックス/PyNGLog.csv', encoding = "shift-jis")
            else:
                NGstr = str(H_SCode) + "_" + H_TKCName + "_" + "エラー"
                NGstr = NGstr.replace('\uff0d', '-').replace('\xa0', '')
                NGLog.append(NGstr)
                pd.DataFrame(NGLog).to_csv('//Sv05121a/e/電子ファイル/メッセージボックス/PyNGLog.csv', encoding = "shift-jis")
    except:
        traceback.print_exc()
        try:
            NGstr = str(H_SCode) + "_" + H_TKCName + "_" + "exceptエラー"
            NGstr = NGstr.replace('\uff0d', '-').replace('\xa0', '').replace('\u71c1','').replace('\u9348','').replace('\u9ad9','')
            NGLog.append(NGstr)
            pd.DataFrame(NGLog).to_csv('//Sv05121a/e/電子ファイル/メッセージボックス/PyNGLog.csv', encoding = "shift-jis")
        except:
            print("どうしようもないがな！")
