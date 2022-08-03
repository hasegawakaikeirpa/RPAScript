import tkinter as tk
import tkinter.ttk as ttk
import numpy as np

# from tkinter import messagebox
import pandas as pd
import os
import csv
import toml
import MyTable as MT
import MyTable2 as MT2
import MyTable3 as MT3
import AutoJournal as AJ
import CSVOut as CSVO
import TKEntry as tke


class DataGrid:
    def __init__(self, window_root, default_path):
        global csvurl, Banktoml, AJurl, AJSeturl, Roolurl, tomltitle

        # toml読込------------------------------------------------------------------------------
        self.Banktoml = Banktoml
        # -----------------------------------------------------------
        self.FileName = csvurl
        self.JounalFileName = AJurl
        self.Roolurl = Roolurl
        self.tomlList = self.Banktoml["ParList"]["Name"]
        self.HidukeColNo = self.Banktoml[tomltitle]["HidukeColNo"]
        self.MoneyCol = self.Banktoml[tomltitle]["MoneyCol"]
        self.ChangeTextCol = self.Banktoml[tomltitle]["ChangeTextCol"]
        self.ColumnName = self.Banktoml[tomltitle]["ColumnName"]
        self.HidukeColName = self.Banktoml[tomltitle]["HidukeColName"]
        self.NyuName = self.Banktoml[tomltitle]["NyuName"]
        self.SyutuName = self.Banktoml[tomltitle]["SyutuName"]
        self.ZanName = self.Banktoml[tomltitle]["ZanName"]
        self.Henkan = self.Banktoml[tomltitle]["Henkan"]
        self.ChangeText = self.Banktoml[tomltitle]["ChangeText"]
        # ------------------------------------
        # self.CsvHeader()
        # メインウィンドウ設定-------------------------------------------------------------------
        self.root = tk.Tk()  # ウインド画面の作成
        self.root.geometry("1400x750")  # 画面サイズの設定
        self.root.title("OCRTEXT")  # 題名
        # -------------------------------------------------------------------------------------
        # メインフレーム設定--------------------------------------------------------------------
        self.Mframe = tk.Frame(self.root, bd=2, relief=tk.RIDGE)
        self.Mframe.grid(row=1, column=0, sticky=tk.W)
        # -------------------------------------------------------------------------------------
        # フレーム設定--------------------------------------------------------------------------
        self.frame3 = tk.Frame(self.Mframe, bd=2, relief=tk.RIDGE)
        self.frame3.grid(row=0, column=0, sticky=tk.N)
        # -------------------------------------------------------------------------------------
        # フレーム設定--------------------------------------------------------------------------
        self.frame4 = tk.Frame(self.Mframe, bd=2, relief=tk.RIDGE)
        self.frame4.grid(row=0, column=1, sticky=tk.N)
        # -------------------------------------------------------------------------------------
        # フレーム設定--------------------------------------------------------------------------
        self.frame6 = tk.Frame(self.Mframe, bd=2, relief=tk.RIDGE)
        self.frame6.grid(row=0, column=2, sticky=tk.N)
        # MotoCyou------------------------------------------------------------------------------
        # フレーム設定--------------------------------------------------------------------------
        self.frame7 = tk.Frame(self.Mframe, bd=2, relief=tk.RIDGE)
        self.frame7.grid(row=0, column=3, sticky=tk.N)
        self.frame7EntryList = []  # このフレームのEntryのインスタンス
        # -------------------------------------------------------------------------------------
        tk.Label(self.frame6, text="元帳日付列名").grid(row=0, column=0)  # 位置指定
        self.Moto_Day = tk.Entry(self.frame6, width=10)
        self.Moto_Day.insert(0, "元帳日付列名")
        self.Moto_Day.grid(row=0, column=1)
        # ---------------------------------------------------------------------------------------
        tk.Label(self.frame6, text="元帳金額列名").grid(row=1, column=0)  # 位置指定
        self.Moto_Money = tk.Entry(self.frame6, width=10)
        self.Moto_Money.insert(0, "元帳金額列名")
        self.Moto_Money.grid(row=1, column=1)
        # ---------------------------------------------------------------------------------------
        tk.Label(self.frame6, text="元帳摘要列名").grid(row=2, column=0)  # 位置指定
        self.Moto_Tekiyou = tk.Entry(self.frame6, width=10)
        self.Moto_Tekiyou.insert(0, "元帳摘要列名")
        self.Moto_Tekiyou.grid(row=2, column=1)
        # ---------------------------------------------------------------------------------------
        tk.Label(self.frame6, text="元帳借方科目列名").grid(row=3, column=0)  # 位置指定
        self.Moto_Karikata = tk.Entry(self.frame6, width=10)
        self.Moto_Karikata.insert(0, "（借）科目名")
        self.Moto_Karikata.grid(row=3, column=1)
        # ---------------------------------------------------------------------------------------
        tk.Label(self.frame6, text="元帳貸方科目列名").grid(row=4, column=0)  # 位置指定
        self.Moto_Kashikata = tk.Entry(self.frame6, width=10)
        self.Moto_Kashikata.insert(0, "（貸）科目名")
        self.Moto_Kashikata.grid(row=4, column=1)
        # ---------------------------------------------------------------------------------------
        # 選択行自動仕訳作成ボタン----------------------------------------------------------------
        self.AJ_Btn = tk.Button(
            self.frame6,
            text="選択行自動仕訳作成",
            width=20,
            command=lambda: self.AJCalc(csvurl),
            bg="lightblue",
        )
        self.AJ_Btn.grid(row=5, column=0, columnspan=2)  # 位置指定
        # -------------------------------------------------------------------------------------
        # 抽出仕訳転記ボタン----------------------------------------------------------------
        self.AJ_copy = tk.Button(
            self.frame6,
            text="抽出仕訳転記",
            width=20,
            command=lambda: self.AJ_copyCalc(csvurl),
            bg="pink",
        )
        self.AJ_copy.grid(row=6, column=0, columnspan=2)  # 位置指定
        # -------------------------------------------------------------------------------------
        # 置換設定追加ボタン----------------------------------------------------------------
        self.AJ_set = tk.Button(
            self.frame7,
            text="置換設定追加",
            width=20,
            command=lambda: tke.AJ_setCalc(self),
            bg="yellow",
        )
        self.AJ_set.grid(row=0, column=0, columnspan=2)  # 位置指定
        # -------------------------------------------------------------------------------------
        # フレーム設定--------------------------------------------------------------------------
        self.frame5 = tk.Frame(self.root, width=650)
        self.frame5.grid(row=1, column=1, sticky=tk.W)
        # -------------------------------------------------------------------------------------
        # ツリーフレーム設定---------------------------------------------------------------------
        self.tree_frame = tk.Frame(self.root, width=650, height=500)
        self.tree_frame.grid(row=0, column=0, sticky=tk.N + tk.S + tk.W + tk.E)
        # df = TableModel.getSampleData()
        # pt = Table(self.tree_frame)
        pt = MT.MyTable(
            self.tree_frame, width=650, height=500, sticky=tk.N + tk.S + tk.W + tk.E
        )  # テーブルをサブクラス化
        enc = CSVO.getFileEncoding(csvurl)
        self.table = pt.importCSV(csvurl, encoding=enc)
        self.pt = pt
        pt.show()
        # -------------------------------------------------------------------------------------
        # ツリーフレーム設定---------------------------------------------------------------------
        self.tree2_frame = tk.Frame(self.root, width=650, height=500)
        self.tree2_frame.grid(
            row=0, column=1, columnspan=2, sticky=tk.N + tk.S + tk.W + tk.E
        )
        # df = TableModel.getSampleData()
        # pt2 = Table(self.tree2_frame)
        pt2 = MT2.MyTable(
            self.tree2_frame, width=650, height=500, sticky=tk.N + tk.S + tk.W + tk.E
        )  # テーブルをサブクラス化
        enc = CSVO.getFileEncoding(AJurl)
        self.table2 = pt2.importCSV(AJurl, encoding=enc)
        self.pt2 = pt2
        # MotoCyou------------------------------------------------------------------------------
        enc = CSVO.getFileEncoding(Roolurl)
        AJ_np = np.genfromtxt(
            Roolurl, dtype=None, encoding=enc, delimiter=","
        )  # 元帳CSVをnp配列に変換
        AJ_Column = AJ_np[0, :]
        A = 0
        for AJ_Item in AJ_Column:
            if "日付" in AJ_Item:
                self.Moto_Day.delete(0, tk.END)
                self.Moto_Day.insert(0, AJ_Item.replace("'", "").replace('"', ""))
                self.Moto_Day_No = A
            elif "金額" in AJ_Item:
                self.Moto_Money.delete(0, tk.END)
                self.Moto_Money.insert(0, AJ_Item.replace("'", "").replace('"', ""))
                self.Moto_Money_No = A
            elif "摘要" in AJ_Item:
                self.Moto_Tekiyou.delete(0, tk.END)
                self.Moto_Tekiyou.insert(0, AJ_Item.replace("'", "").replace('"', ""))
                self.Moto_Tekiyou_No = A
            A += 1
        # ---------------------------------------------------------------------------------------
        pt2.show()
        # -------------------------------------------------------------------------------------
        # ツリービューを配置
        tke.treeviewEntries(self, tomltitle)
        # ボタン追加----------------------------------------------------------------------------
        self.AllRun = tk.Button(
            self.frame3,
            text="全行自動仕訳",
            bg="lightgreen",
            width=20,
            command=lambda: self.AJAllCalc(csvurl),
        )
        self.AllRun.grid(row=4, column=0, columnspan=2)  # 位置指定
        # -------------------------------------------------------------------------------------
        # tomlListを配置
        tke.tomlEntries(self, tomltitle)
        # フレーム7を配置
        tke.Frame7Entries(self)

    #############################################################################################
    # 以下self関数
    #############################################################################################
    def AJ_copyCalc(self, csvurl):
        try:
            if self.pt3.startrow is None:
                tk.messagebox.showinfo("確認", "抽出仕訳表のセルが選択されていません。")
            else:
                if self.pt.startrow is None:
                    tk.messagebox.showinfo("確認", "OCR表のセルが選択されていません。")
                else:
                    # 自動仕訳保存配列の行数判定------------------------------------------
                    d2_r = len(self.pt2.model.df)
                    if self.pt.startrow + 1 > d2_r:
                        # 各配列をDataFrameに------------------------------------------------
                        dfs = self.pt.model.df  # グリッドをDF化
                        dfsrow = dfs.iloc[self.pt.startrow]  # DF行データ
                        dfs2 = self.pt2.model.df  # グリッドをDF化
                        dfs3 = self.pt3.model.df  # グリッドをDF化
                        # ------------------------------------------------------------------
                        dfs3row = dfs3.iloc[self.pt3.startrow]  # DF行データ
                        CF_df = tke.AJ_copyCalc_Func(dfsrow, dfs3row)  # 自動仕訳抽出
                        CF_df = list(np.array(CF_df))  # list化
                        C_dfColumn = np.array(dfs2.columns)  # DFColumnをnumpy配列へ
                        dfs2 = np.array(dfs2)  # 自動仕訳保存配列をnumpy配列へ
                        dfs2 = np.insert(
                            dfs2, dfs2.shape[0], CF_df, axis=0
                        )  # 末尾へデータ行追加
                        Last_List = np.vstack((C_dfColumn, dfs2))  # 列名リストを縦連結
                        Last_List.astype(str)  # numpy配列型変換
                        Last_List = list(Last_List)  # numpy配列list型変換
                        print(Last_List)
                        # データ内のFalse,nan処理--------------------------------------------
                        for L_r in range(len(Last_List)):
                            if L_r == 0:  # ヘッダー行処理
                                for L_c in range(len(Last_List[L_r])):
                                    print(Last_List[L_r][L_c])
                                    if "Unnamed" in Last_List[L_r][L_c]:
                                        Last_List[L_r][L_c] = ""
                                    if "." in Last_List[L_r][L_c]:
                                        S_txt = Last_List[L_r][L_c].split(".")
                                        Last_List[L_r][L_c] = S_txt[0]
                            else:  # ヘッダー行以外処理
                                for L_c in range(len(Last_List[L_r])):
                                    print(Last_List[L_r][L_c])
                                    if bool(Last_List[L_r][L_c]) is False:
                                        Last_List[L_r][L_c] = ""
                                    if (
                                        Last_List[L_r][L_c] == Last_List[L_r][L_c]
                                        and Last_List[L_r][L_c] is not False
                                    ):
                                        print("")
                                    else:
                                        Last_List[L_r][L_c] = ""
                        # ------------------------------------------------------------------
                        with open(AJurl, "wt", encoding="cp932", newline="") as fout:
                            # ライター（書き込み者）を作成
                            writer = csv.writer(fout)
                            writer.writerows(Last_List)
                        self.pt2.redraw()
                    else:
                        # 各配列をDataFrameに------------------------------------------------
                        dfs = self.pt.model.df  # グリッドをDF化
                        dfsrow = dfs.iloc[self.pt.startrow]  # DF行データ
                        dfs2 = self.pt2.model.df  # グリッドをDF化
                        dfs3 = self.pt3.model.df  # グリッドをDF化
                        # ------------------------------------------------------------------
                        dfs3row = dfs3.iloc[self.pt3.startrow]  # DF行データ
                        CF_df = tke.AJ_copyCalc_Func(dfsrow, dfs3row)  # 自動仕訳抽出
                        CF_df = list(np.array(CF_df))  # list化
                        C_dfColumn = np.array(dfs2.columns)  # DFColumnをnumpy配列へ
                        dfs2 = np.array(dfs2)  # 自動仕訳保存配列をnumpy配列へ
                        dfs2 = np.insert(
                            dfs2, self.pt.startrow + 1, CF_df, axis=0
                        )  # 末尾へデータ行追加
                        Last_List = np.vstack((C_dfColumn, dfs2))  # 列名リストを縦連結
                        Last_List.astype(str)  # numpy配列型変換
                        Last_List = list(Last_List)  # numpy配列list型変換
                        print(Last_List)
                        # データ内のFalse,nan処理--------------------------------------------
                        for L_r in range(len(Last_List)):
                            if L_r == 0:  # ヘッダー行処理
                                for L_c in range(len(Last_List[L_r])):
                                    print(Last_List[L_r][L_c])
                                    if "Unnamed" in Last_List[L_r][L_c]:
                                        Last_List[L_r][L_c] = ""
                                    if "." in Last_List[L_r][L_c]:
                                        S_txt = Last_List[L_r][L_c].split(".")
                                        Last_List[L_r][L_c] = S_txt[0]
                            else:  # ヘッダー行以外処理
                                for L_c in range(len(Last_List[L_r])):
                                    print(Last_List[L_r][L_c])
                                    if bool(Last_List[L_r][L_c]) is False:
                                        Last_List[L_r][L_c] = ""
                                    if (
                                        Last_List[L_r][L_c] == Last_List[L_r][L_c]
                                        and Last_List[L_r][L_c] is not False
                                    ):
                                        print("")
                                    else:
                                        Last_List[L_r][L_c] = ""
                        # ------------------------------------------------------------------
                        with open(AJurl, "wt", encoding="cp932", newline="") as fout:
                            # ライター（書き込み者）を作成
                            writer = csv.writer(fout)
                            writer.writerows(Last_List)
                        self.pt2.redraw()
        except:
            tk.messagebox.showinfo("確認", "エラーです。自動仕訳実行後に抽出仕訳表のセルを選択し、実行してください。")

    # -----------------------------------------------------------------------------------------
    def AJAllCalc(self, csvurl):
        global AJSeturl
        self.FileName = csvurl
        self.JounalFileName = AJurl
        self.Roolurl = Roolurl

        st = 0  # 行ポジション
        for stom in self.entryList:  # Entryウィジェットリスト
            if stom == "自動仕訳基準列名":
                JS_var = st
            elif stom == "日付列名":
                Day_var = st
            elif stom == "入金列名":
                In_var = st
            elif stom == "出金列名":
                Out_var = st
            st += 1
        FileNameenc = CSVO.getFileEncoding(csvurl)
        JounalFileNameenc = CSVO.getFileEncoding(AJurl)
        Roolurlenc = CSVO.getFileEncoding(Roolurl)
        # Entry要素設定-------------------------------------------------------------------
        JS = self.tomlEntries[JS_var].get()  # 自動仕訳基準列名Entry取得
        D = self.tomlEntries[Day_var].get()  # 日付列Entry取得
        I = self.tomlEntries[In_var].get()  # 入金列名Entry取得
        O = self.tomlEntries[Out_var].get()  # 出金列名Entry取得
        # --------------------------------------------------------------------------------
        AJ_List = AJ.AllChange(
            JS,
            self.HidukeColName,
            self.Moto_Day.get(),
            self.Moto_Money_No,
            self.Moto_Karikata.get(),
            self.Moto_Kashikata.get(),
            self.FileName,
            FileNameenc,
            self.JounalFileName,
            JounalFileNameenc,
            self.Roolurl,
            Roolurlenc,
            self.Banktoml,
            self.Label_ChangeURL.get(),
            I,
            O,
        )  # 仕訳候補を抽出

        PT_ColList = list(self.pt.model.df.columns)  # OCR表の列名リスト
        PT_List = np.array(self.pt.model.df)
        PT_List = list(PT_List)  # OCR表の列名リスト
        # データ内のFalse,nan処理--------------------------------------------
        if AJ_List[0] is True:
            AJ_List = AJ_List[1]
            # ################################################################
            # OCR表の値を変換ルールに従って自動仕訳表に代入--------------------
            for r in range(len(self.Frame7EntL)):
                L_CName = self.Frame7EntL[r].get()
                R_CName = self.Frame7EntR[r].get()
                # 自動仕訳表の列番号検索--------------------------------------
                PT_c = 0
                for AJ_ListItem in AJ_List[0]:
                    if L_CName == AJ_ListItem:
                        L_CName_c = PT_c
                        break
                    PT_c += 1
                # -----------------------------------------------------------
                # OCR表の列番号検索-------------------------------------------
                PT_c = 0
                for PT_ColListItem in PT_ColList:
                    if R_CName == PT_ColListItem:
                        R_CName_c = PT_c
                        break
                    PT_c += 1
                # ---------------------------------------------------------------
                for L_r in range(len(AJ_List)):
                    if L_r != 0 and L_r != len(AJ_List):  # ヘッダー行処理
                        if (R_CName == I) or (R_CName == O):
                            # 数値確認-------------------------------------------
                            try:
                                Var = int(PT_List[L_r - 1][R_CName_c])
                                C_Txt = tke.TxtEdit(
                                    L_CName,
                                    AJ_List[L_r][L_CName_c],
                                    Var,
                                )
                                AJ_List[L_r][L_CName_c] = C_Txt[1]
                            except:
                                if R_CName == I:
                                    R_CName = O
                                elif R_CName == O:
                                    R_CName = I
                                # OCR表の列番号検索---------------------------
                                PT_c = 0
                                for PT_ColListItem in PT_ColList:
                                    if R_CName == PT_ColListItem:
                                        R_CName_c = PT_c
                                        break
                                    PT_c += 1
                                # ----------------------------------------
                                Var = int(PT_List[L_r - 1][R_CName_c])
                                C_Txt = tke.TxtEdit(
                                    L_CName,
                                    AJ_List[L_r][L_CName_c],
                                    Var,
                                )
                                AJ_List[L_r][L_CName_c] = C_Txt[1]
                            # ---------------------------------------------------
                        else:
                            Var = PT_List[L_r - 1][R_CName_c]
                            C_Txt = tke.TxtEdit(
                                L_CName,
                                AJ_List[L_r][L_CName_c],
                                Var,
                            )
                            AJ_List[L_r][L_CName_c] = C_Txt[1]
            # ################################################################
            for L_r in range(len(AJ_List)):
                if L_r == 0:  # ヘッダー行処理
                    for L_c in range(len(AJ_List[L_r])):

                        if "Unnamed" in AJ_List[L_r][L_c]:
                            AJ_List[L_r][L_c] = ""
                        if "." in AJ_List[L_r][L_c]:
                            S_txt = AJ_List[L_r][L_c].split(".")
                            AJ_List[L_r][L_c] = S_txt[0]
                        if AJ_List[L_r][L_c] == "False":
                            AJ_List[L_r][L_c] = ""
                else:  # ヘッダー行以外処理
                    for L_c in range(len(AJ_List[L_r])):
                        print(AJ_List[L_r][L_c])
                        if bool(AJ_List[L_r][L_c]) is False:
                            AJ_List[L_r][L_c] = ""
                        if AJ_List[L_r][L_c] == "False":
                            AJ_List[L_r][L_c] = ""
                        if (
                            AJ_List[L_r][L_c] == AJ_List[L_r][L_c]
                            and AJ_List[L_r][L_c] is not False
                        ):
                            print("")
                        else:
                            AJ_List[L_r][L_c] = ""
            # ------------------------------------------------------------------
            with open(AJurl, "wt", encoding="cp932", newline="") as fout:
                # ライター（書き込み者）を作成
                writer = csv.writer(fout)
                writer.writerows(AJ_List)
            self.pt2.redraw()

    # -----------------------------------------------------------------------------------------
    def AJCalc(self, csvurl):
        global AJSeturl
        self.FileName = csvurl
        self.JounalFileName = AJurl
        self.Roolurl = Roolurl

        if self.pt.startrow is None:
            tk.messagebox.showinfo("確認", "OCR表のセルが選択されていません。")
        else:
            print(self.pt.startrow)  # 選択行
            st = 0  # 行ポジション
            for stom in self.entryList:  # Entryウィジェットリスト
                if stom == "自動仕訳基準列名":
                    JS_var = st
                elif stom == "日付列名":
                    Day_var = st
                elif stom == "入金列名":
                    In_var = st
                elif stom == "出金列名":
                    Out_var = st
                st += 1
            # Entry要素設定-------------------------------------------------------------------
            JS = self.tomlEntries[JS_var].get()  # 自動仕訳基準列名Entry取得
            D = self.tomlEntries[Day_var].get()  # 日付列Entry取得
            I = self.tomlEntries[In_var].get()  # 入金列名Entry取得
            O = self.tomlEntries[Out_var].get()  # 出金列名Entry取得
            # --------------------------------------------------------------------------------
            print(self.Label_ChangeURL.get())  # toml金融機関Entry取得
            dfs = self.pt.model.df  # グリッドをDF化
            dfsrow = dfs.iloc[self.pt.startrow]  # DF行データ
            # グリッド選択データの代入---------------------------------------------------------
            FindTxt = dfsrow[JS]  # 検索文字
            D_var = dfsrow[D]  # 日付
            I_var = dfsrow[I]  # 入金
            O_var = dfsrow[O]  # 出金
            # --------------------------------------------------------------------------------
            # ColTxt,SerchTxt,D_var,D_coltxt,M_var,M_coltxt,imgurl,Roolrul,Banktoml,tomltitle,
            # 整数チェック---------------------------------------------------------------------
            IC = IntCheck(I_var)
            OC = IntCheck(O_var)
            if IC is True and OC is True:
                tkm = False, "", "", ""
            elif IC is True:
                tkm = True, I_var, In_var, "入金"
            elif OC is True:
                tkm = True, O_var, Out_var, "出金"

            if tkm[0] is False:
                tk.messagebox.showinfo("確認", "入金、出金双方に金額が出力されています。行を再確認してください。")
            # --------------------------------------------------------------------------------
            else:
                AJ_List = AJ.main(
                    JS,
                    FindTxt,
                    D_var,
                    self.Moto_Day.get(),
                    tkm[1],
                    self.Moto_Money_No,
                    tkm[3],
                    self.Moto_Karikata.get(),
                    self.Moto_Kashikata.get(),
                    self.JounalFileName,
                    self.Roolurl,
                    self.Banktoml,
                    self.Label_ChangeURL.get(),
                )  # 仕訳候補を抽出
                AJDF = pd.DataFrame(AJ_List)
                AJDF.to_csv(AJSeturl, index=False, header=False)
                pt3 = MT3.MyTable(
                    self.frame5, width=650, height=100, sticky=tk.N + tk.S + tk.W + tk.E
                )  # テーブルをサブクラス化
                enc = CSVO.getFileEncoding(AJSeturl)
                self.table3 = pt3.importCSV(AJSeturl, encoding=enc)
                self.pt3 = pt3
                pt3.show()

    # -----------------------------------------------------------------------------------------
    def CsvHeader(self):
        enc = CSVO.getFileEncoding(self.FileName)
        with open(self.FileName, "r", encoding=enc) as f:  # csv読込み(Treeview 表示用)
            reader = csv.reader(f, delimiter=",", quotechar='"')
            for cells in reader:
                # print(cells)
                # c = 0
                # p = 1
                # for cellsItem in cells:
                #     if cellsItem == "":
                #         cells[c] = str(p)
                #         p += 1
                #         c += 1
                #     else:
                #         c += 1
                # for cr in range(len(cells)):
                #     p = 2
                #     CC = cells.count(cells[cr])
                #     if CC > 1:
                #         c = 0
                #         for cellsItem in cells:
                #             if cells[cr] == cellsItem:
                #                 if cr != c:
                #                     cells[c + 1] = cells[cr] + str(p)
                #                     c += 1
                #                     p += 1
                #             else:
                #                 c += 1
                self.ColumnName = cells
                break
        enc = CSVO.getFileEncoding(self.JounalFileName)
        with open(self.JounalFileName, "r", encoding=enc) as f:  # csv読込み(Treeview 表示用)
            reader = csv.reader(f, delimiter=",", quotechar='"')
            for cells in reader:
                # print(cells)
                # c = 0
                # p = 1
                # for cellsItem in cells:
                #     if cellsItem == "":
                #         cells[c] = str(p)
                #         p += 1
                #         c += 1
                #     else:
                #         c += 1
                # for cr in range(len(cells)):
                #     p = 2
                #     CC = cells.count(cells[cr])
                #     if CC > 1:
                #         c = 0
                #         for cellsItem in cells:
                #             if cells[cr] == cellsItem:
                #                 if cr != c:
                #                     cells[c + 1] = cells[cr] + str(p)
                #                     c += 1
                #                     p += 1
                #             else:
                #                 c += 1
                self.ColumnName2 = cells
                break

    # -----------------------------------------------------------------------------------------
    def EveRecalc(self, event):
        c = 0
        self.InStartVal()
        # 列名一致で列番号取得----------------------------------------------------------
        for ColNameItem in self.ColumnName:
            if ColNameItem == self.NyuName:
                NyuCol = c
            elif ColNameItem == self.SyutuName:
                SyutuCol = c
            elif ColNameItem == self.ZanName:
                ZanCol = c
            c += 1
        # ---------------------------------------------------------------------------
        # CSV読込
        enc = CSVO.getFileEncoding(self.FileName)
        with open(self.FileName, "r", encoding=enc) as f:  # csv読込み(Treeview 表示用)
            reader = csv.reader(f, delimiter=",", quotechar='"')
            next(reader)
            CList = list(reader)
        # 残高再計算-----------------------------------------------------------------
        c = 0
        clr = len(CList)
        print(CList[0][ZanCol])
        zanstr = self.ZanNametxt.get()
        if zanstr == "":
            zanstr = CList[0][ZanCol]
        else:
            CList[0][ZanCol] = zanstr
        for r in range(clr):
            if not r == clr - 1:
                try:
                    if r == 0:
                        Zanint = int(zanstr)
                    else:
                        Zanint = int(CList[r][ZanCol])
                except:
                    Zanint = 0
                try:
                    Nyuint = int(CList[r + 1][NyuCol])
                except:
                    Nyuint = 0
                try:
                    Syutuint = int(CList[r + 1][SyutuCol])
                except:
                    Syutuint = 0

                NZan = Zanint + Nyuint - Syutuint
                CList[r + 1][ZanCol] = str(NZan)
        df = pd.DataFrame(CList, columns=self.ColumnName)
        try:
            df.to_csv(self.FileName, index=False, encoding="cp932")
        except:
            with open(
                self.FileName,
                mode="w",
                encoding="cp932",
                errors="ignore",
                newline="",
            ) as f:
                df.to_csv(f, index=False)

        tke.removeEntry(self)
        tke.treeviewEntries(self, tomltitle)

    # -----------------------------------------------------------------------------------------
    def ZanRecalc(self):
        c = 0
        # 列名一致で列番号取得----------------------------------------------------------
        for ColNameItem in self.ColumnName:
            if ColNameItem == self.NyuName:
                NyuCol = c
            elif ColNameItem == self.SyutuName:
                SyutuCol = c
            elif ColNameItem == self.ZanName:
                ZanCol = c
            c += 1
        # ---------------------------------------------------------------------------
        # CSV読込
        enc = CSVO.getFileEncoding(self.FileName)
        with open(self.FileName, "r", encoding=enc) as f:  # csv読込み(Treeview 表示用)
            reader = csv.reader(f, delimiter=",", quotechar='"')
            next(reader)
            CList = list(reader)
        # 残高再計算-----------------------------------------------------------------
        c = 0
        clr = len(CList)
        print(CList[0][ZanCol])
        zanstr = self.ZanNametxt.get()
        if zanstr == "":
            zanstr = CList[0][ZanCol]
        else:
            CList[0][ZanCol] = zanstr
        for r in range(clr):
            if not r == clr - 1:
                try:
                    if r == 0:
                        Zanint = int(zanstr)
                    else:
                        Zanint = int(CList[r][ZanCol])
                except:
                    Zanint = 0
                try:
                    Nyuint = int(CList[r + 1][NyuCol])
                except:
                    Nyuint = 0
                try:
                    Syutuint = int(CList[r + 1][SyutuCol])
                except:
                    Syutuint = 0

                NZan = Zanint + Nyuint - Syutuint
                CList[r + 1][ZanCol] = str(NZan)
        df = pd.DataFrame(CList, columns=self.ColumnName)
        try:
            df.to_csv(self.FileName, index=False, encoding="cp932")
        except:
            df.to_csv(self.FileName, index=False, encoding="utf8")
        tke.removeEntry(self)
        tke.treeviewEntries(self, tomltitle)

    # -----------------------------------------------------------------------------------------
    def Zandaka(self):
        zanstr = self.ZanNametxt.get()
        if zanstr == "":
            Messagebox = tk.messagebox.askquestion("再計算", "残高を再計算しますか？", icon="warning")
            if Messagebox == "yes":  # If関数
                self.ZanNameRecalc()
            else:
                tk.messagebox.showinfo("戻る", "アプリケーション画面に戻ります")
        else:
            Messagebox = tk.messagebox.askquestion(
                "開始残高登録", "開始残高を登録し再計算しますか？", icon="warning"
            )
            if Messagebox == "yes":  # If関数
                self.ZanNameRecalc()
            else:
                tk.messagebox.showinfo("戻る", "アプリケーション画面に戻ります")

    # -----------------------------------------------------------------------------------------
    def InStartVal(self):
        global tr  # 選択行インデックス

        # CSV読込
        enc = CSVO.getFileEncoding(self.FileName)
        with open(self.FileName, "r", encoding=enc) as f:  # csv読込み(Treeview 表示用)
            reader = csv.reader(f, delimiter=",", quotechar='"')
            next(reader)
            CList = list(reader)

        c = 0
        for ColNameItem in self.ColumnName:
            print(CList[tr][c])
            print(self.Entries[c].get())
            CList[tr][c] = str(self.Entries[c].get())
            c += 1
        df = pd.DataFrame(CList, columns=self.ColumnName)
        try:
            df.to_csv(self.FileName, index=False, encoding="cp932")
        except:
            with open(
                self.FileName,
                mode="w",
                encoding="cp932",
                errors="ignore",
                newline="",
            ) as f:
                df.to_csv(f, index=False)

        self.ZanNameRecalc()


#############################################################################################
# 以下関数
#############################################################################################
# -----------------------------------------------------------------------------------------
def IntCheck(c_var):
    try:
        int(c_var)
        return True
    except:
        return False


# -----------------------------------------------------------------------------------------
def Main(US, Bk, DS, MS, RS, RlS):
    """
    呼出構文↓
    DG.Main(
        csvurl,
        Banktoml,
        selfmother.DaySet.get(),
        selfmother.MoneySet.get(),
        selfmother.ReplaceSet.get(),
        selfmother.ReplaceStr.get(),
    )
    """
    global csvurl, Banktoml, DaySet, MoneySet, ReplaceSet, ReplaceStr
    csvurl = US
    Banktoml = Bk
    DaySet = DS
    MoneySet = MS
    ReplaceSet = RS
    ReplaceStr = RlS

    # 　Tk MainWindow 生成
    main_window = tk.Tk()
    main_window.withdraw()
    # Viewクラス生成
    DataGrid(main_window, "./")

    # 　フレームループ処理
    main_window.mainloop()


# -----------------------------------------------------------------------------------------
if __name__ == "__main__":
    global csvurl, Banktoml, AJurl, AJSeturl, Roolurl, tomltitle
    csvurl = r"D:\OCRTESTPDF\PDFTEST\JA_1page.csv"
    AJurl = r"D:\OCRTESTPDF\PDFTEST\JA_1page_AutoJounal.csv"
    AJSeturl = r"D:\OCRTESTPDF\PDFTEST\AJSet.csv"
    Roolurl = r"D:\PythonScript\RPAScript\TKInterGUI\Mototyou\1_仕訳日記帳.csv"
    tomltitle = "JA"
    # toml読込------------------------------------------------------------------------------
    with open(os.getcwd() + r"/TKInterGUI/BankSetting.toml", encoding="utf-8") as f:
        Banktoml = toml.load(f)
        print(Banktoml)
    # -----------------------------------------------------------
    # 　Tk MainWindow 生成
    main_window = tk.Tk()
    main_window.withdraw()
    # Viewクラス生成
    DataGrid(main_window, "./")

    # 　フレームループ処理
    main_window.mainloop()
