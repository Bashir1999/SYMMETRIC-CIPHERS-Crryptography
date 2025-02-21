
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(709, 491)
        self.decryptbutton = QtWidgets.QPushButton(Dialog)
        self.decryptbutton.setGeometry(QtCore.QRect(290, 250, 111, 41))
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
        self.decryptbutton.clicked.connect(self.Decryption)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 711, 491))
        self.label.setStyleSheet("")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/Polybius.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(230, 40, 301, 51))
        self.label_3.setStyleSheet("color: rgb(253, 250, 255);\n"
                                   "font: 30pt \"Rockwell\";")
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(240, 50, 291, 51))
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.plaintext = QtWidgets.QTextBrowser(Dialog)
        self.plaintext.setGeometry(QtCore.QRect(100, 360, 521, 41))
        self.plaintext.setStyleSheet("  padding: 5px 20px;\n"
                                     "\n"
                                     "  text-align: center;\n"
                                     "  outline: none;\n"
                                     "  background-color:     #f7f7f7;\n"
                                     "  border: none;\n"
                                     "  border-radius: 15px;\n"
                                     "font: 14pt \"Futura\";")
        self.plaintext.setObjectName("plaintext")
        self.ciphertext = QtWidgets.QLineEdit(Dialog)
        self.ciphertext.setGeometry(QtCore.QRect(110, 140, 491, 41))
        self.ciphertext.setStyleSheet("QLineEdit{\n"
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
        self.ciphertext.setObjectName("ciphertext")
        self.label.raise_()
        self.decryptbutton.raise_()
        self.label_3.raise_()
        self.label_5.raise_()
        self.plaintext.raise_()
        self.ciphertext.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.decryptbutton.setText(_translate("Dialog", "Decrypt"))
        self.label_3.setText(_translate("Dialog", "Polybius Cipher"))
        self.label_5.setText(_translate("Dialog", "________________________________________"))
        self.plaintext.setPlaceholderText(_translate("Dialog", "The Plaintext (Result)"))
        self.ciphertext.setPlaceholderText(_translate("Dialog", "Enter the Ciphertext:"))

    def Decryption(self):

        Alphabets = "abcdefghiklmnopqrstuvwxyz"
        CipherText = self.ciphertext.text()
        PlainText = ""

        for number in CipherText.strip().split(" "):

            row = int(number[0])
            col = int(number[1])

            if row == 2 and col == 4:
                PlainText += "[i,j]"

            else:

                MatrixPositioning = (row - 1) * 5 + col
                PlainText += Alphabets[MatrixPositioning - 1]

        self.plaintext.setText(PlainText)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
