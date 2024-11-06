# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_login.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import icons_system_rc as icons_system_rc

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        if not LoginWindow.objectName():
            LoginWindow.setObjectName(u"LoginWindow")
        LoginWindow.resize(584, 571)
        LoginWindow.setStyleSheet(u"background-color: rgb(0, 0,10);")
        self.centralwidget = QWidget(LoginWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QPushButton{\n"
"	\n"
"	QPushButton{color:#fff;}\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:  rgb(255, 255, 255);\n"
" 	color:black\n"
" }\n"
"\n"
"\n"
"QLineEdit{\n"
"	\n"
"	background-color: none;\n"
"\n"
"}\n"
"\n"
"QFrame{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 		rgba(192, 255, 255, 255), stop:1 rgba(0, 77, 113, 255));\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.main_frame = QFrame(self.centralwidget)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setStyleSheet(u"background-color: rgb(0, 80, 121);")
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.main_frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label = QLabel(self.main_frame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"background-color: none;")

        self.verticalLayout_4.addWidget(self.label, 0, Qt.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.frame_2 = QFrame(self.main_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgb(0, 80, 121);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.txt_user = QLineEdit(self.frame_2)
        self.txt_user.setObjectName(u"txt_user")
        self.txt_user.setMinimumSize(QSize(120, 30))
        font1 = QFont()
        font1.setPointSize(10)
        self.txt_user.setFont(font1)
        self.txt_user.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_user.setStyleSheet(u"# QLineEdit {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border: 1px solid rgb(255, 206, 206);\n"
"}")
        self.txt_user.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.txt_user, 0, Qt.AlignHCenter)


        self.verticalLayout_4.addWidget(self.frame_2, 0, Qt.AlignHCenter)

        self.frame_3 = QFrame(self.main_frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"background-color: rgb(0, 80, 121);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_3)

        self.txt_password = QLineEdit(self.frame_3)
        self.txt_password.setObjectName(u"txt_password")
        self.txt_password.setMinimumSize(QSize(120, 30))
        self.txt_password.setFont(font1)
        self.txt_password.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_password.setStyleSheet(u"# QLineEdit {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border: 1px solid rgb(255, 206, 206);\n"
"}")
        self.txt_password.setEchoMode(QLineEdit.Password)
        self.txt_password.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.txt_password, 0, Qt.AlignHCenter)


        self.verticalLayout_4.addWidget(self.frame_3, 0, Qt.AlignHCenter)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.btn_login = QPushButton(self.main_frame)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setMinimumSize(QSize(150, 30))
        font2 = QFont()
        self.btn_login.setFont(font2)
        self.btn_login.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_login.setStyleSheet(u"QPushButton {\n"
"  color: rgb(255, 255, 255);\n"
"  border-radius: 10px;\n"
"  font-size: 16px;\n"
"  background-color: rgb(0, 80, 121);\n"
"  border: 2px solid white; \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #fff;\n"
"  color: black;\n"
"}")

        self.verticalLayout_4.addWidget(self.btn_login, 0, Qt.AlignHCenter)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)


        self.verticalLayout_3.addWidget(self.main_frame)

        LoginWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoginWindow)

        QMetaObject.connectSlotsByName(LoginWindow)
    # setupUi

    def retranslateUi(self, LoginWindow):
        LoginWindow.setWindowTitle(QCoreApplication.translate("LoginWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("LoginWindow", u"<html><head/><body><p align=\"center\"><img src=\":/imgs/_imgs/Login.png\"/></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("LoginWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Usu\u00e1rio</span></p></body></html>", None))
        self.txt_user.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"User", None))
        self.label_3.setText(QCoreApplication.translate("LoginWindow", u"<html><head/><body><p><span style=\" color:#ffffff;\">Senha</span></p></body></html>", None))
        self.txt_password.setPlaceholderText(QCoreApplication.translate("LoginWindow", u"Password", None))
        self.btn_login.setText(QCoreApplication.translate("LoginWindow", u"Login", None))
    # retranslateUi

