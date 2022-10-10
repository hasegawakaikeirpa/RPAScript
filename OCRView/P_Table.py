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

###################################################################################################
class Application(tk.Frame):
    def __init__(self, csvurl, master=None):
        global SideWidth, SideHeight, LabelWidth, t_font
        global LabelHeight, BtnWidth, BtnHeight, EntHeight, EntWidth
        global wid_Par, hei_Par, width_of_window, height_of_window, wid, hei
        # Windowの初期設定を行う。
        super().__init__(master)
        # Windowの画面サイズを設定する。
        G_logger.debug("P_Table起動")  # Log出力
        # customtkスタイル
        ck.set_appearance_mode("System")  # Modes: system (default), light, dark
        ck.set_default_color_theme(
            "dark-blue"
        )  # Themes: blue (default), dark-blue, green
        width_of_window = int(int(master.winfo_screenwidth()) * 0.95)
        height_of_window = int(int(master.winfo_screenheight()) * 0.90)
        wid_Par = width_of_window / 1459
        hei_Par = height_of_window / 820
        x_coodinate = width_of_window * 0.01
        y_coodinate = height_of_window * 0.01
        # 　メインウィンドウサイズ指定
        self.master.geometry(
            "%dx%d+%d+%d"
            % (width_of_window, height_of_window, x_coodinate, y_coodinate)
        )
        ########################################
        wid = 2.25  # width割率
        hei = 1.4  # width割率
        ########################################
        self.FileName = csvurl
        self.master.minsize(width_of_window, height_of_window)
        self.master.title("OCR読取 Ver:0.9-比較ウィンドウ-")
        self.master.protocol("WM_DELETE_WINDOW", self.click_close)  # 閉じる処理設定
        # 統合フレーム
        ################################################################################
        SideWidth = int(200 * wid_Par)
        SideHeight = int(200 * hei_Par)
        LabelWidth = int(20 * wid_Par)
        LabelHeight = int(20 * hei_Par)
        BtnWidth = int(180 * wid_Par)
        BtnHeight = int(20 * hei_Par)
        EntWidth = int(70 * hei_Par)
        EntHeight = int(20 * wid_Par)
        t_font = (1, int(10 * wid_Par))
        ################################################################################
        self.Main_Frame = tk.Frame(
            self.master,
            width=width_of_window,
            height=height_of_window,
            bg="#fabd91",
            relief=tk.GROOVE,
        )
        self.Main_Frame.pack(fill=tk.BOTH, expand=True)
        # サイドフレーム
        self.Side_Frame = tk.Frame(
            self.Main_Frame,
            width=int(width_of_window / 4),
            height=int(height_of_window * 0.8),
            bd=2,
            bg="#fabd91",
            relief=tk.RIDGE,
        )
        self.Side_Frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        # # サイドフレーム2
        # self.Side_Frame2 = tk.Frame(
        #     self.Main_Frame, width=330, height=750, bd=2, relief=tk.RIDGE
        # )
        # self.Side_Frame2.grid(row=1, column=1, sticky=tk.NSEW)
        ########################################################################################
        # フレーム設定---------------------------------------------------------------------
        DGF.create_Frame(
            self,
            int(width_of_window / wid),
            int(height_of_window / hei),
            t_font,
            hei_Par,
        )  # OCR抽出結果表フレーム
        # Side_Sub##############################################################################
        self.Side_Sub = tk.Frame(
            self.Side_Frame,
            width=int(width_of_window / 4),
            height=int(height_of_window * 0.8),
            bd=2,
            bg="#fabd91",
            relief=tk.RIDGE,
        )
        self.Side_Sub.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        # --------------------------------------------------------------------------------
        ck.CTkLabel(
            master=self.Side_Sub,
            text="日付列名",
            width=LabelWidth,
            height=LabelHeight,
            corner_radius=8,
            text_font=t_font,
        ).grid(row=0, column=0)
        self.DStxt = ck.CTkEntry(
            master=self.Side_Sub,
            width=EntWidth,
            height=EntHeight,
            border_width=2,
            corner_radius=8,
            text_color="black",
            border_color="snow",
            text_font=t_font,
        )
        self.DStxt.insert(0, "")  # 日付列名テキストボックスに文字代入
        self.DStxt.grid(row=0, column=1, pady=5, sticky=tk.W)  # 日付列名テキストボックス配置
        self.DSbtn = ck.CTkButton(
            master=self.Side_Sub,
            text="選択列名転記",
            command=self.DSSetClick,
            width=BtnWidth,
            height=BtnHeight,
            border_width=2,
            corner_radius=8,
            text_color="snow",
            border_color="snow",
            text_font=t_font,
        )
        self.DSbtn.grid(row=0, column=2, padx=5, pady=5)
        # --------------------------------------------------------------------------------
        ck.CTkLabel(
            master=self.Side_Sub,
            text="出金列名",
            width=LabelWidth,
            height=LabelHeight,
            corner_radius=8,
            text_font=t_font,
        ).grid(row=1, column=0)
        self.OMtxt = ck.CTkEntry(
            master=self.Side_Sub,
            width=EntWidth,
            height=EntHeight,
            border_width=2,
            corner_radius=8,
            text_color="black",
            border_color="snow",
            text_font=t_font,
        )
        self.OMtxt.insert(0, "")  # 出金列名テキストボックスに文字代入
        self.OMtxt.grid(row=1, column=1, pady=5, sticky=tk.W)  # 出金列名テキストボックス配置
        self.OMbtn = ck.CTkButton(
            master=self.Side_Sub,
            text="選択列名転記",
            command=self.OutMoneyClick,
            width=BtnWidth,
            height=BtnHeight,
            border_width=2,
            corner_radius=8,
            text_color="snow",
            border_color="snow",
            text_font=t_font,
        )
        self.OMbtn.grid(row=1, column=2, padx=5)
        # --------------------------------------------------------------------------------
        ck.CTkLabel(
            master=self.Side_Sub,
            text="入金列名",
            width=LabelWidth,
            height=LabelHeight,
            corner_radius=8,
            text_font=t_font,
        ).grid(row=2, column=0)
        self.IMtxt = ck.CTkEntry(
            master=self.Side_Sub,
            width=EntWidth,
            height=EntHeight,
            border_width=2,
            corner_radius=8,
            text_color="black",
            border_color="snow",
            text_font=t_font,
        )
        self.IMtxt.insert(0, "")  # 入金列名テキストボックスに文字代入
        self.IMtxt.grid(row=2, column=1, pady=5, sticky=tk.W)  # 入金列名テキストボックス配置
        self.IMbtn = ck.CTkButton(
            master=self.Side_Sub,
            text="選択列名転記",
            command=self.InMoneyClick,
            width=BtnWidth,
            height=BtnHeight,
            border_width=2,
            corner_radius=8,
            text_color="snow",
            border_color="snow",
            text_font=t_font,
        )
        self.IMbtn.grid(row=2, column=2, padx=5)
        # --------------------------------------------------------------------------------
        ck.CTkLabel(
            master=self.Side_Sub,
            text="金額列数",
            width=LabelWidth,
            height=LabelHeight,
            corner_radius=8,
            text_font=t_font,
        ).grid(row=3, column=0)
        # radio1ウィジェット
        self.select_var = tk.IntVar()  # ウィジェット変数select_varを作成
        self.select_var.set(1)  # select_var変数に数値をセット
        self.languages = [("複数", 1), ("単一", 2)]  # languagesリストを定義
        for language, val in self.languages:  # ループ開始
            self.radio1 = tk.Radiobutton(
                self.Side_Sub,
                text=language,
                value=val,
                variable=self.select_var,
                command=self.radioclick,
                bg="#fabd91",
            )  # languagesリストを選択肢とするradio1ウィジェットを生成
            self.radio1.grid(row=3, column=val, sticky=tk.N)

        self.SplitVarLabel = ck.CTkLabel(
            master=self.Side_Sub,
            text="貸借判定基準列名",
            width=LabelWidth,
            height=LabelHeight,
            corner_radius=8,
            text_font=t_font,
        ).grid(row=5, column=0)
        self.SplitVar = ck.CTkEntry(
            master=self.Side_Sub,
            width=int(EntWidth * 3),
            height=EntHeight,
            border_width=2,
            corner_radius=8,
            text_color="black",
            border_color="snow",
            text_font=t_font,
        )
        self.SplitVar.delete(0, tk.END)
        self.SplitVar.insert(0, "貸借")
        self.SplitVar.configure(state="readonly")
        self.SplitVar.grid(row=5, column=1, pady=5, columnspan=2)
        self.In_vLabel = ck.CTkLabel(
            master=self.Side_Sub,
            text="入金文字列",
            width=LabelWidth,
            height=LabelHeight,
            corner_radius=8,
            text_font=t_font,
        ).grid(row=6, column=0)
        self.In_v = ck.CTkEntry(
            master=self.Side_Sub,
            width=int(EntWidth * 3),
            height=EntHeight,
            border_width=2,
            corner_radius=8,
            text_color="black",
            border_color="snow",
            text_font=t_font,
        )
        self.In_v.delete(0, tk.END)
        self.In_v.insert(0, "借")
        self.In_v.configure(state="readonly")
        self.In_v.grid(row=6, column=1, pady=5, columnspan=2)
        self.Out_vLabel = ck.CTkLabel(
            master=self.Side_Sub,
            text="出金文字列",
            width=LabelWidth,
            height=LabelHeight,
            corner_radius=8,
            text_font=t_font,
        ).grid(row=7, column=0)
        self.Out_v = ck.CTkEntry(
            master=self.Side_Sub,
            width=int(EntWidth * 3),
            height=EntHeight,
            border_width=2,
            corner_radius=8,
            text_color="black",
            border_color="snow",
            text_font=t_font,
        )
        self.Out_v.delete(0, tk.END)
        self.Out_v.insert(0, "貸")
        self.Out_v.configure(state="readonly")
        self.Out_v.grid(row=7, column=1, pady=5, columnspan=2)
        self.Money_Label = ck.CTkLabel(
            master=self.Side_Sub,
            text="金額列名",
            width=LabelWidth,
            height=LabelHeight,
            corner_radius=8,
            text_font=t_font,
        ).grid(row=8, column=0)
        self.Money_v = ck.CTkEntry(
            master=self.Side_Sub,
            width=int(EntWidth * 3),
            height=EntHeight,
            border_width=2,
            corner_radius=8,
            text_color="black",
            border_color="snow",
            text_font=t_font,
        )
        self.Money_v.delete(0, tk.END)
        self.Money_v.insert(0, "金額")
        self.Money_v.configure(state="readonly")
        self.Money_v.grid(row=8, column=1, pady=5, columnspan=2)
        # #######################################################################################
        # Side_Sub2##############################################################################
        self.Side_Sub2 = tk.Frame(
            self.Side_Frame,
            width=int(width_of_window / 4),
            height=int(height_of_window * 0.8),
            bd=2,
            bg="#fabd91",
            relief=tk.RIDGE,
        )
        # self.Side_Sub2.grid(row=1, column=1, sticky=tk.NSEW)
        self.Side_Sub2.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        # 書式整理-------------------------------------------------------------------------
        self.ChangeL = ck.CTkButton(
            master=self.Side_Sub2,
            text="書式整理",
            command=self.ChangeList,
            width=BtnWidth,
            height=BtnHeight,
            border_width=2,
            corner_radius=8,
            text_color="snow",
            border_color="snow",
            fg_color="tomato",
            text_font=t_font,
        )
        self.ChangeL.grid(
            row=0, column=0, columnspan=3, padx=10, pady=5, sticky=tk.N
        )  # 日付列名テキストボックス配置
        # 置換-------------------------------------------------------------------------
        self.ChangeL = ck.CTkButton(
            master=self.Side_Sub2,
            text="置換起動",
            command=self.ReadRepView,
            width=BtnWidth,
            height=BtnHeight,
            border_width=2,
            corner_radius=8,
            text_color="snow",
            border_color="snow",
            fg_color="tomato",
            text_font=t_font,
        )
        self.ChangeL.grid(
            row=1, column=0, columnspan=3, padx=10, pady=5, sticky=tk.N
        )  # 日付列名テキストボックス配置

        # OCR抽出ファイル-----------------------------------------------------------
        self.OCRRead = ck.CTkButton(
            master=self.Side_Sub2,
            text="OCR抽出ファイル選択",
            command=self.OCRFileRead,
            width=BtnWidth,
            height=BtnHeight,
            border_width=2,
            corner_radius=8,
            text_color="snow",
            border_color="snow",
            fg_color="skyblue",
            text_font=t_font,
        )
        self.OCRRead.grid(
            row=2, column=0, columnspan=3, padx=10, pady=5, sticky=tk.N
        )  # 日付列名テキストボックス配置

        # 比較対象ファイル複数選択-----------------------------------------------------------
        self.FileRead = ck.CTkButton(
            master=self.Side_Sub2,
            text="比較対象ファイル複数選択",
            command=self.ChangeFileRead,
            width=BtnWidth,
            height=BtnHeight,
            border_width=2,
            corner_radius=8,
            text_color="snow",
            border_color="snow",
            fg_color="seagreen3",
            text_font=t_font,
        )
        self.FileRead.grid(
            row=3, column=0, columnspan=3, padx=10, pady=5, sticky=tk.N
        )  # 日付列名テキストボックス配置
        # 比較対象ファイル追加---------------------------------------------------------------
        self.SingleFileRead = ck.CTkButton(
            master=self.Side_Sub2,
            text="比較対象ファイル追加",
            command=self.ChangeFileSingleRead,
            width=BtnWidth,
            height=BtnHeight,
            border_width=2,
            corner_radius=8,
            text_color="snow",
            border_color="snow",
            fg_color="Orange",
            text_font=t_font,
        )
        self.SingleFileRead.grid(
            row=4, column=0, columnspan=3, padx=10, sticky=tk.N
        )  # 日付列名テキストボックス配置
        # #######################################################################################
        # Side_Sub3##############################################################################
        self.Side_Sub3 = tk.Frame(
            self.Side_Frame,
            width=int(width_of_window / 4),
            height=int(height_of_window * 0.8),
            bd=2,
            bg="#fabd91",
            relief=tk.RIDGE,
        )
        self.Side_Sub3.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        # 比較対象ファイルリストボックス------------------------------------------------------
        ck.CTkLabel(
            master=self.Side_Sub3,
            text="比較対象ファイル",
            width=LabelWidth,
            height=LabelHeight,
            corner_radius=8,
            text_font=t_font,
        ).grid(row=0, column=0)
        self.module = ""
        self.listbox_var = tk.StringVar(value=self.module)
        self.listbox = tk.Listbox(
            self.Side_Sub3,
            width=int(20 * wid_Par),
            height=int(11 * hei_Par),
            listvariable=self.listbox_var,
        )
        self.listbox.grid(row=1, column=0, padx=5, sticky=tk.E + tk.W)
        # #######################################################################################
        # Side_Sub4##############################################################################
        self.Side_Sub4 = tk.Frame(
            self.Side_Frame,
            width=int(width_of_window / 4),
            height=int(height_of_window * 0.8),
            bd=2,
            bg="#fabd91",
            relief=tk.RIDGE,
        )
        self.Side_Sub4.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        # 列名テキストボックス--------------------------------------------------------------
        ck.CTkLabel(
            master=self.Side_Sub4,
            text="OCR抽出結果表URL",
            width=LabelWidth,
            height=LabelHeight,
            corner_radius=8,
            text_font=t_font,
        ).grid(row=0, column=0)
        self.OCR_url = ck.CTkEntry(
            master=self.Side_Sub4,
            width=int(EntWidth * 3),
            height=EntHeight,
            border_width=2,
            corner_radius=8,
            text_color="black",
            border_color="snow",
            text_font=t_font,
        )
        self.OCR_url.insert(0, csv_u)
        self.OCR_url.grid(
            row=0, column=1, padx=5, pady=5, sticky=tk.W
        )  # OCR抽出結果表列名テキストボックス配置
        ck.CTkLabel(
            master=self.Side_Sub4,
            text="OCR抽出結果表列名",
            width=LabelWidth,
            height=LabelHeight,
            corner_radius=8,
            text_font=t_font,
        ).grid(row=1, column=0)
        self.OCR_col = ck.CTkEntry(
            master=self.Side_Sub4,
            width=int(EntWidth * 3),
            height=EntHeight,
            border_width=2,
            corner_radius=8,
            text_color="black",
            border_color="snow",
            text_font=t_font,
        )
        try:
            print(self.pt.model.df.columns)
            OCR_colStr = ",".join(self.pt.model.df.columns)
            self.OCR_col.insert(0, OCR_colStr)  # OCR抽出結果表列名テキストボックスに文字代入
        except:
            self.OCR_col.insert(0, "")  # OCR抽出結果表列名テキストボックスに文字代入
        self.OCR_col.bind("<Return>", self.OCRtxtCol)
        self.OCR_col.grid(
            row=1, column=1, padx=5, pady=5, sticky=tk.W
        )  # OCR抽出結果表列名テキストボックス配置
        # 列名テキストボックス--------------------------------------------------------------
        ck.CTkLabel(
            master=self.Side_Sub4,
            text="比較ファイル列名",
            width=LabelWidth,
            height=LabelHeight,
            corner_radius=8,
            text_font=t_font,
        ).grid(row=2, column=0)
        self.Diff_col = ck.CTkEntry(
            master=self.Side_Sub4,
            width=int(EntWidth * 3),
            height=EntHeight,
            border_width=2,
            corner_radius=8,
            text_color="black",
            border_color="snow",
            text_font=t_font,
        )
        try:
            print(self.pt2.model.df.columns)
            Diff_colStr = ",".join(self.pt2.model.df.columns)
            self.Diff_col.delete(0, tk.END)
            self.Diff_col.insert(0, Diff_colStr)  # OCR抽出結果表列名テキストボックスに文字代入
        except:
            self.Diff_col.insert(0, "")  # OCR抽出結果表列名テキストボックスに文字代入
        self.Diff_col.bind("<Return>", self.DifftxtCol)
        self.Diff_col.grid(
            row=2, column=1, padx=5, pady=5, sticky=tk.W
        )  # 入金列名テキストボックス配置
        # 画像ファイルテキストボックス--------------------------------------------------------------
        ck.CTkLabel(
            master=self.Side_Sub4,
            text="画像ファイル",
            width=LabelWidth,
            height=LabelHeight,
            corner_radius=8,
            text_font=t_font,
        ).grid(row=3, column=0)
        self.Img_url = ck.CTkEntry(
            master=self.Side_Sub4,
            width=int(EntWidth * 3),
            height=EntHeight,
            border_width=2,
            corner_radius=8,
            text_color="black",
            border_color="snow",
            text_font=t_font,
        )
        self.Img_url.insert(0, imgurl)
        self.Img_url.grid(
            row=3, column=1, padx=5, pady=5, sticky=tk.W
        )  # 入金列名テキストボックス配置
        # #######################################################################################
        # Side_Sub5##############################################################################
        self.Side_Sub5 = tk.Frame(
            self.Side_Frame,
            width=int(width_of_window / 4),
            height=int(height_of_window * 0.8),
            bd=2,
            bg="#fabd91",
            relief=tk.RIDGE,
        )
        # self.Side_Sub5.grid(row=1, column=4, sticky=tk.NSEW)
        self.Side_Sub5.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        # 検索開始ボタン--------------------------------------------------------------------
        self.SearchBtn = ck.CTkButton(
            master=self.Side_Sub5,
            text="全検索",
            command=self.SearchStart,
            width=BtnWidth,
            height=BtnHeight,
            border_width=2,
            corner_radius=8,
            text_color="snow",
            border_color="snow",
            fg_color="mediumPurple",
            text_font=t_font,
        )
        self.SearchBtn.grid(
            row=0, column=0, pady=5, padx=10, sticky=tk.NSEW
        )  # 日付列名テキストボックス配置
        # 選択行検索開始ボタン--------------------------------------------------------------
        self.SingleSearchBtn = ck.CTkButton(
            master=self.Side_Sub5,
            text="選択行検索",
            command=self.SingleSearchStart,
            width=BtnWidth,
            height=BtnHeight,
            border_width=2,
            corner_radius=8,
            text_color="snow",
            border_color="snow",
            fg_color="hotpink1",
            text_font=t_font,
        )
        self.SingleSearchBtn.grid(
            row=1, column=0, pady=5, padx=10, sticky=tk.NSEW
        )  # 日付列名テキストボックス配置
        # 読込ボタン--------------------------------------------------------------
        self.ImgOpen = ck.CTkButton(
            master=self.Side_Sub5,
            text="画像ビューワー起動",
            command=self.ReadImg,
            width=BtnWidth,
            height=BtnHeight,
            border_width=2,
            corner_radius=8,
            text_color="snow",
            border_color="snow",
            fg_color="purple",
            text_font=t_font,
        )
        self.ImgOpen.grid(
            row=2, column=0, pady=5, padx=10, sticky=tk.NSEW
        )  # 日付列名テキストボックス配置
        # 戻るボタン--------------------------------------------------------------
        self.ReturnBackBtn = ck.CTkButton(
            master=self.Side_Sub5,
            text="戻る",
            command=self.ReturnBack,
            width=BtnWidth,
            height=BtnHeight,
            border_width=2,
            corner_radius=8,
            text_color="snow",
            border_color="snow",
            fg_color="gray",
            text_font=t_font,
        )
        self.ReturnBackBtn.grid(
            row=3, column=0, pady=5, padx=10, sticky=tk.NSEW
        )  # 日付列名テキストボックス配置
        # フレーム設定---------------------------------------------------------------------
        DGF.create_Frame2(
            self,
            int(width_of_window / wid),
            int(height_of_window / hei),
            list(self.module),
            t_font,
            hei_Par,
            G_logger,
        )  # OCR抽出結果表フレーム
        # フレーム設定---------------------------------------------------------------------
        self.IMG_frame = tk.Frame(
            self.Main_Frame,
            width=int(width_of_window / wid),
            height=int(height_of_window / hei),
            bd=2,
            bg="#fce4d2",
            relief=tk.RIDGE,
        )  # 親フレーム
        self.IMG_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.IMG_frame.pack_forget()
        self.Img_c = 0
        self.update()

    # ----------------------------------------------------------------------
    def ReadRepView(self):
        """
        置換フレーム起動
        """
        try:
            self.RView = ReplaceView.Main(self, csv_u)
        except:
            tk.messagebox.showinfo("確認", " 置換フレーム起動エラーです。")

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
            DGF.PandasAstype(self.pt2.model.df)
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
            DGF.PandasAstype(self.pt.model.df)
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
        検索開始
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
                DGF.PandasAstype(self.pt.model.df)
                DGF.Pandas_mem_usage(self.pt.model.df)
                self.pt.show()
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
                DGF.PandasAstype(self.pt.model.df)
                DGF.Pandas_mem_usage(self.pt.model.df)
                self.pt.show()
                DGF.PandasAstype(self.pt2.model.df)
                DGF.Pandas_mem_usage(self.pt2.model.df)
                self.pt2.show()
        except:
            tk.messagebox.showinfo("確認", "入金列の書式整理エラーです。")

    # -------------------------------------------------------------------------------------
    def OutMCheck(self, OutM_col, OutM_col2):
        """
        検索開始
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
                DGF.PandasAstype(self.pt.model.df)
                DGF.Pandas_mem_usage(self.pt.model.df)
                self.pt.show()
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
                DGF.PandasAstype(self.pt.model.df)
                DGF.Pandas_mem_usage(self.pt.model.df)
                self.pt.show()
                DGF.PandasAstype(self.pt2.model.df)
                DGF.Pandas_mem_usage(self.pt2.model.df)
                self.pt2.show()
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
                DGF.PandasAstype(self.pt.model.df)
                DGF.Pandas_mem_usage(self.pt.model.df)
                self.pt.show()
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
                DGF.PandasAstype(self.pt.model.df)
                DGF.Pandas_mem_usage(self.pt.model.df)
                self.pt.show()
                DGF.PandasAstype(self.pt2.model.df)
                DGF.Pandas_mem_usage(self.pt2.model.df)
                self.pt2.show()
        except:
            tk.messagebox.showinfo("確認", "日付列の書式整理エラーです。")

    # -------------------------------------------------------------------------------------
    def StrCheck(self, col):
        """
        文字列の形式を揃える
        """
        try:
            code_regex = re.compile(
                "[!\"#$%&'\\\\()*+,-./:;<=>?@[\\]^_`{|}~「」〔〕“”〈〉『』【】＆＊・（）＄＃＠。、？！｀＋￥％]"
            )
            nptxt = np.array(self.pt.model.df)[:, col]
            ptCol = np.array(self.pt.model.df.columns)
            for r in range(nptxt.shape[0]):
                txt = nptxt[r]
                if type(txt) == str:
                    txt = code_regex.sub("", txt)
                    nptxt[r] = txt
            pt = np.array(self.pt.model.df)
            pt[:, col] = nptxt
            pt = pd.DataFrame(pt, columns=ptCol)
            self.pt.model.df = pt
            DGF.PandasAstype(self.pt.model.df)
            DGF.Pandas_mem_usage(self.pt.model.df)
            self.pt.show()
        except:
            tk.messagebox.showinfo("確認", "文字列の書式整理エラーです。")

    # -------------------------------------------------------------------------------------
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
        検索開始
        """
        try:
            CL = self.ChangeList()
            self.SinglePtSearch(CL[0], CL[1], CL[2], CL[3], CL[4], CL[5])
        except:
            tk.messagebox.showinfo("確認", "比較ファイルが指定されていません。")

    # ---------------------------------------------------------------------
    def SinglePtSearch(self, Day_col, Day_col2, OutM_col, OutM_col2, InM_col, InM_col2):
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
            if pt[r, OutM_col] == pt[r, OutM_col]:
                if pt[r, OutM_col] != "" and pt[r, OutM_col] != float("nan"):
                    ptstr = pt[r, Day_col] + pt[r, OutM_col]
                    for rr in range(pt2.shape[0]):
                        if pt2[rr, InM_col2] == pt2[rr, InM_col2]:
                            try:
                                pt2str = pt2[rr, Day_col2] + pt2[rr, InM_col2]
                                if ptstr == pt2str:
                                    self.EntrySelect(self.pt2, r)
                                    break
                                else:
                                    pt_r_list[r] = ""
                            except:
                                pt_r_list[r] = ""
                elif pt[r, InM_col] != "" and pt[r, InM_col] != float("nan"):
                    ptstr = pt[r, Day_col] + pt[r, InM_col]
                    for rr in range(pt2.shape[0]):
                        if pt2[rr, OutM_col2] == pt2[rr, OutM_col2]:
                            try:
                                pt2str = pt2[rr, Day_col2] + pt2[rr, OutM_col2]
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
                CL = self.ChangeList()
                self.PtSearch(CL[0], CL[1], CL[2], CL[3], CL[4], CL[5])
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
        Day_col,
        Day_col2,
        OutM_col,
        OutM_col2,
        InM_col,
        InM_col2,
    ):
        try:
            # if r == 10:
            #     print("")
            if pt[r, OutM_col] == pt[r, OutM_col]:
                if pt[r, OutM_col] != "" and pt[r, OutM_col] != float("nan"):
                    ptstr = pt[r, Day_col] + pt[r, OutM_col]
                    try:
                        for rr in range(pt2.shape[0]):
                            if pt2[rr, InM_col2] == pt2[rr, InM_col2]:
                                try:
                                    pt2str = pt2[rr, Day_col2] + pt2[rr, InM_col2]
                                    if ptstr == pt2str:
                                        pt_r_list[r] = rr + 1
                                        break
                                    else:
                                        pt_r_list[r] = ""
                                except:
                                    pt_r_list[r] = ""
                    except:
                        pt_r_list[r] = ""
                elif pt[r, InM_col] != "" and pt[r, InM_col] != float("nan"):
                    try:
                        ptstr = pt[r, Day_col] + pt[r, InM_col]
                        for rr in range(pt2.shape[0]):
                            if pt2[rr, OutM_col2] == pt2[rr, OutM_col2]:
                                try:
                                    pt2str = pt2[rr, Day_col2] + pt2[rr, OutM_col2]
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
            pt_r_list[r] = ""

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
                self.PtSearch_Sub(
                    r,
                    pt,
                    pt2,
                    pt_r_list,
                    Day_col,
                    Day_col2,
                    OutM_col,
                    OutM_col2,
                    InM_col,
                    InM_col2,
                )
            ptCol.append(PlusCol)
            pt_r_list = np.reshape(pt_r_list, (pt_r_list.shape[0], 1))
            pt = np.hstack([pt, pt_r_list])
            pt = pd.DataFrame(pt, columns=ptCol)
            self.pt.model.df = pt
            DGF.PandasAstype(self.pt.model.df)
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
            DGF.PandasAstype(self.pt2.model.df)
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
            DGF.PandasAstype(self.pt2.model.df)
            DGF.Pandas_mem_usage(self.pt2.model.df)
            self.pt2.show()

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
                DGF.PandasAstype(self.pt2.model.df)
                DGF.Pandas_mem_usage(self.pt2.model.df)
                self.pt2.show()
            ptDF = self.SingleSplit_Sub(self.pt.model.df, In_v, Out_v, Money_v, S_Var)
            if ptDF[0] is True:
                self.pt.model.df = ptDF[1]
                DGF.PandasAstype(self.pt.model.df)
                DGF.Pandas_mem_usage(self.pt.model.df)
                self.pt.show()
        except:
            ptDF = self.SingleSplit_Sub(self.pt.model.df, In_v, Out_v, Money_v, S_Var)
            if ptDF[0] is True:
                self.pt.model.df = ptDF[1]
                DGF.PandasAstype(self.pt.model.df)
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
        データ整理
        """
        if self.DStxt.get() == "":
            if self.select_var.get() == 1:
                D_c = "Day_col"
                D_c2 = "Day_col2"
            else:
                D_c = "Day_col"
        else:
            D_c = "else"
            D_c2 = "else"

        if self.OMtxt.get() == "":
            if self.select_var.get() == 1:
                O_c = "OutM_col"
                O_c2 = "OutM_col2"
            else:
                O_c = "OutM_col"
        else:
            O_c = "else"
            O_c2 = "else"

        if self.IMtxt.get() == "":
            if self.select_var.get() == 1:
                I_c = "InM_col"
                I_c2 = "InM_col2"
            else:
                I_c = "InM_col"
        else:
            I_c = "else"
            I_c2 = "else"

        self.ChangeList_sub(D_c, D_c2, O_c, O_c2, I_c, I_c2)

    # -------------------------------------------------------------------------------------
    def ChangeList_sub(self, Day_col, Day_col2, OutM_col, OutM_col2, InM_col, InM_col2):
        try:
            if self.select_var.get() == 1:
                self.ColumnsDelete(self.pt)
                # 　複数----------------------------------------------------------
                print(self.pt2.model.df.columns)
                ptcol = np.array(self.pt.model.df.columns)
                if Day_col != "Day_col":
                    Day_col = int(np.where(ptcol == self.DStxt.get())[0])
                if OutM_col != "OutM_col":
                    OutM_col = int(np.where(ptcol == self.OMtxt.get())[0])
                if InM_col != "InM_col":
                    InM_col = int(np.where(ptcol == self.IMtxt.get())[0])

                ptcol2 = np.array(self.pt2.model.df.columns)
                if Day_col2 != "Day_col2":
                    Day_col2 = int(np.where(ptcol2 == self.DStxt.get())[0])
                if OutM_col2 != "OutM_col2":
                    OutM_col2 = int(np.where(ptcol2 == self.OMtxt.get())[0])
                if InM_col2 != "InM_col2":
                    InM_col2 = int(np.where(ptcol2 == self.IMtxt.get())[0])

                ptarray = np.array(self.pt.model.df)
                for c in range(ptarray.shape[1]):
                    if c == Day_col and Day_col != "Day_col":
                        self.DaysCheck(Day_col, Day_col2)
                    elif c == OutM_col and OutM_col != "OutM_col":
                        self.OutMCheck(OutM_col, OutM_col2)
                    elif c == InM_col and InM_col != "InM_col":
                        self.InMCheck(InM_col, InM_col2)
                    else:
                        self.StrCheck(c)
                return Day_col, Day_col2, OutM_col, OutM_col2, InM_col, InM_col2
            else:
                self.ColumnsDelete(self.pt)
                # 　単一----------------------------------------------------------
                print(self.pt2.model.df.columns)
                ptcol = np.array(self.pt.model.df.columns)
                Day_col = int(np.where(ptcol == self.DStxt.get())[0])

                ptcol2 = np.array(self.pt2.model.df.columns)
                Day_col2 = int(np.where(ptcol2 == self.DStxt.get())[0])

                ptarray = np.array(self.pt.model.df)
                for c in range(ptarray.shape[1]):
                    if c == Day_col:
                        self.DaysCheck(Day_col, Day_col2)
                    else:
                        self.StrCheck(c)
                self.SingleSplit()

                ptcol = np.array(self.pt.model.df.columns)
                Day_col = int(np.where(ptcol == self.DStxt.get())[0])

                ptcol2 = np.array(self.pt2.model.df.columns)
                Day_col2 = int(np.where(ptcol2 == self.DStxt.get())[0])

                OutM_col = int(np.where(ptcol == "出金")[0][0])
                InM_col = int(np.where(ptcol == "入金")[0][0])
                OutM_col2 = int(np.where(ptcol2 == "出金")[0][0])
                InM_col2 = int(np.where(ptcol2 == "入金")[0][0])

                ptarray = np.array(self.pt.model.df)
                for c in range(ptarray.shape[1]):
                    if c == OutM_col:
                        self.OutMCheck(OutM_col, OutM_col2)
                    elif c == InM_col:
                        self.InMCheck(InM_col, InM_col2)
                return Day_col, Day_col2, OutM_col, OutM_col2, InM_col, InM_col2
        except:
            if self.select_var.get() == 1:
                self.ColumnsDelete(self.pt)
                # 　複数----------------------------------------------------------
                print(self.pt2.model.df.columns)
                ptcol = np.array(self.pt.model.df.columns)
                Day_col = int(np.where(ptcol == self.DStxt.get())[0])
                OutM_col = int(np.where(ptcol == self.OMtxt.get())[0])
                InM_col = int(np.where(ptcol == self.IMtxt.get())[0])
                ptarray = np.array(self.pt.model.df)
                for c in range(ptarray.shape[1]):
                    if c == Day_col:
                        self.DaysCheck(Day_col, "Day_col2")
                    else:
                        self.StrCheck(c)

                return Day_col, "Day_col2", OutM_col, "OutM_col2", InM_col, "InM_col2"
            else:
                self.ColumnsDelete(self.pt)
                # 　単一----------------------------------------------------------
                print(self.pt2.model.df.columns)
                ptcol = np.array(self.pt.model.df.columns)
                Day_col = int(np.where(ptcol == self.DStxt.get())[0])
                ptarray = np.array(self.pt.model.df)
                for c in range(ptarray.shape[1]):
                    if c == Day_col:
                        self.DaysCheck(Day_col, "Day_col2")
                    else:
                        self.StrCheck(c)
                self.SingleSplit()
                return (
                    Day_col,
                    "Day_col2",
                    "OutM_col",
                    "OutM_col2",
                    "InM_col",
                    "InM_col2",
                )

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
        if filename != "":
            enc = DGF.CSVO.getFileEncoding(self.FileName)
            self.table = self.pt.importCSV(self.FileName, encoding=enc)
            options = {"fontsize": t_font[1]}
            DGF.config.apply_options(options, self.pt)
            # DF型変換------------------------------
            DGF.PandasAstype(self.pt.model.df)
            DGF.Pandas_mem_usage(self.pt.model.df)
            # --------------------------------------
            self.pt.show()
            self.OCR_url.delete(0, tk.END)
            self.OCR_url.insert(0, self.FileName)


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
    global Master, csv_u
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
    app = Application(csvurl=csv_u, master=root)
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
    # imgurl = r"D:\OCRTESTPDF\PDFTEST\相続_JA_1page.png"
    imgurl = r"C:\Users\もちねこ\Desktop\PDFTEST\JA_1page.png"
    tomlurl = tomlread()
    # csv_u = r"D:\OCRTESTPDF\PDFTEST\相続_JA_1page.csv"
    csv_u = r"C:/Users/もちねこ/Desktop/PDFTEST/JA_1page_AutoJounal.csv"
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
    app = Application(csvurl=csv_u, master=root)
    # --- 基本的な表示準備 ----------------

    app.mainloop()
