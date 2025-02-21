

from PyQt5 import QtCore, QtGui, QtWidgets


class GeoE(object):
    def reverseList(self, array):
        for i in range(len(array)):
            if i % 2 != 0:
                array[i].reverse()
        return array

    def Encrypt(self):
        Plaintext = self.plaintext_2.text().upper().replace(' ','')
        Key = int(self.key.text())

        completerow = int(len(Plaintext) / Key)

        lastrow = len(Plaintext) % Key

        if (lastrow > 0): completerow += 1

        fill = [['null' for x in range(Key)]
                for y in range(completerow)]

        index = 0
        for i in range(completerow):
            for j in range(Key):
                fill[i][j] = Plaintext[index]
                index += 1
                if index == len(Plaintext):
                    break
        self.reverseList(fill)

        ######

        f = []
        for i in range(Key):
            for j in range(completerow):
                f.append(fill[j][i])

        f2 = []
        i = 0
        while i < len(f):
            f2.append(f[i:i + completerow])
            i += completerow
        self.reverseList(f2)
        Ciphertext = ''.join([ele for sub in f2 for ele in sub if ele != 'null'])
        self.ciphertext.setText(Ciphertext)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(709, 491)
        self.encryptbutton = QtWidgets.QPushButton(Dialog)
        self.encryptbutton.setGeometry(QtCore.QRect(300, 270, 111, 41))
        self.encryptbutton.setStyleSheet("QPushButton {\n"
"  padding: 8px 25px;\n"
"\n"
"  text-align: center;\n"
"  outline: none;\n"
"  color: #fff;\n"
"  background-color:     #008000;\n"
"  border: none;\n"
"  border-radius: 15px;\n"
"font: 15pt \"Rockwell\";\n"
"}\n"
"\n"
"QPushButton:hover {background-color: #006400}")
        self.encryptbutton.setObjectName("encryptbutton")
        self.encryptbutton.clicked.connect(self.Encrypt)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 711, 491))
        self.label.setStyleSheet("")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/End.jpeg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(210, 40, 301, 51))
        self.label_3.setStyleSheet("color: rgb(253, 250, 255);\n"
"font: 30pt \"Rockwell\";")
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(220, 50, 291, 51))
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.ciphertext = QtWidgets.QTextBrowser(Dialog)
        self.ciphertext.setGeometry(QtCore.QRect(100, 370, 521, 41))
        self.ciphertext.setStyleSheet("  padding: 5px 20px;\n"
"\n"
"  text-align: center;\n"
"  outline: none;\n"
"  background-color:     #f7f7f7;\n"
"  border: none;\n"
"  border-radius: 15px;\n"
"font: 14pt \"Futura\";")
        self.ciphertext.setObjectName("ciphertext")
        self.plaintext_2 = QtWidgets.QLineEdit(Dialog)
        self.plaintext_2.setGeometry(QtCore.QRect(110, 140, 491, 41))
        self.plaintext_2.setStyleSheet("QLineEdit{\n"
"  padding: 8px 20px;\n"
"\n"
"  text-align: center;\n"
"  outline: none;\n"
"  background-color:     #f7f7f7;\n"
"  border: 2px solid rgb(194, 191, 196);\n"
"  border-radius: 15px;\n"
"font: 14pt \"Futura\";\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(70, 69, 71);\n"
"}\n"
"QlineEdit:active{\n"
"border: 2px solid rgb(0, 116, 0);\n"
"}")
        self.plaintext_2.setObjectName("plaintext_2")
        self.key = QtWidgets.QLineEdit(Dialog)
        self.key.setGeometry(QtCore.QRect(110, 200, 181, 41))
        self.key.setStyleSheet("QLineEdit{\n"
"  padding: 8px 20px;\n"
"\n"
"  text-align: center;\n"
"  outline: none;\n"
"  background-color:     #f7f7f7;\n"
"  border: 2px solid rgb(194, 191, 196);\n"
"  border-radius: 15px;\n"
"font: 14pt \"Futura\";\n"
"}\n"
"QLineEdit:hover{\n"
"border: 2px solid rgb(70, 69, 71);\n"
"}\n"
"QlineEdit:active{\n"
"border: 2px solid rgb(0, 116, 0);\n"
"}")
        self.key.setObjectName("key")
        self.label.raise_()
        self.encryptbutton.raise_()
        self.label_3.raise_()
        self.label_5.raise_()
        self.ciphertext.raise_()
        self.plaintext_2.raise_()
        self.key.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.encryptbutton.setText(_translate("Dialog", "Encrypt"))
        self.label_3.setText(_translate("Dialog", "Geometric Cipher"))
        self.label_5.setText(_translate("Dialog", "___________________________________________"))
        self.ciphertext.setPlaceholderText(_translate("Dialog", "The Ciphertext (Result)"))
        self.plaintext_2.setPlaceholderText(_translate("Dialog", "Enter the Plaintext:"))
        self.key.setPlaceholderText(_translate("Dialog", "Enter the Key number"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = GeoE()
    ui.setupUi( MainWindow )
    MainWindow.show()
    sys.exit(app.exec_())