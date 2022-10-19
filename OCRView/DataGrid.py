import tkinter as tk
from tkinter import messagebox
import numpy as np

# from tkinter import messagebox
import pandas as pd
from io import StringIO
from csv import QUOTE_NONNUMERIC

# import os
import csv
import toml
import AutoJournal as AJ
import CSVOut as CSVO
import Frame.TKEntry as tke
import re
import Frame.DG_DGFrame as DG_DGF
from datetime import date
from dateutil.relativedelta import relativedelta
import ProgressBar as PB
import IconCode
import customtkinter as ck
import os
from pandastable import config

# class DataGrid:
class DataGrid(tk.Toplevel):
    def __init__(
        self, filename, J_File, A_File, R_Url, C_Url, Banktoml, BanktomlUrl, master=None
    ):
        # Windowの初期設定を行う。
        super().__init__(master)
        self.withdraw()
        # Windowの画面サイズを設定する。
        # G_logger.debug("P_Table起動")  # Log出力
        self.FileName = filename
        self.JounalFileName = J_File
        self.AJSeturl = A_File
        self.Roolurl = R_Url
        self.ChangeTxtURL = C_Url
        self.setctxt()
        # customtkスタイル
        ck.set_appearance_mode("System")  # Modes: system (default), light, dark
        ck.set_default_color_theme(
            "dark-blue"
        )  # Themes: blue (default), dark-blue, green
        self.width_of_window = int(int(master.winfo_screenwidth()) * 0.95)
        self.height_of_window = int(int(master.winfo_screenheight()) * 0.90)
        self.wid_Par = self.width_of_window / 1459
        self.hei_Par = self.height_of_window / 820
        self.x_coodinate = self.width_of_window * 0.01
        self.y_coodinate = self.height_of_window * 0.01
        # 　メインウィンドウサイズ指定
        self.master.geometry(
            "%dx%d+%d+%d"
            % (
                self.width_of_window,
                self.height_of_window,
                self.x_coodinate,
                self.y_coodinate,
            )
        )
        ########################################
        self.SideWidth = int(100 * self.wid_Par)
        self.SideHeight = int(50 * self.hei_Par)
        self.LabelWidth = int(50 * self.wid_Par)
        self.LabelHeight = int(20 * self.hei_Par)
        self.BtnWidth = int(200 * self.wid_Par)
        self.BtnHeight = int(20 * self.hei_Par)
        self.EntWidth = int(100 * self.hei_Par)
        self.EntHeight = int(20 * self.wid_Par)
        self.wid = 2.25  # width割率
        self.hei = 1.4  # width割率
        self.t_font = (1, int(10 * self.wid_Par))
        self.BanktomlUrl = BanktomlUrl
        self.Banktoml = Banktoml
        self.tomlList = self.Banktoml["ParList"]["Name"]  # tomlリスト値
        self.tomlParList = self.Banktoml["ParList"]
        ########################################
        self.master.minsize(self.width_of_window, self.height_of_window)
        self.master.title("OCR読取 Ver:0.9-仕訳検索-")
        self.master.protocol("WM_DELETE_WINDOW", self.click_close)  # 閉じる処理設定
        # -------------------------------------------------------------------------------------
        # 統合フレーム
        self.DG_Main_Frame = tk.Frame(self.master, bd=2, relief=tk.RIDGE)
        self.DG_Main_Frame.pack(expand=True)
        self.DG_Sub_Frame = tk.Frame(self.master, bd=2, relief=tk.RIDGE)
        self.DG_Sub_Frame.pack(expand=True)
        self.DG_Sub_Frame.pack_forget()
        ########################################################################################
        # フレーム設定---------------------------------------------------------------------
        DG_DGF.create_Frame(self, self.t_font)  # OCR抽出結果表フレーム
        self.ColumnName = self.pt.model.df.columns
        DG_DGF.create_Frame2(self, self.t_font)  # 出力表フレーム
        DG_DGF.create_SettingFrame(self)  # 設定メインフレーム
        DG_DGF.create_Frame3(self, self.t_font)  # 元帳(仕訳候補)フレーム
        DG_DGF.create_Frame4(self, self.t_font)  # サブフレーム(変換ルール表示)
        # -------------------------------------------------------------------------------------
        ########################################################################################
        self.setRool()
        # ツリービューを配置
        tke.treeviewEntries(self)
        # -------------------------------------------------------------------------------------
        # テキスト変換設定フレームを配置(サブメニューにもコピー配置)
        tke.FrameChangeEntries(self)
        # tomlListを配置
        tke.tomlEntries(self)
        # フレーム7を配置
        tke.Frame7Entries(self)
        # フレーム7のスクロールバー再設定
        DG_DGF.s_bar_Reset(self)

    #############################################################################################
    # 以下self関数
    #############################################################################################
    def setRool(self):
        if self.Roolurl != "":
            if os.path.isfile(self.Roolurl) is True:
                enc = CSVO.getFileEncoding(self.Roolurl)
                AJ_np = BeforeNGFT(self.Roolurl, enc)
                AJ_Column = AJ_np[0, :]
                A = 0
                # ミロク元帳の列名から元帳列名設定を抽出--------------------------------------------
                for AJ_Item in AJ_Column:
                    if "日付" in AJ_Item:
                        self.Moto_Day.delete(0, tk.END)
                        self.Moto_Day.insert(
                            0, AJ_Item.replace("'", "").replace('"', "")
                        )
                        self.Moto_Day_No = A
                    elif "金額" in AJ_Item and "借" in AJ_Item:
                        self.Moto_KariMoney.delete(0, tk.END)
                        self.Moto_KariMoney.insert(
                            0, AJ_Item.replace("'", "").replace('"', "")
                        )
                        self.Moto_KariMoney_No = A
                    elif "金額" in AJ_Item and "貸" in AJ_Item:
                        self.Moto_KashiMoney.delete(0, tk.END)
                        self.Moto_KashiMoney.insert(
                            0, AJ_Item.replace("'", "").replace('"', "")
                        )
                        self.Moto_KashiMoney_No = A
                    elif "摘要" in AJ_Item:
                        self.Moto_Tekiyou.delete(0, tk.END)
                        self.Moto_Tekiyou.insert(
                            0, AJ_Item.replace("'", "").replace('"', "")
                        )
                        self.Moto_Tekiyou_No = A
                    A += 1
        return
        # ---------------------------------------------------------------------------------------

    def setctxt(self):
        try:
            enc = CSVO.getFileEncoding(self.ChangeTxtURL)  # 摘要変換ルールエンコード
            pt4df = pd.read_csv(self.ChangeTxtURL, encoding=enc)  # 摘要変換ルール読込
            self.ChangeTxtColumns = list(pt4df.columns)  # 摘要変換ルール列名
        except:
            dl = [["OCRテキスト", "元帳テキスト"]]
            df = pd.DataFrame(
                dl,
                columns=["OCRテキスト", "元帳テキスト"],
                index=None,
            )
            print(df)
            try:
                df.to_csv(self.ChangeTxtURL, index=None, encoding=enc)
            except:
                df.to_csv(self.ChangeTxtURL, index=None, encoding="cp932")
            pt4df = pd.read_csv(self.ChangeTxtURL, encoding=enc)  # 摘要変換ルール読込
            self.ChangeTxtColumns = list(pt4df.columns)  # 摘要変換ルール列名

    # -------------------------------------------------------------------------------------
    def click_close(self):
        """
        ウィンドウ×ボタンクリック
        """
        try:
            self.DG_Sub_Frame.pack_forget()
            self.DG_Main_Frame.pack(expand=True)
        except:
            tk.messagebox.showinfo("確認", "フレームを閉じるのに失敗しました。")
            # G_logger.debug("TKINTERCV2SettingClose失敗")  # Log出力

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
                startcol = re.sub(r"[^0-9]", "", pt4c[self.pt4.startcol])
                DelIndex = []
                for pt4cNo in reversed(range(len(pt4c))):
                    if str(startcol) in pt4c[pt4cNo]:
                        pt4c.pop(pt4cNo)
                        DelIndex.append(pt4cNo)
                pt4df = np.array(pt4df)
                for DelIndexItem in DelIndex:
                    pt4df = np.delete(pt4df, DelIndexItem, axis=1)  # 列の削除
                pt4df = pd.DataFrame(pt4df, columns=pt4c)
                pt4df.to_csv(self.ChangeTxtURL, index=False, quoting=QUOTE_NONNUMERIC)
                enc = CSVO.getFileEncoding(self.ChangeTxtURL)
                self.pt4.importCSV(self.ChangeTxtURL, encoding=enc)
                # DF型変換------------------------------
                PandasAstype(self.pt4.model.df)
                # --------------------------------------
                options = {"fontsize": self.t_font[1]}
                config.apply_options(options, self.pt4)
                self.pt4.update()
                self.pt4.show()
                self.ColumnName = pt4c
                self.ChangeTxtColumns = pt4c
                tke.FrameChangeremoveEntry(self)
                tke.FrameChangeEntries(self)
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
                pt4df.to_csv(self.ChangeTxtURL, index=False, quoting=QUOTE_NONNUMERIC)
                enc = CSVO.getFileEncoding(self.ChangeTxtURL)
                self.pt4.importCSV(self.ChangeTxtURL, encoding=enc)
                # DF型変換------------------------------
                PandasAstype(self.pt4.model.df)
                # --------------------------------------
                options = {"fontsize": self.t_font[1]}
                config.apply_options(options, self.pt4)
                self.pt4.update()
                self.pt4.show()
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
            DelIndex = []
            for pt4cItem in pt4c:
                if "OCRテキスト" in pt4cItem:
                    o_count += 1
                    DelIndex.append(re.sub(r"[^0-9]", "", pt4cItem))
            print(max(DelIndex))

            if str(o_count) not in DelIndex:
                O_c = "0"
                # 連番チェック---------------------------------------------------------------
                for DelIndexItem in DelIndex:
                    if DelIndexItem != "":
                        if int(DelIndexItem) + 1 not in DelIndex:
                            O_No = str(int(DelIndexItem) + 1)
                            O_c = str(int(DelIndexItem))
                            break
                # --------------------------------------------------------------------------
                if O_c != "0":
                    c_no = int(np.where(np.array(pt4c) == "元帳テキスト" + O_c)[0])
                else:
                    c_no = int(np.where(np.array(pt4c) == "元帳テキスト")[0])
                    O_No = "2"
                pt4c.insert(c_no + 1, "OCRテキスト" + O_No)
                pt4c.insert(c_no + 2, "元帳テキスト" + O_No)
                NullList = []
                for N_c in range(len(pt4df)):
                    NullList.append("")
                pt4df = np.array(pt4df)
                pt4df = np.insert(pt4df, c_no + 1, NullList, axis=1)  # 列の挿入
                pt4df = np.insert(pt4df, c_no + 2, NullList, axis=1)  # 列の挿入

                self.ColumnName = pt4c
                self.ChangeTxtColumns = pt4c

                pt4df = pd.DataFrame(pt4df, columns=pt4c)
                pt4df.to_csv(self.ChangeTxtURL, index=False, quoting=QUOTE_NONNUMERIC)
                enc = CSVO.getFileEncoding(self.ChangeTxtURL)
                self.pt4.importCSV(self.ChangeTxtURL, encoding=enc)
                # DF型変換------------------------------
                PandasAstype(self.pt4.model.df)
                # --------------------------------------
                options = {"fontsize": self.t_font[1]}
                config.apply_options(options, self.pt4)
                self.pt4.update()
                self.pt4.show()
                # テキスト変換設定フレームを配置(サブメニューにもコピー配置)
                tke.FrameChangeremoveEntry(self)
                tke.FrameChangeEntries(self)

            else:
                c_no = int(np.where(np.array(pt4c) == "元帳テキスト" + str(o_count))[0])
                pt4c.insert(c_no + 1, "OCRテキスト" + str(o_count + 1))
                pt4c.insert(c_no + 2, "元帳テキスト" + str(o_count + 1))
                NullList = []
                for N_c in range(len(pt4df)):
                    NullList.append("")
                pt4df = np.array(pt4df)
                pt4df = np.insert(pt4df, c_no + 1, NullList, axis=1)  # 列の挿入
                pt4df = np.insert(pt4df, c_no + 2, NullList, axis=1)  # 列の挿入

                self.ColumnName = pt4c
                self.ChangeTxtColumns = pt4c

                pt4df = pd.DataFrame(pt4df, columns=pt4c)
                pt4df.to_csv(self.ChangeTxtURL, index=False)
                enc = CSVO.getFileEncoding(self.ChangeTxtURL)
                self.pt4.importCSV(self.ChangeTxtURL, encoding=enc)
                # DF型変換------------------------------
                PandasAstype(self.pt4.model.df)
                # --------------------------------------
                options = {"fontsize": self.t_font[1]}
                config.apply_options(options, self.pt4)
                self.pt4.update()
                self.pt4.show()
                # テキスト変換設定フレームを配置(サブメニューにもコピー配置)
                tke.FrameChangeremoveEntry(self)
                tke.FrameChangeEntries(self)

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
            pt4df.to_csv(self.ChangeTxtURL, index=False, quoting=QUOTE_NONNUMERIC)
            enc = CSVO.getFileEncoding(self.ChangeTxtURL)
            self.pt4.importCSV(self.ChangeTxtURL, encoding=enc)
            # DF型変換------------------------------
            PandasAstype(self.pt4.model.df)
            # --------------------------------------
            options = {"fontsize": self.t_font[1]}
            config.apply_options(options, self.pt4)
            self.pt4.update()
            self.pt4.show()
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
            # ------------------------------------------------------------------------------
            enc = CSVO.getFileEncoding(self.JounalFileName)  # 自動仕訳出力先CSVURL
            self.pt2.importCSV(self.JounalFileName, encoding=enc)  # 自動仕訳出力先CSVURL
            # DF型変換------------------------------
            PandasAstype(self.pt2.model.df)
            # --------------------------------------
            options = {"fontsize": self.t_font[1]}
            config.apply_options(options, self.pt2)
            self.pt2.update()
            self.pt2.show()
            # ------------------------------------------------------------------------------
            enc = CSVO.getFileEncoding(self.FileName)  # OCR結果CSVURL
            self.pt.importCSV(self.FileName, encoding=enc)  # OCR結果CSVURL
            # DF型変換------------------------------
            PandasAstype(self.pt.model.df)
            # --------------------------------------
            options = {"fontsize": self.t_font[1]}
            config.apply_options(options, self.pt)
            self.pt.update()
            self.pt.show()
            # ------------------------------------------------------------------------------
            enc = CSVO.getFileEncoding(self.AJSeturl)
            self.pt3.importCSV(self.AJSeturl, encoding=enc)
            # DF型変換------------------------------
            PandasAstype(self.pt3.model.df)
            # --------------------------------------
            options = {"fontsize": self.t_font[1]}
            config.apply_options(options, self.pt3)
            self.pt3.update()
            self.pt3.show()
            # ------------------------------------------------------------------------------
            self.DG_Sub_Frame.pack_forget()
            self.GetTxt_ChangeEntry(1)
            self.DG_Main_Frame.pack(expand=True)
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
            # ------------------------------------------------------------------------------
            if self.ChangeTxtURL != "":
                if os.path.isfile(self.ChangeTxtURL) is True:
                    enc = CSVO.getFileEncoding(self.ChangeTxtURL)
                    self.pt4.importCSV(self.ChangeTxtURL, encoding=enc)
                    # DF型変換------------------------------
                    PandasAstype(self.pt4.model.df)
                    # --------------------------------------
                    options = {"fontsize": self.t_font[1]}
                    config.apply_options(options, self.pt4)
                    self.pt4.update()
                    self.pt4.show()
            # ------------------------------------------------------------------------------
            if self.FileName != "":
                if os.path.isfile(self.FileName) is True:
                    enc = CSVO.getFileEncoding(self.FileName)  # OCR結果CSVURL
                    self.pt5.importCSV(self.FileName, encoding=enc)  # OCR結果CSVURL
                    # DF型変換------------------------------
                    PandasAstype(self.pt5.model.df)
                    # --------------------------------------
                    options = {"fontsize": self.t_font[1]}
                    config.apply_options(options, self.pt5)
                    self.pt5.update()
                    self.pt5.show()
            # ------------------------------------------------------------------------------
            if self.Roolurl != "":
                if os.path.isfile(self.Roolurl) is True:
                    enc = CSVO.getFileEncoding(self.Roolurl)  # ミロク元帳CSVURL
                    self.pt6.importCSV(self.Roolurl, encoding=enc)  # ミロク元帳CSVURL
                    # DF型変換------------------------------
                    PandasAstype(self.pt6.model.df)
                    # --------------------------------------
                    options = {"fontsize": self.t_font[1]}
                    config.apply_options(options, self.pt6)
                    self.pt6.update()
                    self.pt6.show()
            # ------------------------------------------------------------------------------
            self.DG_Main_Frame.pack_forget()
            # self.GetTxt_ChangeEntry(0)
            self.DG_Sub_Frame.pack(expand=True)
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
            dir = os.getcwd()
            self.JounalFileName = tk.filedialog.askopenfilename(
                filetypes=typ, initialdir=dir
            )  # ファイル指定ダイアログ
            try:
                enc = CSVO.getFileEncoding(self.JounalFileName)
                self.pt2.importCSV(self.JounalFileName, encoding=enc)
                # DF型変換------------------------------
                PandasAstype(self.pt2.model.df)
                # --------------------------------------
                options = {"fontsize": self.t_font[1]}
                config.apply_options(options, self.pt2)
                self.pt2.update()
                self.pt2.show()
                # self.JounalFileName = fle  # 自動仕訳出力先CSVURL
                self.Label_OutURL.delete(0, tk.END)
                self.Label_OutURL.insert(0, self.JounalFileName)  # 自動仕訳出力先CSVURL
            except:
                DG_DGF.create_Frame2(self, self.t_font)  # 出力表フレーム
                self.Label_OutURL.delete(0, tk.END)
                self.Label_OutURL.insert(0, self.JounalFileName)  # 自動仕訳出力先CSVURL
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
            dir = os.getcwd()
            self.Roolurl = tk.filedialog.askopenfilename(
                filetypes=typ, initialdir=dir
            )  # ファイル指定ダイアログ
            self.setRool()
            try:
                enc = CSVO.getFileEncoding(self.Roolurl)
                self.pt3.importCSV(self.Roolurl, encoding=enc)
                # DF型変換------------------------------
                PandasAstype(self.pt3.model.df)
                # --------------------------------------
                options = {"fontsize": self.t_font[1]}
                config.apply_options(options, self.pt3)
                self.motoDF = self.pt3.model.df
                self.pt3.update()
                self.pt3.show()
                self.Label_ChangeURL.delete(0, tk.END)
                self.Label_ChangeURL.insert(0, self.Roolurl)  # ミロク元帳CSVURL
            except:
                DG_DGF.create_Frame3(self, self.t_font)  # 出力表フレーム
                self.Label_ChangeURL.delete(0, tk.END)
                self.Label_ChangeURL.insert(0, self.Roolurl)  # ミロク元帳CSVURL
        except:
            tk.messagebox.showinfo("確認", "ミロク元帳CSVの出力に失敗しました。\n参照先のURLが正しいか確認してください。")

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
            dir = os.getcwd()
            self.FileName = tk.filedialog.askopenfilename(
                filetypes=typ, initialdir=dir
            )  # ファイル指定ダイアログ
            try:
                enc = CSVO.getFileEncoding(self.FileName)
                self.pt.importCSV(self.FileName, encoding=enc)
                # DF型変換------------------------------
                PandasAstype(self.pt.model.df)
                # --------------------------------------
                options = {"fontsize": self.t_font[1]}
                config.apply_options(options, self.pt)
                self.pt.update()
                self.pt.show()
                self.Label_URL.delete(0, tk.END)
                self.Label_URL.insert(0, self.FileName)  # OCR結果CSVURL
            except:
                DG_DGF.create_Frame(self, self.t_font)  # 出力表フレーム
                self.Label_URL.delete(0, tk.END)
                self.Label_URL.insert(0, self.FileName)  # OCR結果CSVURL
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
            # DF型変換------------------------------
            PandasAstype(self.pt3.model.df)
            # --------------------------------------
            options = {"fontsize": self.t_font[1]}
            config.apply_options(options, self.pt3)
            self.motoDF = self.pt3.model.df
            self.pt3.update()
            self.pt3.show()
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
            # self.DG_Main_Frame.pack_forget()

    # -------------------------------------------------------------------------------------
    def AJ_copyCalc(self):
        """
        仕訳候補の転記
        """
        try:
            if self.pt3.startrow is None:
                if len(self.pt3.model.df) == 0:
                    tk.messagebox.showinfo("確認", "仕訳予想結果のセルが選択されていません。")
                else:
                    self.AJ_copyCalc_Sub()
            else:
                if self.pt2.startrow is None:
                    if len(self.pt2.model.df) == 0:
                        self.pt2.startrow = 0
                        self.AJ_copyCalc_Sub()
                    else:
                        tk.messagebox.showinfo("確認", "作成仕訳表の挿入位置が選択されていません。")
                else:
                    self.AJ_copyCalc_Sub()
        except:
            tk.messagebox.showinfo("確認", "エラーです。自動仕訳実行後に仕訳予想結果のセルを選択し、実行してください。")

    # -------------------------------------------------------------------------------------
    def AJ_copyCalc_Sub(self):
        """
        仕訳候補の転記(Sub)
        """
        try:
            self.HidukeColNo  # 日付列番号
            HidukeColNostr = str(self.HidukeColNo).replace("['", "").replace("']", "")
            self.HidukeColName  # 日付列名
            self.AJL  # インポート用変換列名
            self.AJR  # OCR表変換列名
            self.SyutuName  # 出金列名
            # -----------------------------------------------------------
            # OCR結果の列名検索で金額のみ入っている列を特定する
            ptCol = np.array(self.pt.model.df.columns)
            ptarr = np.array(self.pt.model.df)
            # -----------------------------------------------------------
            pt2Col = np.array(self.pt2.model.df.columns)
            pt2arr = np.array(self.pt2.model.df)
            # -----------------------------------------------------------
            pt3Col = np.array(self.pt3.model.df.columns)
            pt3arr = np.array(self.pt3.model.df)
            pt3List = []
            # -----------------------------------------------------------
            if self.pt3.startrow == self.pt3.endrow:
                AJRNo = 0
                Money = ""
                for AJRItem in self.AJR:
                    # OCR表の金額列調査-----------------------
                    ptwhere = np.where(AJRItem == ptCol)
                    ptwherestr = str(ptwhere[0][0] + 1)
                    C_Val = ptarr[self.pt.startrow, ptwhere]
                    C_Val = C_Val[0][0]
                    IC = IntCheck(C_Val)
                    if IC is True:
                        Money = C_Val
                for AJRItem in self.AJR:
                    # OCR表の金額列調査-----------------------
                    ptwhere = np.where(AJRItem == ptCol)
                    ptwherestr = str(ptwhere[0][0] + 1)
                    C_Val = ptarr[self.pt.startrow, ptwhere]
                    C_Val = C_Val[0][0]
                    IC = IntCheck(C_Val)
                    # 日付列と金額列への処理-----------------------------
                    if ptwherestr == HidukeColNostr:
                        # 日付列として指定した処理の場合
                        AJLItem = self.AJL[AJRNo]
                        pt3where = np.where(AJLItem == pt3Col)
                        AJC = AJ.ChangeD_Txt(C_Val)  # 日付文字列の変換
                        if AJC[0] is True:
                            C_Val = AJC[1]
                            pt3arr[self.pt3.startrow, pt3where] = C_Val
                    elif IC is True:
                        pt3where = np.where(self.AJL[AJRNo] == pt3Col)
                        pt3arr[self.pt3.startrow, pt3where] = Money
                    elif IC is False:
                        pt3where = np.where(self.AJL[AJRNo] == pt3Col)
                        pt3arr[self.pt3.startrow, pt3where] = Money
                    # --------------------------------------------------
                    AJRNo += 1
                Money = ""
                pt3List.append(list(pt3arr[self.pt3.startrow]))
            else:
                for s_e_r in range(self.pt3.startrow, self.pt3.endrow + 1):
                    AJRNo = 0
                    Money = ""
                    for AJRItem in self.AJR:
                        # OCR表の金額列調査-----------------------
                        ptwhere = np.where(AJRItem == ptCol)
                        ptwherestr = str(ptwhere[0][0] + 1)
                        C_Val = ptarr[self.pt.startrow, ptwhere]
                        C_Val = C_Val[0][0]
                        IC = IntCheck(C_Val)
                        if IC is True:
                            Money = C_Val
                    for AJRItem in self.AJR:
                        # OCR表の金額列調査-----------------------
                        ptwhere = np.where(AJRItem == ptCol)
                        ptwherestr = str(ptwhere[0][0] + 1)
                        C_Val = ptarr[self.pt.startrow, ptwhere]
                        C_Val = C_Val[0][0]
                        IC = IntCheck(C_Val)
                        # 日付列と金額列への処理-----------------------------
                        if ptwherestr == HidukeColNostr:
                            # 日付列として指定した処理の場合
                            AJLItem = self.AJL[AJRNo]
                            pt3where = np.where(AJLItem == pt3Col)
                            AJC = AJ.ChangeD_Txt(C_Val)  # 日付文字列の変換
                            if AJC[0] is True:
                                C_Val = AJC[1]
                                pt3arr[s_e_r, pt3where] = C_Val
                        elif IC is True:
                            pt3where = np.where(self.AJL[AJRNo] == pt3Col)
                            pt3arr[s_e_r, pt3where] = Money
                        elif IC is False:
                            pt3where = np.where(self.AJL[AJRNo] == pt3Col)
                            pt3arr[s_e_r, pt3where] = Money
                        # --------------------------------------------------
                        AJRNo += 1
                    Money = ""
                    pt3List.append(list(pt3arr[self.pt3.startrow]))
            pt3List = np.array(pt3List)
            if pt2arr.shape[0] == 0:
                pt2arr = pt3arr
            else:
                pt2arr = np.insert(pt2arr, self.pt2.startrow, pt3List, axis=0)
            FinalList = np.vstack((pt2Col, pt2arr))
            FinalList = list(FinalList)
            # ------------------------------------------------------------------
            enc = CSVO.getFileEncoding(self.JounalFileName)  # 自動仕訳出力先CSVURL
            with open(
                self.JounalFileName, "wt", encoding=enc, newline=""
            ) as fout:  # 自動仕訳出力先CSVURL
                # ライター（書き込み者）を作成
                writer = csv.writer(fout)
                writer.writerows(FinalList)
            self.pt2.importCSV(self.JounalFileName, encoding=enc)  # 自動仕訳出力先CSVURL
            # DF型変換------------------------------
            PandasAstype(self.pt2.model.df)
            # --------------------------------------
            options = {"fontsize": self.t_font[1]}
            config.apply_options(options, self.pt2)
            self.pt2.update()
            self.pt2.show()
            return True
        except:
            return False

    # -----------------------------------------------------------------------------------------
    def npDaysSort(self, Finddf):
        """
        元帳を現在日時から指定月数以内にソート
        """

        today = date.today()
        DS = self.Hani.get()
        if DS != "":  # 抽出月範囲を判定
            DS = DS.replace("['", "").replace("']", "")
            next_Month = relativedelta(months=int(DS))
            D = today - next_Month

            FinddfCol = Finddf.columns  # 元帳DFの列名
            Finddf = np.array(Finddf)  # 元帳DFをnp変換
            ind = np.where(FinddfCol == str(self.Moto_Day.get()))  # 元帳DFの日付列番号
            F_Data = Finddf[1 : Finddf.shape[0], :]  # 元帳DFData
            Finddf_Date = Finddf[1 : Finddf.shape[0], ind]  # 元帳DFの日付列のみ抽出
            Finddf_Date_Dim = Finddf_Date.flatten()  # 元帳DFの日付列を1次元化
            Finddf_Date = pd.Series(Finddf_Date_Dim)  # 1次元化した元帳DFの日付列をシリーズ化
            Finddf_Date = Finddf_Date.astype("datetime64")  # シリーズ化した元帳DFの日付列を型変換
            convert_time = Finddf_Date.dt.month  # シリーズ化した元帳DFの日付列から月のみ抽出
            convert_time = np.array(convert_time)

            ind = np.where(convert_time >= int(D.month))  # 元帳DFの日付列番号
            F_Data = F_Data[ind]
            # Ret_Data = np.vstack([FinddfCol, F_Data])
            Ret_Data = pd.DataFrame(F_Data, columns=FinddfCol)
            return Ret_Data
        else:
            return Finddf

    # -----------------------------------------------------------------------------------------
    def ValChange(self, AJ_List):
        """
        元帳を現在日時から指定月数以内にソート
        """
        try:
            AJ_List = np.array(AJ_List)
            AJ_head = AJ_List[0, :]
            AJ = AJ_List[1:, :]
            AJKariMoney = AJ[:, self.Moto_KariMoney_No]
            AJKashiMoney = AJ[:, self.Moto_KashiMoney_No]
            r = 0
            for AJKariMoneyItem in AJKariMoney:
                try:
                    int(AJKariMoneyItem)
                    AJKashiMoney[r] = AJKariMoney[r]
                except:
                    AJKariMoney[r] = AJKashiMoney[r]
                r += 1
            AJ[:, self.Moto_KariMoney_No] = AJKariMoney
            AJ[:, self.Moto_KashiMoney_No] = AJKashiMoney
            R_AJ = np.vstack((AJ_head, AJ))
            R_AJ = list(R_AJ)
            return R_AJ
        except:
            return AJ_List

    # -----------------------------------------------------------------------------------------
    def MoneyCheck(self, AJnp, L_CName_c, R_CName_c):
        """
        OCR結果の金額列を確認入替
        """
        try:
            var = int(AJnp[L_CName_c])
            return var
        except:
            var = int(AJnp[R_CName_c])
            return var

    # -----------------------------------------------------------------------------------------
    def AJCheck(self):
        if os.path.isfile(self.FileName) is False:
            tk.messagebox.showinfo("戻る", "OCR抽出表が存在しません。")
            return False
        if os.path.isfile(self.Roolurl) is False:
            tk.messagebox.showinfo("戻る", "ミロク元帳が存在しません。")
            return False
        if os.path.isfile(self.ChangeTxtURL) is False:
            tk.messagebox.showinfo("戻る", "変換ルールが存在しません。")
            return False
        else:
            return True

    # -----------------------------------------------------------------------------------------
    def AJAllCalc(self):
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

        try:
            # 検索対象月間を判定
            # try:
            #     if self.Hani.get() != "":
            #         int(self.Hani.get())  # 抽出月範囲を判定
            #         Finddf = self.npDaysSort(self.pt6.model.df)
            #         self.pt6.model.df = Finddf
            #     else:
            #         print("DF空白")
            # except:
            #     tk.messagebox.showinfo("確認", "抽出月範囲に数値・空白以外が入っています。")
            #     return
            if self.AJCheck() is False:
                return
            # ##########################################################################
            sv = int(self.SortVar.get())
            st = 0  # 行ポジション
            # OCR表に対する列設定読込---------------------------------------------------
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
            # ------------------------------------------------------------------------
            FileNameenc = CSVO.getFileEncoding(self.FileName)
            Roolurlenc = CSVO.getFileEncoding(self.Roolurl)
            ChangeTxtURLenc = CSVO.getFileEncoding(self.ChangeTxtURL)
            # Entry要素設定-------------------------------------------------------------------
            JS = self.tomlEntries[JS_var].get()  # 自動仕訳基準列名Entry取得
            D = self.tomlEntries[Day_var].get()  # 日付列Entry取得
            I = self.tomlEntries[In_var].get()  # 入金列名Entry取得
            O = self.tomlEntries[Out_var].get()  # 出金列名Entry取得
            # --------------------------------------------------------------------------------
            # 自動仕訳判定条件の集計-----------------------------------------------------------
            CTE = 0
            OJ = 1
            MJ = 1
            OCRList = []
            MJSList = []
            OCRms = []
            MJSms = []
            for CTEItem in self.ChangeTxtEntries:
                ms = CTEItem.get()
                if np.mod(CTE, 2) == 0:
                    OCRList.append(ms)
                    OCRms.append("条件" + str(OJ) + ":" + ms)
                    OJ += 1
                else:
                    MJSList.append(ms)
                    MJSms.append("条件" + str(MJ) + ":" + ms)
                    MJ += 1
                CTE += 1
            OCRTxt = ",".join(OCRms)
            MJSTxt = ",".join(MJSms)
            Messagebox = tk.messagebox.askquestion(
                "再計算",
                "OCR結果の[" + OCRTxt + "]列と\nミロク元帳の[" + MJSTxt + "]列を\n条件に仕訳検索を行いますか？",
                icon="warning",
            )
            # --------------------------------------------------------------------------------
            if Messagebox == "yes":  # If関数
                # プログレスバー起動##########################################################
                self.PBAR = PB.Open(tk.Toplevel())  # プログレスバー起動
                AJ_List = AJ.AllChange(
                    self.Moto_Tekiyou.get(),
                    self.HidukeColName,
                    self.Moto_Day.get(),
                    self.Moto_KariMoney_No,
                    self.Moto_KashiMoney_No,
                    self.Moto_Karikata.get(),  # 元帳借方科目列名
                    self.Moto_Kashikata.get(),  # 元帳貸方科目列名
                    self.FileName,  # OCR結果CSVURL
                    FileNameenc,
                    self.Roolurl,  # ミロク元帳CSVURL
                    Roolurlenc,
                    self.ChangeTxtURL,
                    ChangeTxtURLenc,
                    I,
                    O,
                    OCRList,
                    MJSList,
                    sv,
                    self.motoDF,
                    self.PBAR,
                )  # 仕訳候補を抽出
                PT_ColList = np.array(self.pt.model.df.columns)  # OCR抽出結果表の列名リスト
                PT_List = np.array(self.pt.model.df)
                PT_List = list(PT_List)  # OCR抽出結果表の列名リスト
                # データ内のFalse,nan処理--------------------------------------------
                if AJ_List[0] is True:
                    AJ_Column = AJ_List[1]
                    AJ_List = AJ_List[2]
                    self.PBAR_c = 20 / len(self.Frame7EntL)
                    # OCR抽出結果表の値を変換ルールに従って自動仕訳表に代入--------------------
                    for r in range(len(self.Frame7EntL)):
                        L_CName = self.Frame7EntL[r].get()
                        R_CName = self.Frame7EntR[r].get()
                        L_CName_c = int(
                            np.where(AJ_Column == L_CName)[0]
                        )  # 自動仕訳表の列番号検索
                        R_CName_c = int(
                            np.where(PT_ColList == R_CName)[0]
                        )  # OCR抽出結果表の列番号検索
                        # ヘッダー行処理##################################################
                        for L_r in range(len(AJ_List)):
                            if L_r == 12:
                                print("")
                            AJnp = np.array(AJ_List[L_r])
                            lenAJ = len(AJ_List[L_r])  # 次元数確認
                            RowElement = AJnp.ndim  # 次元数確認
                            if RowElement == 2 and lenAJ == 1:
                                # ########################################################
                                # 一行の仕訳###############################################
                                # ########################################################
                                if (R_CName == I) or (R_CName == O):
                                    # 数値確認-------------------------------------------
                                    Var = self.MoneyCheck(AJnp[0], L_CName_c, R_CName_c)
                                    AJtxt = AJ_List[L_r]
                                    AJtxt = AJtxt[0][L_CName_c]
                                    C_Txt = AJ.TxtEdit(
                                        L_CName,
                                        AJtxt,
                                        Var,
                                    )
                                    AJ_List[L_r][0][R_CName_c] = C_Txt[1]
                                    # ---------------------------------------------------
                                else:
                                    Var = PT_List[L_r][R_CName_c]
                                    AJtxt = AJ_List[L_r]
                                    AJtxt = AJtxt[0][L_CName_c]
                                    C_Txt = AJ.TxtEdit(
                                        L_CName,
                                        AJtxt,
                                        Var,
                                    )
                                    AJ_List[L_r][0][L_CName_c] = C_Txt[1]
                            elif RowElement == 2 and lenAJ != 1:
                                # ########################################################
                                # 複数行の仕訳#############################################
                                # ########################################################
                                # 複合仕訳の金額計算
                                if (R_CName == I) or (R_CName == O):
                                    # 数値確認-------------------------------------------
                                    try:
                                        Var = self.MoneyCheck(
                                            AJnp[0], L_CName_c, R_CName_c
                                        )
                                        AJtxt = AJ_List[L_r]
                                        # 複合仕訳の金額割合摘要関数
                                        AJ.MoneyCalc(
                                            L_r,
                                            AJ_List,
                                            AJtxt,
                                            R_CName,
                                            L_CName,
                                            L_CName_c,
                                            Var,
                                        )
                                    except:
                                        if R_CName == I:
                                            R_CName = O
                                        elif R_CName == O:
                                            R_CName = I
                                            R_CName_c = int(
                                                np.where(PT_ColList == R_CName)[0]
                                            )  # OCR抽出結果表の列番号検索
                                        # ----------------------------------------
                                        Var = int(PT_List[L_r][R_CName_c])
                                        AJtxt = AJ_List[L_r]
                                        # 複合仕訳の金額割合摘要関数
                                        AJ.MoneyCalc(
                                            L_r,
                                            AJ_List,
                                            AJtxt,
                                            R_CName,
                                            L_CName,
                                            L_CName_c,
                                            Var,
                                        )
                                    # ---------------------------------------------------
                                else:
                                    Var = PT_List[L_r][R_CName_c]
                                    AJtxt = AJ_List[L_r]
                                    # 複合仕訳の金額割合摘要関数
                                    AJ.MoneyCalc(
                                        L_r,
                                        AJ_List,
                                        AJtxt,
                                        R_CName,
                                        L_CName,
                                        L_CName_c,
                                        Var,
                                    )
                            else:
                                # ########################################################
                                # 一次元一行の仕訳#########################################
                                # ########################################################
                                Var = PT_List[L_r][R_CName_c]
                                C_Txt = AJ.TxtEdit(
                                    L_CName,
                                    Var,
                                    Var,
                                )
                                AJ_List[L_r][L_CName_c] = C_Txt[1]
                        # ################################################################
                        self.PBAR._target.step(self.PBAR_c)  # プログレスバー更新
                    # ################################################################
                    # 適正次元に処理し、リスト化
                    FinalList = []
                    self.PBAR_c = 20 / len(AJ_List)
                    for L_r in range(len(AJ_List)):
                        AJnp = np.array(AJ_List[L_r])
                        lenAJ = len(AJ_List[L_r])  # 次元数確認
                        RowElement = AJnp.ndim  # 次元数確認
                        if RowElement == 2 and lenAJ == 1:
                            A_Row = list(AJ_List[L_r][0])
                            FinalList.append(A_Row)
                        elif RowElement == 2 and lenAJ != 1:
                            for lenAJ_r in range(lenAJ):
                                A_Row = AJ_List[L_r][lenAJ_r]
                                A_Row = list(A_Row)
                                FinalList.append(A_Row)
                        else:
                            A_Row = list(AJ_List[L_r])
                            FinalList.append(A_Row)
                        # ################################################################
                        self.PBAR._target.step(self.PBAR_c)  # プログレスバー更新
                    # ################################################################
                    FinalList = np.array(FinalList)
                    FinalList = np.vstack((AJ_Column, FinalList))  # ヘッダーと結合
                    FinalList = list(FinalList)
                    # ################################################################
                    PiriDel(FinalList)
                    self.PBAR_c = 20 / len(self.RepLEntries)
                    # 月分等の置換変更処理
                    for i in range(len(self.RepLEntries)):
                        ReplaceKey = self.RepLEntries[i].get()
                        Repstr = self.RepREntries[i].get()
                        lenFL = len(FinalList)
                        for F_r in range(lenFL):
                            if F_r != 0:
                                FL_Row = FinalList[F_r]
                                for F_c in range(len(FL_Row)):
                                    FL_Var = FinalList[F_r][F_c]
                                    if ReplaceKey in FL_Var:
                                        try:
                                            FSTR = str(FinalList[F_r][F_c])
                                            FinalList[F_r][F_c] = FSTR.replace(
                                                ReplaceKey, Repstr
                                            )
                                        except:
                                            print("置換変更無し")
                        # ################################################################
                        self.PBAR._target.step(self.PBAR_c)  # プログレスバー更新
                    # ------------------------------------------------------------------
                    FinalList = self.ValChange(FinalList)  # 金額が文字列の場合変更
                    # ------------------------------------------------------------------
                    with open(
                        self.JounalFileName, "wt", encoding="cp932", newline=""
                    ) as fout:
                        # ライター（書き込み者）を作成
                        writer = csv.writer(fout)
                        writer.writerows(FinalList)
                    enc = CSVO.getFileEncoding(self.JounalFileName)
                    self.pt2.importCSV(self.JounalFileName, encoding=enc)
                    # DF型変換------------------------------
                    PandasAstype(self.pt2.model.df)
                    # --------------------------------------
                    options = {"fontsize": self.t_font[1]}
                    config.apply_options(options, self.pt2)
                    self.pt2.update()
                    self.pt2.show()
                    self.PBAR._target.master.destroy()  # プログレスバー更新
                    tk.messagebox.showinfo("確認", "自動仕訳完了です。")
                else:
                    self.PBAR._target.master.destroy()  # プログレスバー更新
                    tk.messagebox.showinfo("戻る", "アプリケーション画面に戻ります")
        except:
            self.PBAR._target.master.destroy()  # プログレスバー更新
            tk.messagebox.showinfo("確認", "仕訳一致率に数値以外が入っています。")

    # -----------------------------------------------------------------------------------------
    def AJCalc(self):
        """
        DGFrame.py
        ↓
        def create_SettingFrame(self)
        ↓
        self.AJ_Btn
        bind関数
        """
        global AJSeturl

        try:
            # # 検索対象月間を判定
            # try:
            #     if self.Hani.get() != "":
            #         int(self.Hani.get())  # 抽出月範囲を判定
            #         Finddf = self.npDaysSort(self.pt6.model.df)
            #         self.pt6.model.df = Finddf
            #     else:
            #         print("DF空白")
            # except:
            #     tk.messagebox.showinfo("確認", "抽出月範囲に数値・空白以外が入っています。")
            #     return
            if self.AJCheck() is False:
                return
            sv = int(self.SortVar.get())
            if self.pt.startrow is None:
                tk.messagebox.showinfo("確認", "OCR抽出結果表のセルが選択されていません。")
            else:
                Moto_Tekiyou = self.Moto_Tekiyou.get()  # 元帳摘要列名
                Moto_Day = self.Moto_Day.get()  # 元帳日付列名
                Moto_Karikata = self.Moto_Karikata.get()  # 元帳借方科目列名
                Moto_Kashikata = self.Moto_Kashikata.get()  # 元帳貸方科目列名
                st = 0  # 行ポジション
                # OCR表に対する列設定読込---------------------------------------------------
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
                # ------------------------------------------------------------------------
                FileNameenc = CSVO.getFileEncoding(self.FileName)  # OCR表のエンコード取得
                Roolurlenc = CSVO.getFileEncoding(self.Roolurl)  # ミロク元帳のエンコード取得
                ChangeTxtURLenc = CSVO.getFileEncoding(
                    self.ChangeTxtURL
                )  # テキスト変換設定のエンコード取得
                # Entry要素設定-------------------------------------------------------------------
                JS = self.tomlEntries[JS_var].get()  # 自動仕訳基準列名Entry取得
                D = self.tomlEntries[Day_var].get()  # 日付列Entry取得
                I = self.tomlEntries[In_var].get()  # 入金列名Entry取得
                O = self.tomlEntries[Out_var].get()  # 出金列名Entry取得
                # --------------------------------------------------------------------------------
                # 自動仕訳判定条件の集計-----------------------------------------------------------
                CTE = 0
                OJ = 1
                MJ = 1
                OCRList = []
                MJSList = []
                OCRms = []
                MJSms = []
                for CTEItem in self.ChangeTxtEntries:
                    ms = CTEItem.get()
                    if np.mod(CTE, 2) == 0:
                        OCRList.append(ms)
                        OCRms.append("条件" + str(OJ) + ":" + ms)
                        OJ += 1
                    else:
                        MJSList.append(ms)
                        MJSms.append("条件" + str(MJ) + ":" + ms)
                        MJ += 1
                    CTE += 1
                OCRTxt = ",".join(OCRms)
                MJSTxt = ",".join(MJSms)
                Messagebox = tk.messagebox.askquestion(
                    "再計算",
                    "OCR結果の["
                    + OCRTxt
                    + "]列と\nミロク元帳の["
                    + MJSTxt
                    + "]列を\n条件に[単一]の仕訳検索を行いますか？",
                    icon="warning",
                )
                # --------------------------------------------------------------------------------
                if Messagebox == "yes":  # If関数
                    print(self.Label_ChangeURL.get())  # toml金融機関Entry取得
                    dfs = self.pt.model.df  # グリッドをDF化
                    dfsrow = dfs.iloc[self.pt.startrow]  # DF行データ
                    # グリッド選択データの代入---------------------------------------------------------
                    # FindTxt = dfsrow[JS]  # 検索文字
                    # D_var = dfsrow[D]  # 日付
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
                        for r in range(len(self.AJR)):
                            if tkm[3] == "入金":
                                if self.AJR[r] == "出金":
                                    AJ_Key = self.AJL[r]
                                # elif self.AJR[r] == "入金":
                                #     AJ_RefKey = self.AJL[r]
                            elif tkm[3] == "出金":
                                if self.AJR[r] == "入金":
                                    AJ_Key = self.AJL[r]
                                # elif self.AJR[r] == "出金":
                                #     AJ_RefKey = self.AJL[r]

                        AJ_List = AJ.main(
                            self.pt.startrow,
                            Moto_Tekiyou,
                            self.HidukeColName,
                            Moto_Day,
                            self.Moto_KariMoney_No,
                            self.Moto_KashiMoney_No,
                            Moto_Karikata,
                            Moto_Kashikata,
                            self.FileName,  # OCR結果CSVURL
                            FileNameenc,
                            self.Roolurl,  # ミロク元帳CSVURL
                            Roolurlenc,
                            self.ChangeTxtURL,
                            ChangeTxtURLenc,
                            I,
                            O,
                            OCRList,
                            MJSList,
                            sv,
                            self.motoDF,
                        )  # 仕訳候補を抽出

                        PT_ColList = np.array(
                            self.pt.model.df.columns
                        )  # OCR抽出結果表の列名リスト
                        PT_List = np.array(self.pt.model.df)
                        PT_List = list(PT_List)  # OCR抽出結果表の列名リスト
                        # データ内のFalse,nan処理--------------------------------------------
                        if AJ_List[0] is True:
                            AJ_Column = AJ_List[1]
                            AJ_List = AJ_List[2]
                            CalcFlag = True
                            # 取得リストの次元調整############################################
                            BJnp = np.array(AJ_List)
                            RowElement = BJnp.ndim  # 次元数確認
                            while RowElement > 1:
                                BJnp = np.array(BJnp[0])
                                RowElement = BJnp.ndim  # 次元数確認
                            lenAJ = len(BJnp)  # 次元数確認
                            for BJ_ListItem in BJnp:
                                if "自動仕訳候補なし" in BJ_ListItem:
                                    CalcFlag = False
                                    break
                            # ################################################################
                            if CalcFlag is True:
                                # OCR抽出結果表の値を変換ルールに従って自動仕訳表に代入--------------------
                                for r in range(len(self.Frame7EntL)):
                                    L_CName = self.Frame7EntL[r].get()
                                    R_CName = self.Frame7EntR[r].get()
                                    L_CName_c = int(
                                        np.where(AJ_Column == L_CName)[0]
                                    )  # 自動仕訳表の列番号検索
                                    R_CName_c = int(
                                        np.where(PT_ColList == R_CName)[0]
                                    )  # OCR抽出結果表の列番号検索
                                    L_r = self.pt.startrow + 1
                                    # 取得リストの次元調整############################################
                                    AJnp = np.array(AJ_List)
                                    RowElement = AJnp.ndim  # 次元数確認
                                    while RowElement > 2:
                                        AJnp = np.array(AJnp[0])
                                        RowElement = AJnp.ndim  # 次元数確認
                                    lenAJ = len(AJnp)  # 次元数確認
                                    # ###############################################################
                                    if RowElement == 1 and lenAJ == 1:
                                        # ########################################################
                                        # 一行の仕訳###############################################
                                        # ########################################################
                                        AJ_List = AJnp
                                        if (R_CName == I) or (R_CName == O):
                                            # 数値確認-------------------------------------------
                                            try:
                                                Var = self.MoneyCheck(
                                                    AJnp[0], L_CName_c, R_CName_c
                                                )
                                                AJtxt = AJ_List[L_r]
                                                AJtxt = AJtxt[0][L_CName_c]
                                                C_Txt = AJ.TxtEdit(
                                                    L_CName,
                                                    AJtxt,
                                                    Var,
                                                )
                                                if L_CName == AJ_Key:
                                                    AJ_List[0][L_CName_c] = I_var
                                                else:
                                                    AJ_List[0][L_CName_c] = C_Txt[1]
                                            except:
                                                if R_CName == I:
                                                    R_CName = O
                                                elif R_CName == O:
                                                    R_CName = I
                                                    R_CName_c = int(
                                                        np.where(PT_ColList == R_CName)[
                                                            0
                                                        ]
                                                    )  # OCR抽出結果表の列番号検索
                                                # ----------------------------------------
                                                Var = int(PT_List[L_r][R_CName_c])
                                                AJtxt = AJ_List[L_r]
                                                AJtxt = AJtxt[0][L_CName_c]
                                                C_Txt = AJ.TxtEdit(
                                                    L_CName,
                                                    AJtxt,
                                                    Var,
                                                )
                                                if L_CName == AJ_Key:
                                                    AJ_List[0][L_CName_c] = I_var
                                                else:
                                                    AJ_List[0][L_CName_c] = C_Txt[1]
                                            # ---------------------------------------------------
                                        else:
                                            Var = PT_List[L_r][R_CName_c]
                                            AJtxt = AJ_List[L_r]
                                            AJtxt = AJtxt[0][L_CName_c]
                                            C_Txt = AJ.TxtEdit(
                                                L_CName,
                                                AJtxt,
                                                Var,
                                            )
                                            if L_CName == AJ_Key:
                                                AJ_List[0][L_CName_c] = I_var
                                            else:
                                                AJ_List[0][L_CName_c] = C_Txt[1]
                                    elif RowElement == 2 and lenAJ != 1:
                                        # ########################################################
                                        # 複数行の仕訳#############################################
                                        # ########################################################
                                        # AJ_List = list(AJnp)
                                        # 複合仕訳の金額計算
                                        if (R_CName == I) or (R_CName == O):
                                            # 数値確認-------------------------------------------
                                            try:
                                                Var = int(
                                                    PT_List[self.pt.startrow][R_CName_c]
                                                )
                                                AJtxt = AJ_List[0]
                                                # 複合仕訳の金額割合摘要関数
                                                AJ.MoneyCalc(
                                                    0,
                                                    AJ_List,
                                                    AJtxt,
                                                    R_CName,
                                                    L_CName,
                                                    L_CName_c,
                                                    Var,
                                                )
                                            except:
                                                if R_CName == I:
                                                    R_CName = O
                                                elif R_CName == O:
                                                    R_CName = I
                                                    R_CName_c = int(
                                                        np.where(PT_ColList == R_CName)[
                                                            0
                                                        ]
                                                    )  # OCR抽出結果表の列番号検索
                                                if tkm[3] == "入金" and R_CName_c != (
                                                    Out_var - 1
                                                ):
                                                    Var = int(
                                                        PT_List[self.pt.startrow][
                                                            R_CName_c
                                                        ]
                                                    )
                                                    AJtxt = AJ_List[0]
                                                    # 複合仕訳の金額割合摘要関数
                                                    AJ.MoneyCalc(
                                                        0,
                                                        AJ_List,
                                                        AJtxt,
                                                        R_CName,
                                                        L_CName,
                                                        L_CName_c,
                                                        Var,
                                                    )
                                                elif tkm[3] == "出金" and R_CName_c != (
                                                    In_var - 1
                                                ):
                                                    Var = int(
                                                        PT_List[self.pt.startrow][
                                                            R_CName_c
                                                        ]
                                                    )
                                                    AJtxt = AJ_List[0]
                                                    # 複合仕訳の金額割合摘要関数
                                                    AJ.MoneyCalc(
                                                        0,
                                                        AJ_List,
                                                        AJtxt,
                                                        R_CName,
                                                        L_CName,
                                                        L_CName_c,
                                                        Var,
                                                    )
                                                elif tkm[3] == "入金" and R_CName_c == (
                                                    Out_var - 1
                                                ):
                                                    print("入金スキップ")
                                                elif tkm[3] == "出金" and R_CName_c == (
                                                    In_var - 1
                                                ):
                                                    print("出金スキップ")
                                                else:
                                                    Var = int(
                                                        PT_List[self.pt.startrow][
                                                            R_CName_c
                                                        ]
                                                    )
                                                    AJtxt = AJ_List[0]
                                                    # 複合仕訳の金額割合摘要関数
                                                    AJ.MoneyCalc(
                                                        0,
                                                        AJ_List,
                                                        AJtxt,
                                                        R_CName,
                                                        L_CName,
                                                        L_CName_c,
                                                        Var,
                                                    )
                                                # --------------------------------------------------------
                                        else:
                                            # --------------------------------------------------------
                                            if tkm[3] == "入金" and R_CName_c != (
                                                Out_var - 1
                                            ):
                                                Var = PT_List[self.pt.startrow][
                                                    R_CName_c
                                                ]
                                                AJtxt = AJ_List[0]
                                                # 複合仕訳の金額割合摘要関数
                                                AJ.MoneyCalc(
                                                    0,
                                                    AJ_List,
                                                    AJtxt,
                                                    R_CName,
                                                    L_CName,
                                                    L_CName_c,
                                                    Var,
                                                )
                                            elif tkm[3] == "出金" and R_CName_c != (
                                                In_var - 1
                                            ):
                                                Var = PT_List[self.pt.startrow][
                                                    R_CName_c
                                                ]
                                                AJtxt = AJ_List[0]
                                                # 複合仕訳の金額割合摘要関数
                                                AJ.MoneyCalc(
                                                    0,
                                                    AJ_List,
                                                    AJtxt,
                                                    R_CName,
                                                    L_CName,
                                                    L_CName_c,
                                                    Var,
                                                )
                                            elif tkm[3] == "入金" and R_CName_c == (
                                                Out_var - 1
                                            ):
                                                print("入金スキップ")
                                            elif tkm[3] == "出金" and R_CName_c == (
                                                In_var - 1
                                            ):
                                                print("出金スキップ")
                                            else:
                                                Var = PT_List[self.pt.startrow][
                                                    R_CName_c
                                                ]
                                                AJtxt = AJ_List[0]
                                                # 複合仕訳の金額割合摘要関数
                                                AJ.MoneyCalc(
                                                    0,
                                                    AJ_List,
                                                    AJtxt,
                                                    R_CName,
                                                    L_CName,
                                                    L_CName_c,
                                                    Var,
                                                )
                                    else:
                                        # ########################################################
                                        # 一次元一行の仕訳#########################################
                                        # ########################################################
                                        AJ_List = AJnp
                                        # --------------------------------------------------------
                                        if tkm[3] == "入金":
                                            Var = PT_List[self.pt.startrow][R_CName_c]
                                            C_Txt = AJ.TxtEdit(
                                                L_CName,
                                                Var,
                                                Var,
                                            )
                                            if L_CName == AJ_Key:
                                                AJ_List[0][L_CName_c] = I_var
                                            else:
                                                AJ_List[0][L_CName_c] = C_Txt[1]
                                        elif tkm[3] == "出金":
                                            Var = PT_List[self.pt.startrow][R_CName_c]
                                            C_Txt = AJ.TxtEdit(
                                                L_CName,
                                                Var,
                                                Var,
                                            )
                                            if L_CName == AJ_Key:
                                                AJ_List[0][L_CName_c] = O_var
                                            else:
                                                AJ_List[0][L_CName_c] = C_Txt[1]
                                        else:
                                            Var = PT_List[self.pt.startrow][R_CName_c]
                                            C_Txt = AJ.TxtEdit(
                                                L_CName,
                                                Var,
                                                Var,
                                            )
                                            AJ_List[0][L_CName_c] = C_Txt[1]
                                        # --------------------------------------------------------
                                # ################################################################
                                # 適正次元に処理し、リスト化
                                FinalList = []
                                for L_r in range(len(AJ_List)):
                                    AJnp = np.array(AJ_List[L_r])
                                    lenAJ = len(AJ_List[L_r])  # 次元数確認
                                    RowElement = AJnp.ndim  # 次元数確認
                                    if RowElement == 2 and lenAJ == 1:
                                        A_Row = list(AJ_List[L_r][0])
                                        FinalList.append(A_Row)
                                    elif RowElement == 2 and lenAJ != 1:
                                        for lenAJ_r in range(lenAJ):
                                            A_Row = AJ_List[L_r][lenAJ_r]
                                            A_Row = list(A_Row)
                                            FinalList.append(A_Row)
                                    else:
                                        A_Row = list(AJ_List[L_r])
                                        FinalList.append(A_Row)
                                # ################################################################
                                FinalList = np.array(FinalList)
                                FinalList = np.vstack((AJ_Column, FinalList))  # ヘッダーと結合
                                FinalList = list(FinalList)
                                # ################################################################
                                PiriDel(FinalList)
                                # 月分等の置換変更処理
                                for i in range(len(self.RepLEntries)):
                                    ReplaceKey = self.RepLEntries[i].get()
                                    Repstr = self.RepREntries[i].get()
                                    lenFL = len(FinalList)
                                    for F_r in range(lenFL):
                                        if F_r != 0:
                                            FL_Row = FinalList[F_r]
                                            for F_c in range(len(FL_Row)):
                                                FL_Var = FinalList[F_r][F_c]
                                                if ReplaceKey in FL_Var:
                                                    try:
                                                        FSTR = str(FinalList[F_r][F_c])
                                                        FinalList[F_r][
                                                            F_c
                                                        ] = FSTR.replace(
                                                            ReplaceKey, Repstr
                                                        )
                                                    except:
                                                        print("置換変更無し")
                                # ------------------------------------------------------------------
                                AJDF = pd.DataFrame(FinalList)
                                AJDF.to_csv(
                                    self.AJSeturl,
                                    index=False,
                                    header=False,
                                    quoting=QUOTE_NONNUMERIC,
                                )
                                enc = CSVO.getFileEncoding(self.AJSeturl)
                                self.pt3.importCSV(self.AJSeturl, encoding=enc)
                                # DF型変換------------------------------
                                PandasAstype(self.pt3.model.df)
                                # --------------------------------------
                                options = {"fontsize": self.t_font[1]}
                                config.apply_options(options, self.pt3)
                                self.pt3.update()
                                self.pt3.show()
                        else:
                            tk.messagebox.showinfo("確認", "仕訳検索結果がありません。\n元帳全行表示を行います。")
                            self.pt3.importCSV(
                                self.Roolurl, encoding=Roolurlenc
                            )  # ミロク元帳CSVURL
                            # DF型変換------------------------------
                            PandasAstype(self.pt3.model.df)
                            # --------------------------------------
                            options = {"fontsize": self.t_font[1]}
                            config.apply_options(options, self.pt3)
                            self.pt3.update()
                            self.pt3.show()
        except:
            tk.messagebox.showinfo("確認", "仕訳一致率に数値以外が入っています。")

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
        enc = CSVO.getFileEncoding(self.FileName)  # OCR結果CSVURL
        with open(self.FileName, "r", encoding=enc) as f:  # csv読込み(Treeview 表示用)
            reader = csv.reader(f, delimiter=",", quotechar='"')
            for cells in reader:
                self.ColumnName = cells
                break
        enc = CSVO.getFileEncoding(self.JounalFileName)  # 自動仕訳出力先CSVURL
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

        self.master.destroy()
        Master.deiconify()

    # ------------------------------------------------------------------------------


#############################################################################################
# 以下関数
#############################################################################################
def PandasAstype(P_df):
    """
    Pandasデータフレーム型変換
    """
    # DF型変換------------------------------
    ptc = P_df.columns
    for ptcItem in ptc:
        ptc_n = P_df[ptcItem].dtype
        if "float" == ptc_n.name:
            P_df[ptcItem].astype(int)
        elif "float64" == ptc_n.name:
            P_df[ptcItem] = P_df[ptcItem].fillna(0)
            P_df[ptcItem] = P_df[ptcItem].astype(int)
            P_df[ptcItem] = P_df[ptcItem].astype(str)
            P_df[ptcItem] = P_df[ptcItem].replace("0", "")
    # --------------------------------------


# -----------------------------------------------------------------------------------------
def PiriDel(FinalList):
    """
    CSVファイル最終調整
    """

    for F_r in range(len(FinalList)):
        FinalListRow = FinalList[F_r]
        if F_r != 0:
            for F_c in range(len(FinalListRow)):
                F_Var = FinalList[F_r][F_c]
                if "." in F_Var:
                    try:
                        float(F_Var)
                        F_Varsp = F_Var.split(".")
                        FinalList[F_r][F_c] = F_Varsp[0]
                    except ValueError:
                        print("")


# -----------------------------------------------------------------------------------------
def DTS(FL_Var):
    import datetime

    try:
        dte = datetime.datetime.strptime(FL_Var, "%Y/%m/%d")
        return str(dte.month)
    except:
        try:
            dte = datetime.datetime.strptime(FL_Var, "%Y-%m-%d")
            return str(dte.month)
        except:
            try:
                dte = datetime.datetime.strptime(FL_Var, "%Y.%m.%d")
                return str(dte.month)
            except:
                try:
                    dte = datetime.datetime.strptime(FL_Var, "%Y_%m_%d")
                    return str(dte.month)
                except:
                    return ""


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
def BeforeNGFT(url, enc):
    try:
        file = open(url, "r", encoding=enc)
        file_data = file.read()
        file.close()
        print(file_data)
        prc = pd.read_csv(StringIO(file_data), quotechar='"', skipinitialspace=True)
        pdHeaders = prc.columns
        prcList = np.array(prc)
        ReturnList = np.vstack((pdHeaders, prcList))  # ヘッダーと結合
        return ReturnList
    except:
        tk.messagebox.showinfo("確認", "元帳読込エラーです。\n文字列がクォーテーションで囲まれているか確認してください。")
        return ""


# -----------------------------------------------------------------------------------------
def Main(self, Mas, filename, J_File, A_File, R_Url, C_Url, BT, BTURL):
    # root = tk.Tk()  # Window生成
    global Master
    Master = Mas
    root = tk.Toplevel()  # Window生成
    data = IconCode.icondata()
    root.tk.call("wm", "iconphoto", root._w, tk.PhotoImage(data=data, master=root))
    app = DataGrid(filename, J_File, A_File, R_Url, C_Url, BT, BTURL, master=root)
    # --- 基本的な表示準備 ----------------

    app.mainloop()


# -----------------------------------------------------------------------------------------
if __name__ == "__main__":
    global AJurl, AJSeturl, Roolurl, ChangeTxtURL
    global csvurl, Banktoml, BanktomlUrl, DaySet, MoneySet, ReplaceSet, ReplaceStr, ColNameList

    DaySet = ["1"]
    MoneySet = ["3,4,5"]
    ReplaceSet = ["2,3,4"]
    ReplaceStr = ["CDカード", "マツモトトソウテン", "ザンダカショウメイショ"]
    # ColNameList = ["日付", "摘要", "出金", "入金", "残高"]  # OCR出力列名
    # ColNameList = ["日付", "摘要", "入金", "摘要", "出金", "摘要"]  # OCR出力列名
    csvurl = r"D:\OCRTESTPDF\PDFTEST\1869\1869_9page.csv"
    AJurl = r"D:\OCRTESTPDF\PDFTEST\1869\1869_9page_AutoJounal.csv"
    AJSeturl = r"D:\OCRTESTPDF\PDFTEST\1869\AJSet.csv"
    Roolurl = r"D:\OCRTESTPDF\PDFTEST\1869\1869_仕訳日記帳.csv"
    ChangeTxtURL = r"D:\OCRTESTPDF\PDFTEST\1869\1869ChangeTxtList.csv"

    enc = CSVO.getFileEncoding(ChangeTxtURL)  # 摘要変換ルールエンコード
    ColNameList_np = BeforeNGFT(ChangeTxtURL, enc)
    # ColNameList_np = np.genfromtxt(
    #     ChangeTxtURL, dtype=None, encoding=enc, delimiter=","
    # )  # 元帳CSVをnp配列に変換
    ColNameList = ColNameList_np[0, :]
    ColNameList = list(ColNameList)
    BanktomlUrl = r"D:\OCRTESTPDF\PDFTEST\1869\Setting.toml"
    # toml読込------------------------------------------------------------------------------
    with open(BanktomlUrl, encoding="utf-8") as f:
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
