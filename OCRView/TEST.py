import tkinter as tk
import os

if __name__ == "__main__":
    root = tk.Tk()
    try:
        iconfile = os.getcwd() + r"\OCRView\OCR450-540.png"
    except:
        iconfile = os.getcwd() + r"\OCR450-540.png"
    root.iconphoto(False, tk.PhotoImage(file=iconfile))

    root.mainloop()
