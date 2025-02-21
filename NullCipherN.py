
from PyQt5 import QtCore, QtGui, QtWidgets


class NullCEnc(object):
    def Encryption(self):
        message = self.Plaintext.text().upper().replace(' ','')
        key = int(self.key.text())

        import random

        alphabet = (
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
        'W', 'X', 'Y', 'Z')


        message = message.replace(":", "")
        message = message.replace(";", "")
        message = message.replace(",", "")
        message = message.replace(".", "")
        message = message.replace("?", "")
        message = message.replace("!", "")

        message = message.upper()
        word_substitutes = []

        for c in message:
            if c not in alphabet:
                continue

            index_of_plaintext = key % 5

            word_substitute = ""
            for i in range(0, 5):
                if i == index_of_plaintext:
                    word_substitute += c
                else:
                    random_letter_index = random.randint(0, len(alphabet) - 1)
                    word_substitute += alphabet[random_letter_index]

            word_substitutes.append(word_substitute)

        ciphert = ' '.join(word_substitutes)
        self.ciphertext.setText(ciphert)
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(709, 491)
        self.encryptbutton = QtWidgets.QPushButton(Dialog)
        self.encryptbutton.setGeometry(QtCore.QRect(290, 280, 111, 41))
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
        self.encryptbutton.clicked.connect(self.Encryption)
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
        self.Plaintext.raise_()
        self.key.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.encryptbutton.setText(_translate("Dialog", "Encrypt"))
        self.label_3.setText(_translate("Dialog", "Null Cipher"))
        self.label_5.setText(_translate("Dialog", "_____________________________"))
        self.ciphertext.setPlaceholderText(_translate("Dialog", "The Ciphertext (Result)"))
        self.Plaintext.setPlaceholderText(_translate("Dialog", "Enter the Plaintext:"))
        self.key.setPlaceholderText(_translate("Dialog", "Enter the key (0-5)"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = NullCEnc()
    ui.setupUi( MainWindow )
    MainWindow.show()
    sys.exit(app.exec_())