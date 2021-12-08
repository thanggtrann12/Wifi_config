# def Convert(SSID,lenSSID,PASS,lenPASS):
#     converSSID=[]
#     converPASS=[]
#     converSSID[:0]=SSID
#     converPASS[:0]=PASS
#     dataResult =[]
#     for i in range(0,len(converSSID)):
#        dataResult.append(ord(converSSID[i]))
#     for i in range(len(dataResult),lenSSID):
#         dataResult.append(0)
#     for i in range(0, len(converPASS)):
#         dataResult.append(ord(converPASS[i]))
#     for i in range(len(dataResult),lenPASS+lenSSID):
#         dataResult.append(0)
#     return dataResult
#     # for i in range(0,lenSSID):
#     #
#     #     dataResult.append('0')
#     # return converPASS
# 0
#
# TK  = 'Room Technical'
# MK = '12345612zxc'
# print(Convert(TK,32,MK,64))

# for i in range(0,32):
#     print(SSID.append(TK[i]))
# tempTx= SSID+PASS
# dataTx=[]
# for i in range(0,len(tempTx)):
    
#     dataTx.append(ord(tempTx[i]))
SIZE_HEADER = 2
SIZE_LENGTH = 2
a =  b'\xffUf\x00\x03testcase_2\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0012345612zxc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

data = a.hex()
print(data)
# print("data: ",data,"Data split: ",dataTx[0:3])


headerR = data[:SIZE_HEADER*2]
data = data.replace(headerR,'')
lenR = data[:SIZE_LENGTH*2]
data = data.replace(lenR,'')
cmdR = data[:2]
data.replace(cmdR,'')

crcR = data[-2:]
data.replace(crcR,'')
ackR = data[:2]
data.replace(ackR,'')
dataR = data[2:]
print("header: ", headerR, "\nlength: ",lenR,"\ncmd: ",cmdR,"\nack: ",ackR,"\ndata: ",dataR,"\ncrc: ",crcR)


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
# b'\xffUf\x00\x02testcase_2\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0012345612zxc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00