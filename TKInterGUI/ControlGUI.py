import os
from ModelImage import ModelImage


class ControlGUI:
    def __init__(self, default_path):

        # Model Class生成
        self.model = ModelImage()

        self.dir_path = default_path
        self.ext_keys = [".png", ".jpg", ".jpeg", ".JPG", ".PNG"]
        self.target_files = []
        self.file_pos = 0

        self.clip_sx = 0
        self.clip_sy = 0
        self.clip_ex = 0
        self.clip_ey = 0
        self.canvas = None

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
        fname = self.get_file(command, set_pos)
        self.model.DrawImage(fname, self.canvas, "None")
        return self.file_pos

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
        if command == "clip_done":
            args["sx"], args["sy"] = self.clip_sx, self.clip_sy
            args["ex"], args["ey"] = self.clip_ex, self.clip_ey

        fname = self.get_file("current")
        self.model.DrawImage(fname, self.canvas, command, args=args)

    def SaveImage(self):
        """
        画像上書き保存
        """
        fname = self.get_file("current")
        self.model.SaveImage(fname)

    def UndoImage(self, command):
        """
        画像編集復元
        """
        fname = self.get_file("current")
        self.model.DrawImage(fname, self.canvas, command)
