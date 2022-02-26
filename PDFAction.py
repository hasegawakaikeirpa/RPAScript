import os
import PyPDF2
import time
from time import time

def SerchdirFolders(URL):
    List = []
    for fd_path, sb_folder, sb_file in os.walk(URL):
        for fol in sb_folder:
            # print(fd_path + '\\' + fol)
            List.append([fd_path,fol])
    return List
#----------------------------------------------------------------------------------------
def SerchdirFiles(URL):
    List = []
    for fd_path, sb_folder, sb_file in os.walk(URL):
        for fil in sb_file:
            # print(fd_path + '\\' + fil)
            List.append([fd_path,fil])
    return List
#----------------------------------------------------------------------------------------
def DualMerge(Full_Sp,Full_CSp,NewName):
    NewName = NewName.replace(".pdf","")
    merger = PyPDF2.PdfFileMerger()
    merger.append(Full_Sp)
    merger.append(Full_CSp)
    merger.write(NewName + ".pdf")
    merger.close()
    os.remove(Full_Sp)
    os.remove(Full_CSp)
#----------------------------------------------------------------------------------------
def ReadFol(dir_Files):
    for dir_FilesItem in dir_Files:
        Sp_File = dir_FilesItem[1].split("_")
        Sp_dir = dir_FilesItem[0]
        Full_Sp = Sp_dir + '\\' + dir_FilesItem[1]
        for Cdir_FilesItem  in dir_Files:
            CSp_File = Cdir_FilesItem[1].split("_")
            CSp_dir = Cdir_FilesItem[0]
            Full_CSp = CSp_dir + '\\' + Cdir_FilesItem[1]
            if Sp_File[0] == CSp_File[0] and Sp_dir == CSp_dir and Full_Sp != Full_CSp:
                NewName = Sp_File[0] + "_" + Sp_File[1]
                NewFullName = Sp_dir + '\\' + NewName
                if NewFullName == Full_Sp:
                    C_Sp = Sp_dir + '\\' + Sp_File[0] + "_" + 'M_' + Sp_File[1]
                    os.rename(Full_Sp,C_Sp)
                    Full_Sp = C_Sp
                elif NewFullName == Full_CSp:
                    C_Sp = Sp_dir + '\\' + Sp_File[0] + "_" + 'C_' + Sp_File[1]
                    os.rename(Full_CSp,C_Sp)
                    Full_CSp = C_Sp
                try:
                    return Full_Sp,Full_CSp,NewFullName
                except:
                    return False,False,False
                #print(Full_Sp + '==' + Full_CSp)
#----------------------------------------------------------------------------------------
def MergeFils(URL):
    dir_List = SerchdirFolders(URL)
    for dir_ListItem  in dir_List:
        Serchd = dir_ListItem[0] + '\\' + dir_ListItem[1]
        dir_Files = SerchdirFiles(Serchd)
        RF = ReadFol(dir_Files)
        try:
            DualMerge(RF[0],RF[1],RF[2])
        except:
            print('失敗')         
#----------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------
def ListMerge(dir_Files,NewName):
    NewName = NewName.replace(".pdf","")
    merger = PyPDF2.PdfFileMerger()
    for dir in dir_Files:
        FN = dir[0] + '\\' + dir[1]
        merger.append(FN)
    merger.write(dir[0] + '\\' + NewName + ".pdf")
    merger.close()
    for dir in dir_Files:
        FN = dir[0] + '\\' + dir[1]
        os.remove(FN)
#----------------------------------------------------------------------------------------
def ReFiles(dir,TURL):
    FN = str(dir[0]) + '\\' + str(dir[1])
    os.rename(FN,TURL)
#----------------------------------------------------------------------------------------
def SerchNonPDF(URL):
    dir_List = SerchdirFolders(URL)
    List = []
    for dir_ListItem  in dir_List:
        Serchd = dir_ListItem[0] + '\\' + dir_ListItem[1]
        dir_Files = SerchdirFiles(Serchd)
        for dir_FilesItem  in dir_Files:
            if  not ".pdf" in dir_FilesItem[1]:
                #print(dir_FilesItem)
                KeyURLL = dir_FilesItem[0] + '\\' + dir_FilesItem[1]
                TURL = KeyURLL + ".pdf"
                os.rename(KeyURLL,TURL)
#----------------------------------------------------------------------------------------
def MergeFilsT(URL):
    dir_List = SerchdirFolders(URL)
    for dir_ListItem  in dir_List:
        Serchd = dir_ListItem[0] + '\\' + dir_ListItem[1]
        dir_Files = SerchdirFiles(Serchd)
        if len(dir_Files) == 1:
            NewName = dir_Files[0]
            KeyURL = NewName[0]
            NewName = NewName[1].split("_")
            NewName = NewName[0] + "_" + NewName[1]
            KeyURLL = KeyURL + '\\' + NewName
            ReFiles(dir_Files[0],KeyURLL)
        else:
            NewName = dir_Files[0]
            KeyURL = NewName[0]
            NewName = NewName[1].split("_")
            OfName = NewName[0] + "_M-" + NewName[1]
            NewName = NewName[0] + "_" + NewName[1]
            KeyURLL = KeyURL + '\\' + NewName.replace("M-","")
            if os.path.isfile(KeyURLL) == True:
                os.rename(KeyURLL,KeyURL + '\\' + OfName)
                Sdir_List = SerchdirFolders(Serchd)
                for Sdir_ListItem  in Sdir_List:
                    SSerchd = Sdir_ListItem[0] + '\\' + Sdir_ListItem[1]
                    Sdir_Files = SerchdirFiles(SSerchd)
                    dir_Files = Sdir_Files
                    try:
                        ListMerge(dir_Files,NewName.replace("M-",""))
                    except:
                        print('失敗')
            else:   
                try:
                    ListMerge(dir_Files,NewName.replace("M-",""))
                except:
                    print('失敗')
    SerchNonPDF(URL)

URL = "\\\\Sv05121a\\e\\電子ファイル\\メッセージボックス\\2022-2\\送信分受信通知"
# URL = "//Sv05121a/e/電子ファイル/メッセージボックス/2022-2/eLTAX"
# URL = "\\\\\\Sv05121a\\e\\電子ファイル\\メッセージボックス\\2022-2\\eLTAX"

#MergeFilsT(URL)
SerchNonPDF(URL)