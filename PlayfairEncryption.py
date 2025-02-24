# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PlayfairEncryption.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(709, 491)
        self.encryptbutton = QtWidgets.QPushButton(Dialog)
        self.encryptbutton.setGeometry(QtCore.QRect(300, 290, 111, 41))
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
        self.label.setPixmap(QtGui.QPixmap("img/Playfair.jpeg"))
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
        self.Ciphertext = QtWidgets.QTextBrowser(Dialog)
        self.Ciphertext.setGeometry(QtCore.QRect(100, 380, 521, 41))
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
        self.key = QtWidgets.QLineEdit(Dialog)
        self.key.setGeometry(QtCore.QRect(110, 200, 251, 41))
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
        self.Ciphertext.raise_()
        self.Plaintext.raise_()
        self.key.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.encryptbutton.setText(_translate("Dialog", "Encrypt"))
        self.label_3.setText(_translate("Dialog", "Playfair Cipher"))
        self.label_5.setText(_translate("Dialog", "________________________________________"))
        self.Ciphertext.setPlaceholderText(_translate("Dialog", "The Ciphertext (Result)"))
        self.Plaintext.setPlaceholderText(_translate("Dialog", "Enter the Plaintext:"))
        self.key.setPlaceholderText(_translate("Dialog", "Enter the Key e.g. 'do it'"))

    def Encryption(self):

        key = self.key.text().replace(' ','').upper()
        msg = self.Plaintext.text().replace(' ', '').upper()
        def matrix(x, y, initial):
            return [[initial for i in range(x)] for j in range(y)]

        result = list()
        for c in key:  # storing key
            if c not in result:
                if c == 'J':
                    result.append('I')
                else:
                    result.append(c)
        flag = 0
        for i in range(65, 91):  # storing other character
            if chr(i) not in result:
                if i == 73 and chr(74) not in result:
                    result.append("I")
                    flag = 1
                elif flag == 0 and i == 73 or i == 74:
                    pass
                else:
                    result.append(chr(i))
        k = 0
        my_matrix = matrix(5, 5, 0)  # initialize matrix
        for i in range(0, 5):  # making matrix
            for j in range(0, 5):
                my_matrix[i][j] = result[k]
                k += 1

        def locindex(c):  # get location of each character
            loc = list()
            if c == 'J':
                c = 'I'
            for i, j in enumerate(my_matrix):
                for k, l in enumerate(j):
                    if c == l:
                        loc.append(i)
                        loc.append(k)
                        return loc


        i = 0
        for s in range(0, len(msg) + 1, 2):
            if s < len(msg) - 1:
                if msg[s] == msg[s + 1]:
                    msg = msg[:s + 1] + 'X' + msg[s + 1:]
        if len(msg) % 2 != 0:
            msg = msg[:] + 'X'
        c = ''
        while i < len(msg):
            loc = list()
            loc = locindex(msg[i])
            loc1 = list()
            loc1 = locindex(msg[i + 1])
            if loc[1] == loc1[1]:
                # print("{}{}".format(my_matrix[(loc[0] + 1) % 5][loc[1]], my_matrix[(loc1[0] + 1) % 5][loc1[1]]))
                c += "{}{}".format(my_matrix[(loc[0] + 1) % 5][loc[1]], my_matrix[(loc1[0] + 1) % 5][loc1[1]])
            elif loc[0] == loc1[0]:
                # print("{}{}".format(my_matrix[loc[0]][(loc[1] + 1) % 5], my_matrix[loc1[0]][(loc1[1] + 1) % 5]))
                c += "{}{}".format(my_matrix[loc[0]][(loc[1] + 1) % 5], my_matrix[loc1[0]][(loc1[1] + 1) % 5])
            else:
                # print("{}{}".format(my_matrix[loc[0]][loc1[1]], my_matrix[loc1[0]][loc[1]]))
                c += "{}{}".format(my_matrix[loc[0]][loc1[1]], my_matrix[loc1[0]][loc[1]])
            i = i + 2


        self.Ciphertext.setText(c)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
