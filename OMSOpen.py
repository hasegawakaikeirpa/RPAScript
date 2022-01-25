def ExeOpen(AppURL):#URL指定でアプリ起動関数
    subprocess.Popen(AppURL)
#----------------------------------------------------------------------------------------------------------------------
def DriverUIWaitXPATH(UIPATH,driver):#XPATH要素を取得するまで待機
    Flag = 0
    for x in range(1000000):
        try:
            driver.find_element_by_xpath(UIPATH)
            Flag = 1
            return True
        except:
            Flag = 0
    #if Flag == 0:
    #    return False
#----------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------------------
def DriverUIWaitAutomationId(UIPATH,driver):#XPATH要素を取得するまで待機
    Flag = 0
    for x in range(1000000):
        try:
            driver.find_element_by_accessibility_id(UIPATH)
            Flag = 1
            return True
        except:
            Flag = 0
    #if Flag == 0:
    #    return False
#----------------------------------------------------------------------------------------------------------------------
def MainFlow(BatUrl,FolURL2,ImgFolName):
    #WebDriver起動バッチを管理者権限で起動---------------------------------------------------------------------------------
    WDO = ExeOpen(BatUrl)
    desired_caps = {}
    desired_caps["app"] = "Root"#Rootを指定してDriverTargetをデスクトップに
    driver = webdriver.Remote('http://127.0.0.1:4724',desired_caps,direct_connection=True)#ポート指定してDriverインスタンス化

    #----------------------------------------------------------------------------------------------------------------------
    #OMSを起動-------------------------------------------------------------------------------------------------------------
    OMSURL = "C:\Program Files (x86)\TKC\OMS\OMS.exe"
    ExeOpen(OMSURL)
    #time.sleep(10)
    FolURL2 = os.getcwd().replace('\\','/')#先
    FileName = "OpenWin.png"
    while pg.locateOnScreen(FolURL2 + "/RPAPhoto/OMSOpen/" + FileName, confidence=0.9) is None:
        time.sleep(1)
    #tAutomationId要素が出現するまで待機-------------------------------------------------------------------------------------------
    if DriverUIWaitAutomationId("passwordTextBox",driver) == True:
        #正常待機後処理
        OMSPassWindowClc = driver.find_element_by_accessibility_id("passwordTextBox")
        OMSPassWindowClc.click()
        pg.write("051210561111111", interval=0.01)#直接SENDできないのでpyautoguiで入力
        # OMSPassOKBtn = driver.find_element_by_accessibility_id("okButton")
        # OMSPassOKBtn.click()
        pg.press(['return','return'])
    else:
        #異常待機後処理
        print("要素取得に失敗しました。")
    #----------------------------------------------------------------------------------------------------------------------
    #tAutomationId要素が出現するまで待機-------------------------------------------------------------------------------------------
    if DriverUIWaitAutomationId("codeTextBox",driver) == True:
        print("起動しました。")
        return driver
    else:
        #異常待機後処理
        print("要素取得に失敗しました。")
    #----------------------------------------------------------------------------------------------------------------------
#モジュールインポート
from appium import webdriver
import subprocess
from subprocess import run
from subprocess import PIPE
import pyautogui as pg
import time
import os
from selenium.webdriver.common.keys import Keys
