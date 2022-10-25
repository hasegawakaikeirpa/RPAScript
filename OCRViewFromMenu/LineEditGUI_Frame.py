import tkinter as tk

from PIL import Image, ImageTk
import customtkinter as ck

# from CV2Setting import straightlinesetting
# from GCloudVision import AutoLine, LineTomlOut
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
    # サイドメニューフレーム##########################################################
    SideWidth = 50
    SideHeight = 50
    LabelWidth = 50
    LabelHeight = 50
    BtnWidth = 50
    BtnHeight = 50
    EntWidth = 50
    EntHeight = 50
    t_font = 50

    # サイドメニュー内フレーム########################################################
    Tframe = tk.Frame(
        self.bottumFrame,
        width=SideWidth,
        height=SideHeight,
        bg="#ecb5f5",
        relief=tk.GROOVE,
    )
    Tframe.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    # LineNo表示テキスト
    ck.CTkLabel(
        master=Tframe,
        text="選択ライン名",
        width=LabelWidth,
        height=LabelHeight,
        corner_radius=8,
        text_font=t_font,
    ).grid(row=0, column=0, pady=5)
    # テキストボックスの作成と配置
    txt = ck.CTkEntry(
        master=Tframe,
        width=EntWidth,
        height=EntHeight,
        border_width=2,
        corner_radius=8,
        text_color="black",
        border_color="snow",
        fg_color="snow",
    )
    txt.grid(row=0, column=1, pady=5)
    # テキスト変換一致率
    ck.CTkLabel(
        master=Tframe,
        text="テキスト変換一致率",
        width=LabelWidth,
        height=LabelHeight,
        corner_radius=8,
        text_font=t_font,
    ).grid(row=1, column=0, pady=5)
    # テキストボックスの作成と配置
    self.ChangeVar = ck.CTkEntry(
        master=Tframe,
        width=EntWidth,
        height=EntHeight,
        border_width=2,
        corner_radius=8,
        text_color="black",
        border_color="snow",
        fg_color="snow",
    )
    self.ChangeVar.insert(0, 50)
    self.ChangeVar.grid(row=1, column=1, pady=5)
    # 行数表示テキスト
    ck.CTkLabel(
        master=Tframe,
        text="設定ファイル",
        width=LabelWidth,
        height=LabelHeight,
        corner_radius=8,
        text_font=t_font,
    ).grid(row=3, column=0, pady=5)
    self.tomlurl = ck.CTkEntry(
        master=Tframe,
        width=EntWidth,
        height=EntHeight,
        border_width=2,
        corner_radius=8,
        text_color="black",
        border_color="snow",
        fg_color="snow",
    )
    self.tomlurl.insert(0, self.control.tomlurl)
    self.tomlurl.grid(row=3, column=1, pady=5)
    # 行数表示テキスト
    # 設定ファイル変更ボタン--------------------------------------------------------
    self.tomlbutton = ck.CTkButton(
        master=Tframe,
        text="設定ファイル変更",
        command=self.ChangeToml,
        width=BtnWidth,
        height=BtnHeight,
        border_width=2,
        corner_radius=8,
        text_color="snow",
        border_color="snow",
    )
    self.tomlbutton.grid(row=4, column=0, columnspan=2, sticky=tk.N)


def Frame2(self):
    #################################################################################
    # 列名設定フレーム################################################################
    # サイドメニュー内フレーム########################################################
    # 配置
    # サイドメニューフレーム##########################################################
    SideWidth = 50
    SideHeight = 50
    LabelWidth = 50
    LabelHeight = 50
    BtnWidth = 50
    BtnHeight = 50
    EntWidth = 50
    EntHeight = 50
    t_font = 50

    Tframe2 = tk.Frame(
        self.bottumFrame,
        width=SideWidth,
        height=SideHeight,
        bg="#ecb5f5",
        relief=tk.GROOVE,
    )
    Tframe2.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    create_table(self, Tframe2)


def create_table(self, Tframe2):
    # ツリーフレーム設定---------------------------------------------------------------------
    self.OCR_frame = tk.Frame(
        Tframe2, width=1000, height=100, bd=2, bg="#fce4d2", relief=tk.RIDGE
    )  # 親フレーム
    # self.OCR_frame.grid(row=0, column=0, sticky=tk.N + tk.S + tk.W + tk.E)
    self.OCR_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    self.tree_frame = tk.Frame(
        self.OCR_frame, width=1000, height=100, bg="#fce4d2"
    )  # 子フレーム
    # サイズグリップ
    # sizegrip = ttk.Sizegrip(self.OCR_frame)
    # sizegrip.grid(row=0, column=0, sticky=(tk.S, tk.E))
    tk.Label(self.OCR_frame, text="OCR抽出結果表", bg="#fce4d2").grid(
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

    self.tree_frame.grid(row=2, column=0, padx=30, sticky=tk.N + tk.S + tk.W + tk.E)
    # df = TableModel.getSampleData()
    # pt = Table(self.tree_frame)
    pt = MT.MyTable(
        self.tree_frame,
        width=int(1000 * 0.90),
        height=int(100 * (100 * 0.75)),
        sticky=tk.N + tk.S + tk.W + tk.E,
    )  # テーブルをサブクラス化
    enc = Functions.getFileEncoding(self.FileName)
    self.table = pt.importCSV(self.FileName, encoding=enc)
    self.pt = pt
    self.pt._name = "OCR抽出結果表Main"
    # options is a dict that you can set yourself
    options = {"fontsize": self.control.t_font[1]}
    config.apply_options(options, self.pt)
    # DF型変換------------------------------
    Functions.Pandas_mem_usage(self.pt.model.df)
    # --------------------------------------
    self.pt.resized
    self.pt.show()
