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