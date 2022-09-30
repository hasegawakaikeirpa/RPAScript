import tkinter as tk
import Frame.DGFrame as DGF
import Frame.ScrollableFrame as SF

###################################################################################################
class Application(tk.Frame):
    def __init__(self, csvurl, master=None):
        # Windowの初期設定を行う。
        super().__init__(master)
        # Windowの画面サイズを設定する。
        G_logger.debug("P_Table起動")  # Log出力
        self.FileName = csvurl
        self.master.geometry("1480x750+0+0")  # Window表示位置指定
        self.master.minsize(1480, 750)
        self.master.protocol("WM_DELETE_WINDOW", self.click_close)  # 閉じる処理設定
        # 統合フレーム
        self.Main_Frame = tk.Frame(
            self.master, width=1480, height=750, bd=2, relief=tk.RIDGE
        )
        self.Main_Frame.grid(row=0, rowspan=2, column=0, sticky=tk.NSEW)
        # サイドフレーム
        self.Side_Frame = tk.Frame(
            self.master, width=330, height=750, bd=2, relief=tk.RIDGE
        )
        self.Side_Frame.grid(row=0, column=1, sticky=tk.NSEW)
        # サイドフレーム2
        self.Side_Frame2 = tk.Frame(
            self.master, width=330, height=750, bd=2, relief=tk.RIDGE
        )
        self.Side_Frame2.grid(row=1, column=1, sticky=tk.NSEW)
        ########################################################################################
        # フレーム設定---------------------------------------------------------------------
        DGF.create_Frame(self, int(1480 / 2), 700)  # OCR抽出結果表フレーム
        # サイドフレーム-------------------------------------------------------------------
        tk.Label(self.Side_Frame, text="日付列名").grid(row=0, column=0)  # 日付列名ラベル
        txt = tk.Entry(self.Side_Frame, width=35, bg="snow")  # 日付列名テキストボックス
        txt.insert(0, "")  # 日付列名テキストボックスに文字代入
        txt.grid(row=0, column=1, sticky=tk.W)  # 日付列名テキストボックス配置
        tk.Label(self.Side_Frame, text="入金列名").grid(row=1, column=0)  # 日付列名ラベル
        txt = tk.Entry(self.Side_Frame, width=35, bg="snow")  # 日付列名テキストボックス
        txt.insert(0, "")  # 日付列名テキストボックスに文字代入
        txt.grid(row=1, column=1, sticky=tk.W)  # 日付列名テキストボックス配置
        tk.Label(self.Side_Frame, text="出金列名").grid(row=2, column=0)  # 日付列名ラベル
        txt = tk.Entry(self.Side_Frame, width=35, bg="snow")  # 日付列名テキストボックス
        txt.insert(0, "")  # 日付列名テキストボックスに文字代入
        txt.grid(row=2, column=1, sticky=tk.W)  # 日付列名テキストボックス配置
        self.FileRead = tk.Button(
            self.Side_Frame,
            text="比較対象ファイル複数選択",
            fg="White",
            command=self.ChangeFileRead,
            bg="steelblue3",
            font=1,
            width=23,
            height=1,
        )  # ボタン作成
        self.FileRead.grid(row=3, column=0, columnspan=2, sticky=tk.N)  # 日付列名テキストボックス配置
        self.SingleFileRead = tk.Button(
            self.Side_Frame,
            text="比較対象ファイル追加",
            fg="White",
            command=self.ChangeFileSingleRead,
            bg="Orange",
            font=1,
            width=23,
            height=1,
        )  # ボタン作成
        self.SingleFileRead.grid(
            row=4, column=0, columnspan=2, sticky=tk.N
        )  # 日付列名テキストボックス配置
        # サイドフレーム2------------------------------------------------------------------
        tk.Label(self.Side_Frame2, text="比較対象ファイル").grid(row=0, column=0)  # 日付列名ラベル
        self.module = ""
        self.listbox_var = tk.StringVar(value=self.module)
        self.listbox = tk.Listbox(
            self.Side_Frame2, width=60, listvariable=self.listbox_var
        )
        self.listbox.grid(row=1, column=0, sticky=tk.NSEW)

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

    # -------------------------------------------------------------------------------------
    def ChangeFileRead(self):
        """
        比較対象CSVの複数追加
        """
        fTyp = [("CSV", ".csv")]
        read_list = tk.filedialog.askopenfilenames(filetypes=fTyp, initialdir="./")
        self.module = read_list
        self.listbox_var.set(self.module)

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
