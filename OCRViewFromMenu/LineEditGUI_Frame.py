import tkinter as tk

from PIL import Image, ImageTk
import customtkinter as ck

# from CV2Setting import straightlinesetting
from GCloudVision import AutoLine, LineTomlOut

# import ScrollableFrame as SF
# import tomlCreate as toml_c
from tkinter import filedialog, messagebox

from functools import wraps
import os
import MyTable as MT
import Functions
from pandastable import config

# 要素作成######################################################################################
def Frame1(self):
    # 配置
    # ボトムメニューフレーム##########################################################
    t_font = (1, int(8))

    Tframe = tk.Frame(
        self.bottumFrame,
        width=self.control.SideWidth,
        height=self.control.SideHeight,
        bg="#ecb5f5",
        relief=tk.GROOVE,
    )
    Tframe.pack(side=tk.LEFT, fill=tk.Y)  # , fill=tk.BOTH, expand=True)
    # LineNo表示テキスト
    ck.CTkLabel(
        master=Tframe,
        text="選択ライン名",
        width=self.control.Btn_width,
        height=self.control.Btn_height,
        corner_radius=8,
        text_font=t_font,
    ).grid(row=0, column=0, pady=5, sticky=tk.W)
    # テキストボックスの作成と配置
    self.Line_txt = ck.CTkEntry(
        master=Tframe,
        width=self.control.Btn_width,
        height=self.control.Btn_height,
        border_width=2,
        corner_radius=8,
        text_color="black",
        border_color="snow",
        fg_color="snow",
    )
    self.Line_txt.grid(row=0, column=1, pady=5, sticky=tk.W)
    # テキスト変換一致率
    ck.CTkLabel(
        master=Tframe,
        text="テキスト変換一致率",
        width=self.control.Btn_width,
        height=self.control.Btn_height,
        corner_radius=8,
        text_font=t_font,
    ).grid(row=1, column=0, pady=5, sticky=tk.W)
    # テキストボックスの作成と配置
    self.ChangeVar = ck.CTkEntry(
        master=Tframe,
        width=self.control.Btn_width,
        height=self.control.Btn_height,
        border_width=2,
        corner_radius=8,
        text_color="black",
        border_color="snow",
        fg_color="snow",
    )
    self.ChangeVar.insert(0, 50)
    self.ChangeVar.grid(row=1, column=1, pady=5, sticky=tk.W)
    # 行数表示テキスト
    ck.CTkLabel(
        master=Tframe,
        text="設定ファイル",
        width=self.control.Btn_width,
        height=self.control.Btn_height,
        corner_radius=8,
        text_font=t_font,
    ).grid(row=3, column=0, pady=5, sticky=tk.W)
    self.tomlurl = ck.CTkEntry(
        master=Tframe,
        width=int(self.control.Btn_width * 1.5),
        height=self.control.Btn_height,
        border_width=2,
        corner_radius=8,
        text_color="black",
        border_color="snow",
        fg_color="snow",
    )
    self.tomlurl.insert(0, self.control.tomlurl)
    self.tomlurl.grid(row=3, column=1, pady=5, sticky=tk.W)
    # 行数表示テキスト
    # 設定ファイル変更ボタン--------------------------------------------------------
    self.tomlbutton = ck.CTkButton(
        master=Tframe,
        text="設定ファイル変更",
        command=self.ChangeToml,
        width=int(self.control.Btn_width * 1.5),
        height=self.control.Btn_height,
        border_width=2,
        corner_radius=8,
        text_color="snow",
        border_color="snow",
    )
    self.tomlbutton.grid(row=4, column=1, columnspan=2, sticky=tk.W)


# ------------------------------------------------------------------------------------
def Frame2(self):
    # ボトムメニュー内フレーム2########################################################
    Tframe2 = tk.Frame(
        self.bottumFrame,
        width=self.control.SideWidth,
        height=self.control.SideHeight,
        bg="#ecb5f5",
        relief=tk.GROOVE,
    )
    Tframe2.pack(side=tk.LEFT, fill=tk.Y)  # , fill=tk.BOTH, expand=True)
    create_table(
        self,
        Tframe2,
        "各列指定",
        self.control.SettingCsvurl,
        int(self.control.width_of_window / 5),
        int(self.control.height_of_window / 10),
    )
    create_table(
        self,
        Tframe2,
        "列名変換",
        self.control.SettingCsvurl_column,
        int(self.control.width_of_window / 8),
        int(self.control.height_of_window / 10),
    )


# ------------------------------------------------------------------------------------
def Frame3(self):
    # ボトムメニュー内ボタンフレーム3###################################################
    Tframe3 = tk.Frame(
        self.bottumFrame,
        width=self.control.SideWidth,
        height=self.control.SideHeight,
        bg="#ecb5f5",
        relief=tk.GROOVE,
    )
    Tframe3.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    # 自動直線描画ボタン---------------------------------------------------------------
    button3 = ck.CTkButton(
        master=Tframe3,
        text="自動直線描画",
        command=lambda: AutoNewLineCreate(self.top.forward, 400, 400),
        width=self.control.Btn_width,
        height=self.control.Btn_height,
        border_width=2,
        corner_radius=8,
        text_color="snow",
        border_color="snow",
        fg_color="#2b5cff",
    )
    button3.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W + tk.E)
    # 削除ボタン---------------------------------------------------------------
    button5 = ck.CTkButton(
        master=Tframe3,
        text="全直線削除",
        command=lambda: AllLineDelete(self, self.top.forward),
        width=self.control.Btn_width,
        height=self.control.Btn_height,
        border_width=2,
        corner_radius=8,
        text_color="snow",
        border_color="snow",
        fg_color="Orange",
    )
    button5.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W + tk.E)
    # # 新規直線描画ボタン---------------------------------------------------------------
    # button3 = ck.CTkButton(
    #     master=frame2,
    #     text="新規直線描画",
    #     command=lambda: NewLineCreate(self, self.top.forward, HCW, HCH),
    #     width=self.control.Btn_width,
    #     height=self.control.Btn_height,
    #     border_width=2,
    #     corner_radius=8,
    #     text_color="snow",
    #     border_color="snow",
    #     fg_color="mediumPurple",
    # )
    # button3.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W + tk.E)
    # 確定ボタン---------------------------------------------------------------
    button4 = ck.CTkButton(
        master=Tframe3,
        text="確定",
        command=lambda: EnterP(
            self.top.forward, HCW, HCH, self, self.master, self.top, self.ChangeVar
        ),
        width=self.control.Btn_width,
        height=self.control.Btn_height,
        border_width=2,
        corner_radius=8,
        text_color="snow",
        border_color="snow",
        fg_color="steelblue3",
    )
    button4.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W + tk.E)


# ------------------------------------------------------------------------------------
def create_table(self, frame, t_title, csvurl, wid, hei):
    """
    csv読込テーブル
    arg:self
    arg:tk.frame
    arg:str(title)
    arg:str(csvurl)
    return:tk.Frame
    """
    # ツリーフレーム設定---------------------------------------------------------------------
    f = tk.Frame(
        frame,
        width=wid,
        height=hei,
        bd=2,
        bg="#fce4d2",
        relief=tk.RIDGE,
    )  # 親フレーム
    # self.OCR_frame.grid(row=0, column=0, sticky=tk.N + tk.S + tk.W + tk.E)
    f.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    f_tree = tk.Frame(
        f,
        width=wid,
        height=hei,
        bg="#fce4d2",
    )  # 子フレーム
    # サイズグリップ
    # sizegrip = ttk.Sizegrip(self.OCR_frame)
    # sizegrip.grid(row=0, column=0, sticky=(tk.S, tk.E))
    tk.Label(f, text=t_title, bg="#fce4d2").grid(
        row=0, column=0, sticky=tk.N + tk.W
    )  # 位置指定

    # self.pt_bln = tk.BooleanVar()
    # self.pt_bln.set(False)
    # self.pt_chk = tk.Checkbutton(
    #     self.OCR_frame,
    #     bg="#fce4d2",
    #     text="変更を記録する",
    #     command=lambda: self.chk_click(self.pt_bln),
    # )
    # self.pt_chk.grid(row=1, column=0, sticky=tk.N + tk.W)

    f_tree.grid(row=2, column=0, padx=30, sticky=tk.N + tk.S + tk.W + tk.E)
    # df = TableModel.getSampleData()
    # pt = Table(self.tree_frame)
    pt = MT.MyTable(
        f_tree,
        width=wid,
        height=hei,
        sticky=tk.N + tk.S + tk.W + tk.E,
    )  # テーブルをサブクラス化
    enc = Functions.getFileEncoding(csvurl)
    pt.importCSV(csvurl, encoding=enc)
    pt._name = t_title
    # options is a dict that you can set yourself
    options = {"fontsize": self.control.t_font[1]}
    config.apply_options(options, pt)
    # DF型変換------------------------------
    Functions.Pandas_mem_usage(pt.model.df)
    # --------------------------------------
    pt.resized
    pt.show()
    return f


# ------------------------------------------------------------------------------------
def AutoNewLineCreate(self, selfC, HCW, HCH):
    """
    自動直線描画ボタン処理
    """
    unmap(self)
    MSG = messagebox.askokcancel("確認", "自動直線描画しますか？")
    if MSG is True:

        selfC = self.top.forward
        AL = AutoLine(self.control.imgurl, 1)
        if AL[0] is True:
            ####################################################################################
            F_N = os.path.splitext(os.path.basename(self.control.imgurl))[0]
            Yoko_N = F_N + "_Yoko"
            Tate_N = F_N + "_Tate"
            AL[1].sort()
            AL[2].sort(key=lambda x: x[1])
            self.tomlsetting["LineSetting"][Yoko_N] = AL[1]
            self.tomlsetting["LineSetting"][Tate_N] = AL[2]
            Functions.dump_toml(self.tomlsetting, self.control.tomlurl)
            ####################################################################################
            AllLineDelete(self, selfC)
            self.Transparent_Create()  # 透過キャンバスに罫線描画

            MSG = messagebox.showinfo("確認", "自動直線描画完了")
            map(self)
        else:
            MSG = messagebox.showinfo("確認", "自動直線描画に失敗しました。")
    else:
        map(self)


# ---------------------------------------------------------------------------------------------
def AllLineDelete(self, selfC):
    """
    選択直線の削除
    """
    global tagsList
    r = len(tagsList) - 1
    selfC.delete("all")
    for tagsListItem in reversed(tagsList):
        selfC.delete(tagsListItem[0][0])
        tagsList.pop(r)
        r -= 1


# ---------------------------------------------------------------------------------------------
def EnterP(self, HCW, HCH, selfmother, Mter, Top, ChangeVar):
    """
    確定ボタンクリック
    """
    global tagsList
    global MaxW, MaxH

    FList = []
    FYokoList = []
    FTateList = []
    SGEL = selfmother.GetEntryTextButton_click()  # OCR出力列名
    # 条件テキストボックスの値格納---------------------------
    DaySet = selfmother.DaySet.get()
    MoneySet = selfmother.MoneySet.get()
    # ReplaceSet = selfmother.ReplaceSet.get()
    # ReplaceStr = selfmother.ReplaceStr.get()
    # ------------------------------------------------------
    # 条件テキストボックスのリスト化---------------------------
    if "," in DaySet:
        DaySet = DaySet.split(",")
    elif " " in DaySet:
        DaySet = DaySet.split(" ")
    else:
        DaySet = list(DaySet)
    # --------------------------------------------------------
    if "," in MoneySet:
        MoneySet = MoneySet.split(",")
    elif " " in MoneySet:
        MoneySet = MoneySet.split(" ")
    else:
        MoneySet = list(MoneySet)
    # 条件テキストボックスの内容で処理分け-------------------------------------------------------------------
    if listintCheck(DaySet) is False:
        unmap(selfmother)
        messagebox.showinfo("エラー", "日付列番号が不正です。数値以外を指定していないか確認してください。")
        map(selfmother)
    elif listintCheck(MoneySet) is False:
        unmap(selfmother)
        messagebox.showinfo("エラー", "金額表示列番号が不正です。数値以外を指定していないか確認してください。")
        map(selfmother)
    # elif listintCheck(ReplaceSet) is False:
    #     messagebox.showinfo("エラー", "置換対象列番号が不正です。数値以外を指定していないか確認してください。")
    else:
        if len(tagsList) == 0:
            unmap(selfmother)
            messagebox.showinfo("エラー", "軸が設定されていません。")
            map(selfmother)
        else:
            for tagsListItem in tagsList:
                BB = self.bbox(tagsListItem[0][0])
                try:
                    BBS = [BB[0], BB[1], BB[2], BB[3]]
                    FList.append([tagsListItem[0], tagsListItem[1], BBS])
                except:
                    print("BBSErr")
            ###################################################################################
            ###################################################################################
            ###################################################################################
            ###################################################################################
            ###################################################################################
            ###################################################################################
            ###################################################################################
            ###################################################################################
            ###################################################################################
            ###################################################################################
            ###################################################################################
            ###################################################################################
            ###################################################################################
            ###################################################################################
            for FListItem in FList:
                # FSSC1 = round((FListItem[1][0] + FListItem[2][0]) / HCW)
                # FSSC2 = round((FListItem[1][1] + FListItem[2][1]) / HCH)
                # FSSC3 = round((FListItem[1][2] + FListItem[2][2]) / HCW)
                # FSSC4 = round((FListItem[1][3] + FListItem[2][3]) / HCH)
                if FListItem[2][0] < 0:
                    FSSC1 = 0
                else:
                    FSSC1 = int(round((FListItem[2][0] / HCW), 0))
                if FListItem[2][1] < 0:
                    FSSC2 = 0
                else:
                    FSSC2 = int(round((FListItem[2][1] / HCH), 0))
                if FListItem[2][2] < 0:

                    FSSC3 = 0
                else:
                    FSSC3 = int(round((FListItem[2][0] / HCW), 0))
                if FListItem[2][3] < 0:
                    FSSC4 = 0
                else:
                    FSSC4 = int(round((FListItem[2][1] / HCH), 0))
                # FSSC1 = FListItem[0][1] / HCW
                # FSSC2 = FListItem[0][2] / HCH
                # FSSC3 = FListItem[0][3] / HCW
                # FSSC4 = FListItem[0][4] / HCH
                if FSSC1 < 0 and FSSC1 < MaxW:
                    FSSC1 = 0
                elif FSSC1 > MaxW:
                    FSSC1 = MaxW
                if FSSC2 < 0 and FSSC2 < MaxH:
                    FSSC2 = 0
                elif FSSC2 > MaxH:
                    FSSC2 = MaxH
                if FSSC3 < 0 and FSSC3 < MaxW:
                    FSSC3 = 0
                elif FSSC3 > MaxW:
                    FSSC3 = MaxW
                if FSSC4 < 0 and FSSC4 < MaxH:
                    FSSC4 = 0
                elif FSSC4 > MaxH:
                    FSSC4 = MaxH
                FSS = [FSSC1, FSSC2, FSSC3, FSSC4]
                if FListItem[0][5] == "Yoko":
                    FYokoList.append(FSS)
                else:
                    FTateList.append(FSS)
                print(FSS)
            if len(FTateList) == 0:
                unmap(selfmother)
                messagebox.showinfo("エラー", "横軸が設定されていません。")
                map(selfmother)
            elif len(FYokoList) == 0:
                unmap(selfmother)
                messagebox.showinfo("エラー", "縦軸が設定されていません。")
                map(selfmother)
            else:
                # メッセージボックス（OK・キャンセル）
                unmap(selfmother)
                if len(FYokoList) == len(SGEL):
                    # --------------------------------------------------------------
                    if Master.HeaderCol_c == len(SGEL) or Master.HeaderCol_c == 0:
                        try:
                            ChangeVar = int(ChangeVar.get())
                        except:
                            MSG = messagebox.showinfo("エラー", "テキスト変換一致率に数値以外が入力されています。")
                            map(selfmother)
                            return
                        MSG = messagebox.askokcancel("確認", str(SGEL) + "の列名で出力します。")
                        if MSG is True:
                            map(selfmother)
                            PBAR = PB.Open(tk.Toplevel())  # サブWindow作成
                            ####################################################################################
                            F_N = os.path.splitext(os.path.basename(imgurl))[0]
                            Yoko_N = F_N + "_Yoko"
                            Tate_N = F_N + "_Tate"
                            FYokoList.sort()
                            FTateList.sort(key=lambda x: x[1])
                            Banktoml["LineSetting"][Yoko_N] = FYokoList
                            Banktoml["LineSetting"][Tate_N] = FTateList
                            toml_c.dump_toml(Banktoml, tomlurl)
                            ####################################################################################
                            print("csv保存完了")
                            OM = OCRF.Main(
                                imgurl,
                                FYokoList,
                                FTateList,
                                Banktoml,
                                SGEL,
                                DaySet,
                                MoneySet,
                                "ReplaceSet",
                                "ReplaceStr",
                                ChangeVar,
                            )
                            if OM[0] is True:
                                Read_Url = str(OM[1])
                                PBAR._target.step(10)
                                PBAR._target.master.destroy()

                                unmap(selfmother)
                                MSG = messagebox.showinfo(
                                    "抽出完了", Read_Url + "_に保存しました。"
                                )
                                MSG = messagebox.askokcancel(
                                    "確認", "次ページ読込を行いますか？\nキャンセルで比較ウィンドウを起動します。"
                                )
                                if MSG is True:
                                    Master.HeaderCol_c = len(SGEL)
                                    if "抽出文字列" in SGEL:
                                        Master.HeaderCol_c = Master.HeaderCol_c - 1
                                    if "抽出数値" in SGEL:
                                        Master.HeaderCol_c = Master.HeaderCol_c - 1

                                    FUL.append(Read_Url)  # 書出しCSVURLリスト
                                    ReturnBack(selfmother)
                                else:
                                    FUL.append(Read_Url)  # 書出しCSVURLリスト
                                    if len(FUL) == 1:
                                        selfmother.top.withdraw()  # 透過ウィンドウ最小化
                                        selfmother.master.withdraw()  # 下ウィンドウ最小化

                                        PT.Main(
                                            self,
                                            Read_Url,
                                            G_logger,
                                            Mter,
                                            Top,
                                            imgurl,
                                            Banktoml,
                                            tomlurl,
                                        )
                                    else:
                                        RU = OCRF.JoinCSV(FUL)
                                        if RU[0] is True:
                                            Read_Url = RU[1]
                                            selfmother.top.withdraw()  # 透過ウィンドウ最小化
                                            selfmother.master.withdraw()  # 下ウィンドウ最小化

                                            PT.Main(
                                                self,
                                                Read_Url,
                                                G_logger,
                                                Mter,
                                                Top,
                                                imgurl,
                                                Banktoml,
                                                tomlurl,
                                            )
                                        else:
                                            print("")
                            else:

                                unmap(selfmother)
                                MSG = messagebox.showinfo("抽出失敗", "エラーにより抽出に失敗しました。")
                                map(selfmother)
                        else:

                            messagebox.showinfo("中断", "処理を中断します。")
                            map(selfmother)
                    else:

                        messagebox.showinfo("エラー", "先頭ページの列数と設定列名の数が一致しません。再確認してください。")
                        map(selfmother)
                else:

                    messagebox.showinfo("確認", "縦軸数と設定列名の数が一致しません。再確認してください。")
                    map(selfmother)


# ---------------------------------------------------------------------------------------------
def unmap(self):
    """
    最上部ウィンドウを非表示
    """
    self.top.withdraw()


# ---------------------------------------------------------------------------------------------
def map(self):
    """
    self.topを最上部へ
    """
    self.lift()
    self.top.wm_deiconify()
    self.top.attributes("-topmost", True)
