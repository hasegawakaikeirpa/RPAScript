import tkinter

# イベントハンドラ
def event_handler(event):
    print(event.type)


app = tkinter.Tk()
app.title("イベント")

# 利用可能なイベントを全てbind
for event_type in tkinter.EventType.__members__.keys():
    if event_type == "Expose":
        event_seq = "<" + event_type + ">"
        try:
            app.bind_all(event_seq, event_handler)
            print(event_type)
        except tkinter.TclError:
            print("bind error:", event_type)
            pass

# メインループ
app.mainloop()
