
from PyQt5 import QtCore, QtGui, QtWidgets


class GeoCipherD(object):
    def reverseList(self, array):
        for i in range(len(array)):
            if i % 2 != 0:
                array[i].reverse()
        return array

    def fullMatrix(self,array, row, Ciphertext, Key):
        for i in range(len(array)):
            if len(Ciphertext) % Key > 0 and len(array[i]) != row:
                array[i].append('null')
        f = []
        for x in range(row):
            for y in range(Key):
                f.append(array[y][x])

        f2 = []
        i = 0
        while i < len(f):
            f2.append(f[i:i + Key])
            i += Key
        self.reverseList(f2)

        return f2
    def Decrypt(self):
        Ciphertext = self.ciphertext_2.text().upper().replace(' ','')
        Key = int(self.key.text())


        completerow = int(len(Ciphertext) / Key)
        c_row = completerow
        lastrow = len(Ciphertext) % Key
        if lastrow > 0: c_row += 1
        c = c_row
        arr, arr2 = [], []
        for i in range(len(Ciphertext)):
            arr.append(Ciphertext[i])
        i, j, k = 0, 0, 0

        if completerow % 2 == 0 and lastrow > 0:
            while i < lastrow:
                arr2.append(arr[k:c])
                c += c_row
                i += 1
                k += c_row
            c -= c_row
            j = c
            while j < len(Ciphertext):
                c += completerow
                arr2.append(arr[j:c])
                j += completerow
            self.reverseList(arr2)

        elif completerow % 2 != 0 and lastrow > 0:
            while j < Key - lastrow:
                arr2.append(arr[k:k + completerow])
                k += completerow
                j += 1

            while i < lastrow:
                arr2.append(arr[k:k + c_row])
                k += c_row
                i += 1
            self.reverseList(arr2)

        else:
            while i < len(Ciphertext):
                arr2.append(arr[i:i + completerow])
                i += completerow
            self.reverseList(arr2)

        fM = self.fullMatrix(arr2, c_row, Ciphertext, Key)
        Plaintext = ''.join([ele for sub in fM for ele in sub if ele != 'null'])
        self.plaintext.setText(Plaintext)


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
        self.label_3.setText(_translate("Dialog", "Geometric Cipher"))
        self.label_5.setText(_translate("Dialog", "___________________________________________"))
        self.plaintext.setPlaceholderText(_translate("Dialog", "The Plaintext (Result)"))
        self.ciphertext_2.setPlaceholderText(_translate("Dialog", "Enter the Ciphertext:"))
        self.key.setPlaceholderText(_translate("Dialog", "Enter the Key number"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = GeoCipherD()
    ui.setupUi( MainWindow )
    MainWindow.show()
    sys.exit(app.exec_())