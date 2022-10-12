import tkinter as tk
import Frame.DGFrame as DGF
import numpy as np
import WarekiHenkan as wh
import pandas as pd
import re
import logging.config
import toml
import os
import IconCode
import customtkinter as ck
import ImageViewer
import ReplaceView
from difflib import SequenceMatcher
from mojimoji import han_to_zen
import P_Table_btn

###################################################################################################
class Application(tk.Frame):
    def __init__(self, csvurl, imgurl, master=None):
        # Windowの初期設定を行う。
        super().__init__(master)
        # Windowの画面サイズを設定する。
        G_logger.debug("P_Table起動")  # Log出力
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
        self.wid = 2.25  # width割率
        self.hei = 1.4  # width割率
        ########################################
        self.master.minsize(self.width_of_window, self.height_of_window)
        self.master.title("OCR読取 Ver:0.9-比較ウィンドウ-")
        self.master.protocol("WM_DELETE_WINDOW", self.click_close)  # 閉じる処理設定
        # 統合フレーム
        ################################################################################
        self.SideWidth = int(200 * self.wid_Par)
        self.SideHeight = int(200 * self.hei_Par)
        self.LabelWidth = int(20 * self.wid_Par)
        self.LabelHeight = int(20 * self.hei_Par)
        self.BtnWidth = int(180 * self.wid_Par)
        self.BtnHeight = int(20 * self.hei_Par)
        self.EntWidth = int(70 * self.hei_Par)
        self.EntHeight = int(20 * self.wid_Par)
        self.t_font = (1, int(10 * self.wid_Par))
        ################################################################################
        self.FileName = csvurl
        self.imgurl = imgurl
        self.G_logger = G_logger
        # 要素配置
        P_Table_btn.CreateFrame(self)
        self.pt1_OpenFlag = True
        self.pt2_OpenFlag = False

    # 以下関数----------------------------------------------------------------------
    def ReadRepView(self):
        """
        置換フレーム起動
        """
        try:
            m = self.children_get()
            m.ColumnHeader = ["変更前", "変更後"]
            self.RView.destroy()
            self.RView = ReplaceView.Main(self, self.FileName)  # 置換テーブルの読込
            # ReplaceView.CreateDB.readsql(self, self.OCR_dbname, self.OCR_tbname, m)
            self.RView.update()
        except:
            tk.messagebox.showinfo("確認", " 置換フレーム起動エラーです。")

    # ----------------------------------------------------------------------
    def children_get(self):
        """
        置換フレームからテーブル取得
        """
        try:
            m = self.RView
            m = m.children["!frame"]
            m = m.children["!frame2"]
            m = m.children["!mytablesql"]
            m.ColumnHeader = ["変更前", "変更後"]
            return m
        except:
            return False

    # -------------------------------------------------------------------------------------
    def ReadImg(self):
        """
        画像フレーム起動
        """
        try:
            if self.Img_c != 1:
                self.OCR_frame2.pack_forget()
                self.IMG_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
                try:
                    print(self.IView.master)
                except:
                    self.IView = ImageViewer.call(imgurl, self.IMG_frame)
                self.Img_c = 1
            else:
                self.IMG_frame.pack_forget()
                self.OCR_frame2.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
                self.Img_c = 0
        except:
            tk.messagebox.showinfo("確認", " 画像フレーム起動エラーです。")

    # -------------------------------------------------------------------------------------
    def radioclick(self):
        """
        ラジオボタン切替
        """
        if self.select_var.get() == 1:
            self.SplitVar.configure(bg="gray10", state="readonly")
            self.In_v.configure(bg="gray10", state="readonly")
            self.Out_v.configure(bg="gray10", state="readonly")
            self.Money_v.configure(bg="gray10", state="readonly")
            self.IMtxt.configure(bg="snow", state="normal")
            self.OMtxt.configure(bg="snow", state="normal")
            self.update()
        else:
            self.SplitVar.configure(bg="snow", state="normal")
            self.In_v.configure(bg="snow", state="normal")
            self.Out_v.configure(bg="snow", state="normal")
            self.Money_v.configure(bg="snow", state="normal")
            self.IMtxt.configure(bg="gray10", state="readonly")
            self.OMtxt.configure(bg="gray10", state="readonly")
            self.update()

    # -------------------------------------------------------------------------------------
    def DifftxtCol(self, event):
        """
        OCR列名更新
        """
        ColList = self.Diff_col.get().split(",")
        if len(self.pt2.model.df.columns) == len(ColList):
            self.pt2.model.df.columns = ColList
            DGF.Pandas_mem_usage(self.pt2.model.df)
            self.pt2.show()
        else:
            tk.messagebox.showinfo("確認", "指定列名数と比較ファイルの列数が一致しません。再確認してください。")

    # -------------------------------------------------------------------------------------
    def OCRtxtCol(self, event):
        """
        OCR列名更新
        """
        ColList = self.OCR_col.get().split(",")
        self.ColumnsDelete(self.pt)
        if len(self.pt.model.df.columns) == len(ColList):
            self.pt.model.df.columns = ColList
            DGF.Pandas_mem_usage(self.pt.model.df)
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
        入金列の書式整理
        """
        try:
            if type(InM_col2) == str:
                ptIn = np.array(self.pt.model.df)[:, InM_col]
                ptCol = np.array(self.pt.model.df.columns)
                for r in range(ptIn.shape[0]):
                    txt = ptIn[r]
                    if type(txt) != float:
                        ptIn[r] = re.sub(r"\D", "", txt)
                pt = np.array(self.pt.model.df)
                pt[:, InM_col] = ptIn
                pt = pd.DataFrame(pt, columns=ptCol)
                self.pt.model.df = pt
                DGF.Pandas_mem_usage(self.pt.model.df)
                # self.pt.show()
            else:
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
                DGF.Pandas_mem_usage(self.pt.model.df)
                # self.pt.show()
                DGF.Pandas_mem_usage(self.pt2.model.df)
                # self.pt2.show()
        except:
            tk.messagebox.showinfo("確認", "入金列の書式整理エラーです。")

    # -------------------------------------------------------------------------------------
    def OutMCheck(self, OutM_col, OutM_col2):
        """
        出金列の書式整理
        """
        try:
            if type(OutM_col2) == str:
                ptOut = np.array(self.pt.model.df)[:, OutM_col]
                ptCol = np.array(self.pt.model.df.columns)
                for r in range(ptOut.shape[0]):
                    txt = ptOut[r]
                    if type(txt) != float:
                        ptOut[r] = re.sub(r"\D", "", txt)
                pt = np.array(self.pt.model.df)
                pt[:, OutM_col] = ptOut
                pt = pd.DataFrame(pt, columns=ptCol)
                self.pt.model.df = pt
                DGF.Pandas_mem_usage(self.pt.model.df)
                # self.pt.show()
            else:
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
                DGF.Pandas_mem_usage(self.pt.model.df)
                # self.pt.show()
                DGF.Pandas_mem_usage(self.pt2.model.df)
                # self.pt2.show()
        except:
            tk.messagebox.showinfo("確認", "出金列の書式整理エラーです。")

    # -------------------------------------------------------------------------------------
    def DaysCheck(self, Day_col, Day_col2):
        """
        日付列の形式を揃える
        """
        try:
            if type(Day_col2) == str:
                ptDay = np.array(self.pt.model.df)[:, Day_col]
                ptCol = np.array(self.pt.model.df.columns)
                for r in range(ptDay.shape[0]):
                    txt = self.ChangeD_Txt(ptDay[r])
                    if txt[0] is True:
                        ptDay[r] = txt[1]
                pt = np.array(self.pt.model.df)
                pt[:, Day_col] = ptDay
                pt = pd.DataFrame(pt, columns=ptCol)
                self.pt.model.df = pt
                DGF.Pandas_mem_usage(self.pt.model.df)
                # self.pt.show()
            else:
                ptDay = np.array(self.pt.model.df)[:, Day_col]
                ptCol = np.array(self.pt.model.df.columns)
                pt2Day = np.array(self.pt2.model.df)[:, Day_col2]
                pt2Col = np.array(self.pt2.model.df.columns)
                for r in range(ptDay.shape[0]):
                    txt = self.ChangeD_Txt(ptDay[r])
                    if txt[0] is True:
                        ptDay[r] = txt[1]
                for r in range(pt2Day.shape[0]):
                    txt = self.ChangeD_Txt(pt2Day[r])
                    if txt[0] is True:
                        pt2Day[r] = txt[1]
                pt = np.array(self.pt.model.df)
                pt2 = np.array(self.pt2.model.df)
                pt[:, Day_col] = ptDay
                pt2[:, Day_col2] = pt2Day
                pt = pd.DataFrame(pt, columns=ptCol)
                pt2 = pd.DataFrame(pt2, columns=pt2Col)
                self.pt.model.df = pt
                self.pt2.model.df = pt2
                DGF.Pandas_mem_usage(self.pt.model.df)
                # self.pt.show()
                DGF.Pandas_mem_usage(self.pt2.model.df)
                # self.pt2.show()
        except:
            tk.messagebox.showinfo("確認", "日付列の書式整理エラーです。")

    # -------------------------------------------------------------------------------------
    def StrCheck(self, col, pt):
        """
        文字列の形式を揃える
        """
        try:
            code_regex = re.compile(
                "[!\"#$%&'\\\\()*+,-./:;<=>?@[\\]^_`{|}~「」〔〕“”〈〉『』【】＆＊・（）＄＃＠。、？！｀＋￥％]"
            )
            GFTable = np.array(pt.model.df)
            nptxt = np.array(pt.model.df)[:, col]
            ptCol = np.array(pt.model.df.columns)
            Before_L = np.array(self.RView_df)[:, 0]
            After_L = np.array(self.RView_df)[:, 1]
            Par = 0.5
            for r in range(nptxt.shape[0]):
                txt = nptxt[r]
                if type(txt) == str:
                    R_parList = []  # 文字列マッチングリスト初期化
                    # tomlから摘要変換リストを読込一致率50％を超えるものがあれば置換-----------------
                    for RView_r in range(Before_L.shape[0]):
                        if Before_L.shape[0] != 0:  # 置換設定読込
                            ReplaceStr = Before_L[RView_r]  # 置換設定変更前文字列読込
                            src, trg = han_to_zen(txt.lower()), han_to_zen(
                                ReplaceStr.lower()
                            )  # 半角を全角に
                            R_par = SequenceMatcher(None, src, trg).ratio()  # 文字列マッチング
                            R_parList.append([RView_r, R_par])  # 文字列マッチングリストに追加

                    R_parList = np.array(R_parList)  # 文字列マッチングリストnparray化
                    ind = np.where(R_parList[:, 1] >= Par)  # 文字列マッチングインダイス
                    # 文字列マッチングインダイスが一つになるまでループ
                    if ind[0].shape[0] != 0:
                        while ind[0].shape[0] != 1:
                            Max_r = max(R_parList[:, 1])
                            Min_r = min(R_parList[:, 1])
                            if Max_r == Min_r:
                                break
                            else:
                                ind = np.where(R_parList[:, 1] != Min_r)
                                R_parList = R_parList[ind]
                        txt = After_L[ind][0]
                        nptxt[r] = txt

            nppt = np.array(pt.model.df)
            nppt[:, col] = nptxt
            nppt_t = pd.DataFrame(nppt, columns=ptCol)

            DGF.Pandas_mem_usage(nppt_t)
            pt.model.df = nppt_t
            # pt.show()
            # pt.update()
        except:
            tk.messagebox.showinfo("確認", "文字列の書式整理エラーです。")

    # ----------------------------------------------------------------------------
    def ChangeD_Txt(self, Txt):
        """
        日付西暦和暦変換
        """
        try:
            TxtSP = re.findall(r"\d+", Txt)
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
    def EntrySelect(self, pt, r):
        """
        Entry選択
        """
        try:
            pt.setSelectedRow(r)
            pt.setSelectedCol(0)
            pt.drawSelectedRect(r, 0)
            pt.drawSelectedRow()
            x, y = pt.getCanvasPos(pt.currentrow, pt.currentcol - 1)
            rmin = pt.visiblerows[0]
            rmax = pt.visiblerows[-1] - 2
            cmax = pt.visiblecols[-1] - 1
            cmin = pt.visiblecols[0]
            FirstPos = pt.currentrow

            if x is None:
                return

            if pt.currentcol > cmax or pt.currentcol <= cmin:
                pt.xview("moveto", x)
                pt.colheader.xview("moveto", x)
                pt.redraw()

            if pt.currentrow < rmin and FirstPos == 0:
                vh = len(pt.visiblerows) / 2
                x, y = pt.getCanvasPos(pt.currentrow - vh, 0)

            if pt.currentrow >= rmax or pt.currentrow <= rmin:
                pt.yview("moveto", y)
                pt.rowheader.yview("moveto", y)
                pt.redraw()

            pt.drawSelectedRect(pt.currentrow, pt.currentcol)
            coltype = pt.model.getColumnType(pt.currentcol)
            return

        # ---------------------------------------------------------------------

        except:
            tk.messagebox.showinfo("確認", "表選択操作に失敗しました。")

    # ---------------------------------------------------------------------
    def SingleSearchStart(self):
        """
        単一通帳整理
        """
        try:
            # CL = self.ChangeList()
            # self.SinglePtSearch(CL[0], CL[1], CL[2], CL[3], CL[4], CL[5])
            self.ChangeList()
            self.SinglePtSearch()
        except:
            tk.messagebox.showinfo("確認", "比較ファイルが指定されていません。")

    # ---------------------------------------------------------------------
    def SinglePtSearch(self):
        """
        検索開始
        """
        try:
            pt = np.array(self.pt.model.df)
            pt2 = np.array(self.pt2.model.df)
            pt_r_list = np.array(self.pt.model.df)[:, 0]
            r = self.pt.startrow
            if r is None:
                tk.messagebox.showinfo("確認", "検索したいOCR抽出結果表のセルを選択してください。")
                return
            if pt[r, self.OutM_col] == pt[r, self.OutM_col]:
                if pt[r, self.OutM_col] != "" and pt[r, self.OutM_col] != float("nan"):
                    ptstr = pt[r, self.Day_col] + pt[r, self.OutM_col]
                    for rr in range(pt2.shape[0]):
                        if pt2[rr, self.InM_col2] == pt2[rr, self.InM_col2]:
                            try:
                                pt2str = pt2[rr, self.Day_col2] + pt2[rr, self.InM_col2]
                                if ptstr == pt2str:
                                    self.EntrySelect(self.pt2, r)
                                    break
                                else:
                                    pt_r_list[r] = ""
                            except:
                                pt_r_list[r] = ""
                elif pt[r, self.InM_col] != "" and pt[r, self.InM_col] != float("nan"):
                    ptstr = pt[r, self.Day_col] + pt[r, self.InM_col]
                    for rr in range(pt2.shape[0]):
                        if pt2[rr, self.OutM_col2] == pt2[rr, self.OutM_col2]:
                            try:
                                pt2str = (
                                    pt2[rr, self.Day_col2] + pt2[rr, self.OutM_col2]
                                )
                                if ptstr == pt2str:
                                    self.EntrySelect(self.pt2, r)
                                    break
                                else:
                                    pt_r_list[r] = ""
                            except:
                                pt_r_list[r] = ""
        except:
            tk.messagebox.showinfo("確認", "比較ファイルが指定されていません。")

    # ---------------------------------------------------------------------
    def ColumnsDelete(self, DF):
        """
        DF列削除
        """
        DF_Columns = DF.model.df.columns
        if (PlusCol in DF_Columns) is True:
            Col_n = int(np.where(DF_Columns == PlusCol)[0])
            npDF = np.array(DF.model.df)
            DF_Columns = DF_Columns[0:Col_n]
            npDF = npDF[:, 0:Col_n]
            Ret_DF = pd.DataFrame(npDF, columns=DF_Columns)
            DF.model.df = Ret_DF
            DF.show()

    # ---------------------------------------------------------------------
    def SearchStart(self):
        """
        検索開始
        """
        try:
            self.ColumnsDelete(self.pt)
            if len(self.pt.model.df.columns) == len(self.pt2.model.df.columns):
                try:
                    # CL = self.ChangeList()
                    # self.PtSearch(CL[0], CL[1], CL[2], CL[3], CL[4], CL[5])
                    self.ChangeList()
                    self.PtSearch()
                except:
                    tk.messagebox.showinfo("確認", "書式整理時にエラーが発生しました。")
            else:
                tk.messagebox.showinfo("確認", "OCR抽出結果表と比較ファイルの設定列数が一致しません。")
        except:
            tk.messagebox.showinfo("確認", "比較ファイルが指定されていません。")

    # ---------------------------------------------------------------------
    def PtSearch_Sub(
        self,
        r,
        pt,
        pt2,
        pt_r_list,
    ):
        try:
            # if r == 10:
            #     print("")
            if pt[r, self.OutM_col] == pt[r, self.OutM_col]:
                if pt[r, self.OutM_col] != "" and pt[r, self.OutM_col] != float("nan"):
                    ptstr = pt[r, self.Day_col] + pt[r, self.OutM_col]
                    try:
                        for rr in range(pt2.shape[0]):
                            if pt2[rr, self.InM_col2] == pt2[rr, self.InM_col2]:
                                try:
                                    pt2str = (
                                        pt2[rr, self.Day_col2] + pt2[rr, self.InM_col2]
                                    )
                                    if ptstr == pt2str:
                                        pt_r_list[r] = rr + 1
                                        break
                                    else:
                                        pt_r_list[r] = ""
                                except:
                                    pt_r_list[r] = ""
                    except:
                        pt_r_list[r] = ""
                elif pt[r, self.InM_col] != "" and pt[r, self.InM_col] != float("nan"):
                    try:
                        ptstr = pt[r, self.Day_col] + pt[r, self.InM_col]
                        for rr in range(pt2.shape[0]):
                            if pt2[rr, self.OutM_col2] == pt2[rr, self.OutM_col2]:
                                try:
                                    pt2str = (
                                        pt2[rr, self.Day_col2] + pt2[rr, self.OutM_col2]
                                    )
                                    if ptstr == pt2str:
                                        pt_r_list[r] = rr + 1
                                        break
                                    else:
                                        pt_r_list[r] = ""
                                except:
                                    pt_r_list[r] = ""
                    except:
                        pt_r_list[r] = ""
                else:
                    pt_r_list[r] = ""
            else:
                pt_r_list[r] = ""
        except:
            pt_r_list[r] = pt_r_list[r]

    # ---------------------------------------------------------------------
    def PtSearch(self):
        """
        検索開始
        """
        try:
            pt = np.array(self.pt.model.df)

            ptCol = list(self.pt.model.df.columns)
            pt2 = np.array(self.pt2.model.df)
            pt_r_list = np.array(self.pt.model.df)[:, 0]
            for r in range(pt.shape[0]):
                self.PtSearch_Sub(
                    r,
                    pt,
                    pt2,
                    pt_r_list,
                )
            ptCol.append(PlusCol)
            pt_r_list = np.reshape(pt_r_list, (pt_r_list.shape[0], 1))
            pt = np.hstack([pt, pt_r_list])
            pt = pd.DataFrame(pt, columns=ptCol)
            self.pt.model.df = pt
            DGF.Pandas_mem_usage(self.pt.model.df)
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
                if self.Img_c != 0:
                    self.canvas.pack_forget()
                    self.Img_frame.pack_forget()
                    self.OCR_frame2.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
                    self.Img_c = 0
                print(self.pt2.model.df.columns)
                self.ColumnsDelete(self.pt)
                if len(self.pt.model.df.columns) == len(self.pt2.model.df.columns):
                    Diff_colStr = ",".join(self.pt2.model.df.columns)
                    self.Diff_col.delete(0, tk.END)
                    self.Diff_col.insert(0, Diff_colStr)  # OCR抽出結果表列名テキストボックスに文字代入
                else:
                    tk.messagebox.showinfo("確認", "OCR抽出結果表と比較ファイルの設定列数が一致しません。")
            except:
                self.Diff_col.delete(0, tk.END)
                self.Diff_col.insert(0, "")  # OCR抽出結果表列名テキストボックスに文字代入
            DGF.Pandas_mem_usage(self.pt2.model.df)
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
            self.OCR_frame2.destroy()
            DGF.create_Frame2(
                self,
                int(self.width_of_window / self.wid),
                int(self.height_of_window / self.hei),
                list(self.module),
                self.t_font,
                self.hei_Par,
                self.G_logger,
            )  # 比較表フレーム
            self.pt2.update()
            self.pt2.show()
            self.pt2_OpenFlag = True

    # -------------------------------------------------------------------------------------
    def click_close(self):
        """
        ウィンドウ×ボタンクリック
        """
        if tk.messagebox.askokcancel("確認", "終了しますか？"):
            self.master.destroy()
            G_logger.debug("TKINTERCV2SettingClose完了")  # Log出力
        else:
            G_logger.debug("TKINTERCV2SettingClose失敗")  # Log出力

    # -------------------------------------------------------------------------------------
    def SingleSplit(self):
        """
        データ整理サブ
        """
        print(self.SplitVar.get())
        In_v = self.In_v.get()  # 入金文字列
        Out_v = self.Out_v.get()  # 出金文字列
        Money_v = self.Money_v.get()  # 金額列名
        S_Var = self.SplitVar.get()  # 貸借判定基準列数値
        try:
            ptDF = self.SingleSplit_Sub(self.pt2.model.df, In_v, Out_v, Money_v, S_Var)
            if ptDF[0] is True:
                self.pt2.model.df = ptDF[1]
                DGF.Pandas_mem_usage(self.pt2.model.df)
                self.pt2.show()
            ptDF = self.SingleSplit_Sub(self.pt.model.df, In_v, Out_v, Money_v, S_Var)
            if ptDF[0] is True:
                self.pt.model.df = ptDF[1]
                DGF.Pandas_mem_usage(self.pt.model.df)
                self.pt.show()
        except:
            ptDF = self.SingleSplit_Sub(self.pt.model.df, In_v, Out_v, Money_v, S_Var)
            if ptDF[0] is True:
                self.pt.model.df = ptDF[1]
                DGF.Pandas_mem_usage(self.pt.model.df)
                self.pt.show()

    # -------------------------------------------------------------------------------------
    def SingleSplit_Sub(self, DF, In_v, Out_v, Money_v, S_Var):
        try:
            DFCol = np.array(DF.columns)
            In_vList = []
            Out_vList = []
            for r in range(len(DF)):
                DF_itemRow = DF.iloc[r]
                if DF_itemRow[S_Var] == In_v:
                    In_vList.append(DF_itemRow[Money_v])
                    Out_vList.append("")
                    DF_itemRow[Money_v] = ""
                elif DF_itemRow[S_Var] == Out_v:
                    In_vList.append("")
                    Out_vList.append(DF_itemRow[Money_v])
                    DF_itemRow[Money_v] = ""
                else:
                    In_vList.append("")
                    Out_vList.append("")
                    DF_itemRow[Money_v] = ""
            SplitCol = int(np.where(DFCol == S_Var)[0][0])
            DF = np.array(DF)
            LEFTDF = DF[:, 0:SplitCol]
            LEFTDFCol = DFCol[0:SplitCol]
            RIGHTDF = DF[:, (SplitCol + 1) : DFCol.shape[0]]
            RIGHTDFCol = DFCol[(SplitCol + 1) : DFCol.shape[0]]
            In_vList = np.array(In_vList)
            In_vList = In_vList.reshape(In_vList.shape[0], 1)
            In_vListCol = np.array(["入金"])
            Out_vList = np.array(Out_vList)
            Out_vList = Out_vList.reshape(Out_vList.shape[0], 1)
            Out_vListCol = np.array(["出金"])
            MergeDF = np.hstack([LEFTDF, In_vList])
            MergeCol = np.hstack([LEFTDFCol, In_vListCol])
            MergeDF = np.hstack([MergeDF, Out_vList])
            MergeCol = np.hstack([MergeCol, Out_vListCol])
            MergeDF = np.hstack([MergeDF, RIGHTDF])
            MergeCol = np.hstack([MergeCol, RIGHTDFCol])

            Money_vCol = int(np.where(MergeCol == Money_v)[0][0])
            LEFTDF = MergeDF[:, 0:Money_vCol]
            LEFTDFCol = MergeCol[0:Money_vCol]
            RIGHTDF = MergeDF[:, (Money_vCol + 1) : MergeCol.shape[0]]
            RIGHTDFCol = MergeCol[(Money_vCol + 1) : MergeCol.shape[0]]

            MergeDF = np.hstack([LEFTDF, RIGHTDF])
            MergeCol = np.hstack([LEFTDFCol, RIGHTDFCol])

            MergePD = pd.DataFrame(MergeDF, columns=MergeCol)
            return True, MergePD
        except:
            return False, ""

    # -------------------------------------------------------------------------------------
    def ChangeList(self):
        """
        データ整理分岐処理
        """

        try:
            m = self.children_get()
            ReplaceView.CreateDB.readsql(self, self.OCR_dbname, self.OCR_tbname, m)
            self.RView_df = m.model.df
        except:
            tk.messagebox.showinfo("確認", " 置換フレーム起動エラーです。")

        if self.DStxt.get() != "":
            if self.pt2_OpenFlag is True:
                self.D_c = "Day_col"
                self.D_c2 = "Day_col2"
            else:
                self.D_c = "Day_col"
                self.D_c2 = "else"
        else:
            self.D_c = "else"
            self.D_c2 = "else"

        if self.OMtxt.get() != "":
            if self.pt2_OpenFlag is True:
                self.O_c = "OutM_col"
                self.O_c2 = "OutM_col2"
            else:
                self.O_c = "OutM_col"
                self.O_c2 = "else"
        else:
            self.O_c = "else"
            self.O_c2 = "else"

        if self.IMtxt.get() != "":
            if self.pt2_OpenFlag is True:
                self.I_c = "InM_col"
                self.I_c2 = "InM_col2"
            else:
                self.I_c = "InM_col"
                self.I_c2 = "else"
        else:
            self.I_c = "else"
            self.I_c2 = "else"

        self.ChangeList_sub()
        return

    # -------------------------------------------------------------------------------------
    def ChangeList_split(self):
        try:
            self.ColumnsDelete(self.pt)
            # Table2
            ptcol2 = np.array(self.pt2.model.df.columns)
            if self.D_c2 == "Day_col2":
                self.Day_col2 = int(np.where(ptcol2 == self.DStxt.get())[0])
            elif self.D_c2 == "else":
                self.Day_col2 = ""
            if self.O_c2 == "OutM_col2":
                self.OutM_col2 = int(np.where(ptcol2 == self.OMtxt.get())[0])
            elif self.O_c2 == "else":
                self.OutM_col2 = ""
            if self.I_c2 == "InM_col2":
                self.InM_col2 = int(np.where(ptcol2 == self.IMtxt.get())[0])
            elif self.I_c2 == "else":
                self.InM_col2 = ""
            # ----------------------------------------------------------------
            # Table1
            ptcol = np.array(self.pt.model.df.columns)
            if self.D_c == "Day_col":
                self.Day_col = int(np.where(ptcol == self.DStxt.get())[0])
            elif self.D_c == "else":
                self.Day_col = ""
            if self.O_c == "OutM_col":
                self.OutM_col = int(np.where(ptcol == self.OMtxt.get())[0])
            elif self.O_c == "else":
                self.OutM_col = ""
            if self.I_c == "InM_col":
                self.InM_col = int(np.where(ptcol == self.IMtxt.get())[0])
            elif self.I_c == "else":
                self.InM_col = ""
            # ----------------------------------------------------------------
            return
        except:
            self.Day_col = ""
            self.OutM_col = ""
            self.InM_col = ""
            self.Day_col2 = ""
            self.OutM_col2 = ""
            self.InM_col2 = ""
            return

    # -------------------------------------------------------------------------------------
    def C_L(self, pt):
        ptarray = np.array(pt.model.df)
        for c in range(ptarray.shape[1]):
            try:
                if pt._name == "OCR抽出結果表Main":
                    if c == self.Day_col and self.D_c == "Day_col":
                        self.DaysCheck(self.Day_col, self.Day_col2)
                    elif c == self.OutM_col and self.O_c == "OutM_col":
                        self.OutMCheck(self.OutM_col, self.OutM_col2)
                    elif c == self.InM_col and self.I_c == "InM_col":
                        self.InMCheck(self.InM_col, self.InM_col2)
                    else:
                        self.StrCheck(c, pt)
                elif pt._name == "比較ファイルMain":
                    if c == self.Day_col2 and self.D_c2 == "Day_col2":
                        self.DaysCheck(self.Day_col, self.Day_col2)
                    elif c == self.OutM_col2 and self.O_c2 == "OutM_col2":
                        self.OutMCheck(self.OutM_col, self.OutM_col2)
                    elif c == self.InM_col2 and self.I_c == "InM_col2":
                        self.InMCheck(self.InM_col, self.InM_col2)
                    else:
                        self.StrCheck(c, pt)
            except:
                print("No_ColSet")
        pt.update()
        pt.show()

    # -------------------------------------------------------------------------------------
    def ChangeList_sub(self):
        try:
            self.ChangeList_split()
            if self.select_var.get() == 1:
                # PandasTable
                self.C_L(self.pt)
                # PandasTable2
                if self.pt2_OpenFlag is True:
                    self.C_L(self.pt2)
                # End
                return (
                    self.Day_col,
                    self.Day_col2,
                    self.OutM_col,
                    self.OutM_col2,
                    self.InM_col,
                    self.InM_col2,
                )
            else:
                # PandasTable
                self.C_L(self.pt)
                # PandasTable2
                if self.pt2_OpenFlag is True:
                    self.C_L(self.pt2)
                    # Table2
                    ptcol2 = np.array(self.pt2.model.df.columns)
                    # self.Day_col2 = int(np.where(ptcol2 == self.DStxt.get())[0])
                    self.OutM_col2 = int(np.where(ptcol2 == "出金")[0][0])
                    self.InM_col2 = int(np.where(ptcol2 == "入金")[0][0])
                # ----------------------------------------------------------------
                self.SingleSplit()
                # Table1
                ptcol = np.array(self.pt.model.df.columns)
                # self.Day_col = int(np.where(ptcol == self.DStxt.get())[0])
                # ----------------------------------------------------------------
                self.OutM_col = int(np.where(ptcol == "出金")[0][0])
                self.InM_col = int(np.where(ptcol == "入金")[0][0])

                ptarray = np.array(self.pt.model.df)
                for c in range(ptarray.shape[1]):
                    try:
                        if c == self.OutM_col:
                            self.OutMCheck(self.OutM_col, self.OutM_col2)
                        elif c == self.InM_col:
                            self.InMCheck(self.InM_col, self.InM_col2)
                    except:
                        print("No_ColSet")
                return (
                    self.Day_col,
                    self.Day_col2,
                    self.OutM_col,
                    self.OutM_col2,
                    self.InM_col,
                    self.InM_col2,
                )
        except:
            return

    # ---------------------------------------------------------------------------------------------
    def ReturnBack(self):
        """
        前UI起動
        """
        self.master.destroy()
        C_MT.deiconify()
        C_TP.deiconify()

    def OCRFileRead(self):
        # ファイル→開く
        filename = tk.filedialog.askopenfilename(
            filetypes=[
                ("CSV", ".csv"),
            ],  # ファイルフィルタ
            initialdir=os.getcwd(),  # カレントディレクトリ
        )
        self.FileName = filename
        self.OCR_dbname = "ReplaceView.db"
        self.OCR_tbname = os.path.splitext(os.path.basename(self.FileName))[0]
        if filename != "":
            enc = DGF.CSVO.getFileEncoding(self.FileName)
            self.table = self.pt.importCSV(self.FileName, encoding=enc)
            options = {"fontsize": self.t_font[1]}
            DGF.config.apply_options(options, self.pt)
            # DF型変換------------------------------
            DGF.Pandas_mem_usage(self.pt.model.df)
            # --------------------------------------
            self.pt.show()
            self.pt.update()
            self.pt1_OpenFlag = True
            self.OCR_url.delete(0, tk.END)
            self.OCR_url.insert(0, self.FileName)
            m = self.children_get()

            self.RView.destroy()
            self.RView = ReplaceView.Main(self, self.FileName)  # 置換テーブルの読込
            # ReplaceView.CreateDB.readsql(self, self.OCR_dbname, self.OCR_tbname, m)
            self.RView.update()


# ---------------------------------------------------------------------------------------------
def tomlread():
    """
    tomlリード
    """
    try:
        r_toml = os.getcwd() + r"\OCRView\Setting.toml"
        return r_toml
    except:
        r_toml = os.getcwd() + r"\Setting.toml"
        return r_toml


# -------------------------------------------------------------------------------------
def Main(MUI, US, tom, logger, MT, TP, imgu):
    """
    呼出関数
    """
    global Master
    global G_logger, C_MT, C_TP
    global Banktoml, tomlurl, PlusCol, imgurl

    Master = MUI
    C_MT = MT
    C_TP = TP
    csv_u = US
    Banktoml = tom
    G_logger = logger
    imgurl = imgu
    PlusCol = "比較対象行番号"
    # -----------------------------------------------------------
    root = tk.Tk()  # Window生成
    data = IconCode.icondata()
    root.tk.call("wm", "iconphoto", root._w, tk.PhotoImage(data=data, master=root))
    app = Application(csvurl=csv_u, imgurl=imgurl, master=root)
    # --- 基本的な表示準備 ----------------

    app.mainloop()


# ------------------------------------------------------------------------------------------
if __name__ == "__main__":
    # logger設定-----------------------------------------------------------------------------------------------------
    logging.config.fileConfig(os.getcwd() + r"\LogConf\logging_debug.conf")
    G_logger = logging.getLogger(__name__)
    # ---------------------------------------------------------------------------------------------------------------

    global Banktoml, tomlurl, PlusCol, imgurl
    URL = os.getcwd()
    imgurl = r"D:\OCRTESTPDF\PDFTEST\相続_JA_1page.png"
    # imgurl = r"C:\Users\もちねこ\Desktop\PDFTEST\JA_1page.png"
    tomlurl = tomlread()
    csv_u = r"D:\OCRTESTPDF\PDFTEST\相続_JA_1page.csv"
    # csv_u = r"C:/Users/もちねこ/Desktop/PDFTEST/JA_1page_AutoJounal.csv"
    PlusCol = "比較対象行番号"
    # toml読込------------------------------------------------------------------------------
    with open(tomlurl, encoding="utf-8") as f:
        Banktoml = toml.load(f)
        print(Banktoml)
    # -----------------------------------------------------------
    # -----------------------------------------------------------
    root = tk.Tk()  # Window生成
    data = IconCode.icondata()
    root.tk.call("wm", "iconphoto", root._w, tk.PhotoImage(data=data, master=root))
    app = Application(csvurl=csv_u, imgurl=imgurl, master=root)
    # --- 基本的な表示準備 ----------------

    app.mainloop()
