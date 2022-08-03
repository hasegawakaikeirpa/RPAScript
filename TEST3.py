import os
from datetime import datetime as dt


def FolCre(C_SCode, C_Name, C_Nendo, C_Zeimoku, C_Syurui):
    Fol = str(dt.today().year) + "-" + str(dt.today().month)
    pt = r"\\nas-sv\B_監査etc\B2_電子ﾌｧｲﾙ\ﾒｯｾｰｼﾞﾎﾞｯｸｽ\\" + Fol
    try:
        # ---------------------------------------------------------
        if os.path.exists(pt) is False:
            os.mkdir(pt)
            pt = pt + r"\\送信分受信通知"
            if os.path.exists(pt) is False:  # 1
                os.mkdir(pt)
                C_Fol = pt + r"\\" + str(C_SCode)
                if os.path.exists(C_Fol) is False:  # 2
                    os.mkdir(C_Fol)
                    C_F = C_Fol + r"\\" + "ミロク送信分"
                    if os.path.exists(C_F) is False:  # 3
                        os.mkdir(C_F)
                        return True, C_F
                    else:
                        return False, ""
                else:
                    C_F = C_Fol + r"\\" + "ミロク送信分"
                    if os.path.exists(C_F) is False:  # 3
                        os.mkdir(C_F)
                        return True, C_F
                    else:
                        return False, ""
            else:
                C_Fol = pt + r"\\" + str(C_SCode)
                if os.path.exists(C_Fol) is False:  # 2
                    os.mkdir(C_Fol)
                    C_F = C_Fol + r"\\" + "ミロク送信分"
                    if os.path.exists(C_F) is False:  # 3
                        os.mkdir(C_F)
                        return True, C_F
                    else:
                        return False, ""
                else:
                    C_F = C_Fol + r"\\" + "ミロク送信分"
                    if os.path.exists(C_F) is False:  # 3
                        os.mkdir(C_F)
                        return True, C_F
                    else:
                        return False, ""
        else:
            pt = pt + r"\\送信分受信通知"
            if os.path.exists(pt) is False:  # 1
                os.mkdir(pt)
                C_Fol = pt + r"\\" + str(C_SCode)
                if os.path.exists(C_Fol) is False:  # 2
                    os.mkdir(C_Fol)
                    C_F = C_Fol + r"\\" + "ミロク送信分"
                    if os.path.exists(C_F) is False:  # 3
                        os.mkdir(C_F)
                        return True, C_F
                    else:
                        return False, ""
                else:
                    C_F = C_Fol + r"\\" + "ミロク送信分"
                    if os.path.exists(C_F) is False:  # 3
                        os.mkdir(C_F)
                        return True, C_F
                    else:
                        return False, ""
            else:
                C_Fol = pt + r"\\" + str(C_SCode)
                if os.path.exists(C_Fol) is False:  # 2
                    os.mkdir(C_Fol)
                    C_F = C_Fol + r"\\" + "ミロク送信分"
                    if os.path.exists(C_F) is False:  # 3
                        os.mkdir(C_F)
                        return True, C_F
                    else:
                        return False, ""
                else:
                    C_F = C_Fol + r"\\" + "ミロク送信分"
                    if os.path.exists(C_F) is False:  # 3
                        os.mkdir(C_F)
                        return True, C_F
                    else:
                        return False, ""
        # ---------------------------------------------------------
    except:
        return False, ""


FolCre(750, "山一建機　株式会社", "R4", "法人二税・特別税", "確定")
