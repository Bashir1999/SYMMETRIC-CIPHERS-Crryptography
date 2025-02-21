
from PyQt5 import QtCore, QtGui, QtWidgets


class RailFDec(object):
    def Decrypt(self):
        Ciphertext = self.ciphertext_2.text().upper().replace(' ','')
        Key = int(self.key.text())

        fill = [['null' for x in range(len(Ciphertext))]
                for y in range(Key)]

        direction = None
        r, c = 0, 0

        for i in range(len(Ciphertext)):
            if r == 0:
                direction = True
            if r == Key - 1:
                direction = False

            fill[r][c] = '@'
            c += 1


            if direction:
                r += 1
            else:
                r -= 1

        ind = 0
        for i in range(Key):
            for j in range(len(Ciphertext)):
                if ((ind < len(Ciphertext) and (fill[i][j] == '@'))):
                    fill[i][j] = Ciphertext[ind]
                    ind += 1

        plaintext = []
        r, c = 0, 0
        for i in range(len(Ciphertext)):
            if r == 0:
                direction = True
            if r == Key - 1:
                direction = False

            if (fill[r][c] != '@'):
                plaintext.append(fill[r][c])
                c += 1

            if direction:
                r += 1
            else:
                r -= 1
        plaint = ''.join(plaintext)
        self.plaintext.setText(plaint)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(709, 491)
        self.decryptbutton = QtWidgets.QPushButton(Dialog)
        self.decryptbutton.setGeometry(QtCore.QRect(300, 270, 111, 41))
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
        self.label.setPixmap(QtGui.QPixmap("img/Columnar.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(220, 40, 301, 51))
        self.label_3.setStyleSheet("color: rgb(253, 250, 255);\n"
"font: 30pt \"Rockwell\";")
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(230, 50, 291, 51))
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.plaintext = QtWidgets.QTextBrowser(Dialog)
        self.plaintext.setGeometry(QtCore.QRect(100, 370, 521, 41))
        self.plaintext.setStyleSheet("  padding: 5px 20px;\n"
"\n"
"  text-align: center;\n"
"  outline: none;\n"
"  background-color:     #f7f7f7;\n"
"  border: none;\n"
"  border-radius: 15px;\n"
"font: 14pt \"Futura\";")
        self.plaintext.setObjectName("plaintext")
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
        self.decryptbutton.raise_()
        self.label_3.raise_()
        self.label_5.raise_()
        self.plaintext.raise_()
        self.ciphertext_2.raise_()
        self.key.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.decryptbutton.setText(_translate("Dialog", "Decrypt"))
        self.label_3.setText(_translate("Dialog", "Rail Fence Cipher"))
        self.label_5.setText(_translate("Dialog", "___________________________________________"))
        self.plaintext.setPlaceholderText(_translate("Dialog", "The Plaintext (Result)"))
        self.ciphertext_2.setPlaceholderText(_translate("Dialog", "Enter the Ciphertext:"))
        self.key.setPlaceholderText(_translate("Dialog", "Enter the Key number"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = RailFDec()
    ui.setupUi( MainWindow )
    MainWindow.show()
    sys.exit(app.exec_())