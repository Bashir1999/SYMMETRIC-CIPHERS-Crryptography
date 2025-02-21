# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HillDecryption.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
import numpy as np

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(709, 491)
        self.decryptbutton = QtWidgets.QPushButton(Dialog)
        self.decryptbutton.setGeometry(QtCore.QRect(290, 290, 111, 41))
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
        self.label.setPixmap(QtGui.QPixmap("img/Hill.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(260, 40, 301, 51))
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
        self.Ciphertext_2 = QtWidgets.QLineEdit(Dialog)
        self.Ciphertext_2.setGeometry(QtCore.QRect(110, 140, 491, 41))
        self.Ciphertext_2.setStyleSheet("QLineEdit{\n"
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
        self.Ciphertext_2.setObjectName("Ciphertext_2")
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
        self.label.raise_()
        self.decryptbutton.raise_()
        self.label_3.raise_()
        self.label_5.raise_()
        self.Plaintext.raise_()
        self.Ciphertext_2.raise_()
        self.key.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.decryptbutton.setText(_translate("Dialog", "Decrypt"))
        self.label_3.setText(_translate("Dialog", "Hill Cipher"))
        self.label_5.setText(_translate("Dialog", "________________________"))
        self.Plaintext.setPlaceholderText(_translate("Dialog", "The Plaintext (Result)"))
        self.Ciphertext_2.setPlaceholderText(_translate("Dialog", "Enter the Ciphertext:"))
        self.key.setPlaceholderText(_translate("Dialog", "Enter the Key e.g. 'Hill'"))

    def Decryption(self):
        import numpy as np
        encrypted_msg = self.Ciphertext_2.text().upper().replace(' ','')
        key = self.key.text().upper()
        def find_multiplicative_inverse(determinant):
            multiplicative_inverse = -1
            for i in range(26):
                inverse = determinant * i
                if inverse % 26 == 1:
                    multiplicative_inverse = i
                    break
            return multiplicative_inverse

        def make_key(cipher):
            # Make sure cipher determinant is relatively prime to 26 and only a/A - z/Z are given
            determinant = 0
            C = None
            while True:
                # cipher = input("Input 4 letter cipher: ")
                C = create_matrix_of_integers_from_string(cipher)
                determinant = C[0][0] * C[1][1] - C[0][1] * C[1][0]
                determinant = determinant % 26
                inverse_element = find_multiplicative_inverse(determinant)
                if inverse_element == -1:
                    print("Determinant is not relatively prime to 26, uninvertible key")
                elif np.amax(C) > 26 and np.amin(C) < 0:
                    print("Only a-z characters are accepted")
                    print(np.amax(C), np.amin(C))
                else:
                    break
            return C

        def create_matrix_of_integers_from_string(string):
            # Map string to a list of integers a/A <-> 0, b/B <-> 1 ... z/Z <-> 25
            integers = [chr_to_int(c) for c in string]
            length = len(integers)
            M = np.zeros((2, int(length / 2)), dtype=np.int32)
            iterator = 0
            for column in range(int(length / 2)):
                for row in range(2):
                    M[row][column] = integers[iterator]
                    iterator += 1
            return M

        def chr_to_int(char):
            # Uppercase the char to get into range 65-90 in ascii table
            char = char.upper()
            # Cast chr to int and subtract 65 to get 0-25
            integer = ord(char) - 65
            return integer

        C = make_key(key)
        # Inverse matrix
        determinant = C[0][0] * C[1][1] - C[0][1] * C[1][0]
        determinant = determinant % 26
        multiplicative_inverse = find_multiplicative_inverse(determinant)
        C_inverse = C
        # Swap a <-> d
        C_inverse[0][0], C_inverse[1][1] = C_inverse[1, 1], C_inverse[0, 0]
        # Replace
        C[0][1] *= -1
        C[1][0] *= -1
        for row in range(2):
            for column in range(2):
                C_inverse[row][column] *= multiplicative_inverse
                C_inverse[row][column] = C_inverse[row][column] % 26

        P = create_matrix_of_integers_from_string(encrypted_msg)
        msg_len = int(len(encrypted_msg) / 2)
        decrypted_msg = ""
        for i in range(msg_len):
            # Dot product
            column_0 = P[0][i] * C_inverse[0][0] + P[1][i] * C_inverse[0][1]
            # Modulate and add 65 to get back to the A-Z range in ascii
            integer = int(column_0 % 26 + 65)
            # Change back to chr type and add to text
            decrypted_msg += chr(integer)
            # Repeat for the second column
            column_1 = P[0][i] * C_inverse[1][0] + P[1][i] * C_inverse[1][1]
            integer = int(column_1 % 26 + 65)
            decrypted_msg += chr(integer)
        if decrypted_msg[-1] == "0":
            decrypted_msg = decrypted_msg[:-1]
        self.Plaintext.setText(decrypted_msg)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
