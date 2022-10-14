import tkinter as tk
import Frame.DGFrame as DGF

# import numpy as np
# import WarekiHenkan as wh
import pandas as pd

# import re
import logging.config
import toml
import os
import IconCode
import customtkinter as ck
import sqlite3 as sql
from CSVOut import getFileEncoding
import Frame.MyTableSQL as MyTableSQL

###################################################################################################
class Application(tk.Toplevel):
    def __init__(self, Top, master=None):
        global SideWidth, SideHeight, LabelWidth, t_font
        global LabelHeight, BtnWidth, BtnHeight, EntHeight, EntWidth
        global wid_Par, hei_Par, width_of_window, height_of_window, wid, hei
        f = False
        m = Top
        while f is False:
            m = m.master
            if m.master is None:
                try:
                    m = m.children["!application"]
                    Top = m.top
                    break
                except:
                    m = Top
                    break
        # customtkスタイル
        ck.set_appearance_mode("System")  # Modes: system (default), light, dark
        ck.set_default_color_theme(
            "dark-blue"
        )  # Themes: blue (default), dark-blue, green
        width_of_window = int(int(m.winfo_screenwidth()) * 0.3)
        height_of_window = int(int(m.winfo_screenheight()) * 0.5)
        wid_Par = width_of_window / 1459
        hei_Par = height_of_window / 820
        x_coodinate = width_of_window * 2
        y_coodinate = height_of_window * 0.01
        data = IconCode.icondata()
        Top.tk.call("wm", "iconphoto", Top._w, tk.PhotoImage(data=data))
        Top.title("OCR読取 Ver:0.9-比較ウィンドウ-" + tbname)
        Top.minsize(width_of_window, height_of_window)
        Top.protocol("WM_DELETE_WINDOW", lambda: self.Rep_click_close(Top))  # 閉じる処理設定
        Top.wm_attributes("-topmost", True)  # 常に一番上のウィンドウに指定
        # Top.resizable(0, 0)
        Top.minsize(width_of_window, height_of_window)
        Top.geometry(
            "%dx%d+%d+%d"
            % (width_of_window, height_of_window, x_coodinate, y_coodinate)
        )
        ########################################
        wid = 2.25  # width割率
        hei = 1.4  # width割率
        ########################################
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
        t_font = (1, int(30 * wid_Par))
        ################################################################################
        self.Main_Frame = tk.Frame(
            Top,
            width=width_of_window,
            height=height_of_window,
            bg="#fabd91",
            relief=tk.GROOVE,
        )
        self.Main_Frame.pack(fill=tk.BOTH, expand=True)
        # フレーム
        self.Upper_Frame = tk.Frame(
            self.Main_Frame,
            width=int(width_of_window / 4),
            height=int(height_of_window * 0.8),
            bd=2,
            bg="#fabd91",
            relief=tk.RIDGE,
        )
        self.Upper_Frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        # フレーム
        self.Bottom_Frame = tk.Frame(
            self.Main_Frame,
            width=int(width_of_window / 4),
            height=int(height_of_window * 0.8),
            bd=2,
            bg="#fabd91",
            relief=tk.RIDGE,
        )
        self.Bottom_Frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        #######################################################################################
        # Start ####################################################################
        ck.CTkLabel(
            master=self.Upper_Frame,
            text="OCR抽出結果表",
            width=LabelWidth,
            height=LabelHeight,
            corner_radius=8,
            text_font=t_font,
        ).grid(row=0, column=0, padx=5)
        self.ReplaceSet = ck.CTkEntry(
            master=self.Upper_Frame,
            width=EntWidth,
            height=EntHeight,
            border_width=2,
            corner_radius=8,
            text_color="black",
            border_color="snow",
            fg_color="snow",
        )
        self.ReplaceSet.grid(row=0, column=1, padx=5)
        # SQL
        # self.CDB_btn = ck.CTkButton(
        #     master=self.Upper_Frame,
        #     text="読込",
        #     command=self.FileOpen,
        #     width=EntWidth,
        #     height=EntHeight,
        #     border_width=2,
        #     corner_radius=8,
        #     text_color="black",
        #     border_color="snow",
        #     fg_color="blue",
        # )
        # self.CDB_btn.grid(row=0, column=3, padx=5)
        self.Ent_btn = ck.CTkButton(
            master=self.Upper_Frame,
            text="確定",
            command=lambda: CreateDB.EntDF(self, dbname, tbname, self.P_table.model.df),
            width=EntWidth,
            height=EntHeight,
            border_width=2,
            corner_radius=8,
            text_color="black",
            border_color="snow",
            fg_color="lightblue",
        )
        self.Ent_btn.grid(row=0, column=4, padx=5)
        self.P_table = self.Read_P_Table(
            self.Bottom_Frame,
            int(width_of_window / wid),
            int(height_of_window / hei),
            t_font,
        )  # OCR抽出結果表フレーム
        self.sql_data = CreateDB(dbname, tbname)
        self.sql_data.readsql(dbname, tbname, self.P_table)
        # m.update()

    # -------------------------------------------------------------------------------------
    def Read_P_Table(self, Frame, width, height, t_font):
        r_pt = MyTableSQL.MyTableSQL(
            Frame,
            width=width,
            height=height,
            sticky=tk.N + tk.S + tk.W + tk.E,
        )  # テーブルをサブクラス化
        # enc = getFileEncoding(csv_url)
        # r_pt.importCSV(csv_url, encoding=enc)
        r_pt._name = "SQLMain"
        # options is a dict that you can set yourself
        options = {"fontsize": t_font[1]}
        DGF.config.apply_options(options, r_pt)
        r_pt.resized
        r_pt.show()
        return r_pt

    # -------------------------------------------------------------------------------------
    def FileOpen(self):
        global csv_url, dbname, tbname
        self.master.wm_attributes("-topmost", False)  # 常に一番上のウィンドウに指定
        # ファイル→開く
        csv_url = tk.filedialog.askopenfilename(
            filetypes=[
                ("CSV", ".csv"),
            ],  # ファイルフィルタ
            initialdir=os.getcwd(),  # カレントディレクトリ
        )
        tbname = os.path.splitext(os.path.basename(csv_url))[0]
        self.sql_data.CsvConvert(csv_url, dbname, tbname)
        self.top.wm_attributes("-topmost", True)  # 常に一番上のウィンドウに指定

    # -------------------------------------------------------------------------------------
    def Rep_click_close(self, Win):
        """
        ウィンドウ×ボタンクリック
        """
        try:
            Win.withdraw()
            # G_logger.debug("ReplaceView完了")  # Log出力
        except:
            G_logger.debug("ReplaceView失敗")  # Log出力


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


# ---------------------------------------------------------------------------------------------
class CreateDB:
    """
    dbを作成する
    """

    def __init__(self, dbname, tbname):
        # すでに存在していれば、それにアスセスする。
        conn = sql.connect(dbname)

        # データベースへのコネクションを閉じる。(必須)
        conn.close()

    def CreateTable(self, dbname, tbname):

        conn = sql.connect(dbname)
        # sqliteを操作するカーソルオブジェクトを作成
        cur = conn.cursor()

        # personsというtableを作成してみる
        # 大文字部はSQL文。小文字でも問題ない。
        cur.execute(
            "CREATE TABLE "
            + tbname
            + "(id INTEGER PRIMARY KEY AUTOINCREMENT,name STRING)"
        )

        # データベースへコミット。これで変更が反映される。
        conn.commit()
        conn.close()

    def TableInsert(self, dbname):

        conn = sql.connect(dbname)
        cur = conn.cursor()

        # "name"に"Taro"を入れる
        cur.execute('INSERT INTO persons(name) values("Taro")')
        # 同様に
        cur.execute('INSERT INTO persons(name) values("Hanako")')
        cur.execute('INSERT INTO persons(name) values("Hiroki")')

        conn.commit()

        cur.close()
        conn.close()

    def CheckTable(self, dbname, tbname):

        conn = sql.connect(dbname)
        cur = conn.cursor()

        # terminalで実行したSQL文と同じようにexecute()に書く
        cur.execute("SELECT * FROM " + tbname)

        # 中身を全て取得するfetchall()を使って、printする。
        print(cur.fetchall())

        cur.close()
        conn.close()

    def readsql(self, dbname, tbname, Pandas_T):

        conn = sql.connect(dbname)
        cur = conn.cursor()

        # terminalで実行したSQL文と同じようにexecute()に書く
        try:
            df = pd.read_sql_query("SELECT * FROM " + tbname, conn)
            Pandas_T.model.df = df
            Pandas_T.show()
        except:
            df = pd.DataFrame(
                data={
                    "変更前": ["変更前_文字列"],
                    "変更後": ["変更後_文字列"],
                }
            )
            Pandas_T.model.df = df
            Pandas_T.show()
            CreateDB.EntDF(self, dbname, tbname, df)
        cur.close()
        conn.close()

    def EntDF(self, dbname, tbname, df):

        conn = sql.connect(dbname)
        cur = conn.cursor()
        df = df.drop_duplicates()
        # データの投入
        df.to_sql(tbname, conn, if_exists="replace", index=False)
        cur.close()
        conn.close()

    def CsvConvert(self, csv_url, dbname, tbname):
        # pandasでカレントディレクトリにあるcsvファイルを読み込む
        # csvには、1列目にyear, 2列目にmonth, 3列目にdayが入っているとする。
        enc = getFileEncoding(csv_url)
        df = pd.read_csv(csv_url, encoding=enc)

        # カラム名（列ラベル）を作成。csv file内にcolumn名がある場合は、下記は不要
        # pandasが自動で1行目をカラム名として認識してくれる。
        # df.columns = ["year", "month", "day"]

        conn = sql.connect(dbname)
        cur = conn.cursor()

        # dbのnameをsampleとし、読み込んだcsvファイルをsqlに書き込む
        # if_existsで、もしすでにexpenseが存在していたら、書き換えるように指示
        df.to_sql(tbname, conn, if_exists="replace", index=False)

        # 作成したデータベースを1行ずつ見る
        select_sql = "SELECT * FROM " + tbname
        for row in cur.execute(select_sql):
            print(row)

        cur.close()
        conn.close()


# -------------------------------------------------------------------------------------
def Main(self, csv_u, tbn):
    """
    呼出関数
    """
    global Master, csv_url, dbname, tbname
    global G_logger, C_MT, C_TP
    global Banktoml, tomlurl, PlusCol, imgurl

    csv_url = csv_u
    tbname = tbn
    dbname = "ReplaceView.db"
    # -----------------------------------------------------------
    self.top = tk.Toplevel()  # サブWindow作成
    app = Application(self.top, self.master)
    CreateDB(dbname, tbname)
    CreateDB.readsql(self, dbname, tbname, app.P_table)
    return self.top


# ------------------------------------------------------------------------------------------
if __name__ == "__main__":

    global Banktoml, tomlurl, PlusCol, imgurl, dbname

    dbname = "ReplaceView.db"
    # CreateDB(dbname, tbname)
    # logger設定-----------------------------------------------------------------------------------------------------
    logging.config.fileConfig(os.getcwd() + r"\LogConf\logging_debug.conf")
    G_logger = logging.getLogger(__name__)
    # ---------------------------------------------------------------------------------------------------------------

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
