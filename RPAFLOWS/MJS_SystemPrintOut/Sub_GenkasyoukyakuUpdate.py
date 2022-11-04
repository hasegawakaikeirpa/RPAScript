from ctypes import windll
import pyautogui as pg
import time
import RPA_Function as RPA
import pyperclip  # クリップボードへのコピーで使用

# ------------------------------------------------------------------------------------------------------------------
def GenkasyoukyakuUpdate(Job, Exc):
    """
    概要: 減価償却更新処理
    @param FolURL : ミロク起動関数のフォルダ(str)
    @param Job.PrintOut_url : このpyファイルのフォルダ(str)
    @param Exc.row_data : Excel抽出行(obj)
    @param driver : 画面操作ドライバー(obj)
    @return : bool,ミロク入力関与先コード, ミロク入力処理年, ミロク入力処理月
    """
    try:
        # 減価償却のアイコンを探す-------------------------------------------------
        ImgList = [r"\G_Syoukyaku.png", r"\G_Syoukyaku2.png"]
        ICFL = RPA.ImgCheckForList(Job.PrintOut_url, ImgList, 0.9, 10)
        # -----------------------------------------------------------------------
        if ICFL[0] is True:  # 減価償却のアイコンがあれば
            RPA.ImgClick(Job.PrintOut_url, ICFL[1], 0.9, 10)  # 減価償却のアイコンをクリック
            # 減価償却フラグが表示されるまで待機------------------------------------
            while (
                pg.locateOnScreen(
                    Job.PrintOut_url + r"\G_SyoukyakuFlag.png", confidence=0.9
                )
                is None
            ):
                time.sleep(1)
            # ------------------------------------------------------------------
            time.sleep(1)
            # 年度を最新に指定----------------------------------------------------
            IC = RPA.ImgCheck(Job.PrintOut_url, r"\Nendo_Saisin.png", 0.9, 10)
            if IC[0] is False:
                IC2 = RPA.ImgCheck(Job.PrintOut_url, r"\Nendo_All.png", 0.9, 10)
                if IC2[0] is False:
                    print("年度選択がない")
                else:
                    RPA.ImgClick(Job.PrintOut_url, r"\Nendo_All.png", 0.9, 10)
                    pg.press("home")
                    time.sleep(1)
                    pg.press("down")
                    time.sleep(1)
                    pg.press("return")
                    time.sleep(1)
            # ------------------------------------------------------------------
            # 関与先コード入力ボックスをクリック------------------------------------
            RPA.ImgClick(Job.PrintOut_url, r"\K_NoBox.png", 0.9, 10)
            while (
                pg.locateOnScreen(
                    Job.PrintOut_url + r"\K_AfterNoBox.png", confidence=0.9
                )
                is None
            ):
                time.sleep(1)
            pg.write(str(Exc.row_kanyo_no))
            pg.press(["return", "return", "return"])
            # 入力した関与先コードを取得------------
            pg.keyDown("shift")
            pg.press(["tab", "tab", "tab"])
            pg.keyUp("shift")
            if windll.user32.OpenClipboard(None):
                windll.user32.EmptyClipboard()
                windll.user32.CloseClipboard()
            pg.hotkey("ctrl", "c")
            ThisNo = pyperclip.paste()
            # -----------------------------------
            pg.press("return")
            # 表示された年度を取得-----------------
            if windll.user32.OpenClipboard(None):
                windll.user32.EmptyClipboard()
                windll.user32.CloseClipboard()
            pg.hotkey("ctrl", "c")
            ThisYear = pyperclip.paste()
            # -----------------------------------
            pg.press("return")
            # 表示された月を取得-------------------
            if windll.user32.OpenClipboard(None):
                windll.user32.EmptyClipboard()
                windll.user32.CloseClipboard()
            pg.hotkey("ctrl", "c")
            ThisMonth = pyperclip.paste()
            # -----------------------------------
            time.sleep(1)
            if str(Exc.row_kanyo_no) == ThisNo:
                print("関与先あり")
                pg.press(["return", "return", "return"])
                # 減価償却メニューが表示されるまで待機------------------------------------
                while (
                    pg.locateOnScreen(
                        Job.PrintOut_url + r"\G_SyoukyakuMenu.png", confidence=0.9
                    )
                    is None
                ):
                    time.sleep(1)
                    # アップデート情報画面が出たら閉じる-------------------------------
                    GSUM = RPA.ImgCheck(
                        Job.PrintOut_url, r"\G_SyoukyakuUpMsg.png", 0.9, 10
                    )
                    if GSUM[0] is True:
                        RPA.ImgClick(
                            Job.PrintOut_url, r"\G_SyoukyakuUpMsgCansel.png", 0.9, 10
                        )
                    # 顧問先情報更新ダイアログ確認-----------------------------------------
                    KK = RPA.ImgCheck(Job.PrintOut_url, r"\KomonKoushin.png", 0.9, 10)
                    if KK[0] is True:
                        pg.press("y")
                        while (
                            pg.locateOnScreen(
                                Job.PrintOut_url + r"\KomonKoushinBar.png",
                                confidence=0.9,
                            )
                            is None
                        ):
                            time.sleep(1)
                        RPA.ImgClick(
                            Job.PrintOut_url, r"\KomonKoushinInput.png", 0.9, 10
                        )
                    # 参照表示確認ダイアログ確認------------------------------------------
                    KK = RPA.ImgCheck(Job.PrintOut_url, r"\KSansyouQ.png", 0.9, 10)
                    if KK[0] is True:
                        pg.press("return")
                    DL = RPA.ImgCheck(Job.PrintOut_url, r"\DLCheck.png", 0.9, 10)
                    if DL[0] is True:
                        pg.press("return")
                        while (
                            pg.locateOnScreen(
                                Job.PrintOut_url + r"\K_TaisyouMenu.png", confidence=0.9
                            )
                            is None
                        ):
                            time.sleep(1)
                # --------------------------------------------------------------------
                RPA.ImgClick(
                    URL, r"\GenkaSyoukyaku\G_Insatu.png", 0.9, 10
                )  # 2.印刷処理アイコンをクリック
                # 印刷処理メニューが表示されるまで待機------------------------------------
                while (
                    pg.locateOnScreen(
                        URL + r"\GenkaSyoukyaku\G_InsatuFlag.png", confidence=0.9
                    )
                    is None
                ):
                    time.sleep(1)
                # --------------------------------------------------------------------
                if PN == "固定資産台帳":
                    GIF = RPA.ImgCheckForList(
                        URL,
                        [
                            r"\GenkaSyoukyaku\01G_Uchiwake.png",
                            r"\GenkaSyoukyaku\01G_Uchiwake2.png",
                        ],
                        0.9,
                        10,
                    )
                    if GIF[0] is True:
                        RPA.ImgClick(URL, GIF[1], 0.9, 10)
                    # 出力条件ウィンドウが表示されるまで待機---------------------------------
                    while (
                        pg.locateOnScreen(
                            URL + r"\GenkaSyoukyaku\01G_PrintWait.png",
                            confidence=0.9,
                        )
                        is None
                    ):
                        time.sleep(1)
                    # --------------------------------------------------------------------
                    time.sleep(1)
                    RPA.ImgClick(
                        URL, r"\GenkaSyoukyaku\01G_PrintOK.png", 0.9, 10
                    )  # 出力条件設定OKをクリック
                    # --------------------------------------------------------------------
                    NOB = False, ""
                    NOB = RPA.ImgCheck(URL, r"\GenkaSyoukyaku\G_NOB.png", 0.9, 10)
                    if NOB[0] is True:
                        pg.press("return")
                        # 出力条件ウィンドウが表示されるまで待機---------------------------------
                        while (
                            pg.locateOnScreen(
                                URL + r"\GenkaSyoukyaku\01G_PrintWait.png",
                                confidence=0.9,
                            )
                            is None
                        ):
                            time.sleep(1)
                        RPA.ImgClick(URL, r"\GenkaSyoukyaku\G_NOBCan.png", 0.9, 10)
                        # --------------------------------------------------------------------
                    # 出力条件ウィンドウが表示されるなくなるまで待機--------------------------
                    while (
                        pg.locateOnScreen(
                            URL + r"\GenkaSyoukyaku\01G_PrintWait.png",
                            confidence=0.9,
                        )
                        is not None
                    ):
                        time.sleep(1)
                    if NOB[0] is False:
                        time.sleep(3)
                        # --------------------------------------------------------------------
                        RPA.ImgClick(
                            URL, r"\GenkaSyoukyaku\01G_PrintBtn.png", 0.9, 10
                        )  # 印刷ボタンをクリック
                        # 印刷設定が表示されるまで待機---------------------------------
                        while (
                            pg.locateOnScreen(
                                URL + r"\Houjinzei\PrintBar.png", confidence=0.9
                            )
                            is None
                        ):
                            time.sleep(1)
                        # --------------------------------------------------------------------
                        # 申告税一覧表印刷処理----------------------------------------------------
                        FO = RPA.ImgCheckForList(
                            URL,
                            [
                                r"\Houjinzei\FileOut.png",
                                r"\Houjinzei\FileOut2.png",
                            ],
                            0.9,
                            10,
                        )
                        if FO[0] is True:
                            RPA.ImgClick(URL, FO[1], 0.9, 10)
                        RPA.ImgClick(URL, r"\Houjinzei\PDFBar.png", 0.9, 10)
                        pg.press("return")
                        pg.press("delete")
                        pg.press("backspace")
                        time.sleep(1)
                        pyperclip.copy(
                            Exc.Fname.replace("\\\\", "\\").replace("/", "\\")
                        )
                        time.sleep(1)
                        pg.hotkey("ctrl", "v")
                        pg.press("return")
                        time.sleep(1)
                        RPA.ImgClick(URL, r"\Houjinzei\PrintOut.png", 0.9, 10)
                        time.sleep(2)
                        #  印刷設定が表示されなくなるまで待機---------------------------------
                        while (
                            pg.locateOnScreen(
                                URL + r"\Houjinzei\PrintBar.png", confidence=0.9
                            )
                            is not None
                        ):
                            time.sleep(1)
                            FO = RPA.ImgCheck(URL, r"\Houjinzei\FileOver.png", 0.9, 10)
                            if FO[0] is True:
                                pg.press("y")
                        # --------------------------------------------------------------------
                        time.sleep(1)
                        # 確実に閉じる---------------------------------------------------
                        ZME = RPA.ImgCheck(URL, r"\GenkaSyoukyaku\01G_End.png", 0.9, 10)
                        if ZME[0] is True:
                            RPA.ImgClick(URL, r"\GenkaSyoukyaku\01G_End.png", 0.9, 10)
                        else:
                            pg.keyDown("alt")
                            pg.press("x")
                            pg.keyUp("alt")
                        # ---------------------------------------------------------------
                        time.sleep(1)
                        while (
                            RPA.ImgCheckForList(
                                URL,
                                [
                                    r"\GenkaSyoukyaku\01G_Uchiwake.png",
                                    r"\GenkaSyoukyaku\01G_Uchiwake2.png",
                                ],
                                0.9,
                                10,
                            )[0]
                            is False
                        ):
                            time.sleep(1)
                        # 閉じる処理--------------------------
                        pg.keyDown("alt")
                        pg.press("f4")
                        pg.keyUp("alt")
                        # -----------------------------------
                        f = 0
                        # 減価償却フラグが表示されるまで待機------------------------------------
                        while (
                            pg.locateOnScreen(
                                Job.PrintOut_url + r"\G_SyoukyakuFlag.png",
                                confidence=0.9,
                            )
                            is None
                        ):
                            time.sleep(1)
                            f += 1
                            if f == 5:
                                pg.keyDown("alt")
                                pg.press("f4")
                                pg.keyUp("alt")
                                f = 0
                        # ------------------------------------------------------------------
                        return True, ThisNo, ThisYear, ThisMonth
                    else:
                        # 閉じる処理--------------------------
                        pg.keyDown("alt")
                        pg.press("f4")
                        pg.keyUp("alt")
                        # -----------------------------------
                        f = 0
                        # 減価償却フラグが表示されるまで待機------------------------------------
                        while (
                            pg.locateOnScreen(
                                Job.PrintOut_url + r"\G_SyoukyakuFlag.png",
                                confidence=0.9,
                            )
                            is None
                        ):
                            time.sleep(1)
                            f += 1
                            if f == 5:
                                pg.keyDown("alt")
                                pg.press("f4")
                                pg.keyUp("alt")
                                f = 0
                        # ------------------------------------------------------------------
                        return False, "物件無し", "", ""
                elif PN == "一括償却資産":
                    Nod = ""
                    GIF = RPA.ImgCheckForList(
                        URL,
                        [
                            r"\GenkaSyoukyaku\03G_Meisai.png",
                            r"\GenkaSyoukyaku\03G_Meisai2.png",
                        ],
                        0.9,
                        10,
                    )
                    if GIF[0] is True:
                        RPA.ImgClick(URL, GIF[1], 0.9, 10)
                    # 出力条件ウィンドウが表示されるまで待機---------------------------------
                    while (
                        pg.locateOnScreen(
                            URL + r"\GenkaSyoukyaku\03G_PrintWait.png",
                            confidence=0.9,
                        )
                        is None
                    ):
                        time.sleep(1)
                        GN = RPA.ImgCheck(
                            URL, r"\GenkaSyoukyaku\03G_Nodata.png", 0.9, 10
                        )
                        if GN[0] is True:
                            pg.press("return")
                            Nod = "Nodata"
                        if Nod == "Nodata":
                            break
                    # --------------------------------------------------------------------
                    time.sleep(1)
                    if Nod == "":
                        RPA.ImgClick(
                            URL, r"\GenkaSyoukyaku\03G_PrintOK.png", 0.9, 10
                        )  # 出力条件設定OKをクリック
                        # 出力条件ウィンドウが表示されるなくなるまで待機--------------------------
                        while (
                            pg.locateOnScreen(
                                URL + r"\GenkaSyoukyaku\03G_PrintWait.png",
                                confidence=0.9,
                            )
                            is not None
                        ):
                            time.sleep(1)
                        time.sleep(3)
                        # --------------------------------------------------------------------
                        RPA.ImgClick(
                            URL, r"\GenkaSyoukyaku\01G_PrintBtn.png", 0.9, 10
                        )  # 印刷ボタンをクリック
                        # 印刷設定が表示されるまで待機---------------------------------
                        while (
                            pg.locateOnScreen(
                                URL + r"\Houjinzei\PrintBar.png", confidence=0.9
                            )
                            is None
                        ):
                            time.sleep(1)
                            SJS = RPA.ImgCheckForList(
                                URL,
                                [r"\Houjinzei\Nodata.png", r"\Houjinzei\NodataQ.png"],
                                0.9,
                                10,
                            )
                            if SJS[0] is True:
                                if "NodataQ.png" in SJS[1] is True:
                                    pg.press("return")
                                    Nod = "Nodata"
                                else:
                                    pg.press("return")
                                    RPA.ImgClick(
                                        URL, r"\Houjinzei\NodataCan.png", 0.9, 10
                                    )
                                    Nod = "Nodata"
                            if Nod == "Nodata":
                                break
                        # --------------------------------------------------------------------
                    if Nod == "":
                        # 申告税一覧表印刷処理----------------------------------------------------
                        FO = RPA.ImgCheckForList(
                            URL,
                            [
                                r"\Houjinzei\FileOut.png",
                                r"\Houjinzei\FileOut2.png",
                            ],
                            0.9,
                            10,
                        )
                        if FO[0] is True:
                            RPA.ImgClick(URL, FO[1], 0.9, 10)
                        RPA.ImgClick(URL, r"\Houjinzei\PDFBar.png", 0.9, 10)
                        pg.press("return")
                        pg.press("delete")
                        pg.press("backspace")
                        time.sleep(1)
                        pyperclip.copy(
                            Exc.Fname.replace("\\\\", "\\").replace("/", "\\")
                        )
                        time.sleep(1)
                        pg.hotkey("ctrl", "v")
                        pg.press("return")
                        time.sleep(1)
                        RPA.ImgClick(URL, r"\Houjinzei\PrintOut.png", 0.9, 10)
                        time.sleep(2)
                        #  印刷設定が表示されなくなるまで待機---------------------------------
                        while (
                            pg.locateOnScreen(
                                URL + r"\Houjinzei\PrintBar.png", confidence=0.9
                            )
                            is not None
                        ):
                            time.sleep(1)
                            FO = RPA.ImgCheck(URL, r"\Houjinzei\FileOver.png", 0.9, 10)
                            if FO[0] is True:
                                pg.press("y")
                        # --------------------------------------------------------------------
                        time.sleep(1)
                        # 確実に閉じる---------------------------------------------------
                        ZME = RPA.ImgCheck(URL, r"\GenkaSyoukyaku\01G_End.png", 0.9, 10)
                        if ZME[0] is True:
                            RPA.ImgClick(URL, r"\GenkaSyoukyaku\01G_End.png", 0.9, 10)
                        else:
                            pg.keyDown("alt")
                            pg.press("x")
                            pg.keyUp("alt")
                        # ---------------------------------------------------------------
                        time.sleep(1)
                        while (
                            RPA.ImgCheckForList(
                                URL,
                                [
                                    r"\GenkaSyoukyaku\01G_Uchiwake.png",
                                    r"\GenkaSyoukyaku\01G_Uchiwake2.png",
                                ],
                                0.9,
                                10,
                            )[0]
                            is False
                        ):
                            time.sleep(1)
                        # 閉じる処理--------------------------
                        pg.keyDown("alt")
                        pg.press("f4")
                        pg.keyUp("alt")
                        # -----------------------------------
                        f = 0
                        # 減価償却フラグが表示されるまで待機------------------------------------
                        while (
                            pg.locateOnScreen(
                                Job.PrintOut_url + r"\G_SyoukyakuFlag.png",
                                confidence=0.9,
                            )
                            is None
                        ):
                            time.sleep(1)
                            f += 1
                            if f == 5:
                                pg.keyDown("alt")
                                pg.press("f4")
                                pg.keyUp("alt")
                                f = 0
                        # ------------------------------------------------------------------
                        return True, ThisNo, ThisYear, ThisMonth
                    else:
                        while (
                            RPA.ImgCheckForList(
                                URL,
                                [
                                    r"\GenkaSyoukyaku\01G_Uchiwake.png",
                                    r"\GenkaSyoukyaku\01G_Uchiwake2.png",
                                ],
                                0.9,
                                10,
                            )[0]
                            is False
                        ):
                            time.sleep(1)
                        # 閉じる処理--------------------------
                        pg.keyDown("alt")
                        pg.press("f4")
                        pg.keyUp("alt")
                        # -----------------------------------
                        f = 0
                        # 減価償却フラグが表示されるまで待機------------------------------------
                        while (
                            pg.locateOnScreen(
                                Job.PrintOut_url + r"\G_SyoukyakuFlag.png",
                                confidence=0.9,
                            )
                            is None
                        ):
                            time.sleep(1)
                            f += 1
                            if f == 5:
                                pg.keyDown("alt")
                                pg.press("f4")
                                pg.keyUp("alt")
                                f = 0
                        # ------------------------------------------------------------------
                        return False, ThisNo, ThisYear, Nod
                elif PN == "少額償却資産":
                    Nod = ""
                    GIF = RPA.ImgCheckForList(
                        URL,
                        [
                            r"\GenkaSyoukyaku\04G_Syougaku.png",
                            r"\GenkaSyoukyaku\04G_Syougaku2.png",
                        ],
                        0.9,
                        10,
                    )
                    if GIF[0] is True:
                        RPA.ImgClick(URL, GIF[1], 0.9, 10)
                    # 出力条件ウィンドウが表示されるまで待機---------------------------------
                    while (
                        pg.locateOnScreen(
                            URL + r"\GenkaSyoukyaku\04G_PrintWait.png",
                            confidence=0.9,
                        )
                        is None
                    ):
                        time.sleep(1)
                    # --------------------------------------------------------------------
                    time.sleep(1)
                    RPA.ImgClick(
                        URL, r"\GenkaSyoukyaku\04G_PrintOK.png", 0.9, 10
                    )  # 出力条件設定OKをクリック
                    # 出力条件ウィンドウが表示されるなくなるまで待機--------------------------
                    while (
                        pg.locateOnScreen(
                            URL + r"\GenkaSyoukyaku\04G_PrintWait.png",
                            confidence=0.9,
                        )
                        is not None
                    ):
                        time.sleep(1)
                    time.sleep(3)
                    GN = RPA.ImgCheck(URL, r"\GenkaSyoukyaku\01G_Nodata.png", 0.9, 10)
                    if GN[0] is True:
                        pg.press("return")
                        Nod = "Nodata"
                    if Nod == "":
                        # --------------------------------------------------------------------
                        RPA.ImgClick(
                            URL, r"\GenkaSyoukyaku\01G_PrintBtn.png", 0.9, 10
                        )  # 印刷ボタンをクリック
                        # 印刷設定が表示されるまで待機---------------------------------
                        while (
                            pg.locateOnScreen(
                                URL + r"\Houjinzei\PrintBar.png", confidence=0.9
                            )
                            is None
                        ):
                            time.sleep(1)
                            SJS = RPA.ImgCheck(URL, r"\Houjinzei\Nodata.png", 0.9, 10)
                            if SJS[0] is True:
                                pg.press("return")
                                RPA.ImgClick(URL, r"\Houjinzei\NodataCan.png", 0.9, 10)
                                Nod = "Nodata"
                            if Nod == "Nodata":
                                break
                        # --------------------------------------------------------------------
                    else:
                        RPA.ImgClick(URL, r"\GenkaSyoukyaku\03G_Cancel.png", 0.9, 10)
                    if Nod == "":
                        # 申告税一覧表印刷処理----------------------------------------------------
                        FO = RPA.ImgCheckForList(
                            URL,
                            [
                                r"\Houjinzei\FileOut.png",
                                r"\Houjinzei\FileOut2.png",
                            ],
                            0.9,
                            10,
                        )
                        if FO[0] is True:
                            RPA.ImgClick(URL, FO[1], 0.9, 10)
                        RPA.ImgClick(URL, r"\Houjinzei\PDFBar.png", 0.9, 10)
                        pg.press("return")
                        pg.press("delete")
                        pg.press("backspace")
                        time.sleep(1)
                        pyperclip.copy(
                            Exc.Fname.replace("\\\\", "\\").replace("/", "\\")
                        )
                        time.sleep(1)
                        pg.hotkey("ctrl", "v")
                        pg.press("return")
                        time.sleep(1)
                        RPA.ImgClick(URL, r"\Houjinzei\PrintOut.png", 0.9, 10)
                        time.sleep(2)
                        #  印刷設定が表示されなくなるまで待機---------------------------------
                        while (
                            pg.locateOnScreen(
                                URL + r"\Houjinzei\PrintBar.png", confidence=0.9
                            )
                            is not None
                        ):
                            time.sleep(1)
                            FO = RPA.ImgCheck(URL, r"\Houjinzei\FileOver.png", 0.9, 10)
                            if FO[0] is True:
                                pg.press("y")
                        # --------------------------------------------------------------------
                        time.sleep(1)
                        # 確実に閉じる---------------------------------------------------
                        ZME = RPA.ImgCheck(URL, r"\GenkaSyoukyaku\01G_End.png", 0.9, 10)
                        if ZME[0] is True:
                            RPA.ImgClick(URL, r"\GenkaSyoukyaku\01G_End.png", 0.9, 10)
                        else:
                            pg.keyDown("alt")
                            pg.press("x")
                            pg.keyUp("alt")
                        # ---------------------------------------------------------------
                        time.sleep(1)
                        while (
                            RPA.ImgCheckForList(
                                URL,
                                [
                                    r"\GenkaSyoukyaku\01G_Uchiwake.png",
                                    r"\GenkaSyoukyaku\01G_Uchiwake2.png",
                                ],
                                0.9,
                                10,
                            )[0]
                            is False
                        ):
                            time.sleep(1)
                        # 閉じる処理--------------------------
                        pg.keyDown("alt")
                        pg.press("f4")
                        pg.keyUp("alt")
                        # -----------------------------------
                        f = 0
                        # 減価償却フラグが表示されるまで待機------------------------------------
                        while (
                            pg.locateOnScreen(
                                Job.PrintOut_url + r"\G_SyoukyakuFlag.png",
                                confidence=0.9,
                            )
                            is None
                        ):
                            time.sleep(1)
                            f += 1
                            if f == 5:
                                pg.keyDown("alt")
                                pg.press("f4")
                                pg.keyUp("alt")
                                f = 0
                        # ------------------------------------------------------------------
                        return True, ThisNo, ThisYear, ThisMonth
                    else:
                        while (
                            RPA.ImgCheckForList(
                                URL,
                                [
                                    r"\GenkaSyoukyaku\01G_Uchiwake.png",
                                    r"\GenkaSyoukyaku\01G_Uchiwake2.png",
                                ],
                                0.9,
                                10,
                            )[0]
                            is False
                        ):
                            time.sleep(1)
                        # 閉じる処理--------------------------
                        pg.keyDown("alt")
                        pg.press("f4")
                        pg.keyUp("alt")
                        # -----------------------------------
                        f = 0
                        # 減価償却フラグが表示されるまで待機------------------------------------
                        while (
                            pg.locateOnScreen(
                                Job.PrintOut_url + r"\G_SyoukyakuFlag.png",
                                confidence=0.9,
                            )
                            is None
                        ):
                            time.sleep(1)
                            f += 1
                            if f == 5:
                                pg.keyDown("alt")
                                pg.press("f4")
                                pg.keyUp("alt")
                                f = 0
                        # ------------------------------------------------------------------
                        return False, ThisNo, ThisYear, Nod
            else:
                print("関与先なし")
                return False, "関与先なし", "", ""
        else:
            return False, "減価償却起動失敗", "", ""
    except:
        return False, "exceptエラー", "", ""


# # ------------------------------------------------------------------------------------------------------------------
# def GenkasyoukyakuUpdate(Job, Exc):
#     """
#     概要: 減価償却更新処理
#     @param FolURL : ミロク起動関数のフォルダ(str)
#     @param URL : このpyファイルのフォルダ(str)
#     @param Exc.row_data : Excel抽出行(obj)
#     @param driver : 画面操作ドライバー(obj)
#     @return : bool,ミロク入力関与先コード, ミロク入力処理年, ミロク入力処理月
#     """
#     try:
#         URL = Job.imgdir_url + r"\\GenkasyoukyakuUpdate"
#         ErrStr = ""  # Rpaエラー判別変数
#         # 減価償却フラグが表示されるまで待機------------------------------------
#         while pg.locateOnScreen(URL + r"\G_SyoukyakuFlag.png", confidence=0.9) is None:
#             time.sleep(1)
#         # ------------------------------------------------------------------
#         time.sleep(1)
#         # 年度を最新に指定----------------------------------------------------
#         IC = RPA.RPA.ImgCheck(URL, r"\Nendo_Saisin.png", 0.9, 10)
#         if IC[0] is False:
#             IC2 = RPA.RPA.ImgCheck(URL, r"\Nendo_All.png", 0.9, 10)
#             if IC2[0] is False:
#                 print("年度選択がない")
#             else:
#                 RPA.RPA.ImgClick(URL, r"\Nendo_All.png", 0.9, 10)
#                 pg.press("home")
#                 time.sleep(1)
#                 pg.press("down")
#                 time.sleep(1)
#                 pg.press("return")
#                 time.sleep(1)
#         # ------------------------------------------------------------------
#         # 関与先コード入力ボックスをクリック------------------------------------
#         while pg.locateOnScreen(URL + r"\K_NoBox.png", confidence=0.9) is None:
#             time.sleep(1)
#         time.sleep(1)
#         RPA.RPA.ImgClick(URL, r"\K_NoBox.png", 0.9, 10)
#         while pg.locateOnScreen(URL + r"\K_AfterNoBox.png", confidence=0.9) is None:
#             time.sleep(1)
#         pg.write(str(Exc.row_data["関与先番号"]))
#         pg.press(["return", "return", "return"])
#         # 入力した関与先コードを取得------------
#         pg.keyDown("shift")
#         pg.press(["tab", "tab", "tab"])
#         pg.keyUp("shift")
#         if windll.user32.OpenClipboard(None):
#             windll.user32.EmptyClipboard()
#             windll.user32.CloseClipboard()
#         pg.hotkey("ctrl", "c")
#         ThisNo = pyperclip.paste()
#         # -----------------------------------
#         pg.press("return")
#         # 表示された年度を取得-----------------
#         if windll.user32.OpenClipboard(None):
#             windll.user32.EmptyClipboard()
#             windll.user32.CloseClipboard()
#         pg.hotkey("ctrl", "c")
#         ThisYear = pyperclip.paste()
#         # -----------------------------------
#         pg.press("return")
#         # 表示された月を取得-------------------
#         if windll.user32.OpenClipboard(None):
#             windll.user32.EmptyClipboard()
#             windll.user32.CloseClipboard()
#         pg.hotkey("ctrl", "c")
#         ThisMonth = pyperclip.paste()
#         # -----------------------------------
#         time.sleep(1)
#         if str(Exc.row_data["関与先番号"]) == ThisNo:
#             print("関与先あり")
#             if (
#                 Job.Start_Year < int(ThisYear) or Job.Start_Year - int(ThisYear) == 1
#             ):  # 次年度更新か判定
#                 pg.press(["return", "return", "return"])
#                 # 減価償却メニューが表示されるまで待機------------------------------------
#                 while (
#                     pg.locateOnScreen(URL + r"\G_SyoukyakuMenu.png", confidence=0.9)
#                     is None
#                 ):
#                     time.sleep(1)
#                     # アップデート情報画面が出たら閉じる-------------------------------
#                     GSUM = RPA.RPA.ImgCheck(URL, r"\G_SyoukyakuUpMsg.png", 0.9, 10)
#                     if GSUM[0] is True:
#                         RPA.RPA.ImgClick(URL, r"\G_SyoukyakuUpMsgCansel.png", 0.9, 10)
#                     # 顧問先情報変更ダイアログが表示されたら
#                     CDQ = RPA.RPA.ImgCheck(
#                         URL,
#                         r"ChangeDataQ.png",
#                         0.9,
#                         10,
#                     )
#                     if CDQ[0] is True:
#                         pg.press("y")  # yで決定
#                         # 顧問先情報取込メニューが表示されるまで待機--------------------------
#                         while (
#                             RPA.RPA.ImgCheckForList(
#                                 URL,
#                                 [r"ChangeDataBtn.png", r"ChangeDataBtn2.png"],
#                                 0.9,
#                                 10,
#                             )[0]
#                             is False
#                         ):
#                             time.sleep(1)
#                         CDB = RPA.RPA.ImgCheckForList(
#                             URL,
#                             [r"ChangeDataBtn.png", r"ChangeDataBtn2.png"],
#                             0.9,
#                             10,
#                         )
#                         RPA.RPA.ImgClick(URL, CDB[1], 0.9, 10)  # 顧問先情報取込ボタンをクリック
#                 # --------------------------------------------------------------------
#                 RPA.RPA.ImgClick(URL, r"\G_SyoukyakuMenu.png", 0.9, 10)  # 一括更新のアイコンをクリック
#                 RPA.RPA.ImgClick(URL, r"\M_G_Sonota.png", 0.9, 10)  # 5.その他処理アイコンをクリック
#                 # 一括更新メニューが表示されるまで待機------------------------------------
#                 while (
#                     pg.locateOnScreen(URL + r"\IkkatsuGenkaKousin.png", confidence=0.9)
#                     is None
#                 ):
#                     time.sleep(1)
#                 # --------------------------------------------------------------------
#                 RPA.RPA.ImgClick(
#                     URL, r"\IkkatsuGenkaKousin.png", 0.9, 10
#                 )  # 一括更新メニューのアイコンをクリック
#                 # 一括更新メニューが表示されるまで待機------------------------------------
#                 while (
#                     pg.locateOnScreen(URL + r"\IkkatuOpenGenkaFlag.png", confidence=0.9)
#                     is None
#                 ):
#                     time.sleep(1)
#                 # --------------------------------------------------------------------
#                 RPA.RPA.ImgClick(
#                     URL, r"\IkkatuOpenGenkaFlag.png", 0.9, 10
#                 )  # 一括更新メニューのアイコンをクリック
#                 time.sleep(1)
#                 RPA.RPA.ImgClick(URL, r"\IkkatuGenakStart.png", 0.9, 10)  # 一括更新開始のアイコンをクリック
#                 # 確認ウィンドウが表示されるまで待機-------------------------------------
#                 while (
#                     pg.locateOnScreen(URL + r"\SakuseiGenkaQ.png", confidence=0.9)
#                     is None
#                 ):
#                     time.sleep(1)
#                 # --------------------------------------------------------------------
#                 pg.press("y")  # yで決定(nがキャンセル)
#                 # 処理終了ウィンドウが表示されるまで待機----------------------------------
#                 while (
#                     pg.locateOnScreen(URL + r"\SakuseiGenkaEnd.png", confidence=0.9)
#                     is None
#                 ):
#                     time.sleep(1)
#                     Noren = RPA.RPA.ImgCheck(URL, r"\No_Rendou.png", 0.9, 10)
#                     if Noren[0] is True:
#                         ErrStr = "Noren"
#                         pg.press("y")  # yで決定(nがキャンセル)
#                 # --------------------------------------------------------------------
#                 pg.press("return")  # 決定
#                 # 一括更新のアイコンが表示されるまで待機----------------------------------
#                 while (
#                     pg.locateOnScreen(URL + r"\G_SyoukyakuMenu.png", confidence=0.9)
#                     is None
#                 ):
#                     time.sleep(1)
#                 # --------------------------------------------------------------------
#                 # 閉じる処理--------------------------
#                 pg.keyDown("alt")
#                 pg.press("f4")
#                 pg.keyUp("alt")
#                 # -----------------------------------
#                 # 減価償却フラグが表示されるまで待機-------------------------------------
#                 while (
#                     pg.locateOnScreen(URL + r"\G_SyoukyakuFlag.png", confidence=0.9)
#                     is None
#                 ):
#                     time.sleep(1)
#                     al4c = RPA.RPA.ImgCheck(URL, r"\altf4Q.png", 0.9, 10)  # 終了確認が表示されたら
#                     if al4c[0] is True:
#                         pg.press("y")  # yで決定(nがキャンセル)
#                 # --------------------------------------------------------------------
#                 print("更新完了")
#                 if ErrStr == "":
#                     return True, ThisNo, ThisYear, ThisMonth
#                 elif ErrStr == "Noren":
#                     return False, ErrStr, "", ""
#             elif Job.Start_Year == int(ThisYear):  # 次年度更新か判定
#                 return False, "当年データ重複エラー", "", ""
#         else:
#             print("関与先なし")
#             return False, "関与先なし", "", ""
#     except:
#         return False, "exceptエラー", "", ""
