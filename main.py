from PyQt5 import QtCore, QtGui, QtWidgets, uic
import sys
import checkconnect
import storedwifi


class UI(QtWidgets.QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi("login1.ui", self)
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
        if checkconnect.flag == True:
            self.Led.setStyleSheet('\nbackground-color: rgb(0, 255, 0);')
            self.status.setText("Connected")
        else:
            self.Led.setStyleSheet('\nbackground-color: rgb(255, 0q, 0);')
            self.status.setText("Disconnected")
        self.Getstt.clicked.connect(self.wifi_log)
        import serial.tools.list_ports
        for i in serial.tools.list_ports.comports():
            port = str(i).split(" ")[0]
            self.Getport.addItem(port)
        self.show()

    def Push_wifi(self):
        if self.Getssid.text() == '' or self.Getpass == '':
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Error")
            msg.setInformativeText("SSID or PASS is empty")
            msg.setWindowTitle("Alert")
            msg.exec_()
        if checkconnect.flag == True:
            self.Led.setStyleSheet('\nbackground-color: rgb(0, 255, 0);')
            self.status.setText("Connected")
        else:
            self.Led.setStyleSheet('\nbackground-color: rgb(255, 0q, 0);')
            self.status.setText("Disconnected")

    def Get_wifi(self):
        if self.Getssid.text() == '':
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Error")
            msg.setInformativeText("SSID is empty")
            msg.setWindowTitle("Alert")
            msg.exec_()
        print(self.Getssid.text())

    def Stored_wifi(self):
        # for i in storedwifi.SSID:
        #     if self.Getssid.text() ==  i:
        #         self.statu.setText(i)
        for x, y in zip(storedwifi.SSID, storedwifi.PASS):
            self.Stored.addItem(str(x)+' ' + str(*y))
        
        self.SelectedWifi.clicked.connect(self.add_wifi)
    def add_wifi(self):
        ssid= storedwifi.SSID[self.Stored.currentRow()]
        passw =storedwifi.PASS[self.Stored.currentRow()]
        self.Getpass.setText(*passw)
        self.Getssid.setText(ssid)
        

    def wifi_log(self):
        import subprocess
        wifi = subprocess.check_output(['netsh', 'WLAN', 'show', 'interfaces'])
        data = wifi.decode('utf-8')
        self.wifistatus.addItem(data)


app = QtWidgets.QApplication(sys.argv)
window = UI()
app.exec_()
