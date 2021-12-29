from ctypes import sizeof
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys
from Resource import storedwifi
import struct
import time
from array import array
from Resource.PushAndGet import *


class UI(QtWidgets.QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("Gui/mainWindow.ui", self)
        self.Getssid = self.findChild(QtWidgets.QLineEdit, 'SSID')
        self.Getpass = self.findChild(QtWidgets.QLineEdit, 'PASS')
        self.Getport = self.findChild(QtWidgets.QComboBox, 'Port')
        self.Pushwifi = self.findChild(QtWidgets.QPushButton, 'Pushwifi')
        self.Getwifi = self.findChild(QtWidgets.QPushButton, 'Getwifi')
        self.Getstt = self.findChild(QtWidgets.QPushButton, 'Getstatuswifi')
        self.Stored = self.findChild(QtWidgets.QListWidget, 'stored')
        self.status = self.findChild(QtWidgets.QLabel, 'statusConnection')
        self.Storedwifi = self.findChild(QtWidgets.QPushButton, 'Storedwifi')
        self.Led = self.findChild(QtWidgets.QLabel, 'Connectled')
        self.wifistatus = self.findChild(QtWidgets.QListWidget, 'Wifistatus')
        self.SelectedWifi = self.findChild(QtWidgets.QPushButton,'selectwifi')
        self.Pushwifi.clicked.connect(self.Push_wifi)
        self.Getwifi.clicked.connect(self.Get_wifi)
        self.Storedwifi.clicked.connect(self.Stored_wifi)
        self.Getstt.clicked.connect(self.wifi_log)
        import serial.tools.list_ports
        for i in serial.tools.list_ports.comports():
            port = str(i).split(" ")[0]
            self.Getport.addItem(port)
        self.show()
        portName = self.Getport.currentText()
        try:
            ser = serial.Serial(port=portName)
            self.Led.setStyleSheet('\nbackground-color: rgb(0, 255, 0);')
            self.status.setText("Connected")

        except:
            self.Led.setStyleSheet('\nbackground-color: rgb(255, 0q, 0);')
            self.status.setText("Disconnected")

    def Push_wifi(self):
        def portIsUsable(portName):
            try:
                ser = serial.Serial(port=portName)
                self.Led.setStyleSheet('\nbackground-color: rgb(0, 255, 0);')
                self.status.setText("Connected")
                return True
            except:
                self.Led.setStyleSheet('\nbackground-color: rgb(255, 0q, 0);')
                self.status.setText("Disconnected")
                return False


        if self.Getssid.text() == '' or self.Getpass.text() == '':
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Error")
            msg.setInformativeText("SSID or PASS is empty")
            msg.setWindowTitle("Alert")
            msg.exec_()
            self.wifistatus.addItem('Transmit Failed !')
        portName = self.Getport.currentText()
        SSID = self.Getssid.text()
        PASS = self.Getpass.text()
        if portIsUsable(portName):
            WifiComSetInfoWifi(SSID,PASS,portName)
            ser = serial.Serial(portName, 115200, timeout=0.5)
            bufR = ser.read(103)
            print("BufR: ",bufR)
            ser.close()
            if str(bufR) == "200":

                self.wifistatus.addItem('Transmit Successed !')
                self.wifistatus.addItem(str(bufR))
            else: 
                self.wifistatus.addItem('Transmit Failed !')
        else:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Error")
            msg.setInformativeText("Port busy")
            msg.setWindowTitle("Alert")
            msg.exec_()
            self.wifistatus.addItem('Transmit Failed ! Port busy')
            self.Push_wifi()
        
            
       
        
    def Get_wifi(self):
        def portIsUsable(portName):
            try:
                ser = serial.Serial(port=portName)
                return True
            except:
                return False
        portName = self.Getport.currentText()
        if portIsUsable(portName):
            WifiComGetInfoWifi(portName)
            frame=dataFrame(portName)
            print(frame)
            
            self.Getpass.setText(frame[5])
            self.Getssid.setText(frame[4])
        else:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Error")
            msg.setInformativeText("Port busy")
            msg.setWindowTitle("Alert")
            msg.exec_()
            self.wifistatus.addItem('Transmit Failed !')

        
        
    def Stored_wifi(self):
        for x, y in zip(storedwifi.SSID, storedwifi.PASS):
            self.Stored.addItem(str(x)+' ' + str(*y))
        
        self.SelectedWifi.clicked.connect(self.add_wifi)
    def add_wifi(self):
        ssid= storedwifi.SSID[self.Stored.currentRow()]
        passw =storedwifi.PASS[self.Stored.currentRow()]
        self.Getpass.setText(*passw)
        self.Getssid.setText(ssid)
    

    def wifi_log(self):
        portName = self.Getport.currentText()
        WifiComGetStatusWifi(portName)
        


    


        
app = QtWidgets.QApplication(sys.argv)
window = UI()
app.exec_()
