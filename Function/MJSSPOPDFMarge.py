import PyPDF2
import os
import pandas as pd
import csv
import mojimoji
import unicodedata


def dirCheck(Url):
    List = []
    for fd_path, sb_folder, sb_file in os.walk(Url):
        for fil in sb_file:
            List.append([fd_path + "\\" + fil, fil.replace(".pdf", "")])
    print(List)
    Ldf = pd.DataFrame(List)
    return Ldf


def Remoji(text):
    if unicodedata.east_asian_width(text) == "F":  # 全角。全角英数など。
        return mojimoji.zen_to_han(text)
    elif unicodedata.east_asian_width(text) == "H":  # 半角。半角カナなど。
        return text
    elif unicodedata.east_asian_width(text) == "W":  # 全角。漢字やかななど。
        return mojimoji.zen_to_han(text)
    elif unicodedata.east_asian_width(text) == "Na":  # 半角。半角英数など。
        return text
    elif unicodedata.east_asian_width(text) == "A":  # 曖昧。ギリシア文字など。
        return text
    elif unicodedata.east_asian_width(text) == "N":  # 中立。アラビア文字など。
        return text


def dirCreate(Url, No, YearT):
    for fd_path, sb_folder, sb_file in os.walk(Url):
        for fol in sb_folder:
            Target = fd_path + r"\\" + fol
            if (
                unicodedata.east_asian_width(fol[0]) == "A"
                or unicodedata.east_asian_width(fol[0]) == "N"
            ):
                f = 0
                Newfol = ""
                for folitem in fol:
                    if not f == 0:
                        Newfol += Remoji(folitem)
                    f += 1
                fol = Newfol
            if "～" in fol:
                FolSP = fol.split("～")
            elif "~" in fol:
                FolSP = fol.split("~")
            if int(FolSP[1]) >= No:
                Nofol = False
                for fd_path, sb_folder, sb_file in os.walk(Target):
                    for fol in sb_folder:
                        try:
                            if int(fol) == No:
                                print("フォルダ有")
                                TTarget = Target + r"\\" + fol
                                for fd_path, sb_folder, sb_file in os.walk(TTarget):
                                    for fol in sb_folder:
                                        if YearT == fol:
                                            Nofol = True
                                            return TTarget + r"\\" + fol
                        except:
                            print("Err")
                if Nofol is False:
                    os.mkdir(Target + str(No))
                    TTarget = Target + r"\\" + str(fol)
                    os.mkdir(TTarget + r"\\" + str(YearT))
                    return TTarget + r"\\" + str(YearT)


def dirMarge(Line, PDFUrl, SerchURL, PDFDir, Title, No, YearT):
    # １つのPDFファイルにまとめる
    PR = len(PDFDir)
    merger = PyPDF2.PdfFileMerger()
    for LineR in Line:
        for PRow in range(PR):
            PDFRow = PDFDir.iloc[PRow]
            PN = str(PDFRow[1])
            if str(LineR[0]) == PN:
                MU = str(PDFRow[0])
                print(MU)
                merger.append(MU)
    TURL = dirCreate(SerchURL, No, YearT)
    # 保存ファイル名（先頭と末尾のファイル名で作成）
    merged_file = TURL + r"\\" + Title + ".pdf"
    Matu = "2"
    if os.path.isfile(merged_file) is True:
        merged_file = merged_file.replace(".pdf", "") + Matu + ".pdf"
        while os.path.isfile(merged_file) is True:
            Matu = str(int(Matu) + 1)
            merged_file = merged_file.replace(".pdf", "") + Matu + ".pdf"
    # 保存
    merger.write(merged_file)
    merger.close()
    for PRow in range(PR):
        PDFRow = PDFDir.iloc[PRow]
        MU = str(PDFRow[0])
        os.remove(MU)
    return merged_file


def PDFMarge(Url, PDFUrl, SerchURL, Title, No, YearT):
    with open(Url, "r", encoding="utf8") as f:
        LM = csv.reader(f)
        Line = [row for row in LM]
    print(Line)
    PDFDir = dirCheck(PDFUrl)
    print(PDFDir)
    MF = dirMarge(Line, PDFUrl, SerchURL, PDFDir, Title, No, YearT)
    return MF
