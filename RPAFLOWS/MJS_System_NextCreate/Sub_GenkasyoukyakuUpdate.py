# ------------------------------------------------------------------------------------------------------------------
def GenkasyoukyakuUpdate(FolURL, TFolURL, ExRow, driver):
    """
    概要: 減価償却更新処理
    @param FolURL : ミロク起動関数のフォルダ(str)
    @param TFolURL : このpyファイルのフォルダ(str)
    @param ExRow : Excel抽出行(obj)
    @param driver : 画面操作ドライバー(obj)
    @return : bool,ミロク入力関与先コード, ミロク入力処理年, ミロク入力処理月
    """
    try:
        ErrStr = ""  # Rpaエラー判別変数
        # 減価償却のアイコンを探す-------------------------------------------------
        ImgList = [r"\G_Syoukyaku.png", r"\G_Syoukyaku2.png"]
        ICFL = RPA.ImgCheckForList(TFolURL, ImgList, 0.9, 10)
        # -----------------------------------------------------------------------
        if ICFL[0] is True:  # 減価償却のアイコンがあれば
            RPA.ImgClick(TFolURL, ICFL[1], 0.9, 10)  # 減価償却のアイコンをクリック
            # 減価償却フラグが表示されるまで待機------------------------------------
            while (
                pg.locateOnScreen(TFolURL + r"\G_SyoukyakuFlag.png", confidence=0.9)
                is None
            ):
                time.sleep(1)
            # ------------------------------------------------------------------
            time.sleep(1)
            # 年度を最新に指定----------------------------------------------------
            IC = RPA.ImgCheck(TFolURL, r"\Nendo_Saisin.png", 0.9, 10)
            if IC[0] is False:
                IC2 = RPA.ImgCheck(TFolURL, r"\Nendo_All.png", 0.9, 10)
                if IC2[0] is False:
                    print("年度選択がない")
                else:
                    RPA.ImgClick(TFolURL, r"\Nendo_All.png", 0.9, 10)
                    pg.press("home")
                    time.sleep(1)
                    pg.press("down")
                    time.sleep(1)
                    pg.press("return")
                    time.sleep(1)
            # ------------------------------------------------------------------
            # 関与先コード入力ボックスをクリック------------------------------------
            while pg.locateOnScreen(TFolURL + r"\K_NoBox.png", confidence=0.9) is None:
                time.sleep(1)
            time.sleep(1)
            RPA.ImgClick(TFolURL, r"\K_NoBox.png", 0.9, 10)
            while (
                pg.locateOnScreen(TFolURL + r"\K_AfterNoBox.png", confidence=0.9)
                is None
            ):
                time.sleep(1)
            pg.write(str(ExRow["関与先番号"]))
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
            if str(ExRow["関与先番号"]) == ThisNo:
                print("関与先あり")
                if (
                    Start_Year < int(ThisYear) or Start_Year - int(ThisYear) == 1
                ):  # 次年度更新か判定
                    pg.press(["return", "return", "return"])
                    # 減価償却メニューが表示されるまで待機------------------------------------
                    while (
                        pg.locateOnScreen(
                            TFolURL + r"\G_SyoukyakuMenu.png", confidence=0.9
                        )
                        is None
                    ):
                        time.sleep(1)
                        # アップデート情報画面が出たら閉じる-------------------------------
                        GSUM = RPA.ImgCheck(TFolURL, r"\G_SyoukyakuUpMsg.png", 0.9, 10)
                        if GSUM[0] is True:
                            RPA.ImgClick(
                                TFolURL, r"\G_SyoukyakuUpMsgCansel.png", 0.9, 10
                            )
                        # 顧問先情報変更ダイアログが表示されたら
                        CDQ = RPA.ImgCheck(
                            TFolURL,
                            r"ChangeDataQ.png",
                            0.9,
                            10,
                        )
                        if CDQ[0] is True:
                            pg.press("y")  # yで決定
                            # 顧問先情報取込メニューが表示されるまで待機--------------------------
                            while (
                                RPA.ImgCheckForList(
                                    TFolURL,
                                    [r"ChangeDataBtn.png", r"ChangeDataBtn2.png"],
                                    0.9,
                                    10,
                                )[0]
                                is False
                            ):
                                time.sleep(1)
                            CDB = RPA.ImgCheckForList(
                                TFolURL,
                                [r"ChangeDataBtn.png", r"ChangeDataBtn2.png"],
                                0.9,
                                10,
                            )
                            RPA.ImgClick(TFolURL, CDB[1], 0.9, 10)  # 顧問先情報取込ボタンをクリック
                    # --------------------------------------------------------------------
                    RPA.ImgClick(
                        TFolURL, r"\G_SyoukyakuMenu.png", 0.9, 10
                    )  # 一括更新のアイコンをクリック
                    RPA.ImgClick(
                        TFolURL, r"\M_G_Sonota.png", 0.9, 10
                    )  # 5.その他処理アイコンをクリック
                    # 一括更新メニューが表示されるまで待機------------------------------------
                    while (
                        pg.locateOnScreen(
                            TFolURL + r"\IkkatsuGenkaKousin.png", confidence=0.9
                        )
                        is None
                    ):
                        time.sleep(1)
                    # --------------------------------------------------------------------
                    RPA.ImgClick(
                        TFolURL, r"\IkkatsuGenkaKousin.png", 0.9, 10
                    )  # 一括更新メニューのアイコンをクリック
                    # 一括更新メニューが表示されるまで待機------------------------------------
                    while (
                        pg.locateOnScreen(
                            TFolURL + r"\IkkatuOpenGenkaFlag.png", confidence=0.9
                        )
                        is None
                    ):
                        time.sleep(1)
                    # --------------------------------------------------------------------
                    RPA.ImgClick(
                        TFolURL, r"\IkkatuOpenGenkaFlag.png", 0.9, 10
                    )  # 一括更新メニューのアイコンをクリック
                    time.sleep(1)
                    RPA.ImgClick(
                        TFolURL, r"\IkkatuGenakStart.png", 0.9, 10
                    )  # 一括更新開始のアイコンをクリック
                    # 確認ウィンドウが表示されるまで待機-------------------------------------
                    while (
                        pg.locateOnScreen(
                            TFolURL + r"\SakuseiGenkaQ.png", confidence=0.9
                        )
                        is None
                    ):
                        time.sleep(1)
                    # --------------------------------------------------------------------
                    pg.press("y")  # yで決定(nがキャンセル)
                    # 処理終了ウィンドウが表示されるまで待機----------------------------------
                    while (
                        pg.locateOnScreen(
                            TFolURL + r"\SakuseiGenkaEnd.png", confidence=0.9
                        )
                        is None
                    ):
                        time.sleep(1)
                        Noren = RPA.ImgCheck(TFolURL, r"\No_Rendou.png", 0.9, 10)
                        if Noren[0] is True:
                            ErrStr = "Noren"
                            pg.press("y")  # yで決定(nがキャンセル)
                    # --------------------------------------------------------------------
                    pg.press("return")  # 決定
                    # 一括更新のアイコンが表示されるまで待機----------------------------------
                    while (
                        pg.locateOnScreen(
                            TFolURL + r"\G_SyoukyakuMenu.png", confidence=0.9
                        )
                        is None
                    ):
                        time.sleep(1)
                    # --------------------------------------------------------------------
                    # 閉じる処理--------------------------
                    pg.keyDown("alt")
                    pg.press("f4")
                    pg.keyUp("alt")
                    # -----------------------------------
                    # 減価償却フラグが表示されるまで待機-------------------------------------
                    while (
                        pg.locateOnScreen(
                            TFolURL + r"\G_SyoukyakuFlag.png", confidence=0.9
                        )
                        is None
                    ):
                        time.sleep(1)
                        al4c = RPA.ImgCheck(
                            TFolURL, r"\altf4Q.png", 0.9, 10
                        )  # 終了確認が表示されたら
                        if al4c[0] is True:
                            pg.press("y")  # yで決定(nがキャンセル)
                    # --------------------------------------------------------------------
                    print("更新完了")
                    if ErrStr == "":
                        return True, ThisNo, ThisYear, ThisMonth
                    elif ErrStr == "Noren":
                        return False, ErrStr, "", ""
                elif Start_Year == int(ThisYear):  # 次年度更新か判定
                    return False, "当年データ重複エラー", "", ""
            else:
                print("関与先なし")
                return False, "関与先なし", "", ""
        else:
            return False, "減価償却起動失敗", "", ""
    except:
        return False, "exceptエラー", "", ""
