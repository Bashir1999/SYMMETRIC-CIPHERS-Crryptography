
from PyQt5 import QtCore, QtGui, QtWidgets


class ADFGXEnc(object):
    def Encrypt(self):
        cipher5 = 'ADFGX'
        alph = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
        plaintext = self.Plaintext.text().upper().replace(' ','')
        key1 = (self.FirstKey.text().upper()) + alph
        key2 = self.SecondKey.text().upper()

        StoreKey = []
        for letter in key2:
            if letter not in StoreKey: StoreKey.append(letter)

        cleanKey1 = ''
        for i in key1:
            if i not in cleanKey1: cleanKey1 += i
        ck1L = len(cleanKey1)

        # make sort index
        l = len(StoreKey)
        s = sorted(range(l), key=lambda i: StoreKey[i])

        # encrypt
        ciphertext = []
        for letter in plaintext:
            if letter.isalpha() or letter.isdigit():
                r, c = divmod(cleanKey1.index(letter), 5)
                ciphertext += [cipher5[r], cipher5[c]]

        # reorder index
        cipherT = ''.join(ciphertext[j] for i in s for j in range(i, len(ciphertext), l))
        self.ciphertext.setText(cipherT)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(709, 491)
        self.encryptbutton = QtWidgets.QPushButton(Dialog)
        self.encryptbutton.setGeometry(QtCore.QRect(290, 300, 111, 41))
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
        self.label.setPixmap(QtGui.QPixmap("img/black.jpeg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(240, 40, 301, 51))
        self.label_3.setStyleSheet("color: rgb(253, 250, 255);\n"
"font: 30pt \"Rockwell\";")
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(240, 50, 291, 51))
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.ciphertext = QtWidgets.QTextBrowser(Dialog)
        self.ciphertext.setGeometry(QtCore.QRect(100, 380, 521, 41))
        self.ciphertext.setStyleSheet("  padding: 5px 20px;\n"
"\n"
"  text-align: center;\n"
"  outline: none;\n"
"  background-color:     #f7f7f7;\n"
"  border: none;\n"
"  border-radius: 15px;\n"
"font: 14pt \"Futura\";")
        self.ciphertext.setObjectName("ciphertext")
        self.FirstKey = QtWidgets.QLineEdit(Dialog)
        self.FirstKey.setGeometry(QtCore.QRect(140, 210, 201, 41))
        self.FirstKey.setStyleSheet("QLineEdit{\n"
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
        self.FirstKey.setObjectName("FirstKey")
        self.SecondKey = QtWidgets.QLineEdit(Dialog)
        self.SecondKey.setGeometry(QtCore.QRect(370, 210, 201, 41))
        self.SecondKey.setStyleSheet("QLineEdit{\n"
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
        self.SecondKey.setObjectName("SecondKey")
        self.Plaintext = QtWidgets.QLineEdit(Dialog)
        self.Plaintext.setGeometry(QtCore.QRect(110, 140, 491, 41))
        self.Plaintext.setStyleSheet("QLineEdit{\n"
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
        self.Plaintext.setObjectName("Plaintext")
        self.label.raise_()
        self.encryptbutton.raise_()
        self.label_3.raise_()
        self.label_5.raise_()
        self.ciphertext.raise_()
        self.FirstKey.raise_()
        self.SecondKey.raise_()
        self.Plaintext.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.encryptbutton.setText(_translate("Dialog", "Encrypt"))
        self.label_3.setText(_translate("Dialog", "ADFGX Cipher"))
        self.label_5.setText(_translate("Dialog", "_______________________________________"))
        self.ciphertext.setPlaceholderText(_translate("Dialog", "The Ciphertext (Result)"))
        self.FirstKey.setPlaceholderText(_translate("Dialog", "Enter the First Key"))
        self.SecondKey.setPlaceholderText(_translate("Dialog", "Enter the Second Key"))
        self.Plaintext.setPlaceholderText(_translate("Dialog", "Enter the Plaintext:"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ADFGXEnc()
    ui.setupUi( MainWindow )
    MainWindow.show()
    sys.exit(app.exec_())