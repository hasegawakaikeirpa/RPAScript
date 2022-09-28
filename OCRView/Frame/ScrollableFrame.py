import tkinter as tk
import tkinter.ttk as ttk


class ScrollableFrame(ttk.Frame):
    def __init__(self, container, bar_x=True, bar_y=True):
        super().__init__(container)
        self.canvas = tk.Canvas(
            self,
            bg="gray94",
        )
        self.scrollable_frame = tk.Frame(
            self.canvas,
            bg="gray94",
            relief=tk.GROOVE,
            bd=2,
        )
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")),
        )
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        if bar_y:
            self.scrollable_frame.bind("<MouseWheel>", self.mouse_y_scroll)
            self.scrollbar_y = ttk.Scrollbar(
                self.scrollable_frame, orient="vertical", command=self.canvas.yview
            )
            self.scrollbar_y.grid(row=0, column=3, sticky=tk.S + tk.N)
            self.canvas.configure(yscrollcommand=self.scrollbar_y.set)
        if bar_x:
            self.scrollable_frame.bind("<MouseWheel>", self.mouse_x_scroll)
            self.scrollbar_x = ttk.Scrollbar(
                self.scrollable_frame, orient="horizontal", command=self.canvas.xview
            )
            self.scrollbar_x.grid(sticky=tk.E + tk.W)
            self.canvas.configure(xscrollcommand=self.scrollbar_x.set)
        self.canvas.grid(row=0, column=1, sticky=tk.S + tk.N)

    def mouse_y_scroll(self, event):
        if event.delta > 0:
            self.canvas.yview_scroll(-1, "units")
        elif event.delta < 0:
            self.canvas.yview_scroll(1, "units")

    def mouse_x_scroll(self, event):
        if event.delta > 0:
            self.canvas.xview_scroll(-1, "units")
        elif event.delta < 0:
            self.canvas.xview_scroll(1, "units")
