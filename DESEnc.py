
from PyQt5 import QtCore, QtGui, QtWidgets
import DESENCDEC

class DESEn(object):
    def Encrypt(self):
        Plaintext = self.Plaintext.text().upper().replace(' ','')
        Key = self.key.text().upper().replace(' ','')

        key = DESENCDEC.hex2bin(Key)

        # --parity bit drop table
        keyp = [57, 49, 41, 33, 25, 17, 9,
                1, 58, 50, 42, 34, 26, 18,
                10, 2, 59, 51, 43, 35, 27,
                19, 11, 3, 60, 52, 44, 36,
                63, 55, 47, 39, 31, 23, 15,
                7, 62, 54, 46, 38, 30, 22,
                14, 6, 61, 53, 45, 37, 29,
                21, 13, 5, 28, 20, 12, 4]

        # getting 56 bit key from 64 bit using the parity bits
        key = DESENCDEC.permute(key, keyp, 56)

        # Number of bit shifts
        shift_table = [1, 1, 2, 2,
                       2, 2, 2, 2,
                       1, 2, 2, 2,
                       2, 2, 2, 1]

        # Key- Compression Table : Compression of key from 56 bits to 48 bits
        key_comp = [14, 17, 11, 24, 1, 5,
                    3, 28, 15, 6, 21, 10,
                    23, 19, 12, 4, 26, 8,
                    16, 7, 27, 20, 13, 2,
                    41, 52, 31, 37, 47, 55,
                    30, 40, 51, 45, 33, 48,
                    44, 49, 39, 56, 34, 53,
                    46, 42, 50, 36, 29, 32]

        # Splitting
        left = key[0:28]  # rkb for RoundKeys in binary
        right = key[28:56]  # rk for RoundKeys in hexadecimal

        rkb = []
        rk = []
        for i in range(0, 16):
            # Shifting the bits by nth shifts by checking from shift table
            left = DESENCDEC.shift_left(left, shift_table[i])
            right = DESENCDEC.shift_left(right, shift_table[i])

            # Combination of left and right string
            combine_str = left + right

            # Compression of key from 56 to 48 bits
            round_key = DESENCDEC.permute(combine_str, key_comp, 48)

            rkb.append(round_key)
            rk.append(DESENCDEC.bin2hex(round_key))

        c = DESENCDEC.bin2hex(DESENCDEC.encrypt(Plaintext, rkb, rk))
        self.ciphertext.setText(c)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(709, 491)
        self.encryptbutton = QtWidgets.QPushButton(Dialog)
        self.encryptbutton.setGeometry(QtCore.QRect(300, 300, 111, 41))
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
        self.label.setPixmap(QtGui.QPixmap("img/ACT.jpeg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(270, 40, 191, 51))
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
        self.key = QtWidgets.QLineEdit(Dialog)
        self.key.setGeometry(QtCore.QRect(110, 200, 491, 41))
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
        self.key.raise_()
        self.Plaintext.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.encryptbutton.setText(_translate("Dialog", "Encrypt"))
        self.label_3.setText(_translate("Dialog", "DES Cipher"))
        self.label_5.setText(_translate("Dialog", "______________________________"))
        self.ciphertext.setPlaceholderText(_translate("Dialog", "The Ciphertext (Result)"))
        self.key.setPlaceholderText(_translate("Dialog", "Enter the key (must be 16 char\'s"))
        self.Plaintext.setPlaceholderText(_translate("Dialog", "Enter the Plaintext: (must be 16 char\'s)"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = DESEn()
    ui.setupUi( MainWindow )
    MainWindow.show()
    sys.exit(app.exec_())