def KaikeiUpDate(self):
    """
    概要: 会計大将更新処理
    @param FolURL : ミロク起動関数のフォルダ(str)
    @param TFolURL : このpyファイルのフォルダ(str)
    @param ExRow : Excel抽出行(obj)
    @param driver : 画面操作ドライバー(obj)
    @return : bool,ミロク入力関与先コード, ミロク入力処理年, ミロク入力処理月
    """
    try:
        # ErrStr = ""  # Rpaエラー判別変数
        # 会計大将のアイコンを探す-------------------------------------------------
        ImgList = [r"\K_TaisyouIcon.png", r"\K_TaisyouIcon2.png"]
        ICFL = RPA.ImgCheckForList(TFolURL, ImgList, 0.9, 10)
        # -----------------------------------------------------------------------
        if ICFL[0] is True:  # 会計大将のアイコンがあれば
            RPA.ImgClick(TFolURL, ICFL[1], 0.9, 10)  # 会計大将のアイコンをクリック
            # 会計大将フラグが表示されるまで待機------------------------------------
            while (
                pg.locateOnScreen(TFolURL + r"\Kaikei_CFlag.png", confidence=0.9)
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
                pg.press(["return", "return", "return"])
                # 会計大将メニューが表示されるまで待機------------------------------------
                while (
                    pg.locateOnScreen(TFolURL + r"\K_TaisyouMenu.png", confidence=0.9)
                    is None
                ):
                    time.sleep(1)
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
                if (
                    Start_Year < int(ThisYear) or Start_Year - int(ThisYear) == 1
                ):  # 次年度更新か判定
                    IUD = IkkatuUpDate(FolURL, TFolURL, ExRow, driver)
                    time.sleep(3)
                    pg.keyDown("alt")
                    pg.press("x")
                    pg.keyUp("alt")
                    # --------------------------------------------------------------------
                    ME = RPA.ImgCheckForList(
                        TFolURL, [r"\MenuEnd.png", r"\MenuEnd2.png"], 0.9, 10
                    )
                    if ME[0] is True:
                        RPA.ImgClick(TFolURL, ME[1], 0.9, 10)  # 終了アイコンをクリック
                    # --------------------------------------------------------------------
                    # 閉じる処理--------------------------
                    pg.keyDown("alt")
                    pg.press("f4")
                    pg.keyUp("alt")
                    # -----------------------------------
                elif Start_Year == int(ThisYear):  # 次年度更新か判定
                    # 閉じる処理--------------------------
                    pg.keyDown("alt")
                    pg.press("f4")
                    pg.keyUp("alt")
                    # -----------------------------------
                    IUD = "当年"
                else:
                    IUD = IkkatuUpDate(FolURL, TFolURL, ExRow, driver)
                    time.sleep(3)
                    pg.keyDown("alt")
                    pg.press("x")
                    pg.keyUp("alt")
                    # --------------------------------------------------------------------
                    ME = RPA.ImgCheckForList(
                        TFolURL, [r"\MenuEnd.png", r"\MenuEnd2.png"], 0.9, 10
                    )
                    if ME[0] is True:
                        RPA.ImgClick(TFolURL, ME[1], 0.9, 10)  # 終了アイコンをクリック
                    # --------------------------------------------------------------------
                    # 閉じる処理--------------------------
                    pg.keyDown("alt")
                    pg.press("f4")
                    pg.keyUp("alt")
                    # -----------------------------------
                    # RPA.ImgClick(TFolURL, r"\PrintOutTab.png", 0.9, 10)  # 2印刷タブクリック
                    # # 6月次締めが表示されるまで待機--------------------------
                    # while (
                    #     pg.locateOnScreen(TFolURL + r"\SimeIcon.png", confidence=0.9)
                    #     is None
                    # ):
                    #     time.sleep(1)
                    # RPA.ImgClick(TFolURL, r"\SimeIcon.png", 0.9, 10)  # その他メニュ-のアイコンをクリック
                    # while (
                    #     pg.locateOnScreen(TFolURL + r"\GetujiIcon.png", confidence=0.9)
                    #     is None
                    # ):
                    #     time.sleep(1)
                    # RPA.ImgClick(TFolURL, r"\GetujiIcon.png", 0.9, 10)  # 月次処理アイコンをクリック
                    # # 月次確定済みか判定して処理分け-------------------------------------------------------
                    # # 月次処理解除-----------------------------------------------------------------------
                    # KUL = RPA.ImgCheck(
                    #     TFolURL, r"\KakuteUnLock.png", 0.9, 10
                    # )  # 月次処理解除アイコンを検索
                    # if KUL[0] is True:
                    #     RPA.ImgClick(
                    #         TFolURL, r"\KakuteUnLock.png", 0.9, 10
                    #     )  # 月次処理アイコンをクリック
                    #     time.sleep(2)
                    #     pg.press("y")
                    #     while (
                    #         pg.locateOnScreen(
                    #             TFolURL + r"\GetusjiKakutei.png", confidence=0.9
                    #         )
                    #         is None
                    #     ):
                    #         time.sleep(1)
                    #     pg.press("return")
                    #     time.sleep(1)
                    # # ---------------------------------------------------------------------------------
                    time.sleep(3)
                    pg.keyDown("alt")
                    pg.press("x")
                    pg.keyUp("alt")
                    while (
                        pg.locateOnScreen(TFolURL + r"\M_Sonota.png", confidence=0.9)
                        is None
                    ):
                        time.sleep(1)
                    RPA.ImgClick(TFolURL, r"\D_TourokuTAB.png", 0.9, 10)  # 6導入・登録タブクリック
                    # 会社基本情報アイコンが表示されるまで待機--------------------------------------
                    while (
                        pg.locateOnScreen(TFolURL + r"\CamIcon.png", confidence=0.9)
                        is None
                    ):
                        time.sleep(1)
                    RPA.ImgClick(TFolURL, r"\CamIcon.png", 0.9, 10)  # 会社基本情報アイコンをクリック
                    # 顧問先情報取り込みアイコンが表示されるまで待機--------------------------------
                    while (
                        pg.locateOnScreen(TFolURL + r"\DataInIcon.png", confidence=0.9)
                        is None
                    ):
                        time.sleep(1)
                    RPA.ImgClick(
                        TFolURL, r"\DataInIcon.png", 0.9, 10
                    )  # 顧問先情報取り込みアイコンをクリック
                    while (
                        pg.locateOnScreen(TFolURL + r"\DataInOK.png", confidence=0.9)
                        is None
                    ):
                        time.sleep(1)
                    RPA.ImgClick(TFolURL, r"\DataInOK.png", 0.9, 10)  # 取り込むボタンをクリック
                    time.sleep(3)
                    pg.keyDown("alt")
                    pg.press("x")
                    pg.keyUp("alt")
                    time.sleep(1)
                    # --------------------------------------------------------------------------------
                    RPA.ImgClick(TFolURL, r"\PrintOutTab.png", 0.9, 10)  # 2印刷タブクリック
                    # マスター更新------------------------------------------------------------------------
                    RPA.ImgClick(TFolURL, r"\MasterUp.png", 0.9, 10)  # マスター更新をクリック
                    while (
                        RPA.ImgCheckForList(
                            TFolURL,
                            [r"MasterUpStart.png", r"MasterUpStart2.png"],
                            0.9,
                            10,
                        )[0]
                        is True
                    ):
                        time.sleep(1)
                        TL = RPA.ImgCheckForList(
                            TFolURL,
                            [r"MasterUpStart.png", r"MasterUpStart2.png"],
                            0.9,
                            10,
                        )
                        RPA.ImgClick(TFolURL, TL[1], 0.9, 10)  # マスター更新開始をクリック
                        break
                    time.sleep(3)
                    pg.press("y")
                    time.sleep(3)
                    pg.press("return")
                    time.sleep(3)
                    pg.keyDown("alt")
                    pg.press("x")
                    pg.keyUp("alt")
                    # 月次確定--------------------------------------------------------------------------
                    # 月次確定アイコンが表示されるまで待機--------------------------
                    while (
                        pg.locateOnScreen(
                            TFolURL + r"\AfterGetujiKakutei.png", confidence=0.9
                        )
                        is None
                    ):
                        time.sleep(1)
                    RPA.ImgClick(
                        TFolURL, r"\AfterGetujiKakutei.png", 0.9, 10
                    )  # 月次確定アイコンクリック
                    KL = RPA.ImgCheck(
                        TFolURL, r"\KakuteiLock.png", 0.9, 10
                    )  # 月次処理確定アイコンを検索
                    if KL[0] is True:
                        while (
                            pg.locateOnScreen(
                                TFolURL + r"\KakuteiKaijyo.png", confidence=0.99999
                            )
                            is not None
                        ):
                            RPA.ImgClick(
                                TFolURL, r"\KakuteiKaijyo.png", 0.99999, 10
                            )  # 月次未確定チェックボックスをクリック
                            time.sleep(1)
                        RPA.ImgClick(
                            TFolURL, r"\KakuteiLock.png", 0.9, 10
                        )  # 月次処理確定アイコンをクリック
                        time.sleep(1)
                        pg.press("y")
                        # ---------------------------------------------------------
                        while (
                            pg.locateOnScreen(
                                TFolURL + r"\KessanKQ.png", confidence=0.9
                            )
                            is None
                        ):
                            time.sleep(1)
                            KessanKakuteiErr(FolURL, TFolURL, ExRow, driver)
                        # ---------------------------------------------------------
                    time.sleep(1)
                    pg.keyDown("alt")
                    pg.press("x")
                    pg.keyUp("alt")
                    RPA.ImgClick(
                        TFolURL, r"\M_Sonota.png", 0.9, 10
                    )  # その他メニュ-のアイコンをクリック
                    # 一括更新のアイコンが表示されるまで待機----------------------------------
                    while (
                        pg.locateOnScreen(
                            TFolURL + r"\IkkatsuKousin.png", confidence=0.9
                        )
                        is None
                    ):
                        time.sleep(1)
                    # --------------------------------------------------------------------
                    RPA.ImgClick(
                        TFolURL, r"\IkkatsuKousin.png", 0.9, 10
                    )  # その他メニュ-のアイコンをクリック
                    # 一括更新メニューが表示されるまで待機------------------------------------
                    while (
                        pg.locateOnScreen(
                            TFolURL + r"\IkkatuOpenFlag.png", confidence=0.9
                        )
                        is None
                    ):
                        time.sleep(1)
                        # UW = RPA.ImgCheck(TFolURL, r"\Underwindow.png", 0.9, 10)
                        # if UW[0] is True:
                        #     RPA.ImgClick(TFolURL, r"\Underwindow.png", 0.9, 10)
                        #     UW2 = RPA.ImgCheck(TFolURL, r"\Underwindow2.png", 0.9, 10)
                        #     if UW2[0] is True:
                        #         RPA.ImgClick(TFolURL, r"\Underwindow2.png", 0.9, 10)
                    # --------------------------------------------------------------------
                    RPA.ImgClick(
                        TFolURL, r"\IkkatuOpenFlag.png", 0.9, 10
                    )  # 一括更新メニューのアイコンをクリック
                    while (
                        RPA.ImgCheckForList(
                            TFolURL, [r"IkkatuFind.png", r"IkkatuFind2.png"], 0.9, 10
                        )[0]
                        is False
                    ):
                        time.sleep(1)
                    FC = RPA.ImgCheckForList(
                        TFolURL,
                        [
                            r"IkkatuFind.png",
                            r"IkkatuFind2.png",
                        ],
                        0.9,
                        10,
                    )
                    if FC[0] is True:
                        RPA.ImgClick(TFolURL, FC[1], 0.9, 10)  # 一括更新メニューのアイコンをクリック
                        pyperclip.copy(str(ExRow["関与先番号"]))
                        pg.hotkey("ctrl", "v")
                        # 検索ボタンまでエンター-------------------------------------
                        while (
                            RPA.ImgCheck(TFolURL, r"FindFlag.png", 0.9, 10)[0] is False
                        ):
                            time.sleep(1)
                            pg.press("return")
                    pg.press("return")
                    time.sleep(1)
                    pg.press("space")
                    # チェックマークが表示されるまで待機-------------------------------------
                    while (
                        RPA.ImgCheckForList(
                            TFolURL,
                            [
                                r"IkkatuCheck.png",
                                r"ZaisanCheck.png",
                                r"NendCheck.png",
                                r"HouteiCheck.png",
                            ],
                            0.9,
                            10,
                        )[0]
                        is False
                    ):
                        time.sleep(1)
                    # --------------------------------------------------------------------
                    time.sleep(1)
                    RPA.ImgClick(
                        TFolURL, r"\IkkatuStart.png", 0.9, 10
                    )  # 一括更新開始のアイコンをクリック
                    # 確認ウィンドウが表示されるまで待機-------------------------------------
                    while (
                        pg.locateOnScreen(TFolURL + r"\SakuseiQ.png", confidence=0.9)
                        is None
                    ):
                        time.sleep(1)
                    # --------------------------------------------------------------------
                    pg.press("y")  # yで決定(nがキャンセル)
                    # 確認ウィンドウが表示されるまで待機-------------------------------------
                    while (
                        pg.locateOnScreen(TFolURL + r"\SakuseiQ2.png", confidence=0.9)
                        is None
                    ):
                        time.sleep(1)
                    # --------------------------------------------------------------------
                    pg.press("return")  # 決定
                    # 処理終了ウィンドウが表示されるまで待機----------------------------------
                    while (
                        pg.locateOnScreen(
                            TFolURL + r"\IkkatuEndFlag.png", confidence=0.9
                        )
                        is None
                    ):
                        time.sleep(1)
                    # --------------------------------------------------------------------
                    pg.press("return")  # 決定
                    # チェックマークが表示されなくなるまで待機-------------------------------
                    while (
                        RPA.ImgCheckForList(
                            TFolURL,
                            [
                                r"IkkatuCheck.png",
                                r"ZaisanCheck.png",
                                r"NendCheck.png",
                                r"HouteiCheck.png",
                            ],
                            0.9,
                            10,
                        )[0]
                        is True
                    ):
                        time.sleep(1)
                    # 一括更新のアイコンが表示されるまで待機----------------------------------
                    while (
                        pg.locateOnScreen(
                            TFolURL + r"\IkkatsuKousin.png", confidence=0.9
                        )
                        is None
                    ):
                        time.sleep(1)
                        # --------------------------------------------------------------------
                        ME = RPA.ImgCheckForList(
                            TFolURL, [r"\MenuEnd.png", r"\MenuEnd2.png"], 0.9, 10
                        )
                        if ME[0] is True:
                            RPA.ImgClick(TFolURL, ME[1], 0.9, 10)  # 終了アイコンをクリック
                    # --------------------------------------------------------------------
                    # 閉じる処理--------------------------
                    pg.keyDown("alt")
                    pg.press("f4")
                    pg.keyUp("alt")
                    # -----------------------------------
                    # 会計大将フラグが表示されるまで待機-------------------------------------
                    while (
                        pg.locateOnScreen(
                            TFolURL + r"\Kaikei_CFlag.png", confidence=0.9
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
                    IUD = True
                if IUD is True:
                    print("更新完了")
                    return True, ThisNo, ThisYear, ThisMonth
                elif IUD == "当年":
                    return False, "当年データ重複エラー", "", ""
                else:
                    return False, "会計大将一括更新エラー", "", ""
            else:
                print("関与先なし")
                return False, "関与先なし", "", ""
        else:
            return False, "会計大将起動失敗", "", ""
    except:
        return False, "exceptエラー", "", ""
