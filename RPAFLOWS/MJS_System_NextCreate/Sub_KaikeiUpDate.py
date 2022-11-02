from ctypes import windll


def KaikeiUpDate(Job, Exc):
    """
    概要: 会計大将更新処理
    @param FolURL : ミロク起動関数のフォルダ(str)
    @param URL : このpyファイルのフォルダ(str)
    @param Exc.row_data : Excel抽出行(obj)
    @param driver : 画面操作ドライバー(obj)
    @return : bool,ミロク入力関与先コード, ミロク入力処理年, ミロク入力処理月
    """
    try:
        URL = Job.imgdir_url + r"\\KaikeiUpDate"
        # 会計大将フラグが表示されるまで待機------------------------------------
        while Job.pg.locateOnScreen(URL + r"\Kaikei_CFlag.png", confidence=0.9) is None:
            Job.time.sleep(1)
        # ------------------------------------------------------------------
        Job.time.sleep(1)
        # 年度を最新に指定----------------------------------------------------
        IC = Job.RPA.ImgCheck(URL, r"\Nendo_Saisin.png", 0.9, 10)
        if IC[0] is False:
            IC2 = Job.RPA.ImgCheck(URL, r"\Nendo_All.png", 0.9, 10)
            if IC2[0] is False:
                print("年度選択がない")
            else:
                Job.RPA.ImgClick(URL, r"\Nendo_All.png", 0.9, 10)
                Job.pg.press("home")
                Job.time.sleep(1)
                Job.pg.press("down")
                Job.time.sleep(1)
                Job.pg.press("return")
                Job.time.sleep(1)
        # ------------------------------------------------------------------
        # 関与先コード入力ボックスをクリック------------------------------------
        while Job.pg.locateOnScreen(URL + r"\K_NoBox.png", confidence=0.9) is None:
            Job.time.sleep(1)
        Job.time.sleep(1)
        Job.RPA.ImgClick(URL, r"\K_NoBox.png", 0.9, 10)
        while Job.pg.locateOnScreen(URL + r"\K_AfterNoBox.png", confidence=0.9) is None:
            Job.time.sleep(1)
        Job.pg.write(str(Exc.row_data["関与先番号"]))
        Job.pg.press(["return", "return", "return"])
        # 入力した関与先コードを取得------------
        Job.pg.keyDown("shift")
        Job.pg.press(["tab", "tab", "tab"])
        Job.pg.keyUp("shift")
        if windll.user32.OpenClipboard(None):
            windll.user32.EmptyClipboard()
            windll.user32.CloseClipboard()
        Job.pg.hotkey("ctrl", "c")
        ThisNo = pyperclip.paste()
        # -----------------------------------
        Job.pg.press("return")
        # 表示された年度を取得-----------------
        if windll.user32.OpenClipboard(None):
            windll.user32.EmptyClipboard()
            windll.user32.CloseClipboard()
        Job.pg.hotkey("ctrl", "c")
        ThisYear = pyperclip.paste()
        # -----------------------------------
        Job.pg.press("return")
        # 表示された月を取得-------------------
        if windll.user32.OpenClipboard(None):
            windll.user32.EmptyClipboard()
            windll.user32.CloseClipboard()
        Job.pg.hotkey("ctrl", "c")
        ThisMonth = pyperclip.paste()
        # -----------------------------------
        Job.time.sleep(1)
        if str(Exc.row_data["関与先番号"]) == ThisNo:
            print("関与先あり")
            Job.pg.press(["return", "return", "return"])
            # 会計大将メニューが表示されるまで待機------------------------------------
            while (
                Job.pg.locateOnScreen(URL + r"\K_TaisyouMenu.png", confidence=0.9)
                is None
            ):
                Job.time.sleep(1)
                # 顧問先情報変更ダイアログが表示されたら
                CDQ = Job.RPA.ImgCheck(
                    URL,
                    r"ChangeDataQ.png",
                    0.9,
                    10,
                )
                if CDQ[0] is True:
                    Job.pg.press("y")  # yで決定
                    # 顧問先情報取込メニューが表示されるまで待機--------------------------
                    while (
                        Job.RPA.ImgCheckForList(
                            URL,
                            [r"ChangeDataBtn.png", r"ChangeDataBtn2.png"],
                            0.9,
                            10,
                        )[0]
                        is False
                    ):
                        Job.time.sleep(1)
                    CDB = Job.RPA.ImgCheckForList(
                        URL,
                        [r"ChangeDataBtn.png", r"ChangeDataBtn2.png"],
                        0.9,
                        10,
                    )
                    Job.RPA.ImgClick(URL, CDB[1], 0.9, 10)  # 顧問先情報取込ボタンをクリック
            # --------------------------------------------------------------------
            if (
                Job.Start_Year < int(ThisYear) or Job.Start_Year - int(ThisYear) == 1
            ):  # 次年度更新か判定
                # IUD = IkkatuUpDate(FolURL, URL, Exc.row_data, driver)
                Job.time.sleep(3)
                Job.pg.keyDown("alt")
                Job.pg.press("x")
                Job.pg.keyUp("alt")
                # --------------------------------------------------------------------
                ME = Job.RPA.ImgCheckForList(
                    URL, [r"\MenuEnd.png", r"\MenuEnd2.png"], 0.9, 10
                )
                if ME[0] is True:
                    Job.RPA.ImgClick(URL, ME[1], 0.9, 10)  # 終了アイコンをクリック
                # --------------------------------------------------------------------
                # 閉じる処理--------------------------
                Job.pg.keyDown("alt")
                Job.pg.press("f4")
                Job.pg.keyUp("alt")
                # -----------------------------------
            elif Job.Start_Year == int(ThisYear):  # 次年度更新か判定
                # 閉じる処理--------------------------
                Job.pg.keyDown("alt")
                Job.pg.press("f4")
                Job.pg.keyUp("alt")
                # -----------------------------------
                IUD = "当年"
            else:
                # IUD = IkkatuUpDate(FolURL, URL, Exc.row_data, driver)
                Job.time.sleep(3)
                Job.pg.keyDown("alt")
                Job.pg.press("x")
                Job.pg.keyUp("alt")
                # --------------------------------------------------------------------
                ME = Job.RPA.ImgCheckForList(
                    URL, [r"\MenuEnd.png", r"\MenuEnd2.png"], 0.9, 10
                )
                if ME[0] is True:
                    Job.RPA.ImgClick(URL, ME[1], 0.9, 10)  # 終了アイコンをクリック
                # --------------------------------------------------------------------
                # 閉じる処理--------------------------
                Job.pg.keyDown("alt")
                Job.pg.press("f4")
                Job.pg.keyUp("alt")
                # -----------------------------------
                # Job.RPA.ImgClick(URL, r"\PrintOutTab.png", 0.9, 10)  # 2印刷タブクリック
                # # 6月次締めが表示されるまで待機--------------------------
                # while (
                #     Job.pg.locateOnScreen(URL + r"\SimeIcon.png", confidence=0.9)
                #     is None
                # ):
                #     Job.time.sleep(1)
                # Job.RPA.ImgClick(URL, r"\SimeIcon.png", 0.9, 10)  # その他メニュ-のアイコンをクリック
                # while (
                #     Job.pg.locateOnScreen(URL + r"\GetujiIcon.png", confidence=0.9)
                #     is None
                # ):
                #     Job.time.sleep(1)
                # Job.RPA.ImgClick(URL, r"\GetujiIcon.png", 0.9, 10)  # 月次処理アイコンをクリック
                # # 月次確定済みか判定して処理分け-------------------------------------------------------
                # # 月次処理解除-----------------------------------------------------------------------
                # KUL = Job.RPA.ImgCheck(
                #     URL, r"\KakuteUnLock.png", 0.9, 10
                # )  # 月次処理解除アイコンを検索
                # if KUL[0] is True:
                #     Job.RPA.ImgClick(
                #         URL, r"\KakuteUnLock.png", 0.9, 10
                #     )  # 月次処理アイコンをクリック
                #     Job.time.sleep(2)
                #     Job.pg.press("y")
                #     while (
                #         Job.pg.locateOnScreen(
                #             URL + r"\GetusjiKakutei.png", confidence=0.9
                #         )
                #         is None
                #     ):
                #         Job.time.sleep(1)
                #     Job.pg.press("return")
                #     Job.time.sleep(1)
                # # ---------------------------------------------------------------------------------
                Job.time.sleep(3)
                Job.pg.keyDown("alt")
                Job.pg.press("x")
                Job.pg.keyUp("alt")
                while (
                    Job.pg.locateOnScreen(URL + r"\M_Sonota.png", confidence=0.9)
                    is None
                ):
                    Job.time.sleep(1)
                Job.RPA.ImgClick(URL, r"\D_TourokuTAB.png", 0.9, 10)  # 6導入・登録タブクリック
                # 会社基本情報アイコンが表示されるまで待機--------------------------------------
                while (
                    Job.pg.locateOnScreen(URL + r"\CamIcon.png", confidence=0.9) is None
                ):
                    Job.time.sleep(1)
                Job.RPA.ImgClick(URL, r"\CamIcon.png", 0.9, 10)  # 会社基本情報アイコンをクリック
                # 顧問先情報取り込みアイコンが表示されるまで待機--------------------------------
                while (
                    Job.pg.locateOnScreen(URL + r"\DataInIcon.png", confidence=0.9)
                    is None
                ):
                    Job.time.sleep(1)
                Job.RPA.ImgClick(URL, r"\DataInIcon.png", 0.9, 10)  # 顧問先情報取り込みアイコンをクリック
                while (
                    Job.pg.locateOnScreen(URL + r"\DataInOK.png", confidence=0.9)
                    is None
                ):
                    Job.time.sleep(1)
                Job.RPA.ImgClick(URL, r"\DataInOK.png", 0.9, 10)  # 取り込むボタンをクリック
                Job.time.sleep(3)
                Job.pg.keyDown("alt")
                Job.pg.press("x")
                Job.pg.keyUp("alt")
                Job.time.sleep(1)
                # --------------------------------------------------------------------------------
                Job.RPA.ImgClick(URL, r"\PrintOutTab.png", 0.9, 10)  # 2印刷タブクリック
                # マスター更新------------------------------------------------------------------------
                Job.RPA.ImgClick(URL, r"\MasterUp.png", 0.9, 10)  # マスター更新をクリック
                while (
                    Job.RPA.ImgCheckForList(
                        URL,
                        [r"MasterUpStart.png", r"MasterUpStart2.png"],
                        0.9,
                        10,
                    )[0]
                    is True
                ):
                    Job.time.sleep(1)
                    TL = Job.RPA.ImgCheckForList(
                        URL,
                        [r"MasterUpStart.png", r"MasterUpStart2.png"],
                        0.9,
                        10,
                    )
                    Job.RPA.ImgClick(URL, TL[1], 0.9, 10)  # マスター更新開始をクリック
                    break
                Job.time.sleep(3)
                Job.pg.press("y")
                Job.time.sleep(3)
                Job.pg.press("return")
                Job.time.sleep(3)
                Job.pg.keyDown("alt")
                Job.pg.press("x")
                Job.pg.keyUp("alt")
                # 月次確定--------------------------------------------------------------------------
                # 月次確定アイコンが表示されるまで待機--------------------------
                while (
                    Job.pg.locateOnScreen(
                        URL + r"\AfterGetujiKakutei.png", confidence=0.9
                    )
                    is None
                ):
                    Job.time.sleep(1)
                Job.RPA.ImgClick(
                    URL, r"\AfterGetujiKakutei.png", 0.9, 10
                )  # 月次確定アイコンクリック
                KL = Job.RPA.ImgCheck(
                    URL, r"\KakuteiLock.png", 0.9, 10
                )  # 月次処理確定アイコンを検索
                if KL[0] is True:
                    while (
                        Job.pg.locateOnScreen(
                            URL + r"\KakuteiKaijyo.png", confidence=0.99999
                        )
                        is not None
                    ):
                        Job.RPA.ImgClick(
                            URL, r"\KakuteiKaijyo.png", 0.99999, 10
                        )  # 月次未確定チェックボックスをクリック
                        Job.time.sleep(1)
                    Job.RPA.ImgClick(
                        URL, r"\KakuteiLock.png", 0.9, 10
                    )  # 月次処理確定アイコンをクリック
                    Job.time.sleep(1)
                    Job.pg.press("y")
                    # ---------------------------------------------------------
                    while (
                        Job.pg.locateOnScreen(URL + r"\KessanKQ.png", confidence=0.9)
                        is None
                    ):
                        Job.time.sleep(1)
                        KessanKakuteiErr(FolURL, URL, Exc.row_data, driver)
                    # ---------------------------------------------------------
                Job.time.sleep(1)
                Job.pg.keyDown("alt")
                Job.pg.press("x")
                Job.pg.keyUp("alt")
                Job.RPA.ImgClick(URL, r"\M_Sonota.png", 0.9, 10)  # その他メニュ-のアイコンをクリック
                # 一括更新のアイコンが表示されるまで待機----------------------------------
                while (
                    Job.pg.locateOnScreen(URL + r"\IkkatsuKousin.png", confidence=0.9)
                    is None
                ):
                    Job.time.sleep(1)
                # --------------------------------------------------------------------
                Job.RPA.ImgClick(
                    URL, r"\IkkatsuKousin.png", 0.9, 10
                )  # その他メニュ-のアイコンをクリック
                # 一括更新メニューが表示されるまで待機------------------------------------
                while (
                    Job.pg.locateOnScreen(URL + r"\IkkatuOpenFlag.png", confidence=0.9)
                    is None
                ):
                    Job.time.sleep(1)
                    # UW = Job.RPA.ImgCheck(URL, r"\Underwindow.png", 0.9, 10)
                    # if UW[0] is True:
                    #     Job.RPA.ImgClick(URL, r"\Underwindow.png", 0.9, 10)
                    #     UW2 = Job.RPA.ImgCheck(URL, r"\Underwindow2.png", 0.9, 10)
                    #     if UW2[0] is True:
                    #         Job.RPA.ImgClick(URL, r"\Underwindow2.png", 0.9, 10)
                # --------------------------------------------------------------------
                Job.RPA.ImgClick(
                    URL, r"\IkkatuOpenFlag.png", 0.9, 10
                )  # 一括更新メニューのアイコンをクリック
                while (
                    Job.RPA.ImgCheckForList(
                        URL, [r"IkkatuFind.png", r"IkkatuFind2.png"], 0.9, 10
                    )[0]
                    is False
                ):
                    Job.time.sleep(1)
                FC = Job.RPA.ImgCheckForList(
                    URL,
                    [
                        r"IkkatuFind.png",
                        r"IkkatuFind2.png",
                    ],
                    0.9,
                    10,
                )
                if FC[0] is True:
                    Job.RPA.ImgClick(URL, FC[1], 0.9, 10)  # 一括更新メニューのアイコンをクリック
                    pyperclip.copy(str(Exc.row_data["関与先番号"]))
                    Job.pg.hotkey("ctrl", "v")
                    # 検索ボタンまでエンター-------------------------------------
                    while Job.RPA.ImgCheck(URL, r"FindFlag.png", 0.9, 10)[0] is False:
                        Job.time.sleep(1)
                        Job.pg.press("return")
                Job.pg.press("return")
                Job.time.sleep(1)
                Job.pg.press("space")
                # チェックマークが表示されるまで待機-------------------------------------
                while (
                    Job.RPA.ImgCheckForList(
                        URL,
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
                    Job.time.sleep(1)
                # --------------------------------------------------------------------
                Job.time.sleep(1)
                Job.RPA.ImgClick(URL, r"\IkkatuStart.png", 0.9, 10)  # 一括更新開始のアイコンをクリック
                # 確認ウィンドウが表示されるまで待機-------------------------------------
                while (
                    Job.pg.locateOnScreen(URL + r"\SakuseiQ.png", confidence=0.9)
                    is None
                ):
                    Job.time.sleep(1)
                # --------------------------------------------------------------------
                Job.pg.press("y")  # yで決定(nがキャンセル)
                # 確認ウィンドウが表示されるまで待機-------------------------------------
                while (
                    Job.pg.locateOnScreen(URL + r"\SakuseiQ2.png", confidence=0.9)
                    is None
                ):
                    Job.time.sleep(1)
                # --------------------------------------------------------------------
                Job.pg.press("return")  # 決定
                # 処理終了ウィンドウが表示されるまで待機----------------------------------
                while (
                    Job.pg.locateOnScreen(URL + r"\IkkatuEndFlag.png", confidence=0.9)
                    is None
                ):
                    Job.time.sleep(1)
                # --------------------------------------------------------------------
                Job.pg.press("return")  # 決定
                # チェックマークが表示されなくなるまで待機-------------------------------
                while (
                    Job.RPA.ImgCheckForList(
                        URL,
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
                    Job.time.sleep(1)
                # 一括更新のアイコンが表示されるまで待機----------------------------------
                while (
                    Job.pg.locateOnScreen(URL + r"\IkkatsuKousin.png", confidence=0.9)
                    is None
                ):
                    Job.time.sleep(1)
                    # --------------------------------------------------------------------
                    ME = Job.RPA.ImgCheckForList(
                        URL, [r"\MenuEnd.png", r"\MenuEnd2.png"], 0.9, 10
                    )
                    if ME[0] is True:
                        Job.RPA.ImgClick(URL, ME[1], 0.9, 10)  # 終了アイコンをクリック
                # --------------------------------------------------------------------
                # 閉じる処理--------------------------
                Job.pg.keyDown("alt")
                Job.pg.press("f4")
                Job.pg.keyUp("alt")
                # -----------------------------------
                # 会計大将フラグが表示されるまで待機-------------------------------------
                while (
                    Job.pg.locateOnScreen(URL + r"\Kaikei_CFlag.png", confidence=0.9)
                    is None
                ):
                    Job.time.sleep(1)
                    al4c = Job.RPA.ImgCheck(URL, r"\altf4Q.png", 0.9, 10)  # 終了確認が表示されたら
                    if al4c[0] is True:
                        Job.pg.press("y")  # yで決定(nがキャンセル)
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
    except:
        return False, "exceptエラー", "", ""


# ------------------------------------------------------------------------------------------------
def KessanKakuteiErr(Job, Exc):
    URL = Job.imgdir_url + r"\\KaikeiUpDate"

    Job.time.sleep(1)
    Job.pg.press("return")
    Job.time.sleep(1)

    p = Job.pg.locateOnScreen(URL + r"\KessanKey.png", confidence=0.9)  # 決算月の画像
    K_x, K_y = Job.pg.center(p)
    OverCount = 0
    while OverCount <= 6:
        try:
            # マスター更新後月次確定コメントがでたら
            MR = Job.RPA.ImgCheck(URL, r"\MasterRecalcQ2.png", 0.9, 10)
            if MR[0] is True:
                while Job.RPA.ImgCheck(URL, r"\GetusjiKakutei.png", 0.9, 10)[0] is True:
                    Job.time.sleep(1)
                Job.pg.press("return")
                Job.time.sleep(3)
                Job.pg.keyDown("alt")
                Job.pg.press("x")
                Job.pg.keyUp("alt")
                RPQ = Job.RPA.ImgCheck(URL, r"\Replace_Q.png", 0.9, 10)
                if RPQ[0] is True:
                    Job.pg.press("n")
                Job.time.sleep(1)
                # マスター更新------------------------------------------------------------------------
                Job.RPA.ImgClick(URL, r"\MasterUp.png", 0.9, 10)  # マスター更新をクリック
                while (
                    Job.RPA.ImgCheckForList(
                        URL,
                        [r"MasterUpStart.png", r"MasterUpStart2.png"],
                        0.9,
                        10,
                    )[0]
                    is True
                ):
                    Job.time.sleep(1)
                    TL = Job.RPA.ImgCheckForList(
                        URL,
                        [r"MasterUpStart.png", r"MasterUpStart2.png"],
                        0.9,
                        10,
                    )
                    Job.RPA.ImgClick(URL, TL[1], 0.9, 10)  # マスター更新開始をクリック
                    break
                Job.time.sleep(3)
                Job.pg.press("y")
                Job.time.sleep(3)
                Job.pg.press("return")
                Job.time.sleep(3)
                Job.pg.keyDown("alt")
                Job.pg.press("x")
                Job.pg.keyUp("alt")
                return "Master"
            else:
                p = Job.pg.locateOnScreen(URL + r"\UnsettledBox.png", confidence=0.8)
                x, y = Job.pg.center(p)
                try:
                    # 確定取消判定
                    ka_p = Job.pg.locateOnScreen(
                        URL + r"\UnsettledBox2.png", confidence=0.8
                    )
                    ka_x, ka_y = Job.pg.center(ka_p)
                    KakuteiFlag = True
                except:
                    KakuteiFlag = False

                if KakuteiFlag is False:
                    if y <= (K_y + (OverCount * 2)):  # チェックボックスが決算月より上なら
                        Job.pg.click(x, y)
                        BR = Job.RPA.ImgCheck(
                            URL, r"\BranceErr.png", 0.9, 10
                        )  # バランスエラーが表示されたら
                        if BR[0] is True:
                            return False
                    else:
                        OverCount += 1
                else:
                    if ka_y <= (K_y + (OverCount * 2)):  # チェックボックスが決算月より上なら
                        Job.pg.click(ka_x, ka_y)
                        BR = Job.RPA.ImgCheck(
                            URL, r"\BranceErr.png", 0.9, 10
                        )  # バランスエラーが表示されたら
                        if BR[0] is True:
                            return False
                    else:
                        OverCount += 1
        except:
            print("失敗")
            OverCount += 1
    GK = False
    Job.RPA.ImgClick(URL, r"\KakuteiLock.png", 0.9, 10)  # 月次処理確定アイコンをクリック
    Job.time.sleep(1)
    Job.pg.press("y")
    while Job.pg.locateOnScreen(URL + r"\KessanKQ.png", confidence=0.9) is None:
        if GK is True:
            break
        Job.time.sleep(2)
        Job.pg.press("y")
        while (
            Job.pg.locateOnScreen(URL + r"\GetusjiKakutei.png", confidence=0.9) is None
        ):
            Job.time.sleep(1)
            Job.pg.press("return")
            while (
                Job.pg.locateOnScreen(URL + r"\GetusjiKakutei.png", confidence=0.9)
                is None
            ):
                Job.time.sleep(1)
                Job.pg.press("return")
                GK = True
                break
        if GK is True:
            break

    return True
