
from PyQt5 import QtCore, QtGui, QtWidgets


class ADFGXDec(object):

    def Decrypt(self):
        cipher5 = 'ADFGX'
        Ciphertext = self.ciphertext_2.text().upper().replace(' ','')
        alph = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        key1 = (self.FirstKey.text().upper()) + alph
        key2 = self.SecondKey.text().upper()

        StorKey = []
        for i in key2:
            if i not in StorKey:
                StorKey.append(i)

        cleanKey1 = ''
        for i in key1:
            if i not in cleanKey1: cleanKey1 += i
        ck1L = len(cleanKey1)

        # make sort index
        l = len(StorKey)
        kSort = sorted(range(l), key=lambda i: StorKey[i])

        # make reorder index

        t = len(Ciphertext)
        indexC = [j for i in kSort for j in range(i, t, l)]

        # reorder

        x = [''] * t
        for i, let in zip(indexC, Ciphertext):
            x[i] = let
        # decode
        plainT = []
        for i in range(0, t, 2):
            r, c = x[i:i + 2]
            plainT.append(cleanKey1[5 * cipher5.index(r) + cipher5.index(c)])

        Plaintext = ''.join(plainT)
        self.plaintext.setText(Plaintext)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(709, 491)
        self.decryptbutton = QtWidgets.QPushButton(Dialog)
        self.decryptbutton.setGeometry(QtCore.QRect(290, 300, 111, 41))
        self.decryptbutton.setStyleSheet("QPushButton {\n"
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
        self.decryptbutton.setObjectName("decryptbutton")
        self.decryptbutton.clicked.connect(self.Decrypt)
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
        self.plaintext = QtWidgets.QTextBrowser(Dialog)
        self.plaintext.setGeometry(QtCore.QRect(100, 380, 521, 41))
        self.plaintext.setStyleSheet("  padding: 5px 20px;\n"
"\n"
"  text-align: center;\n"
"  outline: none;\n"
"  background-color:     #f7f7f7;\n"
"  border: none;\n"
"  border-radius: 15px;\n"
"font: 14pt \"Futura\";")
        self.plaintext.setObjectName("plaintext")
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
        self.ciphertext_2 = QtWidgets.QLineEdit(Dialog)
        self.ciphertext_2.setGeometry(QtCore.QRect(110, 140, 491, 41))
        self.ciphertext_2.setStyleSheet("QLineEdit{\n"
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
        self.ciphertext_2.setObjectName("ciphertext_2")
        self.label.raise_()
        self.decryptbutton.raise_()
        self.label_3.raise_()
        self.label_5.raise_()
        self.plaintext.raise_()
        self.FirstKey.raise_()
        self.SecondKey.raise_()
        self.ciphertext_2.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.decryptbutton.setText(_translate("Dialog", "Decrypt"))
        self.label_3.setText(_translate("Dialog", "ADFGX Cipher"))
        self.label_5.setText(_translate("Dialog", "_______________________________________"))
        self.plaintext.setPlaceholderText(_translate("Dialog", "The Plaintext (Result)"))
        self.FirstKey.setPlaceholderText(_translate("Dialog", "Enter the First Key"))
        self.SecondKey.setPlaceholderText(_translate("Dialog", "Enter the Second Key"))
        self.ciphertext_2.setPlaceholderText(_translate("Dialog", "Enter the Ciphertext:"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ADFGXDec()
    ui.setupUi( MainWindow )
    MainWindow.show()
    sys.exit(app.exec_())