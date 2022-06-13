# pandasインポート
import pandas as pd

# 配列計算関数numpyインポート
import numpy as np

# 小数点切り捨ての為にmathをインポート
import math

# timeインポート
import time

# reインポート
import re

# seleniumインポート
from selenium import webdriver
from selenium.webdriver.chrome.options import Options  # ブラウザオプションを与える
from selenium.webdriver.support.ui import WebDriverWait  # 読込待機コマンドを与える
from selenium.webdriver.support import expected_conditions as EC  # 読込待機コマンドに条件式を与える

# jsonインポート
import json

# osインポート
import os

# datetimeインポート
from datetime import datetime as dt

# glob(フォルダファイルチェックコマンド)インポート
import glob

# shutil(フォルダファイル編集コマンド)インポート
import shutil

# 例外処理判定の為のtracebackインポート
import traceback

# -----------------------------------------------------------------------------------------------
def eTaxWebCrawler(H_id, H_pass, H_fold, H_SC, H_TN):
    # 作成した変数は頭にH_をつける事
    # ブラウザ閲覧時のオプションを指定するオブジェクト"options"を作成
    H_options = Options()
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
    prefs = {
        "printing.print_preview_sticky_settings.appState": json.dumps(appState),
        "savefile.default_directory": H_fold,  # "D:/PythonScript"
    }
    H_options.add_experimental_option("prefs", prefs)
    # 必要に応じてオプションを追加
    H_options.add_argument("--window-size=1024,768")
    H_options.add_argument("--kiosk-printing")
    # ドライバのpathを指定
    H_path = os.getcwd().replace("\\", "/") + "/chromedriver"
    # WEBURLの指定
    H_WEBurl = "https://uketsuke.e-tax.nta.go.jp/UF_APP/lnk/loginCtlKakutei"
    # ブラウザのウィンドウを表すオブジェクト"driver"を作成
    H_driver = webdriver.Chrome(executable_path=H_path, chrome_options=H_options)
    H_driver.get(H_WEBurl)
    # 初めの拡張機能ポップアップを閉じる
    try:
        H_PopupClose_btn = H_driver.find_element_by_xpath(
            "/html/body/div[4]/div[2]/div[2]/form/input[1]"
        )  # 閉じるボタンの要素指定
        H_PopupClose_btn.click()
        WebDriverWait(H_driver, 30).until(
            EC.presence_of_all_elements_located
        )  # 要素が読み込まれるまで最大30秒待つ
    except:
        WebDriverWait(H_driver, 30).until(
            EC.presence_of_all_elements_located
        )  # 要素が読み込まれるまで最大30秒待つ
    # ログイン画面要素指定------------------------------------------------------------------------------------------------------
    # 利用者識別番号入力欄をxpathで取得
    H_Sikibetu_box1 = H_driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div/div[2]/form[1]/table/tbody/tr/td/input[1]"
    )
    H_Sikibetu_box2 = H_driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div/div[2]/form[1]/table/tbody/tr/td/input[2]"
    )
    H_Sikibetu_box3 = H_driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div/div[2]/form[1]/table/tbody/tr/td/input[3]"
    )
    H_Sikibetu_box4 = H_driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div/div[2]/form[1]/table/tbody/tr/td/input[4]"
    )
    # ログインPASS入力欄をxpathで取得
    H_LogPassBox = H_driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div/div[2]/form[2]/table/tbody/tr/td/span[1]/input"
    )
    H_Log_btn = H_driver.find_element_by_xpath(
        "/html/body/div[1]/div[2]/div/div[2]/form[2]/p/input[1]"
    )
    # WEB操作--------------------------------------------------------------------------------------------------------------------
    H_idArray = [H_id[i : i + 4] for i in range(0, len(H_id), 4)]  # 引数H_idを4文字づつ分割
    H_Sikibetu_box1.send_keys(H_idArray[0])
    H_Sikibetu_box2.send_keys(H_idArray[1])
    H_Sikibetu_box3.send_keys(H_idArray[2])
    H_Sikibetu_box4.send_keys(H_idArray[3])
    H_LogPassBox.send_keys(H_pass)
    H_Log_btn.click()
    WebDriverWait(H_driver, 30).until(
        EC.presence_of_all_elements_located
    )  # 要素が読み込まれるまで最大30秒待つ
    # ---------------------------------------------------------------------------------------------------------------------------
    try:
        H_H1 = H_driver.find_element_by_xpath("/html/body/div[1]/div[2]/h1")  # H1要素を取得
        return H_H1.text, H_driver
    except Exception:
        H_H1 = H_driver.find_element_by_xpath(
            "/html/body/div[1]/div[2]/form/h1"
        )  # H1要素を取得
        return H_H1.text, H_driver
    else:
        pass


# -----------------------------------------------------------------------------------------------------------------------------------------------------
def LogOnOuter(H_driver):
    # ログイン成功の場合
    # WEB画面要素指定------------------------------------------------------------------------------------------------------
    try:
        H_driver.find_element_by_xpath(
            "/html/body/div[1]/div[2]/p[1]"
        )  # メッセージボックスの中身ページのH1を指定
        H_driver.find_element_by_xpath(
            "/html/body/div[1]/div[2]/div/form/table/tbody/tr[1]"
        )  # メッセージボックスのテーブルをxpath取得
    except Exception:
        pass
    else:
        dfs = pd.read_html(H_driver.page_source, encoding="cp932")  # pandasにWEBURLをぶっこむ
        H_MSG_row = len(dfs[0])  # テーブル行数を代入
        return H_driver, H_MSG_row


# -----------------------------------------------------------------------------------------------------------------------------------------------------
def ParGet(H_driver, H_MSG_rowItem, H_MSG_row):
    try:
        # WEBTable日付
        H_MSG_TableItem1 = H_driver.find_element_by_xpath(
            "/html/body/div[1]/div[2]/div/form/table/tbody/tr[{}]/td[1]".format(
                H_MSG_rowItem + 1
            )
        ).text
        H_MSG_TableItem2 = H_driver.find_element_by_xpath(
            "/html/body/div[1]/div[2]/div/form/table/tbody/tr[{}]/td[2]".format(
                H_MSG_rowItem + 1
            )
        ).text
        H_MSG_TableItem3 = H_driver.find_element_by_xpath(
            "/html/body/div[1]/div[2]/div/form/table/tbody/tr[{}]/td[3]".format(
                H_MSG_rowItem + 1
            )
        ).text
        # WEBTableメールタイトル
        H_MSG_TableItem4 = H_driver.find_element_by_xpath(
            "/html/body/div[1]/div[2]/div/form/table/tbody/tr[{}]/td[4]".format(
                H_MSG_rowItem + 1
            )
        ).text.replace("\u3000", " ")
        H_MSG_TableItem5 = H_driver.find_element_by_xpath(
            "/html/body/div[1]/div[2]/div/form/table/tbody/tr[{}]/td[5]".format(
                H_MSG_rowItem + 1
            )
        ).text
        H_MSG_TableItem6 = H_driver.find_element_by_xpath(
            "/html/body/div[1]/div[2]/div/form/table/tbody/tr[{}]/td[6]".format(
                H_MSG_rowItem + 1
            )
        ).text
        H_MSG_TableItem7 = H_driver.find_element_by_xpath(
            "/html/body/div[1]/div[2]/div/form/table/tbody/tr[{}]/td[7]".format(
                H_MSG_rowItem + 1
            )
        ).text

    except Exception:
        pass
        # print(str(H_SC) + "_" + H_TN + "データ無")
    else:
        H_result = H_driver.page_source.split(
            "goDetail", H_MSG_row
        )  # ページソースからgoDetail区切りをテーブル行数分行う
        H_result = H_result[H_MSG_rowItem + 1].split(
            ">"
        )  # goDetail区切り配列からループ回数に応じたJavaScript引数を抽出
        H_OnClickPar = (
            H_result[00]
            .replace("(", "")
            .replace("/", "")
            .replace(")", "")
            .replace('"', "")
        )  # JavaScript引数を置換して成型
        H_driver.execute_script(
            "javascript:goDetail({})".format(H_OnClickPar)
        )  # 抽出したJavaScript引数を利用して実行
        WebDriverWait(H_driver, 30).until(
            EC.presence_of_all_elements_located
        )  # 要素が読み込まれるまで最大30秒待つ
        H_driver.switch_to.window(H_driver.window_handles[1])  # 開いたタブに移動する
        # -----------------------------------------ページ内条件分岐---------------------------------------------
        H_Title = H_driver.find_element_by_xpath(
            "/html/body/div[1]/div[2]/h2[1]"
        ).text  # 先頭H2タイトル取得
        return (
            H_Title,
            H_MSG_TableItem1,
            H_MSG_TableItem2,
            H_MSG_TableItem3,
            H_MSG_TableItem4,
            H_MSG_TableItem5,
            H_MSG_TableItem6,
            H_MSG_TableItem7,
        )


# -----------------------------------------------------------------------------------------------------------------------------------------------------
def PrintIFS(H_Title, H_driver):
    if re.search("法定調書の提出について", H_Title):
        H_driver.execute_script("window.print();")  # 開いたタブを印刷
        # time.sleep(4)
        WebDriverWait(H_driver, 30).until(
            EC.presence_of_all_elements_located
        )  # 要素が読み込まれるまで最大30秒待つ
        H_driver.close()
        H_driver.switch_to.window(H_driver.window_handles[0])  # タブ移動する
        return "法定調書"
    elif re.search("申告のお知らせ", H_Title):
        H_driver.find_element_by_xpath(
            "/html/body/div[1]/div[2]/form/p/input"
        ).click()  # 申告のお知らせボタンをクリック
        WebDriverWait(H_driver, 30).until(
            EC.presence_of_all_elements_located
        )  # 要素が読み込まれるまで最大30秒待つ
        H_driver.execute_script("window.print();")  # 開いたタブを印刷
        # time.sleep(4)
        WebDriverWait(H_driver, 30).until(
            EC.presence_of_all_elements_located
        )  # 要素が読み込まれるまで最大30秒待つ
        H_driver.close()
        H_driver.switch_to.window(H_driver.window_handles[0])  # タブ移動する
        return "申告のお知らせ"
    elif re.search("振替納税のお知らせ", H_Title):
        H_driver.find_element_by_xpath(
            "/html/body/div[1]/div[2]/form/p/input"
        ).click()  # 申告のお知らせボタンをクリック
        WebDriverWait(H_driver, 30).until(
            EC.presence_of_all_elements_located
        )  # 要素が読み込まれるまで最大30秒待つ
        H_driver.execute_script("window.print();")  # 開いたタブを印刷
        # time.sleep(4)
        WebDriverWait(H_driver, 30).until(
            EC.presence_of_all_elements_located
        )  # 要素が読み込まれるまで最大30秒待つ
        H_driver.close()
        H_driver.switch_to.window(H_driver.window_handles[0])  # タブ移動する
        return "振替納税のお知らせ"
    else:
        H_driver.execute_script("window.print();")  # 開いたタブを印刷
        # time.sleep(4)
        WebDriverWait(H_driver, 30).until(
            EC.presence_of_all_elements_located
        )  # 要素が読み込まれるまで最大30秒待つ
        H_driver.close()
        H_driver.switch_to.window(H_driver.window_handles[0])  # タブ移動する
        return H_Title


# ----------------------------------------------------------------------------------------------------------------------------
def LogReturn(LogAns, H_driver):
    if LogAns == "メインメニュー":  # ログイン成功の場合
        # WEB画面要素指定------------------------------------------------------------------------------------------------------
        try:
            H_MSG_OpenMyNo = H_driver.find_element_by_xpath(
                "/html/body/div[1]/div[2]/div/div[1]/div/div[1]/div[3]/div/form/p/input"
            )
            H_MSG_OpenMyNo.click()
            WebDriverWait(H_driver, 30).until(
                EC.presence_of_all_elements_located
            )  # 要素が読み込まれるまで最大30秒待つ
            return H_driver.find_element_by_xpath(
                "/html/body/div[1]/div[2]/p[1]"
            ).text  # メッセージボックス画面の文言を返す
        except:
            H_MSG_Open = H_driver.find_element_by_xpath(
                "/html/body/div[1]/div[2]/div/div[1]/div/div[1]/div[2]/form/p/input"
            )  # メッセージボックスを開くボタンをxpath指定
            H_MSG_Open.click()
            WebDriverWait(H_driver, 30).until(
                EC.presence_of_all_elements_located
            )  # 要素が読み込まれるまで最大30秒待つ
            return H_driver.find_element_by_xpath(
                "/html/body/div[1]/div[2]/p[1]"
            ).text  # メッセージボックス画面の文言を返す
    elif LogAns == "認証エラー":  # ログイン失敗の場合
        WebDriverWait(H_driver, 30).until(
            EC.presence_of_all_elements_located
        )  # 要素が読み込まれるまで最大30秒待つ
        return "認証エラー"
    elif LogAns == "暗証番号の変更":  # ログイン失敗の場合
        try:
            H_PassKousinBtn = H_driver.find_element_by_xpath(
                "/html/body/div[2]/div/form[2]/input[3]"
            )
            H_PassKousinBtn.click()
            WebDriverWait(H_driver, 30).until(
                EC.presence_of_all_elements_located
            )  # 要素が読み込まれるまで最大30秒待つ
            try:
                H_MSG_OpenMyNo = H_driver.find_element_by_xpath(
                    "/html/body/div[1]/div[2]/div/div[1]/div/div[1]/div[3]/div/form/p/input"
                )
                H_MSG_OpenMyNo.click()
                WebDriverWait(H_driver, 30).until(
                    EC.presence_of_all_elements_located
                )  # 要素が読み込まれるまで最大30秒待つ
                return H_driver.find_element_by_xpath(
                    "/html/body/div[1]/div[2]/p[1]"
                ).text  # メッセージボックス画面の文言を返す
            except:
                H_MSG_Open = H_driver.find_element_by_xpath(
                    "/html/body/div[1]/div[2]/div/div[1]/div/div[1]/div[2]/form/p/input"
                )  # メッセージボックスを開くボタンをxpath指定
                H_MSG_Open.click()
                WebDriverWait(H_driver, 30).until(
                    EC.presence_of_all_elements_located
                )  # 要素が読み込まれるまで最大30秒待つ
                return H_driver.find_element_by_xpath(
                    "/html/body/div[1]/div[2]/p[1]"
                ).text  # メッセージボックス画面の文言を返す
        except Exception:
            pass
        return "暗証番号の変更"
    else:  # その他の場合
        WebDriverWait(H_driver, 30).until(
            EC.presence_of_all_elements_located
        )  # 要素が読み込まれるまで最大30秒待つ


# -----------------------------------------------------------------------------------------------------------------------------------------------------
def RenamePDF(DownTime, MTitle, KanyoNo, KanyoName):
    tdy = dt.strptime(DownTime, "%Y/%m/%d %H:%M:%S")  # 文字列を日付型に変換
    CfolName = str(tdy.year) + "-" + str(tdy.month)
    folders = glob.glob("//Sv05121a/e/電子ファイル/メッセージボックス/*-*")
    KanyoFolName = str(KanyoNo) + "_" + KanyoName
    for foldersItem in folders:
        if foldersItem == "//Sv05121a/e/電子ファイル/メッセージボックス\\" + CfolName:
            Subfolders = glob.glob(foldersItem + "/*")  # フォルダーがあった場合
            MotherFol = foldersItem + "\\eTAX"
            for SubfoldersItem in Subfolders:
                if SubfoldersItem.replace("\u3000", " ") == MotherFol:
                    SubFFlag = 1
                    print(MotherFol + "あります")
                    break
                else:
                    SubFFlag = 0
            if SubFFlag == 0:
                os.mkdir(foldersItem + "/eTAX")
                print(MotherFol + "作りました。")
                break
            Tfolders = glob.glob(foldersItem + "\\eTAX" + "/*")  # フォルダーがあった場合
            ChildFol = foldersItem + "\\eTAX" + "\\" + KanyoFolName
            TFFlag = 0
            for TfoldersItem in Tfolders:
                if TfoldersItem == ChildFol:
                    TFFlag = 1
                    print(ChildFol + "あります")
                    break
                else:
                    TFFlag = 0
            if TFFlag == 0:
                os.mkdir(foldersItem + "/eTAX" + "/" + KanyoFolName)
                print(ChildFol + "作りました。")
                break
            break
        else:
            print("ありません")  # フォルダーがなかった場合
    PDFfolder = glob.glob(os.getcwd().replace("\\", "/") + "/" + "*.pdf")  # フォルダーがあった場合
    for PDFfolderItem in PDFfolder:
        PDFSerch = "国税電子申告・納税システム" in PDFfolderItem
        DTime = (
            "{0:04}".format(tdy.year)
            + "{0:02}".format(tdy.month)
            + "{0:02}".format(tdy.day)
            + " "
            + "{0:02}".format(tdy.hour)
            + "{0:02}".format(tdy.minute)
            + "{0:02}".format(tdy.second)
        )
        PDFName = KanyoFolName + "_" + MTitle + "_" + DTime + ".pdf"
        PDFPath = os.getcwd().replace("\\", "/") + "/" + PDFName
        PDFPath = PDFPath.replace("/", "\\")

        try:
            if PDFSerch is True:
                os.rename(PDFfolderItem, PDFPath)
                MovePDFPath = ChildFol + "/" + PDFName
                MovePDFPath = MovePDFPath.replace("/", "\\")
                shutil.move(PDFPath, MovePDFPath)
                OKstr = MovePDFPath + "成功"
                OKstr = OKstr.replace("\uff0d", "-").replace("\xa0", "")
                OKLog.append(OKstr)
            # 'D:\\PythonScript\\国税電子申告・納税システム－SU00S100 メール詳細 (1).pdf'
            else:
                NGstr = MovePDFPath + "_リネーム失敗-国税電子申告・納税システムが含まれないファイル名-"
                NGstr = NGstr.replace("\uff0d", "-").replace("\xa0", "")
                NGLog.append(NGstr)
        except:
            traceback.print_exc()
            NGstr = MovePDFPath + "_リネーム失敗-トレースバックエラー-"
            NGstr = NGstr.replace("\uff0d", "-").replace("\xa0", "")
            NGLog.append(NGstr)


# -----------------------------------------------------------------------------------------------------------------------------------------------------
def SortPDF(DownTime, MTitle, KanyoNo, KanyoName):
    tdy = dt.strptime(DownTime, "%Y/%m/%d %H:%M:%S")  # 文字列を日付型に変換
    CfolName = str(tdy.year) + "-" + str(tdy.month)
    KanyoFolName = str(KanyoNo) + "_" + KanyoName
    DTime = (
        "{0:04}".format(tdy.year)
        + "{0:02}".format(tdy.month)
        + "{0:02}".format(tdy.day)
        + " "
        + "{0:02}".format(tdy.hour)
        + "{0:02}".format(tdy.minute)
        + "{0:02}".format(tdy.second)
    )
    PDFName = KanyoFolName + "_" + MTitle + "_" + DTime + ".pdf"
    dir_path = "//Sv05121a/e/電子ファイル/メッセージボックス/" + CfolName + "/eTax"
    for current_dir, sub_dirs, files_list in os.walk(dir_path):
        for file_name in files_list:
            foldersItem = os.path.join(current_dir, file_name)
            PDFSerch = PDFName in foldersItem
            try:
                if PDFSerch is True:
                    return True
                else:
                    print(foldersItem)
            except:
                Exception


# -----------------------------------------------------------------------------------------------------------------------------------------------------
def LoginLoop(H_SCode, H_TKCName, H_First, H_FirstP, H_SecondP):
    LogAns = eTaxWebCrawler(
        str(math.floor(H_First)),
        H_FirstP,
        os.getcwd().replace("\\", "/"),
        H_SCode,
        H_TKCName,
    )  # Nanではない場合
    H_LogAns = LogAns[0]  # ログオン後のH1テキストを代入
    H_LogAnsOBJ = LogAns[1]  # ログオン後のWEBドライバーを代入
    H_LogMSGAns = LogReturn(H_LogAns, H_LogAnsOBJ)  # ログオン後のH1テキストをで処理分けしWEBテーブルページへ
    if not H_LogMSGAns == "表示するメッセージはありません。" and not H_LogMSGAns == "認証エラー":
        H_Lo = LogOnOuter(H_LogAnsOBJ)  # WEBテーブル取得
        H_L_D = H_Lo[0]  # WEBテーブルページ
        H_L_Row = H_Lo[1]  # WEBテーブル行数
        for H_MSG_rowItem in range(H_L_Row):  # WEBテーブル行数分ループ
            H_Parameters = ParGet(H_L_D, H_MSG_rowItem, H_L_Row)  # WEBテーブルから要素取得
            H_P1 = H_Parameters[0]
            H_P2 = H_Parameters[1]
            H_P5 = H_Parameters[4]
            SPDF = SortPDF(H_P2, H_P5, H_SCode, H_TKCName)
            Hurikae = "振替納税のお知らせ" in H_P5
            if SPDF is False or SPDF is None or Hurikae is True:
                PrintIFS(H_P1, H_LogAnsOBJ)  # メッセージボックスの内容に応じて処理分け
                RenamePDF(H_P2, H_P5, H_SCode, H_TKCName)  # PDF保存先フォルダー作成後リネーム&移動
                if H_MSG_rowItem == H_L_Row - 1:
                    H_LogAnsOBJ.quit()
                    time.sleep(1)
                else:
                    H_LogAnsOBJ.switch_to.window(
                        H_LogAnsOBJ.window_handles[0]
                    )  # タブ移動する
                    WebDriverWait(H_LogAnsOBJ, 30).until(
                        EC.presence_of_all_elements_located
                    )  # 要素が読み込まれるまで最大30秒待つ
            else:
                H_LogAnsOBJ.close()
                time.sleep(1)
                if H_MSG_rowItem == H_L_Row - 1:
                    H_LogAnsOBJ.quit()
                    time.sleep(2)
                else:
                    H_LogAnsOBJ.switch_to.window(
                        H_LogAnsOBJ.window_handles[0]
                    )  # タブ移動する
                    WebDriverWait(H_LogAnsOBJ, 30).until(
                        EC.presence_of_all_elements_located
                    )  # 要素が読み込まれるまで最大30秒待つ
    elif H_LogMSGAns == "認証エラー":
        H_LogAnsOBJ.quit()
        time.sleep(1)
        LogAns = eTaxWebCrawler(
            str(math.floor(H_First)),
            H_SecondP,
            os.getcwd().replace("\\", "/"),
            H_SCode,
            H_TKCName,
        )  # Nanではない場合
        H_LogAns = LogAns[0]  # ログオン後のH1テキストを代入
        H_LogAnsOBJ = LogAns[1]  # ログオン後のWEBドライバーを代入
        H_LogMSGAns = LogReturn(H_LogAns, H_LogAnsOBJ)  # ログオン後のH1テキストをで処理分けしWEBテーブルページへ
        if not H_LogMSGAns == "表示するメッセージはありません。" and not H_LogMSGAns == "認証エラー":
            H_Lo = LogOnOuter(H_LogAnsOBJ)  # WEBテーブル取得
            H_L_D = H_Lo[0]  # WEBテーブルページ
            H_L_Row = H_Lo[1]  # WEBテーブル行数
            for H_MSG_rowItem in range(H_L_Row):  # WEBテーブル行数分ループ
                H_Parameters = ParGet(H_L_D, H_MSG_rowItem, H_L_Row)  # WEBテーブルから要素取得
                H_P1 = H_Parameters[0]
                H_P2 = H_Parameters[1]
                H_P5 = H_Parameters[4]
                SPDF = SortPDF(H_P2, H_P5, H_SCode, H_TKCName)
                Hurikae = "振替納税のお知らせ" in H_P5
                if SPDF is False or SPDF is None or Hurikae is True:
                    PrintIFS(H_P1, H_LogAnsOBJ)  # メッセージボックスの内容に応じて処理分け
                    RenamePDF(H_P2, H_P5, H_SCode, H_TKCName)  # PDF保存先フォルダー作成後リネーム&移動
                    if H_MSG_rowItem == H_L_Row - 1:
                        H_LogAnsOBJ.quit()
                        time.sleep(1)
                    else:
                        H_LogAnsOBJ.switch_to.window(
                            H_LogAnsOBJ.window_handles[0]
                        )  # タブ移動する
                        WebDriverWait(H_LogAnsOBJ, 30).until(
                            EC.presence_of_all_elements_located
                        )  # 要素が読み込まれるまで最大30秒待つ
                else:
                    H_LogAnsOBJ.close()
                    time.sleep(1)
                    if H_MSG_rowItem == H_L_Row - 1:
                        H_LogAnsOBJ.quit()
                        time.sleep(1)
                    else:
                        H_LogAnsOBJ.switch_to.window(
                            H_LogAnsOBJ.window_handles[0]
                        )  # タブ移動する
                        WebDriverWait(H_LogAnsOBJ, 30).until(
                            EC.presence_of_all_elements_located
                        )  # 要素が読み込まれるまで最大30秒待つ
        elif H_LogMSGAns == "認証エラー":
            H_LogAnsOBJ.quit()
            time.sleep(1)
    elif H_LogMSGAns == "認証エラー":
        print(H_SCode + "_" + H_TKCName + "_" + "暗証番号の変更")
    else:
        H_LogAnsOBJ.quit()
        time.sleep(1)


# -----------------------------------------------------------------------------------------------------------------------------------------------------
# pandas(pd)で関与先データCSVを取得
H_url = "//Sv05121a/e/C 作業台/RPA/ALLDataBase/Heidi関与先DB.csv"
H_df = pd.read_csv(H_url, encoding="utf-8")
H_forCount = 0
# テストケース
H_dfRow = np.array(H_df).shape[0]  # 配列行数取得
H_dfCol = np.array(H_df).shape[1]  # 配列列数取得
OKLog = []
NGLog = []
for x in range(H_dfRow):
    try:
        if x >= 1000:
            # 関与先DB配列をループして識別番号とPassを取得
            H_dfDataRow = H_df.loc[x]
            H_SCode = H_dfDataRow["SyanaiCode"]
            try:
                H_TKCName = H_dfDataRow["TKCName"].replace("\u3000", " ")  # 空白\u3000を置換
            except:
                H_TKCName = H_dfDataRow["TKCName"]
            H_MSikibetu = H_dfDataRow["MirokuKokuzeiUserCode"]
            H_TSikibetu = H_dfDataRow["TKCKokuzeiUserCode"]
            try:
                H_ePass = H_dfDataRow["etaxPass"].replace("\u3000", " ")  # 空白\u3000を置換
            except:
                H_ePass = H_dfDataRow["etaxPass"]
            try:
                H_elPass = H_dfDataRow["eltaxPass"].replace(
                    "\u3000", " "
                )  # 空白\u3000を置換
            except:
                H_elPass = H_dfDataRow["eltaxPass"]

            if H_MSikibetu == H_MSikibetu:  # 自身比較のNan判定
                if H_ePass == H_ePass:  # 自身比較のNan判定
                    LoginLoop(H_SCode, H_TKCName, H_MSikibetu, H_ePass, H_elPass)
                    pd.DataFrame(OKLog).to_csv(
                        "//Sv05121a/e/電子ファイル/メッセージボックス/PyOKLog.csv",
                        encoding="shift-jis",
                    )
                    pd.DataFrame(NGLog).to_csv(
                        "//Sv05121a/e/電子ファイル/メッセージボックス/PyNGLog.csv",
                        encoding="shift-jis",
                    )
                else:
                    if H_elPass == H_elPass:  # 自身比較のNan判定
                        LoginLoop(H_SCode, H_TKCName, H_MSikibetu, H_ePass, H_elPass)
                        pd.DataFrame(OKLog).to_csv(
                            "//Sv05121a/e/電子ファイル/メッセージボックス/PyOKLog.csv",
                            encoding="shift-jis",
                        )
                        pd.DataFrame(NGLog).to_csv(
                            "//Sv05121a/e/電子ファイル/メッセージボックス/PyNGLog.csv",
                            encoding="shift-jis",
                        )
            elif H_TSikibetu == H_TSikibetu:
                if H_ePass == H_ePass:  # 自身比較のNan判定
                    LoginLoop(H_SCode, H_TKCName, H_TSikibetu, H_ePass, H_elPass)
                    pd.DataFrame(OKLog).to_csv(
                        "//Sv05121a/e/電子ファイル/メッセージボックス/PyOKLog.csv",
                        encoding="shift-jis",
                    )
                    pd.DataFrame(NGLog).to_csv(
                        "//Sv05121a/e/電子ファイル/メッセージボックス/PyNGLog.csv",
                        encoding="shift-jis",
                    )
                else:
                    if H_elPass == H_elPass:  # 自身比較のNan判定
                        LoginLoop(H_SCode, H_TKCName, H_TSikibetu, H_ePass, H_elPass)
                        pd.DataFrame(OKLog).to_csv(
                            "//Sv05121a/e/電子ファイル/メッセージボックス/PyOKLog.csv",
                            encoding="shift-jis",
                        )
                        pd.DataFrame(NGLog).to_csv(
                            "//Sv05121a/e/電子ファイル/メッセージボックス/PyNGLog.csv",
                            encoding="shift-jis",
                        )
                    else:
                        print("NoPassWord")
                        NGstr = str(H_SCode) + "_" + H_TKCName + "_" + "パスワードエラー"
                        NGstr = NGstr.replace("\uff0d", "-").replace("\xa0", "")
                        NGLog.append(NGstr)
                        pd.DataFrame(NGLog).to_csv(
                            "//Sv05121a/e/電子ファイル/メッセージボックス/PyNGLog.csv",
                            encoding="shift-jis",
                        )
            else:
                NGstr = str(H_SCode) + "_" + H_TKCName + "_" + "エラー"
                NGstr = NGstr.replace("\uff0d", "-").replace("\xa0", "")
                NGLog.append(NGstr)
                pd.DataFrame(NGLog).to_csv(
                    "//Sv05121a/e/電子ファイル/メッセージボックス/PyNGLog.csv", encoding="shift-jis"
                )
    except:
        traceback.print_exc()
        try:
            NGstr = str(H_SCode) + "_" + H_TKCName + "_" + "exceptエラー"
            NGstr = (
                NGstr.replace("\uff0d", "-")
                .replace("\xa0", "")
                .replace("\u71c1", "")
                .replace("\u9348", "")
                .replace("\u9ad9", "")
            )
            NGLog.append(NGstr)
            pd.DataFrame(NGLog).to_csv(
                "//Sv05121a/e/電子ファイル/メッセージボックス/PyNGLog.csv", encoding="shift-jis"
            )
        except:
            print("どうしようもないがな！")
