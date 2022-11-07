from ctypes import windll
import pyautogui as pg
import time
import RPA_Function as RPA
import pyperclip  # クリップボードへのコピーで使用

# ------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    URL = r"D:\PythonScript\RPAScript\RPAFLOWS\MJS_SystemPrintOut\img\MJS_SystemPrintOut\DensisinkokuUpDate"
    time.sleep(1)
    # 利用同意書アイコンを探す-------------------------------------------------
    DDR = RPA.ImgCheckForList(URL, [r"\14Doui.png", r"\14Doui2.png"], 0.9, 10)
    # -----------------------------------------------------------------------
    if DDR[0] is True:  # 利用同意書アイコンがあれば
        RPA.ImgClick(URL, DDR[1], 0.9, 10)  # 利用同意書アイコンをクリック
    # 利用同意書メニューが表示されるまで待機------------------------------------
    while pg.locateOnScreen(URL + r"\14D_Print.png", confidence=0.9) is None:
        time.sleep(1)
        # ------------------------------------------------------------------
        RPA.ImgClick(URL, r"\14D_Search.png", 0.9, 10)  # 利用同意書アイコンをクリック
    # 検索メニューが表示されるまで待機------------------------------------
    while pg.locateOnScreen(URL + r"\14D_SearchFlag.png", confidence=0.9) is None:
        time.sleep(1)
    # ------------------------------------------------------------------
    # キャンセルボタンが選択されるまで待機------------------------------------
    while pg.locateOnScreen(URL + r"\CanselBtn.png", confidence=0.99999) is None:
        time.sleep(1)
        pg.keyDown("shift")
        pg.press("tab")
        pg.keyUp("shift")
    # ------------------------------------------------------------------
    # 関与先コードで指定--------------------------------------------------
    pyperclip.copy(str(592))
    pg.press("tab")
    time.sleep(1)
    pg.hotkey("ctrl", "v")
    D_FindList = [r"\D_FindStart.png", r"\D_FindStart2.png"]
    while RPA.ImgCheckForList(URL, D_FindList, 0.9, 1)[0] is True:
        time.sleep(1)
        pg.press("return")
    time.sleep(1)
    pg.hotkey("ctrl", "v")
    D_FindList = [r"\D_FindEnd.png", r"\D_FindEnd2.png"]
    while RPA.ImgCheckForList(URL, D_FindList, 0.9, 1)[0] is True:
        time.sleep(1)
        pg.press("return")
    RPA.ImgClick(URL, r"\14D_SearchOK.png", 0.9, 10)  # OKボタンをクリック
