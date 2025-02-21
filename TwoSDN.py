
from PyQt5 import QtCore, QtGui, QtWidgets

class TwoSD(object):
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

    def DivideIntoTwoL(self,Letters):
        Letter = list(Letters.strip())
        temp, final = [], []
        count = 1
        for i in range(len(Letter)):
            temp.append(Letter[i])

            if count % 2 == 0:
                final.append(temp.copy())
                temp.clear()
            count += 1
        return final

    def Decrypt(self):
        Ciphertext = self.Ciphertext.text().upper().replace(' ','')
        ciphertext = self.DivideIntoTwoL(Ciphertext)
        key1 = self.FirstKey.text().upper().replace(' ','')
        key2 = self.SecondKey.text().upper().replace(' ', '')
        plainText = ''
        keyAlph1 = []
        keyAlph2 = []

        Matrix1 = self.square(key1, keyAlph1)
        Matrix2 = self.square(key2, keyAlph2)
        for i in range(0, len(ciphertext)):
            firstletter = []
            secondletter = []

            firstletter.extend(self.findIndex(Matrix2, ciphertext[i][0]))
            secondletter.extend(self.findIndex(Matrix1, ciphertext[i][1]))

            if firstletter[0] != secondletter[0]:  # if first letter and second letter are in different columns and rows
                plainText += Matrix1[firstletter[0]][secondletter[1]] + Matrix2[secondletter[0]][firstletter[1]]


            elif firstletter[0] == secondletter[0]:  # if first letter and second letter are in the same row
                plainText += Matrix1[secondletter[0]][secondletter[1]] + Matrix2[firstletter[0]][firstletter[1]]
        p = ''
        for i in plainText:
            if i != 'X':
                p+=i

        self.plaintext.setText(p)
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
        self.label.setPixmap(QtGui.QPixmap("Backg.png"))
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
        self.label.raise_()
        self.decryptbutton.raise_()
        self.label_3.raise_()
        self.label_5.raise_()
        self.plaintext.raise_()
        self.FirstKey.raise_()
        self.SecondKey.raise_()
        self.Ciphertext.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.decryptbutton.setText(_translate("Dialog", "Decrypt"))
        self.label_3.setText(_translate("Dialog", "Two Square Cipher"))
        self.label_5.setText(_translate("Dialog", "________________________________________________"))
        self.plaintext.setPlaceholderText(_translate("Dialog", "The Plaintext (Result)"))
        self.FirstKey.setPlaceholderText(_translate("Dialog", "Enter the First Key"))
        self.SecondKey.setPlaceholderText(_translate("Dialog", "Enter the Second Key"))
        self.Ciphertext.setPlaceholderText(_translate("Dialog", "Enter the Ciphertext"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = TwoSD()
    ui.setupUi( MainWindow )
    MainWindow.show()
    sys.exit(app.exec_())