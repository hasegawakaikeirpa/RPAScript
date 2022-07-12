import os
import numpy as np
from datetime import datetime
from PIL import Image, ImageTk, ImageOps


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
            name = name.replace("\\", "/")
            fpath = name.replace("/", r"\\") + ext

            self.edit_img.save(fpath)
            print("Saved: {}".format(fpath))
