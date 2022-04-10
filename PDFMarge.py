import PyPDF2
import os
import pandas as pd


def dirCheck(Url):
    List = []
    for fd_path, sb_folder, sb_file in os.walk(Url):
        for fil in sb_file:
            List.append(fd_path + "\\" + fil)
    print(List)
    Ldf = pd.DataFrame(List)
    Ldf.to_csv(r"\\\\Sv05121a\\e\\電子ファイル\\メッセージボックス\\2022-3\\送信分受信通知\\3-15受信不可リスト.csv")


def dirMarge(Url):
    # フォルダ内のPDFファイル一覧
    pdf_files = []
    for filename in os.listdir(Url):
        if filename.endswith(".pdf"):
            pdf_files.append(filename)
    print(pdf_files)
    print(os.listdir(Url))
    # １つのPDFファイルにまとめる
    pdf_writer = PyPDF2.PdfFileWriter()
    for pdf_file in pdf_files:
        pdf_reader = PyPDF2.PdfFileReader(str(pdf_file))
        for i in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(i))

    # 保存ファイル名（先頭と末尾のファイル名で作成）
    merged_file = pdf_files[0].stem + "-" + pdf_files[-1].stem + ".pdf"

    # 保存
    with open(merged_file, "wb") as f:
        pdf_writer.write(f)


Url = "//Sv05121a/e/電子ファイル/メッセージボックス/2022-3/送信分受信通知"
dirCheck(Url)
