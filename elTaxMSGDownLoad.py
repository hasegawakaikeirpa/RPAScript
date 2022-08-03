# pandasインポート
import pandas as pd

# 配列計算関数numpyインポート
import numpy as np

# timeインポート
import time

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

# 日付加減算インポート
from dateutil.relativedelta import relativedelta

# glob(フォルダファイルチェックコマンド)インポート
import glob

# shutil(フォルダファイル編集コマンド)インポート
import shutil

# 例外処理判定の為のtracebackインポート
import traceback

# logger設定------------------------------------------------------------------------------------------------------------
import logging.config

logging.config.fileConfig(r"LogConf\logging_debugelTaxLog.conf")
logger = logging.getLogger(__name__)
# ----------------------------------------------------------------------------------------------------------------------
def eTaxWebCrawler(H_id, H_pass, H_fold, H_SC, H_TN):
    logger.debug("WebDriver起動")
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
    H_WEBurl = "https://www.portal.eltax.lta.go.jp/apa/web/webindexb#eLTAX"
    # ブラウザのウィンドウを表すオブジェクト"driver"を作成
    H_driver = webdriver.Chrome(executable_path=H_path, chrome_options=H_options)
    H_driver.get(H_WEBurl)
    WebDriverWait(H_driver, 30).until(
        EC.presence_of_all_elements_located
    )  # 要素が読み込まれるまで最大30秒待つ
    # 初めの拡張機能ポップアップを閉じる
    time.sleep(1)
    H_PopupCheck_btn = H_driver.find_element_by_xpath(
        "/html/body/div[3]/div[2]/div/form/div/div[1]/input"
    )
    H_driver.execute_script("arguments[0].click();", H_PopupCheck_btn)
    H_PopupClose_btn = H_driver.find_element_by_xpath(
        "/html/body/div[3]/div[2]/div/form/div/div[2]/div[1]/a"
    )  # 閉じるボタンの要素指定
    H_PopupClose_btn.click()
    WebDriverWait(H_driver, 30).until(
        EC.presence_of_all_elements_located
    )  # 要素が読み込まれるまで最大30秒待つ
    # ログイン画面要素指定------------------------------------------------------------------------------------------------------
    # 利用者識別番号入力欄をxpathで取得
    H_Sikibetu_box1 = H_driver.find_element_by_xpath(
        "/html/body/div[2]/form/div/div/div[1]/div/ul[1]/li[1]/input"
    )
    # ログインPASS入力欄をxpathで取得
    H_LogPassBox = H_driver.find_element_by_xpath(
        "/html/body/div[2]/form/div/div/div[1]/div/ul[1]/li[2]/input"
    )
    H_Log_btn = H_driver.find_element_by_xpath(
        "/html/body/div[2]/form/div/div/div[1]/div/button"
    )
    # WEB操作--------------------------------------------------------------------------------------------------------------------
    H_Sikibetu_box1.send_keys(H_id)
    H_LogPassBox.send_keys(H_pass)
    H_Log_btn.click()
    WebDriverWait(H_driver, 30).until(
        EC.presence_of_all_elements_located
    )  # 要素が読み込まれるまで最大30秒待つ
    # ---------------------------------------------------------------------------------------------------------------------------
    try:
        WebDriverWait(H_driver, 30).until(
            EC.presence_of_all_elements_located
        )  # 要素が読み込まれるまで最大30秒待つ
        time.sleep(1)
        H_H1 = H_driver.find_element_by_xpath(
            "/html/body/div[3]/form/div/div/div[1]/div/p"
        )  # H1要素を取得
        logger.debug(H_H1.text)
        return H_H1.text, H_driver
    except Exception:
        try:
            H_H1 = H_driver.find_element_by_xpath(
                "/html/body/div[1]/div[2]/form/h1"
            )  # H1要素を取得
            logger.debug(H_H1.text)
            return H_H1.text, H_driver
        except Exception:
            try:
                H_H1 = H_driver.find_element_by_xpath(
                    "/html/body/div[2]/form/div/div/div/div/div[1]/div[3]/ul/li[1]/a"
                )  # H1要素を取得
                logger.debug(H_H1.text)
                return H_H1.text, H_driver
            except Exception:
                H_H1 = H_driver.find_element_by_xpath(
                    "/html/body/div[2]/div[2]/div/form/div/p"
                )  # H1要素を取得
                if "現在登録されている電子証明書は、有効期限を過ぎています。" in H_H1.text:  # 有効期限切れの場合は更新[いいえ]を選択
                    H_KousinBtn = H_driver.find_element_by_xpath(
                        "/html/body/div[2]/div[2]/div/form/div/div/div[2]/a"
                    )
                    H_KousinBtn.click()
                    WebDriverWait(H_driver, 30).until(
                        EC.presence_of_all_elements_located
                    )  # 要素が読み込まれるまで最大30秒待つ
                    H_H1 = H_driver.find_element_by_xpath(
                        "/html/body/div[1]/form/div/div/div/div/div[1]/div[3]/ul/li[1]/a"
                    )  # H1要素を取得
                    logger.debug(H_H1.text)
                return H_H1.text, H_driver
    else:
        pass


# -----------------------------------------------------------------------------------------------------------------------------------------------------
def LogOnOuter(H_driver):
    # ログイン成功の場合
    # WEB画面要素指定------------------------------------------------------------------------------------------------------
    try:
        H_driver.find_element_by_xpath(
            "/html/body/div[2]/form/div/div/div[2]/div[2]/div[1]"
        )  # メッセージボックスのテーブルをxpath取得
        # /html/body/div[2]/form/div/div/div[2]/div[2]/div[1]/div[2]/table
    except Exception:
        pass
    else:

        dfs = pd.read_html(H_driver.page_source, encoding="cp932")  # pandasにWEBURLをぶっこむ
        H_MSG_row = len(dfs[2])  # テーブル行数を代入
        return H_driver, H_MSG_row


# -----------------------------------------------------------------------------------------------------------------------------------------------------
def ParGet(H_driver, H_MSG_rowItem, H_MSG_row):
    try:
        # WEBTable
        H_FirstMSG_Cbx = H_driver.find_element_by_xpath(
            "/html/body/div[2]/form/div/div/div[2]/div[2]/div[1]/div[2]/table/tbody/tr[{}]/td[1]/div/label".format(
                H_MSG_rowItem
            )
        )  # 一行上のチェックボックス
        H_MSG_Cbx = H_driver.find_element_by_xpath(
            "/html/body/div[2]/form/div/div/div[2]/div[2]/div[1]/div[2]/table/tbody/tr[{}]/td[1]/div/label".format(
                H_MSG_rowItem + 1
            )
        )  # チェックボックス
        H_driver.execute_script("arguments[0].click();", H_FirstMSG_Cbx)  # チェックボックスクリック
        H_driver.execute_script("arguments[0].click();", H_MSG_Cbx)  # チェックボックスクリック
        WebDriverWait(H_driver, 30).until(
            EC.presence_of_all_elements_located
        )  # 要素が読み込まれるまで最大30秒待つ
        H_driver.execute_script("hyouziAction()")  # Javaで表示
        WebDriverWait(H_driver, 30).until(
            EC.presence_of_all_elements_located
        )  # 要素が読み込まれるまで最大30秒待つ
    except Exception:
        H_MSG_Cbx = H_driver.find_element_by_xpath(
            "/html/body/div[2]/form/div/div/div[2]/div[2]/div[1]/div[2]/table/tbody/tr[{}]/td[1]/div/label".format(
                H_MSG_rowItem + 1
            )
        )  # チェックボックス
        H_driver.execute_script("arguments[0].click();", H_MSG_Cbx)  # チェックボックスクリック
        WebDriverWait(H_driver, 30).until(
            EC.presence_of_all_elements_located
        )  # 要素が読み込まれるまで最大30秒待つ
        H_driver.execute_script("hyouziAction()")  # Javaで表示
        WebDriverWait(H_driver, 30).until(
            EC.presence_of_all_elements_located
        )  # 要素が読み込まれるまで最大30秒待つ
    finally:
        try:
            # 要素取得
            H_MSG_TableItem1 = H_driver.find_element_by_xpath(
                "/html/body/div[2]/form/div/div/div[2]/section/table/tbody/tr[1]/td"
            ).text.replace(
                "\u3000", " "
            )  # 発行元
            H_MSG_TableItem2 = H_driver.find_element_by_xpath(
                "/html/body/div[2]/form/div/div/div[2]/section/table/tbody/tr[2]/td[1]"
            ).text.replace(
                "\u3000", " "
            )  # 発行元2
            H_MSG_TableItem3 = H_driver.find_element_by_xpath(
                "/html/body/div[2]/form/div/div/div[2]/section/table/tbody/tr[3]/td[1]"
            ).text.replace(
                "\u3000", " "
            )  # 発行日時
            H_MSG_TableItem4 = H_driver.find_element_by_xpath(
                "/html/body/div[2]/form/div/div/div[2]/section/table/tbody/tr[4]/td"
            ).text.replace(
                "\u3000", " "
            )  # 件名
            return (
                H_MSG_TableItem1,
                H_MSG_TableItem2,
                H_MSG_TableItem3,
                H_MSG_TableItem4,
            )
        except:
            H_MSG_TableItem1 = H_driver.find_element_by_xpath(
                "/html/body/div[2]/form/div/div/div[2]/table/tbody/tr[1]/td"
            ).text.replace(
                "\u3000", " "
            )  # 発行元
            H_MSG_TableItem2 = H_driver.find_element_by_xpath(
                "/html/body/div[2]/form/div/div/div[2]/table/tbody/tr[2]/td[1]"
            ).text.replace(
                "\u3000", " "
            )  # 発行元2
            H_MSG_TableItem3 = H_driver.find_element_by_xpath(
                "/html/body/div[2]/form/div/div/div[2]/table/tbody/tr[3]/td[1]"
            ).text.replace(
                "\u3000", " "
            )  # 発行日時
            H_MSG_TableItem4 = H_driver.find_element_by_xpath(
                "/html/body/div[2]/form/div/div/div[2]/table/tbody/tr[4]/td"
            ).text.replace(
                "\u3000", " "
            )  # 件名
            if "/" not in H_MSG_TableItem3 and ":" not in H_MSG_TableItem3:
                H_MSG_TableItem1 = H_driver.find_element_by_xpath(
                    "/html/body/div[2]/form/div/div/div[2]/table/tbody/tr[1]/td"
                ).text.replace(
                    "\u3000", " "
                )  # 発行元
                H_MSG_TableItem2 = H_driver.find_element_by_xpath(
                    "/html/body/div[2]/form/div/div/div[2]/table/tbody/tr[3]/td[1]"
                ).text.replace(
                    "\u3000", " "
                )  # 発行元2
                H_MSG_TableItem3 = H_driver.find_element_by_xpath(
                    "/html/body/div[2]/form/div/div/div[2]/table/tbody/tr[2]/td[1]"
                ).text.replace(
                    "\u3000", " "
                )  # 発行日時
                H_MSG_TableItem4 = H_driver.find_element_by_xpath(
                    "/html/body/div[2]/form/div/div/div[2]/table/tbody/tr[6]/td"
                ).text.replace(
                    "\u3000", " "
                )  # 件名

                return (
                    H_MSG_TableItem1,
                    H_MSG_TableItem2,
                    H_MSG_TableItem3,
                    H_MSG_TableItem4,
                )
            else:
                return (
                    H_MSG_TableItem1,
                    H_MSG_TableItem2,
                    H_MSG_TableItem3,
                    H_MSG_TableItem4,
                )


# -----------------------------------------------------------------------------------------------------------------------------------------------------
def PrintIFS(H_Title, H_driver):
    H_driver.execute_script("window.print();")  # 開いたタブを印刷
    # time.sleep(4)
    WebDriverWait(H_driver, 30).until(
        EC.presence_of_all_elements_located
    )  # 要素が読み込まれるまで最大30秒待つ
    H_BackBtn = H_driver.find_element_by_xpath(
        "/html/body/div[2]/form/footer/div[1]/div/div[1]/a"
    )
    H_BackBtn.click()
    WebDriverWait(H_driver, 30).until(
        EC.presence_of_all_elements_located
    )  # 要素が読み込まれるまで最大30秒待つ
    logger.debug("印刷完了")
    return "印刷完了"


# -----------------------------------------------------------------------------------------------------------------------------------------------------
def LogReturn(LogAns, H_driver):
    if LogAns == "ログインしている利用者あてのメッセージを照会します。":  # ログイン成功の場合
        # WEB画面要素指定------------------------------------------------------------------------------------------------------
        try:
            try:
                H_MSG_OpenMyNo = H_driver.find_element_by_xpath(
                    "/html/body/div[1]/form/div/div/div/div/div[1]/div[3]/ul/li[1]/a"
                )  # "/html/body/div[2]/form/div/div/div/div/div[1]/div[1]/ul/li[7]/a"
            except:
                H_MSG_OpenMyNo = H_driver.find_element_by_xpath(
                    "/html/body/div[2]/form/div/div/div/div/div[1]/div[3]/ul/li[1]/a"
                )
            H_MSG_OpenMyNo.click()
            WebDriverWait(H_driver, 30).until(
                EC.presence_of_all_elements_located
            )  # 要素が読み込まれるまで最大30秒待つ
            # H_Today = dt.today() + relativedelta(months=-1)
            # H_dtToday = dt.today()
            H_Today = dt.today() + relativedelta(months=-0)
            H_dtToday = dt.today() + relativedelta(months=+1)
            Hj = str(H_dtToday.year)
            Hjj = str("{0:02}".format(H_dtToday.month))
            H_Str = Hj + "/" + Hjj + "/01 01:01:01"
            H_LT = dt.strptime(H_Str, "%Y/%m/%d %H:%M:%S")
            H_LastToday = H_LT + relativedelta(days=-1)
            H_FirstMonth = H_driver.find_element_by_xpath(
                "/html/body/div[2]/form/div/div/div[2]/div[1]/div/div[2]/input[1]"
            )
            H_EndMonth = H_driver.find_element_by_xpath(
                "/html/body/div[2]/form/div/div/div[2]/div[1]/div/div[2]/input[4]"
            )
            H_FMon = (
                "{0:04}".format(H_Today.year)
                + "{0:02}".format(H_Today.month)
                + "{0:02}".format(1)
            )
            H_EMon = (
                "{0:04}".format(H_LastToday.year)
                + "{0:02}".format(H_LastToday.month)
                + "{0:02}".format(H_LastToday.day)
            )
            H_FirstMonth.send_keys(H_FMon)
            H_EndMonth.send_keys(H_EMon)
            H_KensakuBtn = H_driver.find_element_by_xpath(
                "/html/body/div[2]/form/div/div/div[2]/div[1]/div/input"
            )
            H_KensakuBtn.click()
            WebDriverWait(H_driver, 30).until(
                EC.presence_of_all_elements_located
            )  # 要素が読み込まれるまで最大30秒待つ
            return H_driver.find_element_by_xpath(
                "/html/body/div[2]/form/div/div/div[2]/p[2]/span"
            ).text
        except:
            WebDriverWait(H_driver, 30).until(
                EC.presence_of_all_elements_located
            )  # 要素が読み込まれるまで最大30秒待つ
            return "データ有"
    elif LogAns == "認証エラー":  # ログイン失敗の場合
        WebDriverWait(H_driver, 30).until(
            EC.presence_of_all_elements_located
        )  # 要素が読み込まれるまで最大30秒待つ
        return "認証エラー"
    elif LogAns == "ログインできませんでした。":  # ログイン失敗の場合
        return "ログインできませんでした。"
    elif LogAns == "メッセージ照会":
        try:
            H_MSG_OpenMyNo = H_driver.find_element_by_xpath(
                "/html/body/div[1]/form/div/div/div/div/div[1]/div[3]/ul/li[1]/a"
            )  # "/html/body/div[2]/form/div/div/div/div/div[1]/div[1]/ul/li[7]/a"
        except:
            H_MSG_OpenMyNo = H_driver.find_element_by_xpath(
                "/html/body/div[2]/form/div/div/div/div/div[1]/div[3]/ul/li[1]/a"
            )
        H_MSG_OpenMyNo.click()
        WebDriverWait(H_driver, 30).until(
            EC.presence_of_all_elements_located
        )  # 要素が読み込まれるまで最大30秒待つ
        # H_Today = dt.today() + relativedelta(months=-1)
        # H_dtToday = dt.today()
        H_Today = dt.today() + relativedelta(months=-0)
        H_dtToday = dt.today() + relativedelta(months=+1)
        Hj = str(H_dtToday.year)
        Hjj = str("{0:02}".format(H_dtToday.month))
        H_Str = Hj + "/" + Hjj + "/01 01:01:01"
        H_LT = dt.strptime(H_Str, "%Y/%m/%d %H:%M:%S")
        H_LastToday = H_LT + relativedelta(days=-1)
        H_FirstMonth = H_driver.find_element_by_xpath(
            "/html/body/div[2]/form/div/div/div[2]/div[1]/div/div[2]/input[1]"
        )
        H_EndMonth = H_driver.find_element_by_xpath(
            "/html/body/div[2]/form/div/div/div[2]/div[1]/div/div[2]/input[4]"
        )
        H_FMon = (
            "{0:04}".format(H_Today.year)
            + "{0:02}".format(H_Today.month)
            + "{0:02}".format(1)
        )
        H_EMon = (
            "{0:04}".format(H_LastToday.year)
            + "{0:02}".format(H_LastToday.month)
            + "{0:02}".format(H_LastToday.day)
        )
        H_FirstMonth.send_keys(H_FMon)
        H_EndMonth.send_keys(H_EMon)
        H_KensakuBtn = H_driver.find_element_by_xpath(
            "/html/body/div[2]/form/div/div/div[2]/div[1]/div/input"
        )
        H_KensakuBtn.click()
        WebDriverWait(H_driver, 30).until(
            EC.presence_of_all_elements_located
        )  # 要素が読み込まれるまで最大30秒待つ
        try:
            H1SText = H_driver.find_element_by_xpath(
                "/html/body/div[2]/form/div/div/div[2]/p[2]/span"
            ).text
        except:
            H1SText = ""
        return H1SText
    else:  # その他の場合
        WebDriverWait(H_driver, 30).until(
            EC.presence_of_all_elements_located
        )  # 要素が読み込まれるまで最大30秒待つ


# -----------------------------------------------------------------------------------------------------------------------------------------------------
def RenamePDF(DownTime, MTitle, KanyoNo, KanyoName, Hakkoumoto, Hakkou, H_row):
    tdy = dt.strptime(DownTime, "%Y/%m/%d %H:%M:%S")  # 文字列を日付型に変換
    CfolName = str(tdy.year) + "-" + str(tdy.month)
    folders = glob.glob("//nas-sv/B_監査etc/B2_電子ﾌｧｲﾙ/ﾒｯｾｰｼﾞﾎﾞｯｸｽ/*-*")
    KanyoFolName = str(KanyoNo) + "_" + KanyoName
    for foldersItem in folders:
        if foldersItem == "//nas-sv/B_監査etc/B2_電子ﾌｧｲﾙ/ﾒｯｾｰｼﾞﾎﾞｯｸｽ\\" + CfolName:
            Subfolders = glob.glob(foldersItem + "/*")  # フォルダーがあった場合
            if MTitle == "プレ申告データに関するお知らせ":
                MotherFol = foldersItem + "\\eLTAX"
                for SubfoldersItem in Subfolders:
                    if SubfoldersItem.replace("\u3000", " ") == MotherFol:
                        SubFFlag = 1
                        print(MotherFol + "あります")
                        break
                    else:
                        SubFFlag = 0
                if SubFFlag == 0:
                    os.mkdir(foldersItem + "/eLTAX")
                    logger.debug(str(MotherFol) + "_作成")
                    print(MotherFol + "作りました。")
                    break
                Tfolders = glob.glob(foldersItem + "\\eLTAX" + "/*")  # フォルダーがあった場合
                ChildFol = foldersItem + "\\eLTAX" + "\\" + KanyoFolName
                TFFlag = 0
                for TfoldersItem in Tfolders:
                    if TfoldersItem == ChildFol:

                        TFFlag = 1

                        print(ChildFol + "あります")
                        break
                    else:
                        TFFlag = 0
                if TFFlag == 0:
                    os.mkdir(foldersItem + "/eLTAX" + "/" + KanyoFolName)

                    logger.debug(str(ChildFol) + "_作成")
                    print(ChildFol + "作りました。")
                    break
                break
            else:
                MotherFol = foldersItem + "\\eLTAX受信通知"
                for SubfoldersItem in Subfolders:
                    if SubfoldersItem.replace("\u3000", " ") == MotherFol:
                        SubFFlag = 1
                        print(MotherFol + "あります")
                        ChildFol = MotherFol
                        break
                    else:
                        SubFFlag = 0
                if SubFFlag == 0:
                    os.mkdir(foldersItem + "/eLTAX受信通知")
                    logger.debug(str(MotherFol) + "_作成")
                    print(MotherFol + "作りました。")
                    ChildFol = MotherFol
                    break
                else:
                    break
        else:
            print("ありません")  # フォルダーがなかった場合
    PDFfolder = glob.glob(os.getcwd().replace("\\", "/") + "/" + "*.pdf")  # フォルダーがあった場合
    for PDFfolderItem in PDFfolder:
        PDFSerch = "メッセージ照会_お知らせ" in PDFfolderItem
        if PDFSerch is False:
            PDFSerch = "メッセージ照会_受付通知（申告）" in PDFfolderItem
        if PDFSerch is False:
            PDFSerch = "メッセージ照会_受付通知（利用届出、申請・届出）" in PDFfolderItem
        if PDFSerch is False:
            PDFSerch = "メッセージ照会_申告書不受理通知" in PDFfolderItem
        if PDFSerch is False:
            PDFSerch = "メッセージ照会_納付情報発行依頼通知" in PDFfolderItem
        if MTitle == "プレ申告データに関するお知らせ":
            PDFName = (
                KanyoFolName
                + "_"
                + Hakkoumoto
                + "_"
                + Hakkou
                + "_"
                + MTitle
                + "["
                + H_row
                + "]"
                + ".pdf"
            )
        else:
            PDFName = (
                KanyoFolName + "_" + Hakkoumoto + "_" + Hakkou + "_" + MTitle + ".pdf"
            )
        PDFPath = os.getcwd().replace("\\", "/") + "/" + PDFName
        PDFPath = PDFPath.replace("/", "\\")

    try:
        if PDFSerch is True:
            os.rename(PDFfolderItem, PDFPath)
            MovePDFPath = ChildFol + "/" + PDFName
            MovePDFPath = MovePDFPath.replace("/", "\\")
            shutil.move(PDFPath, MovePDFPath)
            logger.debug(str(MovePDFPath) + "_PDF作成成功")
            OKstr = MovePDFPath + "成功"
            OKstr = OKstr.replace("\uff0d", "-").replace("\xa0", "")
            OKLog.append(OKstr)
        # 'D:\\PythonScript\\国税電子申告・納税システム－SU00S100 メール詳細 (1).pdf'
        else:
            logger.debug(str(MovePDFPath) + "_リネーム失敗-メッセージ照会_お知らせが含まれないファイル名-")
            NGstr = MovePDFPath + "_リネーム失敗-メッセージ照会_お知らせが含まれないファイル名-"
            NGstr = NGstr.replace("\uff0d", "-").replace("\xa0", "")
            NGLog.append(NGstr)
    except:
        traceback.print_exc()
        logger.debug(str(MovePDFPath) + "_リネーム失敗-トレースバックエラー-")
        NGstr = MovePDFPath + "_リネーム失敗-トレースバックエラー-"
        NGstr = NGstr.replace("\uff0d", "-").replace("\xa0", "")
        NGLog.append(NGstr)


# -----------------------------------------------------------------------------------------------------------------------------------------------------
def SortPDF(DownTime, MTitle, KanyoNo, KanyoName, Hakkoumoto, Hakkou, H_row):
    tdy = dt.strptime(DownTime, "%Y/%m/%d %H:%M:%S")  # 文字列を日付型に変換
    CfolName = str(tdy.year) + "-" + str(tdy.month)
    KanyoFolName = str(KanyoNo) + "_" + KanyoName
    if MTitle == "プレ申告データに関するお知らせ":
        PDFName = (
            KanyoFolName
            + "_"
            + Hakkoumoto
            + "_"
            + Hakkou
            + "_"
            + MTitle
            + "["
            + H_row
            + "]"
            + ".pdf"
        )
        dir_path = (
            "//nas-sv/B_監査etc/B2_電子ﾌｧｲﾙ/ﾒｯｾｰｼﾞﾎﾞｯｸｽ/"
            + CfolName
            + "/eLTAX//"
            + KanyoFolName
        )
    else:
        PDFName = KanyoFolName + "_" + Hakkoumoto + "_" + Hakkou + "_" + MTitle + ".pdf"
        dir_path = "//nas-sv/B_監査etc/B2_電子ﾌｧｲﾙ/ﾒｯｾｰｼﾞﾎﾞｯｸｽ/" + CfolName + "/eLTAX受信通知"
    for current_dir, sub_dirs, files_list in os.walk(dir_path):
        for file_name in files_list:
            foldersItem = os.path.join(current_dir, file_name).replace("\u3000", "")
            PDFSerch = PDFName in foldersItem
            try:
                if PDFSerch is True:
                    return True
                else:
                    print(foldersItem)
            except Exception:
                return False


# -----------------------------------------------------------------------------------------------------------------------------------------------------
def LoginLoop(H_SCode, H_TKCName, H_First, H_FirstP, H_SecondP):
    LogAns = eTaxWebCrawler(
        H_First, H_FirstP, os.getcwd().replace("\\", "/"), H_SCode, H_TKCName
    )  # Nanではない場合
    LogArray = LogAns[0].split("\n", 1)
    H_LogAns = LogArray[0]  # ログオン後のH1テキストを代入
    H_LogAnsOBJ = LogAns[1]  # ログオン後のWEBドライバーを代入
    H_LogMSGAns = LogReturn(H_LogAns, H_LogAnsOBJ)  # ログオン後のH1テキストをで処理分けしWEBテーブルページへ
    if (
        not H_LogMSGAns == "ログインできませんでした。"
        and not H_LogMSGAns == "認証エラー"
        and not H_LogMSGAns == "該当するデータはありませんでした。"
    ):
        logger.debug(str(H_SCode) + "_" + str(H_TKCName) + "ログイン成功")
        H_Lo = LogOnOuter(H_LogAnsOBJ)  # WEBテーブル取得
        H_L_D = H_Lo[0]  # WEBテーブルページ
        H_L_Row = H_Lo[1]  # WEBテーブル行数
        for H_MSG_rowItem in range(H_L_Row):  # WEBテーブル行数分ループ
            H_Parameters = ParGet(H_L_D, H_MSG_rowItem, H_L_Row)  # WEBテーブルから要素取得
            H_P1 = H_Parameters[0]
            H_P2 = H_Parameters[1]
            H_P3 = H_Parameters[2]
            H_P4 = H_Parameters[3]
            H_row = str(H_MSG_rowItem + 1)
            SPDF = SortPDF(H_P3, H_P4, H_SCode, H_TKCName, H_P1, H_P2, H_row)
            if SPDF is False or SPDF is None:
                logger.debug(
                    str(H_P3)
                    + "_"
                    + str(H_P4)
                    + "_"
                    + str(H_SCode)
                    + "_"
                    + str(H_TKCName)
                    + "_"
                    + str(H_P1)
                    + "_"
                    + str(H_P2)
                    + "_"
                    + str(H_row)
                    + "_"
                    + "未ダウンロード"
                )
                PrintIFS(H_P4, H_LogAnsOBJ)  # メッセージボックスの内容に応じて処理分け
                RenamePDF(
                    H_P3, H_P4, H_SCode, H_TKCName, H_P1, H_P2, H_row
                )  # PDF保存先フォルダー作成後リネーム&移動 DownTime,MTitle,KanyoNo,KanyoName
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
                logger.debug(
                    str(H_P3)
                    + "_"
                    + str(H_P4)
                    + "_"
                    + str(H_SCode)
                    + "_"
                    + str(H_TKCName)
                    + "_"
                    + str(H_P1)
                    + "_"
                    + str(H_P2)
                    + "_"
                    + str(H_row)
                    + "_"
                    + "ファイルが存在します。"
                )
                print("ファイルが存在します。")
                if H_MSG_rowItem == H_L_Row - 1:
                    H_LogAnsOBJ.quit()
                    time.sleep(1)
                else:
                    H_BackBtn = H_LogAnsOBJ.find_element_by_xpath(
                        "/html/body/div[2]/form/footer/div[1]/div/div[1]/a"
                    )
                    H_BackBtn.click()
                    time.sleep(1)
    elif H_LogMSGAns == "ログインできませんでした。":
        logger.debug(
            str(H_SCode)
            + "_"
            + str(H_TKCName)
            + "ログイン失敗1回目"
            + str(H_First)
            + "_"
            + str(H_FirstP)
        )
        NGstr = str(H_SCode) + "_" + H_TKCName + "_" + "ログインエラー1回目"
        NGstr = (
            NGstr.replace("\uff0d", "-")
            .replace("\xa0", "")
            .replace("\u71c1", "")
            .replace("\u9348", "")
            .replace("\u9ad9", "")
        )
        NGLog.append(NGstr)
        H_LogAnsOBJ.quit()
        time.sleep(1)
        LogAns = eTaxWebCrawler(
            H_First, H_SecondP, os.getcwd().replace("\\", "/"), H_SCode, H_TKCName
        )  # Nanではない場合
        LogArray = LogAns[0].split("\n", 1)
        H_LogAns = LogArray[0]  # ログオン後のH1テキストを代入
        H_LogAnsOBJ = LogAns[1]  # ログオン後のWEBドライバーを代入
        H_LogMSGAns = LogReturn(H_LogAns, H_LogAnsOBJ)  # ログオン後のH1テキストをで処理分けしWEBテーブルページへ
        if H_LogMSGAns == "ログインできませんでした。":
            logger.debug(
                str(H_SCode)
                + "_"
                + str(H_TKCName)
                + "ログイン失敗2回目"
                + str(H_First)
                + "_"
                + str(H_FirstP)
            )
            NGstr = str(H_SCode) + "_" + H_TKCName + "_" + "ログインエラー2回目"
            NGstr = (
                NGstr.replace("\uff0d", "-")
                .replace("\xa0", "")
                .replace("\u71c1", "")
                .replace("\u9348", "")
                .replace("\u9ad9", "")
            )
            NGLog.append(NGstr)
            H_LogAnsOBJ.quit()
            time.sleep(1)
        elif H_LogMSGAns == "認証エラー":
            logger.debug(
                str(H_SCode)
                + "_"
                + str(H_TKCName)
                + "認証エラー"
                + str(H_First)
                + "_"
                + str(H_FirstP)
            )
            H_LogAnsOBJ.quit()
            time.sleep(1)
        elif H_LogMSGAns == "データ有":
            logger.debug(
                str(H_SCode)
                + "_"
                + str(H_TKCName)
                + "ログイン2回目成功データ有"
                + str(H_First)
                + "_"
                + str(H_FirstP)
            )
            H_Lo = LogOnOuter(H_LogAnsOBJ)  # WEBテーブル取得
            H_L_D = H_Lo[0]  # WEBテーブルページ
            H_L_Row = H_Lo[1]  # WEBテーブル行数
            for H_MSG_rowItem in range(H_L_Row):  # WEBテーブル行数分ループ
                H_Parameters = ParGet(H_L_D, H_MSG_rowItem, H_L_Row)  # WEBテーブルから要素取得
                H_P1 = H_Parameters[0]
                H_P2 = H_Parameters[1]
                H_P3 = H_Parameters[2]
                H_P4 = H_Parameters[3]
                H_row = str(H_MSG_rowItem + 1)
                SPDF = SortPDF(H_P3, H_P4, H_SCode, H_TKCName, H_P1, H_P2, H_row)
                if SPDF is False or SPDF is None:
                    logger.debug(
                        str(H_P3)
                        + "_"
                        + str(H_P4)
                        + "_"
                        + str(H_SCode)
                        + "_"
                        + str(H_TKCName)
                        + "_"
                        + str(H_P1)
                        + "_"
                        + str(H_P2)
                        + "_"
                        + str(H_row)
                        + "_"
                        + "未ダウンロード"
                    )
                    PrintIFS(H_P4, H_LogAnsOBJ)  # メッセージボックスの内容に応じて処理分け
                    RenamePDF(
                        H_P3, H_P4, H_SCode, H_TKCName, H_P1, H_P2, H_row
                    )  # PDF保存先フォルダー作成後リネーム&移動 DownTime,MTitle,KanyoNo,KanyoName
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
                    logger.debug(
                        str(H_P3)
                        + "_"
                        + str(H_P4)
                        + "_"
                        + str(H_SCode)
                        + "_"
                        + str(H_TKCName)
                        + "_"
                        + str(H_P1)
                        + "_"
                        + str(H_P2)
                        + "_"
                        + str(H_row)
                        + "_"
                        + "ファイルが存在します。"
                    )
                    print("ファイルが存在します。")
                    if H_MSG_rowItem == H_L_Row - 1:
                        H_LogAnsOBJ.quit()
                        time.sleep(1)
                    else:
                        H_BackBtn = H_LogAnsOBJ.find_element_by_xpath(
                            "/html/body/div[2]/form/footer/div[1]/div/div[1]/a"
                        )
                        H_BackBtn.click()
                        time.sleep(1)
        elif H_LogMSGAns == "該当するデータはありませんでした。":
            logger.debug(str(H_SCode) + "_" + str(H_TKCName) + "該当するデータはありませんでした。")
            NGstr = str(H_SCode) + "_" + H_TKCName + "_" + "データ無"
            NGstr = (
                NGstr.replace("\uff0d", "-")
                .replace("\xa0", "")
                .replace("\u71c1", "")
                .replace("\u9348", "")
                .replace("\u9ad9", "")
            )
            NGLog.append(NGstr)
            H_LogAnsOBJ.quit()
            time.sleep(1)
        else:
            H_LogAnsOBJ.quit()
            time.sleep(1)
    elif H_LogMSGAns == "認証エラー":
        logger.debug(str(H_SCode) + "_" + str(H_TKCName) + "暗証番号の変更")
        print(H_SCode + "_" + H_TKCName + "_" + "暗証番号の変更")
    elif H_LogMSGAns == "該当するデータはありませんでした。":
        logger.debug(str(H_SCode) + "_" + str(H_TKCName) + "該当するデータはありませんでした。")
        NGstr = str(H_SCode) + "_" + H_TKCName + "_" + "データ無"
        NGstr = (
            NGstr.replace("\uff0d", "-")
            .replace("\xa0", "")
            .replace("\u71c1", "")
            .replace("\u9348", "")
            .replace("\u9ad9", "")
        )
        NGLog.append(NGstr)
        H_LogAnsOBJ.quit()
        time.sleep(1)
    else:
        H_LogAnsOBJ.quit()
        time.sleep(1)


# -----------------------------------------------------------------------------------------------------------------------------------------------------
# pandas(pd)で関与先データCSVを取得
H_url = "//nas-sv/A_共通/A8_ｼｽﾃﾑ資料/RPA/ALLDataBase/Heidi関与先DB.csv"
H_df = pd.read_csv(H_url, encoding="utf-8")
H_forCount = 0

H_dfRow = np.array(H_df).shape[0]  # 配列行数取得
H_dfCol = np.array(H_df).shape[1]  # 配列列数取得
OKLog = []
NGLog = []
for x in range(H_dfRow):
    try:
        if x >= 571:
            # 関与先DB配列をループして識別番号とPassを取得
            H_dfDataRow = H_df.loc[x]
            H_SCode = H_dfDataRow["SyanaiCode"]
            try:
                H_TKCName = H_dfDataRow["TKCName"].replace("\u3000", " ")  # 空白\u3000を置換
            except:
                H_TKCName = H_dfDataRow["TKCName"]
            H_MSikibetu = H_dfDataRow["MirokuTihouzeiUserID"]
            H_TSikibetu = H_dfDataRow["TKCTihouzeiUserID"]
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
                        "//nas-sv/B_監査etc/B2_電子ﾌｧｲﾙ/ﾒｯｾｰｼﾞﾎﾞｯｸｽ/PyOKLog.csv",
                        encoding="shift-jis",
                    )
                    pd.DataFrame(NGLog).to_csv(
                        "//nas-sv/B_監査etc/B2_電子ﾌｧｲﾙ/ﾒｯｾｰｼﾞﾎﾞｯｸｽ/PyNGLog.csv",
                        encoding="shift-jis",
                    )
                else:
                    if H_elPass == H_elPass:  # 自身比較のNan判定
                        LoginLoop(H_SCode, H_TKCName, H_MSikibetu, H_ePass, H_elPass)
                        pd.DataFrame(OKLog).to_csv(
                            "//nas-sv/B_監査etc/B2_電子ﾌｧｲﾙ/ﾒｯｾｰｼﾞﾎﾞｯｸｽ/PyOKLog.csv",
                            encoding="shift-jis",
                        )
                        pd.DataFrame(NGLog).to_csv(
                            "//nas-sv/B_監査etc/B2_電子ﾌｧｲﾙ/ﾒｯｾｰｼﾞﾎﾞｯｸｽ/PyNGLog.csv",
                            encoding="shift-jis",
                        )
            elif H_TSikibetu == H_TSikibetu:
                if H_ePass == H_ePass:  # 自身比較のNan判定
                    LoginLoop(H_SCode, H_TKCName, H_TSikibetu, H_ePass, H_elPass)
                    pd.DataFrame(OKLog).to_csv(
                        "//nas-sv/B_監査etc/B2_電子ﾌｧｲﾙ/ﾒｯｾｰｼﾞﾎﾞｯｸｽ/PyOKLog.csv",
                        encoding="shift-jis",
                    )
                    pd.DataFrame(NGLog).to_csv(
                        "//nas-sv/B_監査etc/B2_電子ﾌｧｲﾙ/ﾒｯｾｰｼﾞﾎﾞｯｸｽ/PyNGLog.csv",
                        encoding="shift-jis",
                    )
                else:
                    if H_elPass == H_elPass:  # 自身比較のNan判定
                        LoginLoop(H_SCode, H_TKCName, H_TSikibetu, H_ePass, H_elPass)
                        pd.DataFrame(OKLog).to_csv(
                            "//nas-sv/B_監査etc/B2_電子ﾌｧｲﾙ/ﾒｯｾｰｼﾞﾎﾞｯｸｽ/PyOKLog.csv",
                            encoding="shift-jis",
                        )
                        pd.DataFrame(NGLog).to_csv(
                            "//nas-sv/B_監査etc/B2_電子ﾌｧｲﾙ/ﾒｯｾｰｼﾞﾎﾞｯｸｽ/PyNGLog.csv",
                            encoding="shift-jis",
                        )
                    else:
                        print("NoPassWord")
                        NGstr = str(H_SCode) + "_" + H_TKCName + "_" + "パスワードエラー"
                        NGstr = NGstr.replace("\uff0d", "-").replace("\xa0", "")
                        NGLog.append(NGstr)
                        pd.DataFrame(NGLog).to_csv(
                            "//nas-sv/B_監査etc/B2_電子ﾌｧｲﾙ/ﾒｯｾｰｼﾞﾎﾞｯｸｽ/PyNGLog.csv",
                            encoding="shift-jis",
                        )
            else:
                NGstr = str(H_SCode) + "_" + H_TKCName + "_" + "エラー"
                NGstr = NGstr.replace("\uff0d", "-").replace("\xa0", "")
                NGLog.append(NGstr)
                pd.DataFrame(NGLog).to_csv(
                    "//nas-sv/B_監査etc/B2_電子ﾌｧｲﾙ/ﾒｯｾｰｼﾞﾎﾞｯｸｽ/PyNGLog.csv",
                    encoding="shift-jis",
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
                "//nas-sv/B_監査etc/B2_電子ﾌｧｲﾙ/ﾒｯｾｰｼﾞﾎﾞｯｸｽ/PyNGLog.csv",
                encoding="shift-jis",
            )
        except:
            print("どうしようもないがな！")
