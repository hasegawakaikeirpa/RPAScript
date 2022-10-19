import tkinter as tk
from tkinter import filedialog, messagebox
import customtkinter as ck
from PIL import ImageTk, Image
import time
import os
import threading
import IconCode
import ViewGUI
import TKINTERCV2Setting as TKCV
import Frame.tkRootSetting as tkRoot
import logging.config
from platform import machine, node, platform, processor, release, system, version
from socket import gethostbyname, gethostname
from uuid import getnode


class Open_Win:
    """
    概要: TKinterメインWindowクラス
    """

    def __init__(self, window_root, title_n):
        # logger設定-----------------------------------------------------------------------------------------------------
        logging.config.fileConfig(os.getcwd() + r"\LogConf\logging_debug.conf")
        self.logger = logging.getLogger(__name__)
        # ---------------------------------------------------------------------------------------------------------------
        # 初回Log
        self.logger.debug(f"Network: {node()}")  # ネットワーク名
        self.logger.debug(f"Machine: {machine()}")  # 機種
        self.logger.debug(f"Processor: {processor()}")  # プロセッサ名 (CPU)
        self.logger.debug(f"Platform: {platform() }")  # プラットフォーム (OS) 情報
        self.logger.debug(f"System: {system() }")  # OS名
        self.logger.debug(f"Release: {release()}")  # リリース情報
        self.logger.debug(f"Version: {version()}")  # バージョン情報
        self.logger.debug(f"MAC Address: {getnode():_X}")  # MACアドレス
        self.logger.debug(f"Host name: {gethostname()}")  # ホスト名
        self.logger.debug(f"IP Address: {gethostbyname(gethostname())}")  # IPアドレス
        self.logger.debug("起動")  # Log出力
        # ---------------------------------------------------------------------------------------------------------------
        self.w_root = tkRoot.WindowSet(
            window_root, "blue", 800, 400, "OCR読取 Ver:0.9-Menu-", self.logger
        )  # ルートウィンドウ
        self.w_root_top = tk.Toplevel(self.w_root)
        self.w_root_top.withdraw()
        # self.w_root.overrideredirect(1)
        ######################################################
        # 変数初期化
        self.Com_path = ""
        self.tomlPath = self.tomlread()
        ######################################################
        # フレーム
        self.Menu_fra = tk.Frame(self.w_root, width=800, height=400, bg="#60cad1")
        self.Menu_fra.columnconfigure(0, weight=1)
        self.Menu_fra.rowconfigure(0, weight=1)
        self.Menu_fra.pack(fill=tk.BOTH, expand=True)
        # ラベル
        self.CompOpen_btn = ck.CTkButton(
            self.Menu_fra,
            text="関与先フォルダ選択",
            width=200,
            height=5,
            command=self.ReadCompany,
        )
        self.CompOpen_btn.grid(row=0, column=0, pady=5, sticky=tk.N + tk.W + tk.E)
        # テキスト
        self.Company_ent = ck.CTkEntry(
            self.Menu_fra,
            width=600,
            height=5,
        )
        self.Company_ent.grid(row=0, column=1, pady=5, sticky=tk.N + tk.W + tk.E)
        # ボタン
        self.ViewOpen_btn = ck.CTkButton(
            self.Menu_fra, text="画像編集起動", bg="#60cad1", width=800, command=self.ViewOpen
        )
        self.ViewOpen_btn.grid(
            row=1, column=0, pady=5, columnspan=2, sticky=tk.N + tk.W + tk.E
        )
        # ボタン
        self.TKCV2Open_btn = ck.CTkButton(
            self.Menu_fra,
            text="表形式編集起動",
            bg="#60cad1",
            width=800,
            command=self.TKCVOpen,
        )
        self.TKCV2Open_btn.grid(
            row=2, column=0, pady=5, columnspan=2, sticky=tk.N + tk.W + tk.E
        )
        # ボタン
        self.P_table_btn = ck.CTkButton(
            self.Menu_fra, text="比較編集起動", bg="#60cad1", width=800, command=self.ViewOpen
        )
        self.P_table_btn.grid(
            row=3, column=0, pady=5, columnspan=2, sticky=tk.N + tk.W + tk.E
        )
        # ボタン
        self.Grid_btn = ck.CTkButton(
            self.Menu_fra,
            text="仕訳検索編集起動",
            bg="#60cad1",
            width=800,
            command=self.ViewOpen,
        )
        self.Grid_btn.grid(
            row=4, column=0, pady=5, columnspan=2, sticky=tk.N + tk.W + tk.E
        )

    # クラス関数------------------------------------------------------------------------------
    def ViewOpen(self):
        """
        ViewGUI開く
        """
        url = self.Company_ent.get()
        if url != "":
            self.Menu_fra.pack_forget()
            ViewGUI.Open(self, self.w_root, self.w_root_top, url, self.logger)
        else:
            messagebox.showinfo("確認", "初めに関与先フォルダを指定して下さい。")

    def TKCVOpen(self):
        """
        TKCV2開く
        """
        url = self.Company_ent.get()
        if url != "":
            self.Menu_fra.pack_forget()
            TKCV.Open(self, self.w_root, self.w_root_top, url, self.logger)
        else:
            messagebox.showinfo("確認", "初めに関与先フォルダを指定して下さい。")

    def tomlread(self):
        """
        tomlリード
        """
        try:
            r_toml = os.getcwd() + r"\OCRView\Setting.toml"
            return r_toml
        except:
            r_toml = os.getcwd() + r"\Setting.toml"
            return r_toml

    def ReadCompany(self):
        """
        関与先フォルダリード
        """
        self.Com_path = filedialog.askdirectory(
            initialdir=self.Com_path, mustexist=True
        )
        self.Company_ent.delete(0, tk.END)
        self.Company_ent.insert(0, self.Com_path)

    def click_close(self):
        """
        ウィンドウ×ボタンクリック
        """
        if messagebox.askokcancel("確認", "終了しますか？"):
            self.logger.debug("MenuClose完了")  # Log出力
            self.window_root.destroy()


def RoundButton(w, img1, img2, cmd):
    image_a = ImageTk.PhotoImage(Image.open(img1))
    image_b = ImageTk.PhotoImage(Image.open(img2))

    def on_enter(e):
        btn["image"] = image_b

    def on_leave(e):
        btn["image"] = image_a

    btn = tk.Button(
        w, image=image_b, border=0, cursor="hand2", command=cmd, relief=tk.SUNKEN
    )
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)
    return btn


def Open(title_n):
    main_window = tk.Tk()
    # Viewクラス生成
    Open_Win(main_window, title_n)
    # 　フレームループ処理
    main_window.mainloop()
    return


def FontSearch():
    for f in tk.Tk().call("font", "families"):
        print(f)


if __name__ == "__main__":
    Open("OCR読取 Ver:0.9")
    # FontSearch()
    # 　Tk MainWindow 生成
    # main_window = tk.Tk()
    # main_window = tk.Tk()
    # Viewクラス生成
    # ViewGUI(main_window, "./")

    # 　フレームループ処理
    # main_window.mainloop()
