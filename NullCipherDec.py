
from PyQt5 import QtCore, QtGui, QtWidgets


class NullCipherD(object):

    def Decrypt(self):
        message  =self.Ciphertext.text().upper()
        key = int(self.key.text())
        message = message.replace(":", "")
        message = message.replace(";", "")
        message = message.replace(",", "")
        message = message.replace(".", "")
        message = message.replace("?", "")
        message = message.replace("!", "")

        words_in_message = message.split()

        decrypted_message = ""

        for word in words_in_message:
            decrypted_message += word[key % 5]

        self.Plaintext.setText(decrypted_message)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(709, 491)
        self.decryptbutton = QtWidgets.QPushButton(Dialog)
        self.decryptbutton.setGeometry(QtCore.QRect(290, 280, 111, 41))
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
        self.label.setPixmap(QtGui.QPixmap("Backg.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(260, 40, 201, 51))
        self.label_3.setStyleSheet("color: rgb(253, 250, 255);\n"
"font: 30pt \"Rockwell\";")
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(270, 50, 291, 51))
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.Plaintext = QtWidgets.QTextBrowser(Dialog)
        self.Plaintext.setGeometry(QtCore.QRect(100, 380, 521, 41))
        self.Plaintext.setStyleSheet("  padding: 5px 20px;\n"
"\n"
"  text-align: center;\n"
"  outline: none;\n"
"  background-color:     #f7f7f7;\n"
"  border: none;\n"
"  border-radius: 15px;\n"
"font: 14pt \"Futura\";")
        self.Plaintext.setObjectName("Plaintext")
        self.Ciphertext = QtWidgets.QLineEdit(Dialog)
        self.Ciphertext.setGeometry(QtCore.QRect(110, 140, 491, 41))
        self.Ciphertext.setStyleSheet("QLineEdit{\n"
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
        self.Ciphertext.setObjectName("Ciphertext")
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
        self.Plaintext.raise_()
        self.Ciphertext.raise_()
        self.key.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.decryptbutton.setText(_translate("Dialog", "Decrypt"))
        self.label_3.setText(_translate("Dialog", "Null Cipher"))
        self.label_5.setText(_translate("Dialog", "_____________________________"))
        self.Plaintext.setPlaceholderText(_translate("Dialog", "The Plaintext (Result)"))
        self.Ciphertext.setPlaceholderText(_translate("Dialog", "Enter the Ciphertext:"))
        self.key.setPlaceholderText(_translate("Dialog", "Enter the key (0-5)"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = NullCipherD()
    ui.setupUi( MainWindow )
    MainWindow.show()
    sys.exit(app.exec_())