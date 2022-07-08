import os
import numpy as np
import cv2
from datetime import datetime
from PIL import Image, ImageTk, ImageOps
import math


class ModelImage:
    def __init__(self, ImageType="Photo"):

        self.ImageType = ImageType
        self.edit_img = None
        self.original_img = None
        self.canvas_w = 0
        self.canvas_h = 0

    def set_image_layout(self, canvas, image):
        """
        キャンバスサイズにあわせた画像サイズ変換関数
        """
        self.canvas_w = canvas.winfo_width()
        self.canvas_h = canvas.winfo_height()

        h, w = image.height, image.width

        if h > w:
            self.resize_h = self.canvas_h
            self.resize_w = int(w * (self.canvas_h / h))
            self.pad_x = (self.canvas_w - self.resize_w) // 2
            self.pad_y = 0

        else:
            self.resize_w = self.canvas_w
            self.resize_h = int(h * (self.canvas_w / w))
            self.pad_y = (self.canvas_h - self.resize_h) // 2
            self.pad_x = 0

        print(h, w, self.resize_h, self.resize_w, self.pad_y, self.pad_x)

    def get_correct_values(self, rate, sy, sx, ey, ex):

        mod_sx = int(np.min((sx, ex)) * rate)
        mod_sy = int(np.min((sy, ey)) * rate)
        mod_ex = int(np.max((sx, ex)) * rate)
        mod_ey = int(np.max((sy, ey)) * rate)
        ch, cw = mod_ey - mod_sy, mod_ex - mod_sx

        return mod_sy, mod_sx, ch, cw

    def get_original_coords(self, h, w, args):

        print(args, h, w)
        sy, sx, ey, ex = args["sy"], args["sx"], args["ey"], args["ex"]

        if h > w:
            rate = h / self.canvas_h
            x_spc = self.pad_x * rate
            sy, sx, ch, cw = self.get_correct_values(rate, sy, sx, ey, ex)
            sx = sx - x_spc
            sx = int(np.max((sx, 0)))
            sx = int(np.min((sx, w)))

        else:
            rate = w / self.canvas_w
            y_spc = self.pad_y * rate
            sy, sx, ch, cw = self.get_correct_values(rate, sy, sx, ey, ex)
            # sy = sy - y_spc
            # sy = int(np.max((sy, 0)))
            # sy = int(np.min((sy, h)))

        return sy, sx, ch, cw

    def edit_image_command(self, orginal_image, edit_image, command, args={}):

        if edit_image != None:
            img = edit_image
        else:
            img = orginal_image.copy()

        np_img = np.array(img)

        if "flip-1" in command:  # U/L
            np_img = np.flip(np_img, axis=0)

        elif "flip-2" in command:  # L/R
            np_img = np.flip(np_img, axis=1)

        elif "rotate-" in command:  # 1:rot90 2:rot180 3:rot270
            cmd = int(command.replace("rotate-", ""))
            np_img = np.rot90(np_img, cmd)

        elif "rotateFree-" in command:
            cmd = int(command.replace("rotateFree-", ""))
            return img.rotate(cmd, expand=True)

        elif "clip_done" in command:
            h, w = np_img[:, :, 0].shape
            sy, sx, ch, cw = self.get_original_coords(h, w, args)
            np_img = np_img[sy : sy + ch, sx : sx + cw, :]

        return Image.fromarray(np_img)

    # Public

    def GetValidPos(self, pos_y, pos_x):
        """
        トリミング範囲計算
        """
        if self.resize_h > self.resize_w:
            valid_pos_y = pos_y
            valid_pos_x = np.max((pos_x, self.pad_x))
            valid_pos_x = np.min((valid_pos_x, self.canvas_w - self.pad_x))

        else:
            valid_pos_x = pos_x
            valid_pos_y = np.max((pos_y, self.pad_y))
            valid_pos_y = np.min((valid_pos_y, self.canvas_h - self.pad_y))

        return valid_pos_y, valid_pos_x

    def DrawImage(self, fpath, canvas, command, args={}):

        if canvas.gettags("Photo"):
            canvas.delete("Photo")

        if self.edit_img != None and command != "None":
            img = self.edit_img

        else:
            img = Image.open(fpath)
            self.original_img = img
            self.edit_img = None
            self.set_image_layout(canvas, self.original_img)
            self.original_width = img.size[0]
            self.original_height = img.size[1]
        if command != "None" and not command == "Map":
            if not len(args) == 0:
                args["sx"] = int(args["sx"] * (self.resize_w / self.original_width))
                args["sy"] = int(args["sy"] * (self.resize_h / self.original_height))
                args["ex"] = int(args["ex"] * (self.resize_w / self.original_width))
                args["ey"] = int(args["ey"] * (self.resize_h / self.original_height))
            img = self.edit_image_command(
                self.original_img, self.edit_img, command, args=args
            )
            self.edit_img = img
            self.set_image_layout(canvas, self.edit_img)
        elif command == "Map":
            if not len(args) == 0:
                args["sx"] = int(args["sx"] * (self.resize_w / self.original_width))
                args["sy"] = int(args["sy"] * (self.resize_h / self.original_height))
                args["ex"] = int(args["ex"] * (self.resize_w / self.original_width))
                args["ey"] = int(args["ey"] * (self.resize_h / self.original_height))
            img = self.edit_image_command(
                self.original_img, self.edit_img, command, args=args
            )
            self.edit_img = img
            self.set_image_layout(canvas, self.edit_img)
        pil_img = ImageOps.pad(img, (self.canvas_w, self.canvas_h))
        self.tk_img = ImageTk.PhotoImage(image=pil_img)
        canvas.create_image(
            self.canvas_w / 2, self.canvas_h / 2, image=self.tk_img, tag="Photo"
        )

    def DrawRectangle(self, canvas, clip_sy, clip_sx, clip_ey, clip_ex):

        if canvas.gettags("clip_rect"):
            canvas.delete("clip_rect")

        canvas.create_rectangle(
            clip_sx, clip_sy, clip_ex, clip_ey, outline="red", tag="clip_rect"
        )

    def SaveImage(self, fname):

        if self.edit_img != None:
            name, ext = os.path.splitext(fname)
            dt = datetime.now()
            fpath = name + "_" + dt.strftime("%H%M%S") + ".png"

            self.edit_img.save(fpath)
            print("Saved: {}".format(fpath))

    def OverSaveImage(self, fname):

        if self.edit_img != None:
            name, ext = os.path.splitext(fname)
            fpath = name + ".png"

            self.edit_img.save(fpath)
            print("Saved: {}".format(fpath))

    def ImageLotate(URL, imgurl, disth, canth1, canth2, casize, do):
        """
        概要: 画像から直線を検出し、画像の傾きを調べ回転して上書き保存
        @param URL: 画像フォルダ(str)
        @param imgurl: 画像URL(str)
        @param disth: マージする線分の距離(float)
        @param canth1: Canny Edge Detectorの引数1(float)
        @param canth2: Canny Edge Detectorの引数2(float)
        @param casize: Canny Edge Detectorに使うSobelのサイズ(0ならCannyは適用しない)(int)
        @param dom: Trueなら線分をマージして出力する(boolean)
        @return 傾き値リスト(np配列)
        """
        try:
            img = cv2.imread(imgurl)
            # 回転-----------------------------------------------------------------------
            # StraightLineDetectionで最後の一つになるまで絞りだしたピクセル連続線から
            # 角度をmathアークタンジェントで計算し、degreesでラジアン→℃変換後画像を回転
            Kakuavg = StraightLineDetection(
                URL, imgurl, disth, canth1, canth2, casize, do
            )
            if Kakuavg[0] is True:
                x1 = Kakuavg[1][:, 1]
                y1 = Kakuavg[1][:, 0]
                x2 = Kakuavg[1][:, 3]
                y2 = Kakuavg[1][:, 2]
                # numpyとmathではy,x軸が反対なので入替--------------------------------------
                x = np.average(y1) - np.average(y2)
                y = np.average(x1) - np.average(x2)
                # ------------------------------------------------------------------------
                tan = math.degrees(math.atan2(y, x))
                img = Image.open(imgurl)
                img = img.rotate(tan)
            # ---------------------------------------------------------------------------
            else:
                return False
            return img
        except:
            return False

    def TotalNoise(self, imgurl, ksize):

        Inv_img = ColorInverter(imgurl)  # 白黒反転(PIL)
        Inv_img.save(imgurl)  # 白黒反転保存(PIL)
        img = cv2.imread(imgurl)  # 白黒反転画像(cv2)
        CleanUp_img = NoiseRemoval(img, ksize)  # ノイズ除去(cv2)
        cv2.imwrite(imgurl, CleanUp_img)  # ノイズ除去保存(cv2)
        Inv_img = ColorInverter(imgurl)  # 白黒反転(PIL)
        Inv_img.save(imgurl)  # 白黒反転保存(PIL)
        Inv_img = Image.open(imgurl)
        return Inv_img


def StraightLineDetection(URL, imgurl, disth, canth1, canth2, casize, do):
    """
    概要: 画像から直線を検出し、画像の傾きを調べる
    @param URL: 画像フォルダ(str)
    @param imgurl: 画像URL(str)
    @param disth: マージする線分の距離(float)
    @param canth1: Canny Edge Detectorの引数1(float)
    @param canth2: Canny Edge Detectorの引数2(float)
    @param casize: Canny Edge Detectorに使うSobelのサイズ(0ならCannyは適用しない)(int)
    @param dom: Trueなら線分をマージして出力する(boolean)
    @return 傾き値リスト(np配列)
    """
    try:
        img = cv2.imread(imgurl)
        size = img.shape  # 画像のサイズ x,y
        Pix = int(size[0] / 100)  # 検出ピクセル数
        LCheck = False  # ライン検出フラグ
        while LCheck is False:  # ライン検出フラグTrueまでループ
            FLStock = []
            if Pix <= 0:
                Pix = 1
            # FLDインスタンス生成
            FLDs = FastLineDetector(
                imgurl,
                Pix,
                disth,
                canth1,
                canth2,
                casize,
                do,
            )  # boolean,yx値
            if FLDs[0] is True:  # 連続ピクセルを検知したら
                FLDItem = len(FLDs[1])  # 配列要素数
                if FLDItem <= 3:  # 配列要素数0なら
                    print(str(FLDItem) + "要素なので終了")
                    FLStock = FLDs[1]
                    LCheck = True
                else:
                    print(str(FLDItem) + "要素取得")
                    FLStock = FLDs[1]
            PlPix = size[0] / 1000
            if PlPix < 1:
                Pix += 1
            else:
                Pix += int(PlPix)
        XLFlag = False
        for x in range(len(FLStock)):
            UpY = FLStock[x][0][0]
            UpX = FLStock[x][0][1]
            LoY = FLStock[x][0][2]
            LoX = FLStock[x][0][3]
            if XLFlag is False:
                XList = np.array([[UpY, UpX, LoY, LoX]])
                XLFlag = True
            else:
                XList = np.append(XList, [[UpY, UpX, LoY, LoX]], axis=0)
        return True, XList
    except:
        return False, ""


def FastLineDetector(fileImage, lenth, disth, canth1, canth2, casize, dom):
    """
    概要: 画像の線形を検出
    @param fileImage: 画像URL(str)
    @param lenth: 検出する最小の線分のピクセル数(int)
    @param disth: マージする線分の距離(float)
    @param canth1: Canny Edge Detectorの引数1(float)
    @param canth2: Canny Edge Detectorの引数2(float)
    @param casize: Canny Edge Detectorに使うSobelのサイズ(0ならCannyは適用しない)(int)
    @param dom: Trueなら線分をマージして出力する(boolean)
    @return boolean,検出ラインピクセル値配列,ライン描画後画像のcvインスタンス
    """
    colorimg = cv2.imread(fileImage, cv2.IMREAD_COLOR)  # 元画像
    if colorimg is None:
        return False, "", ""
    image = cv2.cvtColor(colorimg.copy(), cv2.COLOR_BGR2GRAY)

    # FLDパラメーター設定--------------------------------------------
    length_threshold = lenth
    distance_threshold = disth
    canny_th1 = canth1
    canny_th2 = canth2
    canny_aperture_size = casize
    do_merge = dom
    # -------------------------------------------------------------
    # FLDインスタンス化
    fld = cv2.ximgproc.createFastLineDetector(
        length_threshold,
        distance_threshold,
        canny_th1,
        canny_th2,
        canny_aperture_size,
        do_merge,
    )

    # ライン取得
    lines = fld.detect(image)
    # # ライン描画後画像のインスタンス作成
    out = fld.drawSegments(colorimg, lines)
    return True, lines, out


def ColorInverter(imgurl):
    """
    概要: 画像白黒反転
    @param img: 画像URL(str)
    @return 白黒反転した画像(cv2)
    """
    img = Image.open(imgurl).convert("RGB")
    Inv_img = ImageOps.invert(img)
    return Inv_img


def NoiseRemoval(img, ksize):
    """
    概要: 画像ノイズ除去（収縮⇒膨張）
    @param img: cv2で開いた画像
    @return 画像ノイズ除去した画像(cv2)
    """
    kernel = np.ones((2, 2))
    Open_img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    # 中央値フィルタ
    Open_img = cv2.medianBlur(Open_img, ksize)
    return Open_img
