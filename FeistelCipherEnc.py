
from PyQt5 import QtCore, QtGui, QtWidgets


class FeistelEnc(object):
    def Encrypt(self):

        import binascii

        def rand_key(p):
            import random
            key1 = ""
            p = int(p)

            for i in range(p):
                temp = random.randint(0, 1)
                temp = str(temp)
                key1 = key1 + temp

            return (key1)

        def exor(a, b):
            temp = ""

            for i in range(n):

                if (a[i] == b[i]):
                    temp += "0"

                else:
                    temp += "1"

            return temp

        # Defining BinarytoDecimal() function
        def BinaryToDecimal(binary):
            # Using int function to convert to
            # string
            string = int(binary, 2)

            return string

        # Feistel Cipher
        PT = self.Plaintext.text()

        # Converting the plain text to
        # ASCII
        PT_Ascii = [ord(x) for x in PT]

        # Converting the ASCII to
        # 8-bit binary format
        PT_Bin = [format(y, '08b') for y in PT_Ascii]
        PT_Bin = "".join(PT_Bin)

        n = int(len(PT_Bin) // 2)
        L1 = PT_Bin[0:n]
        R1 = PT_Bin[n::]
        m = len(R1)

        # Generate Key K1 for the
        # first round
        K1 = rand_key(m)

        # Generate Key K2 for the
        # second round
        K2 = rand_key(m)

        # first round of Feistel
        f1 = exor(R1, K1)
        R2 = exor(f1, L1)
        L2 = R1

        # Second round of Feistel
        f2 = exor(R2, K2)
        R3 = exor(f2, L2)
        L3 = R2

        # Cipher text
        bin_data = L3 + R3
        str_data = ' '

        for i in range(0, len(bin_data), 7):
            # slicing the bin_data from index range [0, 6]
            # and storing it in temp_data
            temp_data = bin_data[i:i + 7]

            # passing temp_data in BinarytoDecimal() function
            # to get decimal value of corresponding temp_data
            decimal_data = BinaryToDecimal(temp_data)

            # Deccoding the decimal value returned by
            # BinarytoDecimal() function, using chr()
            # function which return the string corresponding
            # character for given ASCII value, and store it
            # in str_data
            str_data = str_data + chr(decimal_data)

        self.Ciphertext.setText(str_data)


        # Decryption
        L4 = L3
        R4 = R3

        f3 = exor(L4, K2)
        L5 = exor(R4, f3)
        R5 = L4

        f4 = exor(L5, K1)
        L6 = exor(R5, f4)
        R6 = L5
        PT1 = L6 + R6

        PT1 = int(PT1, 2)
        RPT = binascii.unhexlify('%x' % PT1)
        self.PlaintextR.setText(str(RPT))


    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(709, 491)
        self.encDecbutton = QtWidgets.QPushButton(Dialog)
        self.encDecbutton.setGeometry(QtCore.QRect(250, 240, 211, 41))
        self.encDecbutton.setStyleSheet("QPushButton {\n"
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
        self.encDecbutton.setObjectName("encDecbutton")
        self.encDecbutton.clicked.connect(self.Encrypt)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 711, 491))
        self.label.setStyleSheet("")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/ACT.jpeg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(250, 40, 231, 51))
        self.label_3.setStyleSheet("color: rgb(253, 250, 255);\n"
"font: 30pt \"Rockwell\";")
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(260, 50, 291, 51))
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.Ciphertext = QtWidgets.QTextBrowser(Dialog)
        self.Ciphertext.setGeometry(QtCore.QRect(110, 340, 241, 41))
        self.Ciphertext.setStyleSheet("  padding: 5px 20px;\n"
"\n"
"  text-align: center;\n"
"  outline: none;\n"
"  background-color:     #f7f7f7;\n"
"  border: none;\n"
"  border-radius: 15px;\n"
"font: 14pt \"Futura\";")
        self.Ciphertext.setObjectName("Ciphertext")
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
        self.PlaintextR = QtWidgets.QTextBrowser(Dialog)
        self.PlaintextR.setGeometry(QtCore.QRect(370, 340, 231, 41))
        self.PlaintextR.setStyleSheet("  padding: 5px 20px;\n"
"\n"
"  text-align: center;\n"
"  outline: none;\n"
"  background-color:     #f7f7f7;\n"
"  border: none;\n"
"  border-radius: 15px;\n"
"font: 14pt \"Futura\";")
        self.PlaintextR.setObjectName("PlaintextR")
        self.label.raise_()
        self.encDecbutton.raise_()
        self.label_3.raise_()
        self.label_5.raise_()
        self.Ciphertext.raise_()
        self.Plaintext.raise_()
        self.PlaintextR.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.encDecbutton.setText(_translate("Dialog", "Encrypt and Decrypt"))
        self.label_3.setText(_translate("Dialog", "Feistel Cipher"))
        self.label_5.setText(_translate("Dialog", "__________________________________"))
        self.Ciphertext.setPlaceholderText(_translate("Dialog", "The Ciphertext (Result)"))
        self.Plaintext.setPlaceholderText(_translate("Dialog", "Enter the Plaintext:"))
        self.PlaintextR.setPlaceholderText(_translate("Dialog", "The Plaintext (Result)"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = FeistelEnc()
    ui.setupUi( MainWindow )
    MainWindow.show()
    sys.exit(app.exec_())