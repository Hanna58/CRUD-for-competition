# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'storytelling.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import pymysql

class Ui_STORYTELLING(object):
    def koneksi(self):
        con = pymysql.connect(db='hection', user='root', passwd='', host='localhost', port=3306, autocommit=True)
        cur = con.cursor()
        if(cur):
            self.messagebox("Koneksi", "Koneksi Berhasil")
        else:
            self.messagebox("Koneksi", "Koneksi Gagal")
            
    def messagebox(self, title, message):
        mess = QtWidgets.QMessageBox()
        mess.setWindowTitle(title)
        mess.setText(message)
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
        mess.exec_()

    def save(self):
        name = self.plainTextEdit.toPlainText()
        hsname = self.plainTextEdit_2.toPlainText()
        hsaddress = self.plainTextEdit_3.toPlainText()
        wa = self.plainTextEdit_4.toPlainText()
        email = self.plainTextEdit_5.toPlainText()
        instagram = self.plainTextEdit_6.toPlainText()
        insert = (name, hsname, hsaddress, wa, email, instagram)
        print(insert)
        con = pymysql.connect(db='hection', user='root', passwd='', host='localhost', port=3306, autocommit=True)
        cur = con.cursor()
        sql = "INSERT INTO hection(name, hs_name, hs_address, wa, email, ig) + VALUES " + str(insert)
        data = cur.execute(sql)
        if(data):
            self.messagebox("SUKSES", "Data Tersimpan")
        else:
            self.messagebox("GAGAL", "Data Gagal Tersimpan")

    def clear(self):
        self.plainTextEdit.setPlainText("")
        self.plainTextEdit_2.setPlainText("")
        self.plainTextEdit_3.setPlainText("")
        self.plainTextEdit_4.setPlainText("")
        self.plainTextEdit_5.setPlainText("")
        self.plainTextEdit_6.setPlainText("")
    
    def setupUi(self, STORYTELLING):
        self.koneksi()
        STORYTELLING.setObjectName("STORYTELLING")
        STORYTELLING.resize(1118, 885)
        STORYTELLING.setStyleSheet("background-color: rgb(255, 219, 166);")
        self.label_7 = QtWidgets.QLabel(STORYTELLING)
        self.label_7.setGeometry(QtCore.QRect(70, 630, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("")
        self.label_7.setObjectName("label_7")
        self.label_5 = QtWidgets.QLabel(STORYTELLING)
        self.label_5.setGeometry(QtCore.QRect(70, 470, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("")
        self.label_5.setObjectName("label_5")
        
        self.Save = QtWidgets.QPushButton(STORYTELLING)
        self.Save.setGeometry(QtCore.QRect(720, 730, 112, 34))
        self.Save.setObjectName("Save")
        self.Save.clicked.connect(self.save)
        
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(STORYTELLING)
        self.plainTextEdit_3.setGeometry(QtCore.QRect(380, 380, 671, 41))
        self.plainTextEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.label_6 = QtWidgets.QLabel(STORYTELLING)
        self.label_6.setGeometry(QtCore.QRect(70, 550, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("")
        self.label_6.setObjectName("label_6")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(STORYTELLING)
        self.plainTextEdit.setGeometry(QtCore.QRect(380, 220, 671, 41))
        self.plainTextEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(STORYTELLING)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(380, 300, 671, 41))
        self.plainTextEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.plainTextEdit_6 = QtWidgets.QPlainTextEdit(STORYTELLING)
        self.plainTextEdit_6.setGeometry(QtCore.QRect(380, 620, 671, 41))
        self.plainTextEdit_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.plainTextEdit_6.setObjectName("plainTextEdit_6")
        self.plainTextEdit_5 = QtWidgets.QPlainTextEdit(STORYTELLING)
        self.plainTextEdit_5.setGeometry(QtCore.QRect(380, 540, 671, 41))
        self.plainTextEdit_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.plainTextEdit_5.setObjectName("plainTextEdit_5")
        self.label_2 = QtWidgets.QLabel(STORYTELLING)
        self.label_2.setGeometry(QtCore.QRect(70, 230, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.plainTextEdit_4 = QtWidgets.QPlainTextEdit(STORYTELLING)
        self.plainTextEdit_4.setGeometry(QtCore.QRect(380, 460, 671, 41))
        self.plainTextEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.plainTextEdit_4.setObjectName("plainTextEdit_4")
        
        self.Clear = QtWidgets.QPushButton(STORYTELLING)
        self.Clear.setGeometry(QtCore.QRect(940, 730, 112, 34))
        self.Clear.setObjectName("Clear")
        self.Clear.clicked.connect(self.clear)
        
        self.label = QtWidgets.QLabel(STORYTELLING)
        self.label.setGeometry(QtCore.QRect(320, 10, 511, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(STORYTELLING)
        self.label_4.setGeometry(QtCore.QRect(70, 390, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("")
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(STORYTELLING)
        self.label_3.setGeometry(QtCore.QRect(70, 310, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("")
        self.label_3.setObjectName("label_3")
        self.label_8 = QtWidgets.QLabel(STORYTELLING)
        self.label_8.setGeometry(QtCore.QRect(70, 150, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("")
        self.label_8.setObjectName("label_8")

        self.retranslateUi(STORYTELLING)
        QtCore.QMetaObject.connectSlotsByName(STORYTELLING)

    def retranslateUi(self, STORYTELLING):
        _translate = QtCore.QCoreApplication.translate
        STORYTELLING.setWindowTitle(_translate("STORYTELLING", "Form"))
        self.label_7.setText(_translate("STORYTELLING", "Instagram"))
        self.label_5.setText(_translate("STORYTELLING", "Phone Number of WhatsApp"))
        self.Save.setText(_translate("STORYTELLING", "Save"))
        self.label_6.setText(_translate("STORYTELLING", "Email Address"))
        self.label_2.setText(_translate("STORYTELLING", "Full Name"))
        self.Clear.setText(_translate("STORYTELLING", "Clear"))
        self.label.setText(_translate("STORYTELLING", "HECTION 9.0 Registration Form"))
        self.label_4.setText(_translate("STORYTELLING", "High School Address"))
        self.label_3.setText(_translate("STORYTELLING", "Name of Highschool"))
        self.label_8.setText(_translate("STORYTELLING", "STORYTELLING"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    STORYTELLING = QtWidgets.QWidget()
    ui = Ui_STORYTELLING()
    ui.setupUi(STORYTELLING)
    STORYTELLING.show()
    sys.exit(app.exec_())