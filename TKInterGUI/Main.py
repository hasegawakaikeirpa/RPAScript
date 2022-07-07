import tkinter as tk
import cv2
from PIL import Image, ImageTk


class Application(tk.Frame):
    def __init__(self, master=None):
        # Windowの初期設定を行う。
        super().__init__(master)

        # Windowの画面サイズを設定する。
        # geometryについて : https://kuroro.blog/python/rozH3S2CYE0a0nB3s2QL/
        self.master.geometry("1280x640")

        # Windowを親要素として、frame Widget(Frame)を作成する。
        # Frameについて : https://kuroro.blog/python/P20XOidA5nh583fYRvxf/
        frame = tk.Frame(self.master)
        # Windowを親要素として、frame Widget(Frame)をどのように配置するのか？
        frame.grid()

        # frame Widget(Frame)を親要素として、label Widgetを作成する。
        # text : テキスト情報
        # width : 幅の設定
        # height : 高さの設定
        # bg : 背景色の設定
        # 色について　: https://kuroro.blog/python/YcZ6Yh4PswqUzaQXwnG2/
        # Labelについて : https://kuroro.blog/python/Pj4Z7JBNRvcHZvtFqiKD/
        # label1 = tk.Label(frame, text="label1", width=10, height=10, bg="red")
        # ##############################################################################
        imgurl = r"D:\PythonScript\RPAScript\RPAPhoto\PDFeTaxReadForList\OCR0.png"
        CW, CH = 1000, 500
        # 画像を指定
        img = Image.open(imgurl)
        w = img.width  # 横幅を取得
        h = img.height  # 縦幅を取得
        img = img.resize((int(w * (CW / h)), int(h * (CH / h))))
        img = ImageTk.PhotoImage(img)
        # canvasサイズも画面サイズと同じにして描画
        canvas = tk.Canvas(frame, width=CW, height=CH)
        canvas.create_line(60, 0, 60, 1000, tags="object1")
        canvas.tag_bind("object1", "<ButtonPress-1>", click1)
        canvas.tag_bind("object1", "<B1-Motion>", drag1)
        canvas.place(x=0, y=0)
        # -------------------------------------
        # キャンバスに画像を表示する
        canvas.create_image(250 - (w * (500 / h) / 2), 0, image=img, anchor=tk.NW)
        # ##############################################################################
        # # frame Widget(Frame)を親要素として、label Widgetをどのように配置するのか？
        # label1.grid()

        canvas.grid()


# 円、矩形、直線を描画＆ドラッグできるようにする【tkinter】
# https://irohaplat.com/python-tkinter-line-rectangle-oval-drag-and-drop-sample/
def click1(event):
    # https://office54.net/python/tkinter/tkinter-bind-event#section2
    global x1
    global y1
    global id1
    x2 = event.x
    y2 = event.y
    id1 = event.widget.find_closest(x2, y2)
    x1 = x2
    y1 = y2


def drag1(event):
    # https://office54.net/python/tkinter/tkinter-bind-event#section2
    global x1
    global y1
    global id1
    x2 = event.x
    y2 = event.y
    id1 = event.widget.find_closest(x2, y2)
    del_x1 = x2 - x1
    del_y1 = y2 - y1
    x0, y0, x1, y1 = event.widget.coords(id1)
    event.widget.coords(id1, x0 + del_x1, y0 + del_y1, x1 + del_x1, y1 + del_y1)
    x1 = x2
    y1 = y2


x1 = 0
y1 = 0
id1 = -1


if __name__ == "__main__":
    # Windowについて : https://kuroro.blog/python/116yLvTkzH2AUJj8FHLx/
    root = tk.Tk()  # Window生成
    app = Application(master=root)
    frame = tk.Frame(root, height=1000, width=1000)  # frame生成
    # --- 基本的な表示準備 ----------------

    app.mainloop()
