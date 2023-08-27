import sys
import os
import sqlite3
import image_rc


from PyQt5 import QtCore, QtGui, QtWidgets
from register import RegisterApp
from forgotpass import ForgotApp
from window import MainWindow

class LoginWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.connect_db()
        self.init_ui()
        self.load_remembered_user()

    def connect_db(self):
        self.database_connect = sqlite3.connect("üyeler.db")
        self.cursor = self.database_connect.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS üyeler (Üye TEXT, Şifre TEXT)")
        self.database_connect.commit()

    def init_ui(self):
        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(30, 10, 841, 571))
        self.frame.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.frame.setStyleSheet("\n"
"background-color: rgb(70, 54, 67);\n"
"border-bottom-right-radius:50px;\n"
"border-top-left-radius:50px\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)

        self.username = QtWidgets.QLineEdit(self.frame)
        self.username.setGeometry(QtCore.QRect(520, 200, 251, 31))
        self.username.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.username.setStyleSheet("background:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(255,255,255,255);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;\n"
"color:rgb(255, 255, 255)")
        self.username.setMaxLength(10)
        self.username.setText("")
        self.username.setPlaceholderText(" Username                                                          ❔")
        
        self.password = QtWidgets.QLineEdit(self.frame)
        self.password.setGeometry(QtCore.QRect(520, 280, 261, 31))
        self.password.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.password.setStyleSheet("background:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(255,255,255,255);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;\n"
"color:rgb(255, 255, 255)")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setMaxLength(7)
        self.password.setText("")
        self.password.setPlaceholderText(" Password                                                           ❔")

        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 441, 641))
        self.frame_2.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.frame_2.setStyleSheet("background-image: url(:/image/sehemnyarragun.png);\n"
"border-top-left-radius:50px")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)

        self.loginbutton = QtWidgets.QPushButton(self.frame)
        self.loginbutton.setGeometry(QtCore.QRect(540, 360, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Nyala")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.loginbutton.setFont(font)
        self.loginbutton.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.loginbutton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-bottom-right-radius:7px;\n"
"border-top-left-radius:7px;")
        
        self.loginbutton.setText("Login")

        self.textlogin = QtWidgets.QLabel(self.frame)
        self.textlogin.setGeometry(QtCore.QRect(590, 100, 131, 61))
        font = QtGui.QFont()
        font.setFamily("Nyala")
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.textlogin.setFont(font)
        self.textlogin.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.textlogin.setStyleSheet("color:rgb(255, 255, 255)")
        self.textlogin.setText("Login")

        self.forgotpass = QtWidgets.QPushButton(self.frame)
        self.forgotpass.setGeometry(QtCore.QRect(470, 520, 111, 23))
        self.forgotpass.setStyleSheet("color:rgb(255, 255, 255)")

        self.forgotpass.setText("Forgot Your Password?")

        self.register_2 = QtWidgets.QPushButton(self.frame)
        self.register_2.setGeometry(QtCore.QRect(770, 520, 51, 23))
        self.register_2.setStyleSheet("color:rgb(255, 255, 255)")

        self.register_2.setText("Register?")

        self.rememberme = QtWidgets.QRadioButton(self.frame)
        self.rememberme.setGeometry(QtCore.QRect(520, 330, 101, 17))
        self.rememberme.setStyleSheet("color:rgb(255, 255, 255);\n"
"\n"
"")
        self.rememberme.setText("Remember Me!")


        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setWindowTitle("(_SHM_)LoginScreenV3")

        self.resize(915,600)
        self.setMaximumSize(915,600)


        
        self.loginbutton.clicked.connect(self.loginn)
        self.register_2.clicked.connect(self.registerr)
        self.forgotpass.clicked.connect(self.forgotpasss)
        self.rememberme.clicked.connect(self.rememberr)
        self.show()






    def loginn(self):
        ka = self.username.text()
        par = self.password.text()

        self.cursor.execute("SELECT * FROM üyeler WHERE Üye = ? AND Şifre = ?", (ka, par))
        data = self.cursor.fetchall()

        if len(data) == 0:
            print("Not Found User!")
            self.username.clear()
            self.password.clear()
        else:
                self.close()
                self.new_window = MainWindow()
                self.new_window.show()

    def registerr(self):
        self.new_window2 = RegisterApp()
        self.new_window2.show()
     
    def forgotpasss(self):
        self.new_window3 = ForgotApp()
        self.new_window3.show()

    def rememberr(self):
        if self.rememberme.isChecked():
            ka = self.username.text()
            par = self.password.text()

            with open("remembered_user.txt", "w") as file:
                file.write(f"{ka}\n{par}")
        else:
            try:
                os.remove("remembered_user.txt")
            except FileNotFoundError:
                pass

    def load_remembered_user(self):
        try:
            with open("remembered_user.txt", "r") as file:
                ka, par = file.read().splitlines()
                self.username.setText(ka)
                self.password.setText(par)
                self.rememberme.setChecked(True)
        except FileNotFoundError:
            pass





if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    login_window = LoginWindow()
    sys.exit(app.exec())