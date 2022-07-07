import os
import MJS_SystemPrintOut as MSP
import MJS_SystemNextCreate as MSN

if __name__ == "__main__":
    try:
        # RPA用画像フォルダの作成---------------------------------------------------------
        FolURL = os.getcwd().replace("\\", "/")  # 先
        TFolURL = FolURL + r"\RPAPhoto\MJS_SystemNextCreate"  # 先
        CFolURL = FolURL + r"\RPAPhoto\MJS_SystemPrintOut"  # 先
        SerchURL = r"\\nas-sv\B_監査etc\B2_電子ﾌｧｲﾙ\03_法人決算"  # 先
        XLSDir = r"\\nas-sv\A_共通\A8_ｼｽﾃﾑ資料\RPA\RPA_ミロクシステム次年更新"
        LURL = r"\\nas-sv\A_共通\A8_ｼｽﾃﾑ資料\RPA\RPA_ミロクシステム次年更新\MJSLog\MJSSysUpLog.txt"  # 処理状況CSVのURL
        # --------------------------------------------------------------------------------
        MSPM = MSP.Main(FolURL, TFolURL, CFolURL, SerchURL, XLSDir, LURL)
        if MSPM is True:
            MSNM = MSN.Main(FolURL, TFolURL, XLSDir, LURL)
            if MSNM is True:
                print("完了")
    except:
        print("Err")
