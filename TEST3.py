# -*- coding: utf-8 -*-

import tkinter


class CanvasOval:
    canvas = None

    def __init__(self, x0, y0, x1, y1, **key):
        self.id = self.canvas.create_oval(x0, y0, x1, y1, **key)
        self.canvas.tag_bind(self.id, "<1>", self.drag_start)
        self.canvas.tag_bind(self.id, "<Button1-Motion>", self.dragging)

    def drag_start(self, event):
        self.x = event.x
        self.y = event.y

    def dragging(self, event):
        self.canvas.move(self.id, event.x - self.x, event.y - self.y)
        self.x = event.x
        self.y = event.y


class Frame(tkinter.Frame):
    def __init__(self, master=None):
        tkinter.Frame.__init__(self, master)
        self.cvs = tkinter.Canvas(self, width="200", height="200", bg="white")
        self.cvs.grid(row=0, column=0)

        CanvasOval.canvas = self.cvs
        CanvasOval(40, 40, 50, 50, fill="red", width=0)
        CanvasOval(130, 130, 170, 170, fill="red", width=0)


if __name__ == "__main__":
    f = Frame()
    f.pack()
    f.mainloop()
