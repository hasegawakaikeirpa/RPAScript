# ----------------------------------------------------------------------------------------------------------------------
def DriverUIWaitXPATH(UIPATH, driver):  # XPATH要素を取得するまで待機
    for x in range(10):
        try:
            driver.find_element_by_xpath(UIPATH)
            Flag = 1
            return True
        except:
            Flag = 0
    if Flag == 0:
        return False


# ----------------------------------------------------------------------------------------------------------------------
def DriverUIWaitAutomationId(UIPATH, driver):  # XPATH要素を取得するまで待機
    for x in range(10):
        try:
            driver.find_element_by_accessibility_id(UIPATH)
            Flag = 1
            return True
        except:
            Flag = 0
    if Flag == 0:
        return False


# ----------------------------------------------------------------------------------------------------------------------
def DriverUIWaitName(UIPATH, driver):  # XPATH要素を取得するまで待機
    for x in range(10):
        try:
            driver.find_element_by_Name(UIPATH)
            Flag = 1
            return True
        except:
            Flag = 0
    if Flag == 0:
        return False


# ------------------------------------------------------------r----------------------------------------------------------
def DriverUIWaitclassname(UIPATH, driver):  # XPATH要素を取得するまで待機
    for x in range(10):
        try:
            driver.find_element_by_class_name(UIPATH)
            Flag = 1
            return True
        except:
            Flag = 0
    if Flag == 0:
        return False


# ----------------------------------------------------------------------------------------------------------------------
def DriverFindClass(UIPATH, driver):  # XPATH要素を取得するまで待機
    for x in range(10):
        try:
            elList = driver.find_elements_by_class_name(UIPATH)
            Flag = 1
            return True, elList
        except:
            Flag = 0
    if Flag == 0:
        return False


# ----------------------------------------------------------------------------------------------------------------------
def DriverCheck(Hub, ObjName, driver):  # XPATH要素を取得するまで待機
    for x in range(10):
        if Hub == "AutomationID":
            if (
                DriverUIWaitAutomationId(ObjName, driver) is True
            ):  # OMSメニューの年調起動ボタンを判定して初期処理分け
                # 正常待機後処理
                driver.find_element_by_accessibility_id(ObjName)  # 一括電子申告送信ボタン
                return True
            else:
                # 異常待機後処理
                print("要素取得に失敗しました。")
        elif Hub == "XPATH":
            if DriverUIWaitXPATH(ObjName, driver) is True:  # OMSメニューの年調起動ボタンを判定して初期処理分け
                # 正常待機後処理
                driver.find_element_by_xpath(ObjName)  # 一括電子申告送信ボタン
                return True
            else:
                # 異常待機後処理
                print("要素取得に失敗しました。")
        elif Hub == "Name":
            if DriverUIWaitName(ObjName, driver) is True:  # OMSメニューの年調起動ボタンを判定して初期処理分け
                # 正常待機後処理
                driver.find_element_by_Name(ObjName)  # 一括電子申告送信ボタン
                return True
            else:
                # 異常待機後処理
                print("要素取得に失敗しました。")


# ----------------------------------------------------------------------------------------------------------------------
def DriverClick(Hub, ObjName, driver):
    if Hub == "AutomationID":
        if (
            DriverUIWaitAutomationId(ObjName, driver) is True
        ):  # OMSメニューの年調起動ボタンを判定して初期処理分け
            # 正常待機後処理
            OMSObj = driver.find_element_by_accessibility_id(ObjName)  # 一括電子申告送信ボタン
            OMSObj.click()
            return OMSObj
        else:
            # 異常待機後処理
            print("要素取得に失敗しました。")
    elif Hub == "XPATH":
        if DriverUIWaitXPATH(ObjName, driver) is True:  # OMSメニューの年調起動ボタンを判定して初期処理分け
            # 正常待機後処理
            OMSObj = driver.find_element_by_xpath(ObjName)  # 一括電子申告送信ボタン
            OMSObj.click()
            return OMSObj
        else:
            # 異常待機後処理
            print("要素取得に失敗しました。")
    elif Hub == "Name":
        if DriverUIWaitName(ObjName, driver) is True:  # OMSメニューの年調起動ボタンを判定して初期処理分け
            # 正常待機後処理
            OMSObj = driver.find_element_by_Name(ObjName)  # 一括電子申告送信ボタン
            OMSObj.click()
            return OMSObj
        else:
            # 異常待機後処理
            print("要素取得に失敗しました。")
    elif Hub == "class_name":
        if DriverUIWaitclassname(ObjName, driver) is True:  # OMSメニューの年調起動ボタンを判定して初期処理分け
            # 正常待機後処理
            OMSObj = driver.find_element_by_class_name(ObjName)  # 一括電子申告送信ボタン
            OMSObj.click()
            return OMSObj
        else:
            # 異常待機後処理
            print("要素取得に失敗しました。")


# ----------------------------------------------------------------------------------------------------------------------
