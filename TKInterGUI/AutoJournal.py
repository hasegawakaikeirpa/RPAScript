import numpy as np

# from tkinter import messagebox

import os

import toml

# -----------------------------------------------------------------------------------------
if __name__ == "__main__":
    global imgurl, Roolrul, Banktoml, tomltitle
    imgurl = r"D:\OCRTESTPDF\PDFTEST\tuka_1page.csv"
    Roolrul = r"D:\PythonScript\RPAScript\TKInterGUI\Mototyou\18_仕訳日記帳.csv"
    tomltitle = "Tuka"
    # toml読込------------------------------------------------------------------------------
    with open(os.getcwd() + r"/TKInterGUI/BankSetting.toml", encoding="utf-8") as f:
        Banktoml = toml.load(f)
        print(Banktoml)
    # -----------------------------------------------------------
    MJS_data = np.genfromtxt(Roolrul, dtype=None, delimiter=",")
    print(MJS_data)
