import serial
def portIsUsable(portName):
    try:
       ser = serial.Serial(port=portName)
       return True
    except:
       return False
if portIsUsable('COM1')==True:
    print("true")
else:
    print("False")

b'\xffU\x07\x00\x02\x00\x06'