import tkinter as tk

# クリックイベントを検出###########################################
# commandオプションで検出------------------------------------------
def btn_clicked():
    print("Button Clicked")


def btn_clickedCheck():
    # ウィンドウ作成
    root = tk.Tk()
    # ボタンの作成と配置
    button1 = tk.Button(root, text="Button", command=btn_clicked)
    button1.place(x=10, y=20, width=100, height=50)
    # メインループ
    root.mainloop()


# bind()メソッドで検出----------------------------------------------
def btn_clicked_e(e):
    print(e.widget["text"])


def btn_clickedCheck_e():
    # ウィンドウ作成
    root = tk.Tk()
    # ボタンの作成と配置
    button1 = tk.Button(
        root,
        text="Button",
    )
    button1.place(x=10, y=20, width=100, height=50)
    button1.bind("<Button-1>", btn_clicked_e)
    # メインループ
    root.mainloop()


##################################################################
# キー入力を検出###################################################
def key_handler(e):
    print(e.keycode)


def key_handlerCheck_e():
    # ウィンドウ作成
    root = tk.Tk()
    # ウィンドウサイズ
    root.geometry("300x200")
    # テキストボックスの作成と配置
    txt = tk.Entry(root)
    txt.place(x=20, y=20, width=150, height=30)
    txt.bind("<KeyPress>", key_handler)
    # メインループ
    root.mainloop()


##################################################################
# テキストボックス以外のキー入力を検出##############################
def NotTxtkey_handler(e):
    print(e.keycode)


def NotTxtkey_handlerCheck_e():
    # ウィンドウ作成
    root = tk.Tk()
    # ウィンドウサイズ
    root.geometry("300x200")
    # メインウィンドウのbind()メソッドで検出-----------------------------
    root.bind("<KeyPress>", key_handler)
    root.bind("<Button-1>", key_handler)

    # メインループ
    root.mainloop()


# bind_all()メソッドで検出------------------------------------------
# txt.bind_all("<KeyPress>", key_handler)

##################################################################
# マウスの移動を検出###############################################
def mouse_move(e, lbl):
    lbl["text"] = str(e.x) + ", " + str(e.y)


def mouse_moveCheck_e():
    # ウィンドウ作成
    root = tk.Tk()
    # ウィンドウサイズ
    root.geometry("300x200")
    # ラベルの作成と配置
    lbl = tk.Label(root, text="", borderwidth=2, relief="ridge")
    lbl.place(x=20, y=20, width=260, height=30)
    root.bind("<Motion>", mouse_move)
    # メインループ
    root.mainloop()


##################################################################
mouse_moveCheck_e()
