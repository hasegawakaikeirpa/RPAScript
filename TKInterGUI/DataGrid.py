import tkinter as tk
import numpy as np

# from tkinter import messagebox
import pandas as pd
import os
import csv
import toml
import AutoJournal as AJ
import CSVOut as CSVO
import TKEntry as tke

import Frame.DGFrame as DGF


class DataGrid:
    def __init__(self, window_root, default_path):
        # toml読込------------------------------------------------------------------------------
        self.Banktoml = Banktoml
        # -------------------------------------------------------------------------------------
        self.FileName = csvurl
        self.JounalFileName = AJurl
        self.Roolurl = Roolurl
        self.AJSeturl = AJSeturl
        self.ChangeTxtURL = ChangeTxtURL
        self.tomlList = self.Banktoml["ParList"]["Name"]
        enc = CSVO.getFileEncoding(self.ChangeTxtURL)
        pt4df = pd.read_csv(self.ChangeTxtURL, encoding=enc)
        self.ChangeTxtColumns = list(pt4df.columns)
        self.HidukeColNo = DaySet
        self.MoneyCol = MoneySet
        self.ChangeTextCol = ReplaceSet
        self.ColumnName = ColNameList
        self.HidukeColName = "日付"
        self.NyuName = "入金"
        self.SyutuName = "出金"
        self.ZanName = "残高"
        self.Henkan = "摘要"
        self.ChangeText = ReplaceStr
        # メインウィンドウ設定-------------------------------------------------------------------
        self.root = tk.Tk()  # ウインド画面の作成
        self.root.geometry("1500x750+0+0")  # 画面サイズの設定
        self.root.title("OCRTEXT")  # 題名
        # -------------------------------------------------------------------------------------
        # 統合フレーム
        self.Main_Frame = tk.Frame(self.root, bd=2, relief=tk.RIDGE)
        # self.Main_Frame.grid(row=0, column=0, sticky=tk.N + tk.S + tk.W + tk.E)
        self.Main_Frame.pack(expand=True)
        self.Sub_Frame = tk.Frame(self.root, bd=2, relief=tk.RIDGE)
        # self.Main_Frame.grid(row=0, column=0, sticky=tk.N + tk.S + tk.W + tk.E)
        self.Sub_Frame.pack(expand=True)
        self.Sub_Frame.pack_forget()
        ########################################################################################
        # フレーム設定---------------------------------------------------------------------
        DGF.create_Frame(self)  # OCR表フレーム
        DGF.create_Frame2(self)  # 出力表フレーム
        DGF.create_SettingFrame(self)  # 設定メインフレーム
        DGF.create_Frame3(self)  # 元帳(仕訳候補)フレーム
        DGF.create_Frame4(self)  # サブフレーム(変換ルール表示)
        # -------------------------------------------------------------------------------------
        ########################################################################################
        ########################################################################################
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
        # ツリービューを配置
        tke.treeviewEntries(self)
        # -------------------------------------------------------------------------------------
        # テキスト変換設定フレームを配置(サブメニューにもコピー配置)
        tke.FrameChangeEntries(self)
        # tomlListを配置
        tke.tomlEntries(self)
        # フレーム7を配置
        tke.Frame7Entries(self)

    #############################################################################################
    # 以下self関数
    #############################################################################################
    def Sub_ColumnDelete(self):
        """
        DGFrame.py
        ↓
        def create_Frame4(self)
        ↓
        self.Sub_RowInsert
        bind関数
        """
        try:
            if self.pt4.startcol is None:  # 選択列
                tk.messagebox.showinfo("確認", "テキスト変換ルール表のセルが選択されていません。")
            else:
                pt4df = self.pt4.model.df
                pt4c = list(pt4df.columns)
                pt4c.pop(self.pt4.startcol)
                NullList = []
                for N_c in range(len(pt4df)):
                    NullList.append("")
                pt4df = np.array(pt4df)
                pt4df = np.delete(pt4df, self.pt4.startcol, axis=1)  # 列の削除
                pt4df = pd.DataFrame(pt4df, columns=pt4c)
                pt4df.to_csv(self.ChangeTxtURL, index=False)
                enc = CSVO.getFileEncoding(self.ChangeTxtURL)
                self.pt4.importCSV(self.ChangeTxtURL, encoding=enc)
                self.pt4.redraw
        except:
            tk.messagebox.showinfo("確認", "メイン画面への復帰に失敗しました。\nSEまでお問い合わせください。")

    # -------------------------------------------------------------------------------------
    def Sub_RowDelete(self):
        """
        DGFrame.py
        ↓
        def create_Frame4(self)
        ↓
        self.Sub_RowInsert
        bind関数
        """
        try:
            if self.pt4.startrow is None:  # 選択行
                tk.messagebox.showinfo("確認", "テキスト変換ルール表のセルが選択されていません。")
            else:
                pt4df = self.pt4.model.df
                pt4c = list(pt4df.columns)
                pt4df = np.array(self.pt4.model.df)
                pt4df = np.delete(pt4df, self.pt4.startrow, axis=0)  # 行の削除
                pt4df = pd.DataFrame(pt4df, columns=pt4c)
                pt4df.to_csv(self.ChangeTxtURL, index=False)
                enc = CSVO.getFileEncoding(self.ChangeTxtURL)
                self.pt4.importCSV(self.ChangeTxtURL, encoding=enc)
                self.pt4.redraw
        except:
            tk.messagebox.showinfo("確認", "メイン画面への復帰に失敗しました。\nSEまでお問い合わせください。")

    # -------------------------------------------------------------------------------------

    def Sub_ColumnInsert(self):
        """
        DGFrame.py
        ↓
        def create_Frame4(self)
        ↓
        self.Sub_RowInsert
        bind関数
        """
        try:
            pt4df = self.pt4.model.df
            pt4c = list(pt4df.columns)
            o_count = 0
            for pt4cItem in pt4c:
                if "OCRテキスト" in pt4cItem:
                    o_count += 1
            c_no = int(np.where(np.array(pt4c) == "元帳テキスト")[0])
            pt4c.insert(c_no, "OCRテキスト" + str(o_count + 1))
            NullList = []
            for N_c in range(len(pt4df)):
                NullList.append("")
            pt4df = np.array(pt4df)
            pt4df = np.insert(pt4df, c_no, NullList, axis=1)  # 列の挿入
            pt4df = pd.DataFrame(pt4df, columns=pt4c)
            pt4df.to_csv(self.ChangeTxtURL, index=False)
            enc = CSVO.getFileEncoding(self.ChangeTxtURL)
            self.pt4.importCSV(self.ChangeTxtURL, encoding=enc)
            self.pt4.redraw
        except:
            tk.messagebox.showinfo("確認", "メイン画面への復帰に失敗しました。\nSEまでお問い合わせください。")

    # -------------------------------------------------------------------------------------
    def Sub_RowInsert(self):
        """
        DGFrame.py
        ↓
        def create_Frame4(self)
        ↓
        self.Sub_RowInsert
        bind関数
        """
        try:
            pt4df = self.pt4.model.df
            pt4c = list(pt4df.columns)
            NullList = []
            InList = []
            for N_c in range(len(pt4c)):
                NullList.append("")
            InList.append(NullList)
            InList = pd.DataFrame(InList, columns=pt4c)
            pt4df = pt4df.append(InList)
            pt4df.to_csv(self.ChangeTxtURL, index=False)
            enc = CSVO.getFileEncoding(self.ChangeTxtURL)
            self.pt4.importCSV(self.ChangeTxtURL, encoding=enc)
            self.pt4.redraw
        except:
            tk.messagebox.showinfo("確認", "メイン画面への復帰に失敗しました。\nSEまでお問い合わせください。")

    # -------------------------------------------------------------------------------------
    def Sub_ReturnBack(self):
        """
        DGFrame.py
        ↓
        def create_Frame4(self)
        ↓
        self.Sub_CloseBtn
        bind関数
        """
        try:
            self.Sub_Frame.pack_forget()
            self.GetTxt_ChangeEntry(1)
            self.Main_Frame.pack(expand=True)
        except:
            tk.messagebox.showinfo("確認", "メイン画面への復帰に失敗しました。\nSEまでお問い合わせください。")

    # -------------------------------------------------------------------------------------
    def Txt_ChangeSetOpen(self):
        """
        TKEntry.py
        ↓
        def treeviewEntries(self)
        ↓
        self.Txt_C
        bind関数
        """
        try:
            self.Main_Frame.pack_forget()
            self.GetTxt_ChangeEntry(0)
            self.Sub_Frame.pack(expand=True)
        except:
            tk.messagebox.showinfo("確認", "テキスト変換ルール設定の起動に失敗しました。\nSEまでお問い合わせください。")

    # -------------------------------------------------------------------------------------
    def GetTxt_ChangeEntry(self, Flag):
        """
        列名設定項目取得関数
        """
        TxtList = []
        # 全てのエントリーウィジェットの内容を配列化
        if Flag == 0:
            for i in range(len(self.ChangeTxtindexes)):
                InTxt = self.ChangeTxtEntries[i].get()
                TxtList.append(InTxt)
                self.Sub_ChangeTxtEntries[i].delete(0, tk.END)
                self.Sub_ChangeTxtEntries[i].insert(0, InTxt)
        else:
            for i in range(len(self.ChangeTxtindexes)):
                InTxt = self.Sub_ChangeTxtEntries[i].get()
                TxtList.append(InTxt)
                self.ChangeTxtEntries[i].delete(0, tk.END)
                self.ChangeTxtEntries[i].insert(0, InTxt)
        # コンソールに表示
        return TxtList

    # -------------------------------------------------------------------------------------
    def Out_Open(self):
        """
        TKEntry.py
        ↓
        def treeviewEntries(self)
        ↓
        self.URL_In2
        bind関数
        """
        try:
            typ = [("自動仕訳出力先CSVを選択してください。", "*.csv")]
            dir = csvurl
            fle = tk.filedialog.askopenfilename(
                filetypes=typ, initialdir=dir
            )  # ファイル指定ダイアログ
            enc = CSVO.getFileEncoding(fle)
            self.pt2.importCSV(fle, encoding=enc)
            self.pt2.redraw
            self.JounalFileName = fle
            self.Label_OutURL.delete(0, tk.END)
            self.Label_OutURL.insert(0, self.JounalFileName)
        except:
            tk.messagebox.showinfo("確認", "OCR抽出結果CSVの出力に失敗しました。\n参照先のURLが正しいか確認してください。")

    # -------------------------------------------------------------------------------------
    def Moto_Open(self):
        """
        TKEntry.py
        ↓
        def treeviewEntries(self)
        ↓
        self.URL_In3
        bind関数
        """
        try:
            typ = [("元帳CSVを選択してください。", "*.csv")]
            dir = csvurl
            fle = tk.filedialog.askopenfilename(
                filetypes=typ, initialdir=dir
            )  # ファイル指定ダイアログ
            enc = CSVO.getFileEncoding(fle)
            self.pt3.importCSV(fle, encoding=enc)
            self.pt3.redraw
            self.Roolurl = fle
            self.Label_ChangeURL.delete(0, tk.END)
            self.Label_ChangeURL.insert(0, self.Roolurl)
        except:
            tk.messagebox.showinfo("確認", "OCR抽出結果CSVの出力に失敗しました。\n参照先のURLが正しいか確認してください。")

    # -------------------------------------------------------------------------------------
    def OCR_Open(self):
        """
        TKEntry.py
        ↓
        def treeviewEntries(self)
        ↓
        self.OCR_Open
        bind関数
        """
        try:
            typ = [("OCR抽出結果CSVを選択してください。", "*.csv")]
            dir = csvurl
            fle = tk.filedialog.askopenfilename(
                filetypes=typ, initialdir=dir
            )  # ファイル指定ダイアログ
            enc = CSVO.getFileEncoding(fle)
            self.pt.importCSV(fle, encoding=enc)
            self.pt.redraw
            self.FileName = fle
            self.Label_URL.delete(0, tk.END)
            self.Label_URL.insert(0, self.FileName)
        except:
            tk.messagebox.showinfo("確認", "OCR抽出結果CSVの出力に失敗しました。\n参照先のURLが正しいか確認してください。")

    # -------------------------------------------------------------------------------------
    def ReadM(self, URL):
        """
        DGFrame.py
        ↓
        def create_SettingFrame(self)
        ↓
        self.AJ_copy
        bind関数
        """
        try:
            enc = CSVO.getFileEncoding(URL)
            self.pt3.importCSV(URL, encoding=enc)
            self.pt3.redraw
        except:
            tk.messagebox.showinfo("確認", "元帳の出力に失敗しました。\n参照先のURLが正しいか確認してください。")

    # -------------------------------------------------------------------------------------
    def ChangeFrame(self, Case):
        """
        TKEntry.py
        ↓
        def Frame7Entries(self)
        ↓
        self.Setting_Btn
        bind関数
        """

        if Case == "詳細設定":
            tk.messagebox.showinfo("確認", "現在開発中です。")
            # self.Main_Frame.pack_forget()

    # -------------------------------------------------------------------------------------
    def AJ_copyCalc(self, csvurl):
        """
        DGFrame.py
        ↓
        def create_SettingFrame(self)
        ↓
        self.AJ_copy
        bind関数
        """
        try:
            if self.pt3.startrow is None:
                tk.messagebox.showinfo("確認", "抽出仕訳表のセルが選択されていません。")
            else:
                if self.pt.startrow is None:
                    tk.messagebox.showinfo("確認", "OCR表のセルが選択されていません。")
                else:
                    SetList = self.GetTxt_ChangeEntry(0)
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
                        EntR_C = 0
                        for EntRItem in self.Frame7EntR:
                            if tkm[3] == I:
                                if O == EntRItem.get():
                                    EntL_CName = self.Frame7EntL[EntR_C].get()
                                elif I == EntRItem.get():
                                    EntL_ChangeCName = self.Frame7EntL[EntR_C].get()
                            elif tkm[3] == O:
                                if I == EntRItem.get():
                                    EntL_CName = self.Frame7EntL[EntR_C].get()
                                elif O == EntRItem.get():
                                    EntL_ChangeCName = self.Frame7EntL[EntR_C].get()
                            EntR_C += 1
                        # 自動仕訳保存配列の行数判定------------------------------------------
                        d2_r = len(self.pt2.model.df)
                        if self.pt.startrow > d2_r:
                            # 各配列をDataFrameに------------------------------------------------
                            dfs = self.pt.model.df  # グリッドをDF化
                            dfsrow = dfs.iloc[self.pt.startrow]  # DF行データ
                            dfs2 = self.pt2.model.df  # グリッドをDF化
                            dfs3 = self.pt3.model.df  # グリッドをDF化
                            # ------------------------------------------------------------------
                            dfs3row = dfs3.iloc[self.pt3.startrow]  # DF行データ
                            CF_df = tke.AJ_copyCalc_Func(
                                SetList, dfsrow, dfs3row, self.ChangeTxtURL
                            )  # 自動仕訳抽出
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
                            # 入出金状況による仕訳金額確定----------------------------------------
                            C_df_c = 0
                            for C_dfColumnItem in C_dfColumn:
                                if EntL_CName == C_dfColumnItem:
                                    EntL_CNo = C_df_c
                                elif EntL_ChangeCName == C_dfColumnItem:
                                    EntL_ChangeCNo = C_df_c
                                C_df_c += 1
                            Last_List[self.pt.startrow + 1][EntL_CNo] = Last_List[
                                self.pt.startrow + 1
                            ][EntL_ChangeCNo]
                            # ------------------------------------------------------------------
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
                            with open(
                                AJurl, "wt", encoding="cp932", newline=""
                            ) as fout:
                                # ライター（書き込み者）を作成
                                writer = csv.writer(fout)
                                writer.writerows(Last_List)
                            enc = CSVO.getFileEncoding(AJurl)
                            self.pt2.importCSV(AJurl, encoding=enc)
                            self.pt2.redraw
                        else:
                            # 各配列をDataFrameに------------------------------------------------
                            dfs = self.pt.model.df  # グリッドをDF化
                            dfsrow = dfs.iloc[self.pt.startrow]  # DF行データ
                            dfs2 = self.pt2.model.df  # グリッドをDF化
                            dfs3 = self.pt3.model.df  # グリッドをDF化
                            # ------------------------------------------------------------------
                            dfs3row = dfs3.iloc[self.pt3.startrow]  # DF行データ
                            CF_df = tke.AJ_copyCalc_Func(
                                SetList, dfsrow, dfs3row, self.ChangeTxtURL
                            )  # 自動仕訳抽出
                            CF_df = list(np.array(CF_df))  # list化
                            C_dfColumn = np.array(dfs2.columns)  # DFColumnをnumpy配列へ
                            dfs2 = np.array(dfs2)  # 自動仕訳保存配列をnumpy配列へ
                            dfs2 = np.delete(dfs2, self.pt.startrow, axis=0)
                            dfs2 = np.insert(
                                dfs2, self.pt.startrow, CF_df, axis=0
                            )  # 末尾へデータ行追加
                            Last_List = np.vstack((C_dfColumn, dfs2))  # 列名リストを縦連結
                            Last_List.astype(str)  # numpy配列型変換
                            Last_List = list(Last_List)  # numpy配列list型変換
                            print(Last_List)
                            # 入出金状況による仕訳金額確定----------------------------------------
                            C_df_c = 0
                            for C_dfColumnItem in C_dfColumn:
                                if EntL_CName == C_dfColumnItem:
                                    EntL_CNo = C_df_c
                                elif EntL_ChangeCName == C_dfColumnItem:
                                    EntL_ChangeCNo = C_df_c
                                C_df_c += 1
                            Last_List[self.pt.startrow + 1][EntL_CNo] = Last_List[
                                self.pt.startrow + 1
                            ][EntL_ChangeCNo]
                            # ------------------------------------------------------------------
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
                            with open(
                                AJurl, "wt", encoding="cp932", newline=""
                            ) as fout:
                                # ライター（書き込み者）を作成
                                writer = csv.writer(fout)
                                writer.writerows(Last_List)
                            enc = CSVO.getFileEncoding(AJurl)
                            self.pt2.importCSV(AJurl, encoding=enc)
                            self.pt2.redraw
        except:
            tk.messagebox.showinfo("確認", "エラーです。自動仕訳実行後に抽出仕訳表のセルを選択し、実行してください。")

    # -----------------------------------------------------------------------------------------
    def AJAllCalc(self, csvurl):
        """
        全行自動仕訳処理
        DGFrame.py
        ↓
        def create_SettingFrame(self)
        ↓
        self.AllRun
        bind関数
        """
        global AJSeturl
        self.FileName = csvurl  # OCR表
        self.JounalFileName = AJurl
        self.Roolurl = Roolurl  # テキスト置換ルール代入
        SetList = self.GetTxt_ChangeEntry(0)  # テキスト置換ルール代入
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
        ChangeTxtURLenc = CSVO.getFileEncoding(self.ChangeTxtURL)
        # Entry要素設定-------------------------------------------------------------------
        JS = self.tomlEntries[JS_var].get()  # 自動仕訳基準列名Entry取得
        D = self.tomlEntries[Day_var].get()  # 日付列Entry取得
        I = self.tomlEntries[In_var].get()  # 入金列名Entry取得
        O = self.tomlEntries[Out_var].get()  # 出金列名Entry取得
        # --------------------------------------------------------------------------------
        Messagebox = tk.messagebox.askquestion(
            "再計算",
            "OCR結果の["
            + str(JS)
            + "]列と\nミロク元帳の["
            + str(self.Moto_Tekiyou.get())
            + "]列を条件に仕訳検索を行いますか？",
            icon="warning",
        )
        if Messagebox == "yes":  # If関数
            AJ_List = AJ.AllChange(
                SetList,
                JS,
                self.Moto_Tekiyou.get(),
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
                self.ChangeTxtURL,
                ChangeTxtURLenc,
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
                    # ヘッダー行処理##################################################
                    for L_r in range(len(AJ_List)):
                        if L_r == 6:
                            print("")
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
                enc = CSVO.getFileEncoding(AJurl)
                self.pt2.importCSV(AJurl, encoding=enc)
                self.pt2.redraw
            else:
                tk.messagebox.showinfo("戻る", "アプリケーション画面に戻ります")

    # -----------------------------------------------------------------------------------------
    def AJCalc(self, csvurl):
        """
        DGFrame.py
        ↓
        def create_SettingFrame(self)
        ↓
        self.AJ_Btn
        bind関数
        """
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
                    FindTxt,
                    self.Moto_Tekiyou.get(),
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
                enc = CSVO.getFileEncoding(AJSeturl)
                self.pt3.importCSV(AJSeturl, encoding=enc)
                self.pt3.redraw

    # -----------------------------------------------------------------------------------------
    def CsvHeader(self):
        """
        DGFrame.py
        ↓
        def create_SettingFrame(self)
        ↓
        self.AJ_Btn
        bind関数
        """
        enc = CSVO.getFileEncoding(self.FileName)
        with open(self.FileName, "r", encoding=enc) as f:  # csv読込み(Treeview 表示用)
            reader = csv.reader(f, delimiter=",", quotechar='"')
            for cells in reader:
                self.ColumnName = cells
                break
        enc = CSVO.getFileEncoding(self.JounalFileName)
        with open(self.JounalFileName, "r", encoding=enc) as f:  # csv読込み(Treeview 表示用)
            reader = csv.reader(f, delimiter=",", quotechar='"')
            for cells in reader:
                self.ColumnName2 = cells
                break

    # ------------------------------------------------------------------------------------------
    def ReturnBack(self):
        """
        treeviewEntries.py
        ↓
        def create_SettingFrame(self)
        ↓
        self.CloseBtn
        bind関数
        """

        self.root.destroy()
        Master.deiconify()


#############################################################################################
# 以下関数
#############################################################################################
# -----------------------------------------------------------------------------------------
def IntCheck(c_var):
    """
    整数判定
    """
    try:
        int(c_var)
        return True
    except:
        return False


# -----------------------------------------------------------------------------------------
def Main(US, Bk, DS, MS, RS, RlS, SGEL, r_win):
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
    global AJurl, AJSeturl, Roolurl, ChangeTxtURL, Master, main_window
    global csvurl, Banktoml, DaySet, MoneySet, ReplaceSet, ReplaceStr, ColNameList
    Master = r_win
    csvurl = US
    Banktoml = Bk
    DaySet = DS
    MoneySet = MS
    ReplaceSet = RS
    ReplaceStr = RlS
    ColNameList = SGEL
    # 自動仕訳変換条件のミロクエクスポートCSVを指定し、変換先ファイルを作成------------------
    # 　Tk MainWindow 生成
    main_window = tk.Tk()
    main_window.withdraw()

    typ = [("ミロク元帳CSVを選択してください。", "*.csv")]
    dir = csvurl
    fle = tk.filedialog.askopenfilename(filetypes=typ, initialdir=dir)  # ファイル指定ダイアログ
    Roolurl = fle
    enc = CSVO.getFileEncoding(Roolurl)
    Roolurldf = pd.read_csv(Roolurl, encoding=enc)
    DelIndex = []
    # ミロク元帳CSVから全行削除------------------------
    for R_r in reversed(range(Roolurldf.shape[0] - 1)):
        DelIndex.append(R_r)
    Roolurldf = Roolurldf.drop(Roolurldf.index[DelIndex])
    # --------------------------------------------------------
    AJurl = csvurl.replace(".csv", "_AutoJounal.csv")
    Roolurldf.to_csv(AJurl, index=False, encoding=enc)
    # -----------------------------------------------------------------------------------
    AJSeturl = r"D:\OCRTESTPDF\PDFTEST\AJSet.csv"
    typ = [("テキスト変換ルールCSVを選択してください。", "*.csv")]
    dir = csvurl
    fle = tk.filedialog.askopenfilename(filetypes=typ, initialdir=dir)  # ファイル指定ダイアログ
    ChangeTxtURL = fle
    # Viewクラス生成
    DataGrid(main_window, "./")

    # 　フレームループ処理
    main_window.mainloop()


# -----------------------------------------------------------------------------------------
if __name__ == "__main__":
    global AJurl, AJSeturl, Roolurl, ChangeTxtURL
    global csvurl, Banktoml, DaySet, MoneySet, ReplaceSet, ReplaceStr, ColNameList

    DaySet = ["1"]
    MoneySet = ["3,4,5"]
    ReplaceSet = ["2,3,4"]
    ReplaceStr = ["CDカード", "マツモトトソウテン", "ザンダカショウメイショ"]
    ColNameList = ["日付", "摘要", "出金", "入金", "残高"]

    csvurl = r"D:\OCRTESTPDF\PDFTEST\Hirogin_1page.csv"
    AJurl = r"D:\OCRTESTPDF\PDFTEST\Hirogin_1page_AutoJounal.csv"
    AJSeturl = r"D:\OCRTESTPDF\PDFTEST\AJSet.csv"
    Roolurl = r"D:\OCRTESTPDF\PDFTEST\1_仕訳日記帳.csv"
    ChangeTxtURL = r"D:\OCRTESTPDF\PDFTEST\ChangeTxtList.csv"
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
