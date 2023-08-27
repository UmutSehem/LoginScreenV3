import sys
import sqlite3
import image_rc

from PyQt5 import QtCore, QtGui, QtWidgets

class ForgotApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.connect_db()
        self.init_ui()

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
        self.username.setPlaceholderText(" Username                                                             ❔")
        
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
        self.password.setPlaceholderText(" Password                                                                ❔")

        self.conf_password = QtWidgets.QLineEdit(self.frame)
        self.conf_password.setGeometry(QtCore.QRect(520, 350, 261, 31))
        self.conf_password.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.conf_password.setStyleSheet("background:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(255,255,255,255);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;\n"
"color:rgb(255, 255, 255)")
        self.conf_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.conf_password.setMaxLength(7)
        self.conf_password.setText("")
        self.conf_password.setPlaceholderText(" New Password                                                        ❔")

        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 441, 641))
        self.frame_2.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.frame_2.setStyleSheet("background-image: url(:/image/sehemnyarragun.png);\n"
"border-top-left-radius:50px")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)

        self.forgotpass = QtWidgets.QPushButton(self.frame)
        self.forgotpass.setGeometry(QtCore.QRect(540, 410, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Nyala")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.forgotpass.setFont(font)
        self.forgotpass.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.forgotpass.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-bottom-right-radius:7px;\n"
"border-top-left-radius:7px;")
        
        
        self.forgotpass.setText("Reset Password")

        self.textlogin = QtWidgets.QLabel(self.frame)
        self.textlogin.setGeometry(QtCore.QRect(540, 70, 250, 90))
        font = QtGui.QFont()
        font.setFamily("Nyala")
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.textlogin.setFont(font)
        self.textlogin.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.textlogin.setStyleSheet("color:rgb(255, 255, 255)")
        self.textlogin.setText("Forgot Your \n  Password")



        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setWindowTitle("(_SHM_)Forgot Your Password?")
        

        self.resize(915,600)
        self.setMaximumSize(915,600)
        
        self.forgotpass.clicked.connect(self.forgotpasss)

        self.show()

    def forgotpasss(self):
        id = self.username.text()
        old_password = self.password.text()
        new_password = self.conf_password.text()
        if not id or not old_password or not new_password:
            print("Please fill in all fields.")
            return
        else:
            self.cursor.execute("SELECT * FROM üyeler WHERE Üye = ? AND Şifre = ?", (id, old_password))
            existing_user = self.cursor.fetchone()
            if existing_user:
                if existing_user[0] == id or old_password:  
                    self.cursor.execute("UPDATE üyeler SET Şifre = ? WHERE Üye = ?", (new_password, id))
                    self.database_connect.commit()
                    print("Password Reset Successful!")
                    self.close()
                else:
                    print("Old Password Incorrect!")
                    self.password.clear()
                    self.conf_password.clear()
            else:
                print("User not found!")
                self.username.clear()
                self.password.clear()
                self.conf_password.clear()
            



