
from PyQt5 import QtCore, QtGui, QtWidgets


class FourSqE(object):
    def findIndex(self, Square, letters):
        for i, x in enumerate(Square):
            if letters in x:
                return [i, x.index(letters)]
    def square(self, key, keyAlph):
        alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                     'V', 'W', 'X', 'Y', 'Z']
        fill = [['null' for x in range(5)]
                for y in range(5)]

        [keyAlph.append(x) for x in key if x not in keyAlph]
        [keyAlph.append(x) for x in alphabets if x not in keyAlph]

        index = 0
        for i in range(5):
            for j in range(5):
                if index < len(keyAlph):
                    fill[i][j] = keyAlph[index]
                    index += 1
        return fill

    def ConvertingPlainText(self, message):
        # converting to list
        plaintext = list(message.strip())
        temp1, temp2, converted = [], [], []
        index, count, i = 1, 1, 0
        # add another duplicate of letter if there are duplicates in each two
        while i < len(plaintext) - 1:
            if plaintext[i] == plaintext[index]:
                plaintext.insert(i, plaintext[i])

            if index + 1 < len(plaintext):
                i += 2
                index += 2
            else:
                break
        # add X at the end if the plaintext is odd
        if len(plaintext) % 2 != 0:
            plaintext.append('X')
        # check only two letters at a time and if the letters are the same, add X instead of the duplicated letter
        for i in range(len(plaintext)):
            temp1.append(plaintext[i])

            if count % 2 == 0:

                for i in range(len(temp1)):
                    if temp1[i] not in temp2:
                        temp2.append(temp1[i])
                    elif temp1[i] in temp2:
                        temp2.append('X')

                converted.append(temp2.copy())
                temp2.clear()
                temp1.clear()
            count += 1

        ##
        return converted
    def Encrypt(self):
        Alphabets = [['A', 'B', 'C', 'D', 'E'], ['F', 'G', 'H', 'I', 'K'], ['L', 'M', 'N', 'O', 'P'],
                     ['Q', 'R', 'S', 'T', 'U'], ['V', 'W', 'X', 'Y', 'Z']]
        PlainText = self.Plaintext.text().upper().replace(' ','')
        plainText = self.ConvertingPlainText(PlainText)
        key1 = self.FirstKey.text().upper().replace(' ', '')
        key2 = self.SecondKey.text().upper().replace(' ', '')
        keyAlph1=[]
        keyAlph2 = []
        cipherText = ''
        Matrix1 = self.square(key1, keyAlph1)
        Matrix2 = self.square(key2, keyAlph2)
        for i in range(0, len(plainText)):
            firstletter = []
            secondletter = []

            firstletter.extend(self.findIndex(Alphabets, plainText[i][0]))
            secondletter.extend(self.findIndex(Alphabets, plainText[i][1]))

            cipherText += Matrix1[firstletter[0]][secondletter[1]] + Matrix2[secondletter[0]][firstletter[1]]

        self.ciphertext.setText(cipherText)

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
        self.label.setPixmap(QtGui.QPixmap("img/End.jpeg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(210, 40, 301, 51))
        self.label_3.setStyleSheet("color: rgb(253, 250, 255);\n"
"font: 30pt \"Rockwell\";")
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(220, 50, 291, 51))
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
        self.label_3.setText(_translate("Dialog", "Four Square Cipher"))
        self.label_5.setText(_translate("Dialog", "________________________________________________"))
        self.ciphertext.setPlaceholderText(_translate("Dialog", "The Ciphertext (Result)"))
        self.FirstKey.setPlaceholderText(_translate("Dialog", "Enter the First Key"))
        self.SecondKey.setPlaceholderText(_translate("Dialog", "Enter the Second Key"))
        self.Plaintext.setPlaceholderText(_translate("Dialog", "Enter the Plaintext:"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = FourSqE()
    ui.setupUi( MainWindow )
    MainWindow.show()
    sys.exit(app.exec_())