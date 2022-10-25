###########################################################################################################
# 稼働設定：解像度 1920*1080 表示スケール125%
###########################################################################################################
import TKCCDBMailAddressUpdate as CDB
import TKCFMSMailAddressUpdate as FMS

CDBA = CDB.AllMain()
if CDBA[0] is True:
    FMS.AllMain(CDBA[1])
else:
    print("CDB失敗の為中断")
