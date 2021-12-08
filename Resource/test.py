def Convert(SSID,lenSSID,PASS,lenPASS):
    converSSID=[]
    converPASS=[]
    converSSID[:0]=SSID
    converPASS[:0]=PASS
    dataResult =[]
    for i in range(0,len(converSSID)):
       dataResult.append(ord(converSSID[i]))
    for i in range(len(dataResult),lenSSID):
        dataResult.append(0)
    for i in range(0, len(converPASS)):
        dataResult.append(ord(converPASS[i]))
    for i in range(len(dataResult),lenPASS+lenSSID):
        dataResult.append(0)
    return dataResult
    # for i in range(0,lenSSID):
    #
    #     dataResult.append('0')
    # return converPASS
0

TK  = 'Room Technical'
MK = '12345612zxc'
print(Convert(TK,32,MK,64))

# for i in range(0,32):
#     print(SSID.append(TK[i]))
# tempTx= SSID+PASS
# dataTx=[]
# for i in range(0,len(tempTx)):
    
#     dataTx.append(ord(tempTx[i]))






# 74 68 61 6E 67 73 61 00 00 00
# 00 00 00 00 00 00 00 00 00 00
# 00 00 00 00 00 00 00 00 00 00
# 00 00

# 20 
# 31 32 33 34 35 36 31 32 7A 78
# 63 00 00 00 00 00 00 00 00 00
# 00 00 00 00 00 00 00 00 00 00
# 00 00 00 00 00 00 00 00 00 00
# 00 00 00 00 00 00 00 00 00 00
# 00 00 00 00 00 00 00 00 00 00
# 00 00 00 2B