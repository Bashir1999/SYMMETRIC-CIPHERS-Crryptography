
from PyQt5 import QtCore, QtGui, QtWidgets
import CaesarCEnc
import CaesarCD
import AtbashCipher
import AtbashCipherDec
import Affine
import AffineD
import ROT13Enc
import ROT13Dec
import NullCipherDec
import ReverseOEn
import ReverseODen
import GeoCipherEnc
import GeoCipherDec
import RailFE
import RailFD
import TwoSENew
import TwoSDN
import FourSE
import FourSD
import ADFGXE
import ADFGXD
import ADFGVXE
import ADFGVXD
import DESEnc
import DESDes
import AESEnc
import FeistelCipherEnc
import NullCipherN
import PolybiusEncryption
import PolybiusDecryption
import VigenereEncryption
import VigenereDecryption
import ColumnEncryption
import ColumnDecryption
import PlayfairEncryption
import PlayfairDecryption
import HillEncryption
import HillDecryption
import BifidEncryption
import BifidDecryption
import AESEnc
import AESDec

class MainMenuP1(object):
    def OpenWindow(self, Page, className):
        self.window = QtWidgets.QMainWindow()
        self.Open = className()
        self.Open.setupUi(self.window)
        self.window.show()

    def EncryptBAction(self):
        if (self.chooseCipher.currentText() == "Caesar Cipher"):
            self.OpenWindow(CaesarCEnc, CaesarCEnc.CaesarCipher)
        elif (self.chooseCipher.currentText() == "Atbash Cipher"):
            self.OpenWindow(AtbashCipher, AtbashCipher.AtbashC)
        elif (self.chooseCipher.currentText() == "Affine Cipher"):
            self.OpenWindow(Affine, Affine.AffineEnc)
        elif (self.chooseCipher.currentText() == "ROT 13 Cipher"):
            self.OpenWindow(ROT13Enc, ROT13Enc.ROT13En)
        elif (self.chooseCipher.currentText() == "Reverse Order Cipher"):
            self.OpenWindow(ReverseOEn, ReverseOEn.ReverseOrderEn)
        elif (self.chooseCipher.currentText() == "Geometric Cipher"):
            self.OpenWindow(GeoCipherEnc, GeoCipherEnc.GeoE)
        elif (self.chooseCipher.currentText() == "Rail Fence Cipher"):
            self.OpenWindow(RailFE, RailFE.RailFEn)
        elif (self.chooseCipher.currentText() == "Two-Square Cipher"):
            self.OpenWindow(TwoSENew, TwoSENew.TwoSENew)
        elif (self.chooseCipher.currentText() == "Four-Square Cipher"):
            self.OpenWindow(FourSE, FourSE.FourSqE)
        elif (self.chooseCipher.currentText() == "ADFGX Cipher"):
            self.OpenWindow(ADFGXE, ADFGXE.ADFGXEnc)
        elif (self.chooseCipher.currentText() == "ADFGVX Cipher"):
            self.OpenWindow(ADFGVXE, ADFGVXE.ADFGVXCipherEnc)
        elif (self.chooseCipher.currentText() == "DES"):
            self.OpenWindow(DESEnc, DESEnc.DESEn)
        elif (self.chooseCipher.currentText() == "AES"):
            self.OpenWindow(AESEnc, AESEnc.AESEn)
        elif (self.chooseCipher.currentText() == "Feistel Cipher"):
            self.OpenWindow(FeistelCipherEnc, FeistelCipherEnc.FeistelEnc)
        elif (self.chooseCipher.currentText() == "Null Cipher"):
            self.OpenWindow(NullCipherN, NullCipherN.NullCEnc)
        elif (self.chooseCipher.currentText() == "Polybius Cipher"):
            self.OpenWindow(PolybiusEncryption, PolybiusEncryption.Ui_MainWindow)
        elif (self.chooseCipher.currentText() == "Vigenere Cipher"):
            self.OpenWindow(VigenereEncryption, VigenereEncryption.Ui_MainWindow)

        elif (self.chooseCipher.currentText() == "Columnar Cipher"):
            self.OpenWindow(ColumnEncryption, ColumnEncryption.Ui_MainWindow)
        elif (self.chooseCipher.currentText() == "Playfair Cipher"):
            self.OpenWindow(PlayfairEncryption, PlayfairEncryption.Ui_MainWindow)
        elif (self.chooseCipher.currentText() == "Hill Cipher"):
            self.OpenWindow(HillEncryption, HillEncryption.Ui_MainWindow)
        elif (self.chooseCipher.currentText() == "Bifid Cipher"):
            self.OpenWindow(BifidEncryption, BifidEncryption.Ui_MainWindow)
        elif (self.chooseCipher.currentText() == "AES"):
            self.OpenWindow(AESEnc, AESEnc.Ui_Dialog)

    def DecryptBAction(self):
        if (self.chooseCipher.currentText() == "Caesar Cipher"):
            self.OpenWindow(CaesarCD, CaesarCD.CaesarD)

        elif (self.chooseCipher.currentText() == "Atbash Cipher"):
            self.OpenWindow(AtbashCipherDec, AtbashCipherDec.Atbash)
        elif (self.chooseCipher.currentText() == "Affine Cipher"):
            self.OpenWindow(AffineD, AffineD.AffineDecr)
        elif (self.chooseCipher.currentText() == "ROT 13 Cipher"):
            self.OpenWindow(ROT13Dec, ROT13Dec.ROT13D)
        elif (self.chooseCipher.currentText() == "Null Cipher"):
            self.OpenWindow(NullCipherDec, NullCipherDec.NullCipherD)
        elif (self.chooseCipher.currentText() == "Reverse Order Cipher"):
            self.OpenWindow(ReverseODen, ReverseODen.ReverseOD)
        elif (self.chooseCipher.currentText() == "Geometric Cipher"):
            self.OpenWindow(GeoCipherDec, GeoCipherDec.GeoCipherD)
        elif (self.chooseCipher.currentText() == "Rail Fence Cipher"):
            self.OpenWindow(RailFD, RailFD.RailFDec)
        elif (self.chooseCipher.currentText() == "Two-Square Cipher"):
            self.OpenWindow(TwoSDN, TwoSDN.TwoSD)
        elif (self.chooseCipher.currentText() == "Four-Square Cipher"):
            self.OpenWindow(FourSD, FourSD.FourSqD)
        elif (self.chooseCipher.currentText() == "ADFGX Cipher"):
            self.OpenWindow(ADFGXD, ADFGXD.ADFGXDec)
        elif (self.chooseCipher.currentText() == "ADFGVX Cipher"):
            self.OpenWindow(ADFGVXD, ADFGVXD.ADFGVXDec)
        elif (self.chooseCipher.currentText() == "DES"):
            self.OpenWindow(DESDes, DESDes.DESDecr)
        elif (self.chooseCipher.currentText() == "Polybius Cipher"):
            self.OpenWindow(PolybiusDecryption, PolybiusDecryption.Ui_MainWindow)
        elif (self.chooseCipher.currentText() == "Vigenere Cipher"):
            self.OpenWindow(VigenereDecryption, VigenereDecryption.Ui_MainWindow)
        elif (self.chooseCipher.currentText() == "Columnar Cipher"):
            self.OpenWindow(ColumnDecryption, ColumnDecryption.Ui_MainWindow)
        elif (self.chooseCipher.currentText() == "Playfair Cipher"):
            self.OpenWindow(PlayfairDecryption, PlayfairDecryption.Ui_MainWindow)
        elif (self.chooseCipher.currentText() == "Hill Cipher"):
            self.OpenWindow(HillDecryption, HillDecryption.Ui_MainWindow)
        elif (self.chooseCipher.currentText() == "Bifid Cipher"):
            self.OpenWindow(BifidDecryption, BifidDecryption.Ui_MainWindow)
        elif (self.chooseCipher.currentText() == "AES"):
            self.OpenWindow(AESDec, AESDec.Ui_Dialog)
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(661, 520)
        self.encryptionB = QtWidgets.QPushButton(Dialog)
        self.encryptionB.setGeometry(QtCore.QRect(170, 390, 131, 51))
        self.encryptionB.setStyleSheet("QPushButton {\n"
"  padding: 15px 25px;\n"
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
        self.encryptionB.setObjectName("encryptionB")
        self.encryptionB.clicked.connect(self.EncryptBAction)
        self.decryptionB = QtWidgets.QPushButton(Dialog)
        self.decryptionB.setGeometry(QtCore.QRect(390, 390, 131, 51))
        self.decryptionB.setStyleSheet("QPushButton {\n"
"  padding: 15px 25px;\n"
"  text-align: center;\n"
"  outline: none;\n"
"  color: #fff;\n"
"  background-color:     #008000;\n"
"  border: none;\n"
"  border-radius: 15px;\n"
"font: 15pt \"Rockwell\";\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #006400;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.decryptionB.setObjectName("decryptionB")
        self.decryptionB.clicked.connect(self.DecryptBAction)
        self.chooseCipher = QtWidgets.QComboBox(Dialog)
        self.chooseCipher.setGeometry(QtCore.QRect(210, 260, 261, 41))
        self.chooseCipher.setStyleSheet("QComboBox{\n"
"font: 14pt \"Futura\";\n"
"width: 200%;\n"
"  min-width: 30ch;\n"
"  border: 1px solid var(--select-border);\n"
"  border-radius: 0.25em;\n"
"  padding: 0.25em 0.5em;\n"
"  line-height: 1.1;\n"
"  background-color: #228B22;\n" #228B22
" color: #002600; \n"
"  border: none;\n"
"}\n"
"\n"
"    ")
        self.chooseCipher.setObjectName("chooseCipher")
        self.chooseCipher.addItem("")
        self.chooseCipher.addItem("")
        self.chooseCipher.addItem("")
        self.chooseCipher.addItem("")
        self.chooseCipher.addItem("")
        self.chooseCipher.addItem("")
        self.chooseCipher.addItem("")
        self.chooseCipher.addItem("")
        self.chooseCipher.addItem("")
        self.chooseCipher.addItem("")
        self.chooseCipher.addItem("")
        self.chooseCipher.addItem("")
        self.chooseCipher.addItem("")
        self.chooseCipher.addItem("")
        self.chooseCipher.addItem("")
        self.chooseCipher.addItem("")
        self.chooseCipher.addItem("")
        self.chooseCipher.addItem("")
        self.chooseCipher.addItem("")
        self.chooseCipher.addItem("")
        self.chooseCipher.addItem("")

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 661, 521))
        self.label.setStyleSheet("")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Backg.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(200, 60, 60, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(240, 30, 231, 121))
        self.label_3.setStyleSheet("color: rgb(253, 250, 255);\n"
"font: 40pt \"Futura\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(170, 200, 371, 31))
        self.label_4.setStyleSheet("color: rgb(253, 250, 255);\n"
"\n"
"font: 15pt \"Rockwell\";\n"
"")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(240, 90, 211, 51))
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(170, 200, 351, 51))
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.label.raise_()
        self.encryptionB.raise_()
        self.decryptionB.raise_()
        self.chooseCipher.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.encryptionB.setText(_translate("Dialog", "Encryption"))
        self.decryptionB.setText(_translate("Dialog", "Decryption"))
        self.chooseCipher.setItemText(0, _translate("Dialog", "Caesar Cipher"))
        self.chooseCipher.setItemText(1, _translate("Dialog", "Atbash Cipher"))
        self.chooseCipher.setItemText(2, _translate("Dialog", "Affine Cipher"))
        self.chooseCipher.setItemText(3, _translate("Dialog", "ROT 13 Cipher"))
        self.chooseCipher.setItemText(4, _translate("Dialog", "Polybius Cipher"))
        self.chooseCipher.setItemText(5, _translate("Dialog", "Null Cipher"))
        self.chooseCipher.setItemText(6, _translate("Dialog", "Vigenere Cipher"))
        self.chooseCipher.setItemText(7, _translate("Dialog", "Reverse Order Cipher"))
        self.chooseCipher.setItemText(8, _translate("Dialog", "Geometric Cipher"))
        self.chooseCipher.setItemText(9, _translate("Dialog", "Rail Fence Cipher"))
        self.chooseCipher.setItemText(10, _translate("Dialog", "Columnar Cipher"))
        self.chooseCipher.setItemText(11, _translate("Dialog", "Playfair Cipher"))
        self.chooseCipher.setItemText(12, _translate("Dialog", "Two-Square Cipher"))
        self.chooseCipher.setItemText(13, _translate("Dialog", "Four-Square Cipher"))
        self.chooseCipher.setItemText(14, _translate("Dialog", "Hill Cipher"))
        self.chooseCipher.setItemText(15, _translate("Dialog", "ADFGX Cipher"))
        self.chooseCipher.setItemText(16, _translate("Dialog", "ADFGVX Cipher"))
        self.chooseCipher.setItemText(17, _translate("Dialog", "Bifid Cipher"))
        self.chooseCipher.setItemText(18, _translate("Dialog", "Feistel Cipher"))
        self.chooseCipher.setItemText(19, _translate("Dialog", "DES"))
        self.chooseCipher.setItemText(20, _translate("Dialog", "AES"))
        self.label_2.setText(_translate("Dialog", "TextLabel"))
        self.label_3.setText(_translate("Dialog", "WELCOME"))
        self.label_4.setText(_translate("Dialog", "Choose the cipher you want to encrypt/decrypt"))
        self.label_5.setText(_translate("Dialog", "__________________________________"))
        self.label_6.setText(_translate("Dialog", "____________________________________________________________"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MainMenuP1()
    ui.setupUi( MainWindow )
    MainWindow.show()
    sys.exit(app.exec_())
