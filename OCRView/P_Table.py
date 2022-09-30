import tkinter as tk
import Frame.DGFrame as DGF
import numpy as np
import WarekiHenkan as wh
import pandas as pd
import re
import math

###################################################################################################
class Application(tk.Frame):
    def __init__(self, csvurl, master=None):
        # Windowの初期設定を行う。
        super().__init__(master)
        # Windowの画面サイズを設定する。
        G_logger.debug("P_Table起動")  # Log出力
        s = tk.ttk.Style()
        s.theme_use("clam")
        ########################################
        wid = 2.25  # width割率
        hei = 1.5  # width割率
        ########################################
        self.FileName = csvurl
        self.master.geometry("1480x750+0+0")  # Window表示位置指定
        self.master.minsize(1480, 750)
        self.master.protocol("WM_DELETE_WINDOW", self.click_close)  # 閉じる処理設定
        # 統合フレーム
        self.Main_Frame = tk.Frame(self.master, width=1480, height=750, bd=2)
        self.Main_Frame.pack(fill=tk.BOTH, expand=True)
        # self.Main_Frame.grid(row=0, column=0, sticky=tk.NSEW)
        # サイドフレーム
        self.Side_Frame = tk.Frame(
            self.Main_Frame, width=330, height=750, bd=2, relief=tk.RIDGE
        )
        self.Side_Frame.grid(row=1, column=0, columnspan=2, sticky=tk.NSEW)
        # # サイドフレーム2
        # self.Side_Frame2 = tk.Frame(
        #     self.Main_Frame, width=330, height=750, bd=2, relief=tk.RIDGE
        # )
        # self.Side_Frame2.grid(row=1, column=1, sticky=tk.NSEW)
        ########################################################################################
        # フレーム設定---------------------------------------------------------------------
        DGF.create_Frame(self, int(1480 / wid), int(750 / hei))  # OCR抽出結果表フレーム
        # Side_Sub##############################################################################
        self.Side_Sub = tk.Frame(
            self.Side_Frame, width=330, height=750, bd=2, relief=tk.RIDGE
        )
        self.Side_Sub.grid(row=1, column=0, sticky=tk.NSEW)
        tk.Label(self.Side_Sub, text="日付列名").grid(row=0, column=0)  # 日付列名ラベル
        self.DStxt = tk.Entry(self.Side_Sub, width=35, bg="snow")  # 日付列名テキストボックス
        self.DStxt.insert(0, "")  # 日付列名テキストボックスに文字代入
        self.DStxt.grid(row=0, column=1, sticky=tk.W)  # 日付列名テキストボックス配置
        fonts = ("", 10)
        PN = tk.PhotoImage(
            file=r"D:\PythonScript\RPAScript\RPAPhoto\MJS_SystemNextCreate\THI.png"
        )
        PN = PN.zoom(3, 3)
        self.DSbtn = tk.Button(
            self.Side_Sub,
            text="選択列名転記",
            fg="White",
            command=self.DSSetClick,
            # bg="orangered3",
            font=fonts,
            width=300,
            height=30,
            image=PN,
            compound="center",
        )  # ボタン作成
        self.DSbtn.grid(row=0, column=2, padx=5)
        # --------------------------------------------------------------------------------
        tk.Label(self.Side_Sub, text="出金列名").grid(row=1, column=0)  # 出金列名ラベル
        self.OMtxt = tk.Entry(self.Side_Sub, width=35, bg="snow")  # 出金列名テキストボックス
        self.OMtxt.insert(0, "")  # 出金列名テキストボックスに文字代入
        self.OMtxt.grid(row=1, column=1, sticky=tk.W)  # 出金列名テキストボックス配置
        fonts = ("", 10)
        self.OMbtn = tk.Button(
            self.Side_Sub,
            text="選択列名転記",
            fg="White",
            command=self.OutMoneyClick,
            bg="orangered3",
            font=fonts,
            width=12,
            height=1,
        )  # ボタン作成
        self.OMbtn.grid(row=1, column=2, padx=5)
        # --------------------------------------------------------------------------------
        tk.Label(self.Side_Sub, text="入金列名").grid(row=2, column=0)  # 入金列名ラベル
        self.IMtxt = tk.Entry(self.Side_Sub, width=35, bg="snow")  # 入金列名テキストボックス
        self.IMtxt.insert(0, "")  # 入金列名テキストボックスに文字代入
        self.IMtxt.grid(row=2, column=1, sticky=tk.W)  # 入金列名テキストボックス配置
        fonts = ("", 10)
        self.IMbtn = tk.Button(
            self.Side_Sub,
            text="選択列名転記",
            fg="White",
            command=self.InMoneyClick,
            bg="orangered3",
            font=fonts,
            width=12,
            height=1,
        )  # ボタン作成
        self.IMbtn.grid(row=2, column=2, padx=5)
        # 比較対象ファイル複数選択-----------------------------------------------------------
        self.FileRead = tk.Button(
            self.Side_Sub,
            text="比較対象ファイル複数選択",
            fg="White",
            command=self.ChangeFileRead,
            bg="steelblue3",
            font=1,
            width=30,
            height=1,
        )  # ボタン作成
        self.FileRead.grid(
            row=3, column=0, columnspan=3, padx=10, sticky=tk.N
        )  # 日付列名テキストボックス配置
        # 比較対象ファイル追加---------------------------------------------------------------
        self.SingleFileRead = tk.Button(
            self.Side_Sub,
            text="比較対象ファイル追加",
            fg="White",
            command=self.ChangeFileSingleRead,
            bg="Orange",
            font=1,
            width=30,
            height=1,
        )  # ボタン作成
        self.SingleFileRead.grid(
            row=4, column=0, columnspan=3, padx=10, sticky=tk.N
        )  # 日付列名テキストボックス配置
        # #######################################################################################
        # Side_Sub2##############################################################################
        self.Side_Sub2 = tk.Frame(
            self.Side_Frame, width=330, height=750, bd=2, relief=tk.RIDGE
        )
        self.Side_Sub2.grid(row=1, column=1, sticky=tk.NSEW)
        # 比較対象ファイルリストボックス------------------------------------------------------
        tk.Label(self.Side_Sub2, text="比較対象ファイル").grid(row=0, column=3)  # 比較対象ファイルラベル
        self.module = ""
        self.listbox_var = tk.StringVar(value=self.module)
        self.listbox = tk.Listbox(
            self.Side_Sub2, width=60, listvariable=self.listbox_var
        )
        self.listbox.grid(row=1, rowspan=4, column=3, padx=30, sticky=tk.NSEW)
        # #######################################################################################
        # Side_Sub3##############################################################################
        self.Side_Sub3 = tk.Frame(
            self.Side_Frame, width=330, height=750, bd=2, relief=tk.RIDGE
        )
        self.Side_Sub3.grid(row=1, column=2, sticky=tk.NSEW)
        # 列名テキストボックス--------------------------------------------------------------
        tk.Label(self.Side_Sub3, text="OCR抽出結果表列名").grid(
            row=0, column=4
        )  # OCR抽出結果表列名ラベル
        self.OCR_col = tk.Entry(
            self.Side_Sub3, width=35, bg="snow"
        )  # OCR抽出結果表列名テキストボックス
        try:
            print(self.pt.model.df.columns)
            OCR_colStr = ",".join(self.pt.model.df.columns)
            self.OCR_col.insert(0, OCR_colStr)  # OCR抽出結果表列名テキストボックスに文字代入
        except:
            self.OCR_col.insert(0, "")  # OCR抽出結果表列名テキストボックスに文字代入
        self.OCR_col.bind("<Return>", self.OCRtxtCol)
        self.OCR_col.grid(row=0, column=5, sticky=tk.W)  # OCR抽出結果表列名テキストボックス配置
        # 列名テキストボックス--------------------------------------------------------------
        tk.Label(self.Side_Sub3, text="比較ファイル列名").grid(row=1, column=4)  # 入金列名ラベル
        self.Diff_col = tk.Entry(self.Side_Sub3, width=35, bg="snow")  # 入金列名テキストボックス
        try:
            print(self.pt2.model.df.columns)
            Diff_colStr = ",".join(self.pt2.model.df.columns)
            self.Diff_col.insert(0, Diff_colStr)  # OCR抽出結果表列名テキストボックスに文字代入
        except:
            self.Diff_col.insert(0, "")  # OCR抽出結果表列名テキストボックスに文字代入
        self.Diff_col.bind("<Return>", self.DifftxtCol)
        self.Diff_col.grid(row=1, column=5, sticky=tk.W)  # 入金列名テキストボックス配置
        # 検索開始ボタン--------------------------------------------------------------------
        self.SearchBtn = tk.Button(
            self.Side_Frame,
            text="検索開始",
            fg="White",
            command=self.SearchStart,
            bg="indianred1",
            font=1,
            width=23,
            height=1,
        )  # ボタン作成
        self.SearchBtn.grid(
            row=1, column=3, pady=10, padx=10, sticky=tk.NSEW
        )  # 日付列名テキストボックス配置
        # フレーム設定---------------------------------------------------------------------
        DGF.create_Frame2(
            self, int(1480 / wid), int(750 / hei), list(self.module), G_logger
        )  # OCR抽出結果表フレーム

    # -------------------------------------------------------------------------------------
    def DifftxtCol(self, event):
        """
        OCR列名更新
        """
        ColList = self.Diff_col.get().split(",")
        if len(self.pt2.model.df.columns) == len(ColList):
            self.pt2.model.df.columns = ColList
            self.pt2.show()
        else:
            tk.messagebox.showinfo("確認", "指定列名数と比較ファイルの列数が一致しません。再確認してください。")

    # -------------------------------------------------------------------------------------
    def OCRtxtCol(self, event):
        """
        OCR列名更新
        """
        ColList = self.OCR_col.get().split(",")
        if len(self.pt.model.df.columns) == len(ColList):
            self.pt.model.df.columns = ColList
            self.pt.show()
        else:
            tk.messagebox.showinfo("確認", "指定列名数とOCR表の列数が一致しません。再確認してください。")

    # -------------------------------------------------------------------------------------
    def OutMoneyClick(self):
        """
        出金列指定
        """
        C_n = self.pt.model.df.columns[self.pt.currentcol]
        self.OMtxt.delete(0, tk.END)
        self.OMtxt.insert(0, C_n)

    # -------------------------------------------------------------------------------------
    def InMoneyClick(self):
        """
        入金列指定
        """
        C_n = self.pt.model.df.columns[self.pt.currentcol]
        self.IMtxt.delete(0, tk.END)
        self.IMtxt.insert(0, C_n)

    # -------------------------------------------------------------------------------------
    def DSSetClick(self):
        """
        日付列指定
        """
        C_n = self.pt.model.df.columns[self.pt.currentcol]
        self.DStxt.delete(0, tk.END)
        self.DStxt.insert(0, C_n)

    # -------------------------------------------------------------------------------------
    def InMCheck(self, InM_col, InM_col2):
        """
        検索開始
        """
        try:
            ptIn = np.array(self.pt.model.df)[:, InM_col]
            ptCol = np.array(self.pt.model.df.columns)
            pt2In = np.array(self.pt2.model.df)[:, InM_col2]
            pt2Col = np.array(self.pt2.model.df.columns)
            for r in range(ptIn.shape[0]):
                txt = ptIn[r]
                if type(txt) != float:
                    ptIn[r] = re.sub(r"\D", "", txt)
            for r in range(pt2In.shape[0]):
                txt = pt2In[r]
                if type(txt) != float:
                    pt2In[r] = re.sub(r"\D", "", txt)
            pt = np.array(self.pt.model.df)
            pt2 = np.array(self.pt2.model.df)
            pt[:, InM_col] = ptIn
            pt2[:, InM_col2] = pt2In
            pt = pd.DataFrame(pt, columns=ptCol)
            pt2 = pd.DataFrame(pt2, columns=pt2Col)
            self.pt.model.df = pt
            self.pt2.model.df = pt2
            self.pt.show()
            self.pt2.show()
        except:
            tk.messagebox.showinfo("確認", "入金列の書式整理エラーです。")

    # -------------------------------------------------------------------------------------
    def OutMCheck(self, OutM_col, OutM_col2):
        """
        検索開始
        """
        try:
            ptOut = np.array(self.pt.model.df)[:, OutM_col]
            ptCol = np.array(self.pt.model.df.columns)
            pt2Out = np.array(self.pt2.model.df)[:, OutM_col2]
            pt2Col = np.array(self.pt2.model.df.columns)
            for r in range(ptOut.shape[0]):
                txt = ptOut[r]
                if type(txt) != float:
                    ptOut[r] = re.sub(r"\D", "", txt)
            for r in range(pt2Out.shape[0]):
                txt = pt2Out[r]
                if type(txt) != float:
                    pt2Out[r] = re.sub(r"\D", "", txt)
            pt = np.array(self.pt.model.df)
            pt2 = np.array(self.pt2.model.df)
            pt[:, OutM_col] = ptOut
            pt2[:, OutM_col2] = pt2Out
            pt = pd.DataFrame(pt, columns=ptCol)
            pt2 = pd.DataFrame(pt2, columns=pt2Col)
            self.pt.model.df = pt
            self.pt2.model.df = pt2
            self.pt.show()
            self.pt2.show()
        except:
            tk.messagebox.showinfo("確認", "出金列の書式整理エラーです。")

    # -------------------------------------------------------------------------------------
    def DaysCheck(self, Day_col, Day_col2):
        """
        日付列の形式を揃える
        """
        try:
            ptDay = np.array(self.pt.model.df)[:, Day_col]
            ptCol = np.array(self.pt.model.df.columns)
            pt2Day = np.array(self.pt2.model.df)[:, Day_col2]
            pt2Col = np.array(self.pt2.model.df.columns)
            for r in range(ptDay.shape[0]):
                txt = self.ChangeD_Txt(ptDay[r])
                ptDay[r] = txt[1]
            for r in range(pt2Day.shape[0]):
                txt = self.ChangeD_Txt(pt2Day[r])
                pt2Day[r] = txt[1]
            pt = np.array(self.pt.model.df)
            pt2 = np.array(self.pt2.model.df)
            pt[:, Day_col] = ptDay
            pt2[:, Day_col2] = pt2Day
            pt = pd.DataFrame(pt, columns=ptCol)
            pt2 = pd.DataFrame(pt2, columns=pt2Col)
            self.pt.model.df = pt
            self.pt2.model.df = pt2
            self.pt.show()
            self.pt2.show()
        except:
            tk.messagebox.showinfo("確認", "日付列の書式整理エラーです。")

    # -------------------------------------------------------------------------------------
    def ChangeD_Txt(self, Txt):
        """
        日付西暦和暦変換
        """
        try:
            # 日付文字列の変換-----------------------------------------------------
            if "-" in Txt:
                TxtSP = Txt.split("-")
                T_Nen = len(TxtSP[0])
                if T_Nen <= 2:
                    print("和暦")
                    D_str = (
                        "令和"
                        + str(TxtSP[0])
                        + "年"
                        + str(TxtSP[1])
                        + "月"
                        + str(TxtSP[2])
                        + "日"
                    )
                    D_str = wh.SeirekiSTRDate(D_str)
                elif T_Nen <= 4:
                    print("西暦")
                    D_str = TxtSP[0] + "/" + TxtSP[1].zfill(2) + "/" + TxtSP[2].zfill(2)
                else:
                    print("西暦")
            elif "/" in Txt:
                TxtSP = Txt.split("/")
                T_Nen = len(TxtSP[0])
                if T_Nen <= 2:
                    print("和暦")
                    D_str = (
                        "令和"
                        + str(TxtSP[0])
                        + "年"
                        + str(TxtSP[1])
                        + "月"
                        + str(TxtSP[2])
                        + "日"
                    )
                    D_str = wh.SeirekiSTRDate(D_str)
                elif T_Nen <= 4:
                    print("西暦")
                    D_str = TxtSP[0] + "/" + TxtSP[1].zfill(2) + "/" + TxtSP[2].zfill(2)
                else:
                    print("西暦")
            elif "_" in Txt:
                TxtSP = Txt.split("_")
                T_Nen = len(TxtSP[0])
                if T_Nen <= 2:
                    print("和暦")
                    D_str = (
                        "令和"
                        + str(TxtSP[0])
                        + "年"
                        + str(TxtSP[1])
                        + "月"
                        + str(TxtSP[2])
                        + "日"
                    )
                    D_str = wh.SeirekiSTRDate(D_str)
                elif T_Nen <= 4:
                    print("西暦")
                    D_str = TxtSP[0] + "/" + TxtSP[1].zfill(2) + "/" + TxtSP[2].zfill(2)
                else:
                    print("西暦")
            elif "." in Txt:
                TxtSP = Txt.split(".")
                T_Nen = len(TxtSP[0])
                if T_Nen <= 2:
                    print("和暦")
                    D_str = (
                        "令和"
                        + str(TxtSP[0])
                        + "年"
                        + str(TxtSP[1])
                        + "月"
                        + str(TxtSP[2])
                        + "日"
                    )
                    D_str = wh.SeirekiSTRDate(D_str)
                elif T_Nen <= 4:
                    print("西暦")
                    D_str = TxtSP[0] + "/" + TxtSP[1].zfill(2) + "/" + TxtSP[2].zfill(2)
                else:
                    print("西暦")
            return True, D_str
        except:
            return False, ""

    # ---------------------------------------------------------------------
    def SearchStart(self):
        """
        検索開始
        """
        try:
            print(self.pt2.model.df.columns)
            ptcol = np.array(self.pt.model.df.columns)
            Day_col = int(np.where(ptcol == self.DStxt.get())[0])
            OutM_col = int(np.where(ptcol == self.OMtxt.get())[0])
            InM_col = int(np.where(ptcol == self.IMtxt.get())[0])
            ptcol2 = np.array(self.pt2.model.df.columns)
            Day_col2 = int(np.where(ptcol2 == self.DStxt.get())[0])
            OutM_col2 = int(np.where(ptcol2 == self.OMtxt.get())[0])
            InM_col2 = int(np.where(ptcol2 == self.IMtxt.get())[0])
            ptarray = np.array(self.pt.model.df)
            for c in range(ptarray.shape[1]):
                if c == Day_col:
                    self.DaysCheck(Day_col, Day_col2)
                elif c == OutM_col:
                    self.OutMCheck(OutM_col, OutM_col2)
                elif c == InM_col:
                    self.InMCheck(InM_col, InM_col2)
            self.PtSearch(Day_col, Day_col2, OutM_col, OutM_col2, InM_col, InM_col2)
        except:
            tk.messagebox.showinfo("確認", "比較ファイルが指定されていません。")

    # ---------------------------------------------------------------------
    def PtSearch(self, Day_col, Day_col2, OutM_col, OutM_col2, InM_col, InM_col2):
        """
        検索開始
        """
        try:
            pt = np.array(self.pt.model.df)

            ptCol = list(self.pt.model.df.columns)
            pt2 = np.array(self.pt2.model.df)
            pt_r_list = np.array(self.pt.model.df)[:, 0]
            for r in range(pt.shape[0]):
                if pt[r, OutM_col] == pt[r, OutM_col]:
                    if pt[r, OutM_col] != "" and pt[r, OutM_col] != float("nan"):
                        ptstr = pt[r, Day_col] + pt[r, OutM_col]
                        for rr in range(pt2.shape[0]):
                            if pt2[rr, InM_col2] == pt2[rr, InM_col2]:
                                pt2str = pt2[rr, Day_col2] + pt2[rr, InM_col2]
                                if ptstr == pt2str:
                                    pt_r_list[r] = rr + 1
                                    break
                                else:
                                    pt_r_list[r] = ""
                    elif pt[r, InM_col] != "" and pt[r, InM_col] != float("nan"):
                        ptstr = pt[r, Day_col] + pt[r, InM_col]
                        for rr in range(pt2.shape[0]):
                            if pt2[rr, OutM_col2] == pt2[rr, OutM_col2]:
                                pt2str = pt2[rr, Day_col2] + pt2[rr, OutM_col2]
                                if ptstr == pt2str:
                                    pt_r_list[r] = rr + 1
                                    break
                                else:
                                    pt_r_list[r] = ""
            ptCol.append("比較対象行番号")
            pt_r_list = np.reshape(pt_r_list, (pt_r_list.shape[0], 1))
            pt = np.hstack([pt, pt_r_list])
            pt = pd.DataFrame(pt, columns=ptCol)
            self.pt.model.df = pt
            self.pt.show()
        except:
            tk.messagebox.showinfo("確認", "比較ファイルが指定されていません。")

    # -------------------------------------------------------------------------------------
    def ChangeFileSingleRead(self):
        """
        比較対象CSVの追加
        """
        fTyp = [("CSV", ".csv")]
        read_list = tk.filedialog.askopenfilename(filetypes=fTyp, initialdir="./")
        aplist = list(self.module)
        aplist.append(read_list)
        self.module = tuple(aplist)
        self.listbox_var.set(self.module)
        JCSV = DGF.JoinCSV(list(self.module), G_logger)
        if JCSV[0] is True:
            self.pt2.model.df = JCSV[1]
            try:
                print(self.pt2.model.df.columns)
                Diff_colStr = ",".join(self.pt2.model.df.columns)
                self.Diff_col.insert(0, Diff_colStr)  # OCR抽出結果表列名テキストボックスに文字代入
            except:
                self.Diff_col.insert(0, "")  # OCR抽出結果表列名テキストボックスに文字代入
            self.pt2.show()

    # -------------------------------------------------------------------------------------
    def ChangeFileRead(self):
        """
        比較対象CSVの複数追加
        """
        fTyp = [("CSV", ".csv")]
        read_list = tk.filedialog.askopenfilenames(filetypes=fTyp, initialdir="./")
        self.module = read_list
        self.listbox_var.set(self.module)
        JCSV = DGF.JoinCSV(list(self.module), G_logger)
        if JCSV[0] is True:
            self.pt2.model.df = JCSV[1]
            try:
                print(self.pt2.model.df.columns)
                Diff_colStr = ",".join(self.pt2.model.df.columns)
                self.Diff_col.insert(0, Diff_colStr)  # OCR抽出結果表列名テキストボックスに文字代入
            except:
                self.Diff_col.insert(0, "")  # OCR抽出結果表列名テキストボックスに文字代入
            self.pt2.show()

    # -------------------------------------------------------------------------------------
    def click_close(self):
        """
        ウィンドウ×ボタンクリック
        """
        self.top.withdraw()
        if tk.messagebox.askokcancel("確認", "終了しますか？"):
            self.top.destroy()
            self.master.destroy()
            G_logger.debug("TKINTERCV2SettingClose完了")  # Log出力
        else:
            self.top.deiconify()
            G_logger.debug("TKINTERCV2SettingClose失敗")  # Log出力


# -------------------------------------------------------------------------------------
def Main(MUI, US, tom, logger):
    """
    呼出関数
    """
    global Master, imgurl
    global G_logger
    global Banktoml, tomlurl

    Master = MUI
    imgurl = US.replace(r"\\\\", r"\\")
    Banktoml = tom
    G_logger = logger
    # -----------------------------------------------------------
    root = tk.Tk()  # Window生成
    app = Application(csvurl=imgurl, master=root)
    # --- 基本的な表示準備 ----------------

    app.mainloop()


# ------------------------------------------------------------------------------------------
if __name__ == "__main__":
    import logging.config
    import toml
    import os

    # logger設定-----------------------------------------------------------------------------------------------------
    logging.config.fileConfig(os.getcwd() + r"\LogConf\logging_debug.conf")
    G_logger = logging.getLogger(__name__)
    # ---------------------------------------------------------------------------------------------------------------

    global Banktoml, tomlurl
    URL = os.getcwd()
    imgurl = r"D:\OCRTESTPDF\PDFTEST\Hirogin_1page.png"
    tomlurl = r"D:\OCRTESTPDF\PDFTEST\Setting.toml"
    csv_u = r"D:\OCRTESTPDF\PDFTEST\Hirogin_1page_merge.csv"
    # toml読込------------------------------------------------------------------------------
    with open(tomlurl, encoding="utf-8") as f:
        Banktoml = toml.load(f)
        print(Banktoml)
    # -----------------------------------------------------------
    # -----------------------------------------------------------
    root = tk.Tk()  # Window生成
    app = Application(csvurl=csv_u, master=root)
    # --- 基本的な表示準備 ----------------

    app.mainloop()
