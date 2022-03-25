import TKCCDBMailAddressUpdate as CDB
import TKCFMSMailAddressUpdate as FMS

CDBA = CDB.AllMain()
if CDBA == True:
    FMS.AllMain
else:
    print("CDB失敗の為中断")