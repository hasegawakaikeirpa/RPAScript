import os

# import numpy as np
import ProgressBar as PB

# from datetime import datetime
# from PIL import Image, ImageTk, ImageOps, ImageDraw
# import cv2

# import math
from pathlib import Path
from pdf2image import convert_from_path
import tkinter as tk


def pdf_image(pdf_file, fmtt, dpi, PBAR):
    """
    概要: popplerでPDFを指定した画像形式に変換
    @param pdf_file : PDFURL(str)
    @param img_path : 画像フォルダURL(str)
    @param fmtt : 変換後の画像形式(str)
    @param dpi : 変換する際の解像度(int)
    @param PDFPage : 変換するPDFのページ番号(str)
    @return : bool
    @return : 変換後画像URLのリスト(list)
    """
    # try:
    Mydir = os.getcwd()
    pppath = Mydir + r"\poppler-22.01.0\Library\bin"
    # pdf_file、img_pathをPathにする
    pdf_path = Path(pdf_file)
    image_dir = os.path.dirname(pdf_file)
    os.environ["PATH"] += os.pathsep + str(pppath)
    FileKey = os.path.basename(pdf_file)
    FileKey = FileKey.replace(".pdf", "").replace(".PDF", "")
    # 線形検出パラメータ設定########################################
    # disth = 1.41421356
    # canth1 = 50.0
    # canth2 = 50.0
    # casize = 3
    # do = True
    # ############################################################
    PBAR._target.step(10)
    # PDFをImage に変換(pdf2imageの関数)
    pages = convert_from_path(pdf_path, dpi, poppler_path=pppath)
    PS = 40
    PS_x = 50 / len(pages)
    PBAR._target.step(PS)

    # 画像ファイルを１ページずつ保存
    for i, page in enumerate(pages):
        file_name = FileKey + "_" + str(i + 1) + "page." + fmtt
        image_path = image_dir + r"/" + file_name
        page.save(image_path, fmtt)
        # self.PDFChange(image_dir, image_path, disth, canth1, canth2, casize, do)
        PBAR._target.step(PS_x)
    PBAR._target.master.destroy()
    return True
    # except:
    #     PBAR._target.master.destroy()
    #     return False


if __name__ == "__main__":
    PBAR = PB.Open(tk.Toplevel())  # サブWindow作成
    pdf_image(r"D:\OCRTESTPDF\PDFTEST\Hirogin.pdf", "png", 300, PBAR)
    print("")
