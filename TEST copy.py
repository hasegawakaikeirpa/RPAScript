import CSVOut

wsNo = int('12302')

if wsNo < 1000:
    wsNo = str(wsNo)
    wsNoSub = ''
elif wsNo >= 1000 and wsNo < 2000 :
    wsNoSub = str(wsNo)[2] + str(wsNo)[3]
    wsNo = str(wsNo)[0] + str(wsNo)[1]
    wsNo = f'{int(wsNo):03}'
elif wsNo >= 4000 and wsNo < 5000 :
    wsNoSub = str(wsNo)[2] + str(wsNo)[3]
    wsNo = str(wsNo)[0] + str(wsNo)[1]
    wsNo = f'{int(wsNo):03}'
elif wsNo >= 9000 and wsNo < 10000 :
    wsNoSub = str(wsNo)[2] + str(wsNo)[3]
    wsNo = str(wsNo)[0] + str(wsNo)[1]
    wsNo = f'{int(wsNo):03}'
elif wsNo >= 10000 :
    wsNoSub = str(wsNo)[3] + str(wsNo)[4]
    wsNo = str(wsNo)[0] + str(wsNo)[1] + str(wsNo)[2]
    wsNo = f'{int(wsNo):03}'

TRow = CSVOut.CsvSortRowDouble("D:\PythonScript\RPAScript\RPAPhoto\TKCFMSMailAddressUpdate/MAILLIST.CSV","関与先コード","個人コード",wsNo,wsNoSub)
print(TRow[1])
print(wsNo)