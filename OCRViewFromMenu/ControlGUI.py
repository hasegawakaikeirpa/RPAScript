import os
from ModelImage import ModelImage
import sqlite3 as sql
from pandas import DataFrame
import toml
from tkinter import font

# from tkinter import messagebox


class ControlGUI:
    def __init__(self, root, default_path):
        """
        初期設定
        """
        # Model Class生成
        self.model = ModelImage()
        # ディスプレイサイズ
        self.width_of_window = int(int(root.winfo_screenwidth()) * 0.98)
        self.height_of_window = int(int(root.winfo_screenheight()) * 0.9)
        # ディスプレイ初期表示位置
        self.x_coodinate = 0  # self.width_of_window / 4
        self.y_coodinate = 0  # self.height_of_window / 4
        # 各オブジェクト配置間隔
        self.padx = self.x_coodinate / 4
        self.pady = self.y_coodinate / 4
        # 各キャンバスサイズ
        self.FCW = int(self.width_of_window * 0.98)
        self.FCH = int(self.height_of_window * 0.8)
        # 各リサイズ比率
        self.HCW = 1
        self.HCH = 1

        # ディレクトリパス
        self.dir_path = default_path
        # 画像ファイルパス初期設定
        if os.path.isfile(os.getcwd() + r"\OCR.png") is True:
            self.imgurl = os.getcwd() + r"\OCR.png"
        else:
            self.imgurl = os.getcwd() + r"\OCRViewFromMenu\OCR.png"
        # 設定CSVファイルパス初期設定
        if os.path.isfile(os.getcwd() + r"\ListSetting.csv") is True:
            self.SettingCsvurl = os.getcwd() + r"\ListSetting.csv"
        else:
            self.SettingCsvurl = os.getcwd() + r"\OCRViewFromMenu\ListSetting.csv"
        # 設定CSVファイル2パス初期設定
        if os.path.isfile(os.getcwd() + r"\ColumnSetting.csv") is True:
            self.SettingCsvurl_column = os.getcwd() + r"\ColumnSetting.csv"
        else:
            self.SettingCsvurl_column = (
                os.getcwd() + r"\OCRViewFromMenu\ColumnSetting.csv"
            )

        # 画像ファイル名称
        self.img_name = os.path.splitext(os.path.basename(self.imgurl))[0]
        # 画像ファイルから抽出した関与先名
        self.Kanyosaki_name = ""
        # 取扱画像ファイル指定
        self.ext_keys = [".png", ".jpg", ".jpeg", ".JPG", ".PNG", "PDF", "pdf"]

        self.target_files = []
        self.file_pos = 0
        self.file_list = ["..[select file]"]
        # tomlファイルオブジェクト
        self.tomlsetting = self.tomlread()
        self.ReadtomlLine()
        self.Toptitle = self.tomlsetting["Title"]["title"]

        self.clip_sx = 0
        self.clip_sy = 0
        self.clip_ex = 0
        self.clip_ey = 0

        self.canvas = None
        self.DefDB_name = "OCR_DB"
        self.CreateDB(self.DefDB_name)
        self.btn_font = ("", 50)  # ボタンフォントサイズ
        self.t_font = (1, int(8))  # テーブルフォントサイズ

    def tomlread(self):
        """
        tomlリード
        """
        try:
            r_toml = os.getcwd() + r"\OCRViewFromMenu\Setting.toml"
            with open(r_toml, encoding="utf-8") as f:
                Banktoml = toml.load(f)
            self.tomlurl = r_toml
            return Banktoml
        except:
            r_toml = os.getcwd() + r"\Setting.toml"
            with open(r_toml, encoding="utf-8") as f:
                Banktoml = toml.load(f)
            self.tomlurl = r_toml
            return Banktoml

    def ReadtomlLine(self):
        """
        tomlからtoml線軸リストを取得
        """
        try:
            self.YokoList = self.tomlsetting["LineSetting"][self.Yoko_N]
            self.TateList = self.tomlsetting["LineSetting"][self.Tate_N]
        except:
            self.YokoList = self.tomlsetting["LineSetting"]["Nomal_Yoko"]
            self.TateList = self.tomlsetting["LineSetting"]["Nomal_Tate"]

    def is_target(self, name, key_list):
        """
        self.ext_keysで指定した拡張子のみリスト化
        """
        valid = False
        for ks in key_list:
            if ks in name:
                valid = True

        return valid

    def get_file(self, command, set_pos=-1):
        """
        画像プレビュー機能の設定
        """
        if command == "prev":
            self.file_pos = self.file_pos - 1
        elif command == "next":
            self.file_pos = self.file_pos + 1
        elif command == "set":
            self.file_pos = set_pos
        else:  # current
            self.file_pos = self.file_pos

        num = len(self.target_files)
        if self.file_pos < 0:
            self.file_pos = num - 1

        elif self.file_pos >= num:
            self.file_pos = 0
        cur_file = os.path.join(self.dir_path, self.target_files[self.file_pos])
        print("{}/{} {} ".format(self.file_pos, num - 1, cur_file))
        return cur_file

    # Public

    def SetDirlist(self, dir_path):
        """
        フォルダー内画像ファイルをリスト化
        """
        self.dir_path = dir_path
        self.target_files = []

        file_list = os.listdir(self.dir_path)
        for fname in file_list:
            if self.is_target(fname, self.ext_keys):
                self.target_files.append(fname)
                print(fname)

        self.file_pos = 0
        if len(self.target_files) > 0:
            cur_file = self.get_file("current")
            print(cur_file)

        return self.target_files

    def SetCanvas(self, window_canvas):
        """
        キャンバス配置
        """
        self.canvas = window_canvas

    def DrawImage(self, command, set_pos=-1):
        """
        キャンバスに画像を読込む
        """
        try:
            fname = self.get_file(command, set_pos)
            if command == "Map":
                self.model.DrawImage(fname, self.canvas, "Map")
            else:
                self.model.DrawImage(fname, self.canvas, "None")
            return self.file_pos, self.model
        except:
            print("DrawImageSkip")

    def pdf_image(self, pdf_file, fmtt, dpi, PBAR):
        mpd = self.model.pdf_image(pdf_file, fmtt, dpi, PBAR)
        if mpd is True:
            return True
        else:
            return False

    def MenuFuncRun(self, command, whlist, set_pos=-1):
        """
        menuボタンクリック
        """
        try:
            fname = self.get_file(command, set_pos)
        except:
            fname = ""
        if fname == "":
            return "画像無"
        else:
            try:
                # 線形検出パラメータ設定########################################
                disth = 1.41421356
                canth1 = 50.0
                canth2 = 50.0
                casize = 3
                do = True
                # ############################################################
                if command == "Noise":
                    limg = self.model.TotalNoise(fname, 7)
                    fname = limg.filename
                    self.model.stock_url = limg.filename
                # elif command == "LineLotate":
                #     limg = self.model.ImageLotate(
                #         fname, disth, canth1, canth2, casize, do
                #     )
                #     fname = limg.filename
                #     self.model.stock_url = limg.filename
                elif command == "Resize":
                    limg = self.model.edit_img
                    fname = limg.filename
                    self.model.stock_url = limg.filename
                elif command == "LineDelete":
                    disth = whlist
                    limg = self.model.StraightLineErase(
                        fname, disth, canth1, canth2, casize, do
                    )
                    fname = limg.filename
                    self.model.stock_url = limg.filename
                # -----------------------------------------------------------
                self.model.edit_img = limg
                args = {}
                self.model.DrawImage(fname, self.canvas, command, args=args)
                return "完了"
            except:
                return "Err"

    # def ResizeRun(self, command, set_pos=-1):
    #     """
    #     resizeボタンクリック
    #     """
    #     fname = self.get_file(command, set_pos)

    def DrawRectangle(self, command, pos_y, pos_x):
        """
        キャンバス画像クリックで範囲指定完了後
        """
        if command == "clip_start":
            self.clip_sy, self.clip_sx = pos_y, pos_x
            self.clip_ey, self.clip_ex = pos_y + 1, pos_x + 1

        elif command == "clip_keep":
            self.clip_ey, self.clip_ex = pos_y, pos_x

        elif command == "clip_end":
            self.clip_ey, self.clip_ex = pos_y, pos_x
            self.clip_sy, self.clip_sx = self.model.GetValidPos(
                self.clip_sy, self.clip_sx
            )
            self.clip_ey, self.clip_ex = self.model.GetValidPos(
                self.clip_ey, self.clip_ex
            )

        self.model.DrawRectangle(
            self.canvas, self.clip_sy, self.clip_sx, self.clip_ey, self.clip_ex
        )

    def EditImage(self, command):
        """
        画像トリミング
        """
        args = {}
        if command == "clip_done" or command == "clip_Erace":  # トリミング確定ボタンが押されたら
            # キャンバスサイズと表示画像サイズの比率を算出---------------------------
            CWiPar = self.model.canvas_w / self.model.resize_w  # 幅
            CHePar = self.model.canvas_h / self.model.resize_h  # 高さ
            # --------------------------------------------------------------------
            # キャンバスサイズと元画像サイズの比率を算出---------------------------
            WiPar = self.model.original_width / self.model.canvas_w
            HePar = self.model.original_height / self.model.canvas_h
            # --------------------------------------------------------------------
            if CWiPar < 1:  # 幅が圧縮されていたら
                minus = ["width", CWiPar]
            elif CHePar < 1:  # 高さが圧縮されていたら
                minus = ["height", CHePar]
            else:  # 比率変更なしの場合(キャンバスと表示画像サイズが一致)
                minus = ["Nothing", 0]
            # --------------------------------------------------------------------
            if minus[0] == "width":  # 幅が圧縮されていたら
                # 幅圧縮率を高さにかける
                IMGSize = [
                    int(self.model.resize_w),
                    int(self.model.resize_h * CWiPar),
                ]
                SXPOS = 0  # スタート幅ポジション
                SYPOS = (self.model.canvas_h - IMGSize[1]) / 2  # スタート高さポジション
                sx = int(((self.clip_sx - SXPOS) / CHePar) * WiPar)
                sy = int(((self.clip_sy - SYPOS) / CWiPar) * HePar)
                ex = int(((self.clip_ex - SXPOS) / CHePar) * WiPar)
                ey = int(((self.clip_ey - SYPOS) / CWiPar) * HePar)
            elif minus[0] == "height":  # 高さが圧縮されていたら
                # 高さ圧縮率を幅にかける
                IMGSize = [
                    int(self.model.resize_w * CHePar),
                    int(self.model.resize_h),
                ]
                SXPOS = (self.model.canvas_w - IMGSize[0]) / 2  # スタート幅ポジション
                SYPOS = 0  # スタート高さポジション
                sx = int(((self.clip_sx - SXPOS) / CHePar) * WiPar)
                sy = int(((self.clip_sy - SYPOS) / CWiPar) * HePar)
                ex = int(((self.clip_ex - SXPOS) / CHePar) * WiPar)
                ey = int(((self.clip_ey - SYPOS) / CWiPar) * HePar)
            else:
                IMGSize = [
                    int(self.model.resize_w),
                    int(self.model.resize_h),
                ]
                SXPOS = (self.model.canvas_w - IMGSize[0]) / 2  # スタート幅ポジション
                SYPOS = (self.model.canvas_h - IMGSize[1]) / 2  # スタート高さポジション
                sx = int(((self.clip_sx - SXPOS) * CWiPar) * WiPar)
                sy = int(((self.clip_sy - SYPOS) * CHePar) * HePar)
                ex = int(((self.clip_ex - SXPOS) * CWiPar) * WiPar)
                ey = int(((self.clip_ey - SYPOS) * CHePar) * HePar)

            # 元画像と比較してポジション調整-------------------------------------------

            if sx < 0:
                sx = 0
            elif sx > self.model.original_width:
                sx = self.model.original_width
            if ex < 0:
                ex = 0
            elif ex > self.model.original_width:
                ex = self.model.original_width
            if sy < 0:
                sy = 0
            elif sy > self.model.original_height:
                sy = self.model.original_height
            if ey < 0:
                ey = 0
            elif ey > self.model.original_height:
                ey = self.model.original_height
            # --------------------------------------------------------------------
            # WiPar = self.model.original_width / self.model.resize_w
            # HePar = self.model.original_height / self.model.resize_h
            args["sx"], args["sy"] = sx, sy
            args["ex"], args["ey"] = ex, ey
            # args["sx"], args["sy"] = self.clip_sx, self.clip_sy
            # args["ex"], args["ey"] = self.clip_ex, self.clip_ey

        fname = self.get_file("current")
        self.model.DrawImage(fname, self.canvas, command, args=args)

    def SaveImage(self, fname):
        """
        画像ファイル名日付追加保存
        """

        self.model.SaveImage(fname)

    def OverSaveImage(self):
        """
        画像上書き保存
        """
        fname = self.get_file("current")
        self.model.OverSaveImage(fname)

    def UndoImage(self, command):
        """
        画像編集復元
        """
        fname = self.get_file("current")
        self.model.DrawImage(fname, self.canvas, command)

    def CreateDB(self, dbname):
        """
        dbを作成する
        """
        conn = sql.connect(dbname)
        conn.close()

    def CreateTable(self, dbname, tbname):
        """
        テーブルを作成する
        """
        conn = sql.connect(dbname)
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS " + tbname + "(変更前 STRING,変更後 STRING)")
        conn.commit()
        conn.close()

    def TableInsert(self, dbname, tbname, text):
        """
        テーブルにデータ追加
        """
        conn = sql.connect(dbname)
        cur = conn.cursor()

        # Insert文
        cur.execute("INSERT INTO " + tbname + "(変更前, 変更後) values(" + text + ")")
        # 同様に
        conn.commit()

        cur.close()
        conn.close()

    def CheckTable(self, dbname, tbname):
        """
        テーブルの中身を確認
        """
        conn = sql.connect(dbname)
        cur = conn.cursor()

        # terminalで実行したSQL文と同じようにexecute()に書く
        cur.execute("SELECT * FROM " + tbname)

        # 中身を全て取得するfetchall()を使って、printする。
        print(cur.fetchall())

        cur.close()
        conn.close()
