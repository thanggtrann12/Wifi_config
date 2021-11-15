
import serial
serial = serial.Serial('COM7',115200,timeout=2) # Connect COM14, Baud's rate 115200
if serial.isOpen():
    print ('The serial port has been opened')
else:
    print ('Serial port is not open')

 # Close the serial port
serial.close()
if serial.isOpen():
    print ('Serial port is not closed')
else:
    print ('The serial port is closed')