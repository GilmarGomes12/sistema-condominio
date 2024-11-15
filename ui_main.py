# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_system.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QStackedWidget, QTabWidget, QTableWidget,
    QTableWidgetItem, QTextEdit, QVBoxLayout, QWidget)
import icons_system_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1009, 814)
        MainWindow.setStyleSheet(u"background-color: rgb(0, 0,10);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.left_frame = QFrame(self.centralwidget)
        self.left_frame.setObjectName(u"left_frame")
        self.left_frame.setStyleSheet(u" background-color: rgb(0, 80, 121);")
        self.left_frame.setFrameShape(QFrame.StyledPanel)
        self.left_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.left_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.title_frame = QFrame(self.left_frame)
        self.title_frame.setObjectName(u"title_frame")
        self.title_frame.setFrameShape(QFrame.StyledPanel)
        self.title_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.title_frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.title_frame)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)


        self.verticalLayout_2.addWidget(self.title_frame)

        self.buttons_frame = QFrame(self.left_frame)
        self.buttons_frame.setObjectName(u"buttons_frame")
        self.buttons_frame.setFrameShape(QFrame.StyledPanel)
        self.buttons_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.buttons_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btn_home = QPushButton(self.buttons_frame)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMinimumSize(QSize(120, 30))
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_home.setStyleSheet(u"QPushButton{color:#fff;}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:  rgb(135,206,235);\n"
" 	color:black\n"
" }")

        self.verticalLayout_3.addWidget(self.btn_home)

        self.btn_menu_moradores = QPushButton(self.buttons_frame)
        self.btn_menu_moradores.setObjectName(u"btn_menu_moradores")
        self.btn_menu_moradores.setMinimumSize(QSize(120, 30))
        self.btn_menu_moradores.setFont(font)
        self.btn_menu_moradores.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_menu_moradores.setStyleSheet(u"QPushButton{color:#fff;}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:  rgb(135,206,235);\n"
" 	color:black\n"
" }")

        self.verticalLayout_3.addWidget(self.btn_menu_moradores)

        self.btn_menu_agendamentos = QPushButton(self.buttons_frame)
        self.btn_menu_agendamentos.setObjectName(u"btn_menu_agendamentos")
        self.btn_menu_agendamentos.setMinimumSize(QSize(120, 30))
        self.btn_menu_agendamentos.setFont(font)
        self.btn_menu_agendamentos.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_menu_agendamentos.setStyleSheet(u"QPushButton{color:#fff;}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:  rgb(135,206,235);\n"
" 	color:black\n"
" }")

        self.verticalLayout_3.addWidget(self.btn_menu_agendamentos)

        self.btn_menu_visitantes = QPushButton(self.buttons_frame)
        self.btn_menu_visitantes.setObjectName(u"btn_menu_visitantes")
        self.btn_menu_visitantes.setMinimumSize(QSize(120, 30))
        self.btn_menu_visitantes.setFont(font)
        self.btn_menu_visitantes.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_menu_visitantes.setStyleSheet(u"QPushButton{color:#fff;}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:  rgb(135,206,235);\n"
" 	color:black\n"
" }")

        self.verticalLayout_3.addWidget(self.btn_menu_visitantes)

        self.btn_menu_prestadores = QPushButton(self.buttons_frame)
        self.btn_menu_prestadores.setObjectName(u"btn_menu_prestadores")
        self.btn_menu_prestadores.setMinimumSize(QSize(120, 30))
        self.btn_menu_prestadores.setFont(font)
        self.btn_menu_prestadores.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_menu_prestadores.setStyleSheet(u"QPushButton{color:#fff;}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:  rgb(135,206,235);\n"
" 	color:black\n"
" }")

        self.verticalLayout_3.addWidget(self.btn_menu_prestadores)

        self.btn_menu_encomendas = QPushButton(self.buttons_frame)
        self.btn_menu_encomendas.setObjectName(u"btn_menu_encomendas")
        self.btn_menu_encomendas.setMinimumSize(QSize(120, 30))
        self.btn_menu_encomendas.setFont(font)
        self.btn_menu_encomendas.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_menu_encomendas.setStyleSheet(u"QPushButton{color:#fff;}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:  rgb(135,206,235);\n"
" 	color:black\n"
" }")

        self.verticalLayout_3.addWidget(self.btn_menu_encomendas)

        self.btn_menu_ocorrencias = QPushButton(self.buttons_frame)
        self.btn_menu_ocorrencias.setObjectName(u"btn_menu_ocorrencias")
        self.btn_menu_ocorrencias.setMinimumSize(QSize(120, 30))
        self.btn_menu_ocorrencias.setFont(font)
        self.btn_menu_ocorrencias.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_menu_ocorrencias.setStyleSheet(u"QPushButton{color:#fff;}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:  rgb(135,206,235);\n"
" 	color:black\n"
" }")

        self.verticalLayout_3.addWidget(self.btn_menu_ocorrencias)

        self.btn_menu_funcionarios = QPushButton(self.buttons_frame)
        self.btn_menu_funcionarios.setObjectName(u"btn_menu_funcionarios")
        self.btn_menu_funcionarios.setMinimumSize(QSize(120, 30))
        self.btn_menu_funcionarios.setFont(font)
        self.btn_menu_funcionarios.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_menu_funcionarios.setStyleSheet(u"QPushButton{color:#fff;}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:  rgb(135,206,235);\n"
" 	color:black\n"
" }")

        self.verticalLayout_3.addWidget(self.btn_menu_funcionarios)

        self.btn_menu_domesticos = QPushButton(self.buttons_frame)
        self.btn_menu_domesticos.setObjectName(u"btn_menu_domesticos")
        self.btn_menu_domesticos.setMinimumSize(QSize(120, 30))
        self.btn_menu_domesticos.setFont(font)
        self.btn_menu_domesticos.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_menu_domesticos.setStyleSheet(u"QPushButton{color:#fff;}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:  rgb(135,206,235);\n"
" 	color:black\n"
" }")

        self.verticalLayout_3.addWidget(self.btn_menu_domesticos)

        self.btn_menu_mudancas = QPushButton(self.buttons_frame)
        self.btn_menu_mudancas.setObjectName(u"btn_menu_mudancas")
        self.btn_menu_mudancas.setMinimumSize(QSize(120, 30))
        self.btn_menu_mudancas.setFont(font)
        self.btn_menu_mudancas.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_menu_mudancas.setStyleSheet(u"QPushButton{color:#fff;}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:  rgb(135,206,235);\n"
" 	color:black\n"
" }")

        self.verticalLayout_3.addWidget(self.btn_menu_mudancas)

        self.btn_menu_sobre = QPushButton(self.buttons_frame)
        self.btn_menu_sobre.setObjectName(u"btn_menu_sobre")
        self.btn_menu_sobre.setMinimumSize(QSize(120, 30))
        self.btn_menu_sobre.setFont(font)
        self.btn_menu_sobre.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_menu_sobre.setStyleSheet(u"QPushButton{color:#fff;}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:  rgb(135,206,235);\n"
" 	color:black\n"
" }")

        self.verticalLayout_3.addWidget(self.btn_menu_sobre)

        self.btn_menu_contatos = QPushButton(self.buttons_frame)
        self.btn_menu_contatos.setObjectName(u"btn_menu_contatos")
        self.btn_menu_contatos.setMinimumSize(QSize(120, 30))
        self.btn_menu_contatos.setFont(font)
        self.btn_menu_contatos.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_menu_contatos.setStyleSheet(u"QPushButton{color:#fff;}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:  rgb(135,206,235);\n"
" 	color:black\n"
" }")

        self.verticalLayout_3.addWidget(self.btn_menu_contatos)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.label_4 = QLabel(self.buttons_frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u" background-color: rgb(0, 80, 121);")

        self.verticalLayout_3.addWidget(self.label_4)


        self.verticalLayout_2.addWidget(self.buttons_frame)


        self.horizontalLayout.addWidget(self.left_frame)

        self.main_container = QFrame(self.centralwidget)
        self.main_container.setObjectName(u"main_container")
        self.main_container.setStyleSheet(u" background-color: rgb(0, 80, 121);")
        self.main_container.setFrameShape(QFrame.StyledPanel)
        self.main_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.main_container)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.top_frame = QFrame(self.main_container)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.top_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.toogle_Button = QPushButton(self.top_frame)
        self.toogle_Button.setObjectName(u"toogle_Button")
        self.toogle_Button.setStyleSheet(u"QPushButton{\n"
"	color:#D3D3D3;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:  rgb(135,206,235);\n"
" 	color:black\n"
" }")
        icon = QIcon()
        icon.addFile(u"_imgs/menu.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.toogle_Button.setIcon(icon)
        self.toogle_Button.setIconSize(QSize(32, 32))

        self.horizontalLayout_3.addWidget(self.toogle_Button)

        self.label = QLabel(self.top_frame)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet(u" background-color: rgb(0, 80, 121);")

        self.horizontalLayout_3.addWidget(self.label)


        self.verticalLayout.addWidget(self.top_frame)

        self.main_frame = QFrame(self.main_container)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_74 = QVBoxLayout(self.main_frame)
        self.verticalLayout_74.setObjectName(u"verticalLayout_74")
        self.Pages = QStackedWidget(self.main_frame)
        self.Pages.setObjectName(u"Pages")
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.verticalLayout_5 = QVBoxLayout(self.pg_home)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.lbl_logo = QLabel(self.pg_home)
        self.lbl_logo.setObjectName(u"lbl_logo")
        self.lbl_logo.setStyleSheet(u" background-color: rgb(0, 80, 121);")

        self.verticalLayout_5.addWidget(self.lbl_logo)

        self.btn_menu_cadastrar = QPushButton(self.pg_home)
        self.btn_menu_cadastrar.setObjectName(u"btn_menu_cadastrar")
        self.btn_menu_cadastrar.setMinimumSize(QSize(180, 30))
        font1 = QFont()
        self.btn_menu_cadastrar.setFont(font1)
        self.btn_menu_cadastrar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_menu_cadastrar.setStyleSheet(u"QPushButton {\n"
"  color: rgb(255, 255, 255);\n"
"  border-radius: 10px;\n"
"  font-size: 16px;\n"
"  background-color: rgb(0, 80, 121);\n"
"  border: 2px solid white; /* Adiciona um contorno branco de 2px */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #87CEEB;\n"
"  color: black;\n"
"}")

        self.verticalLayout_5.addWidget(self.btn_menu_cadastrar, 0, Qt.AlignHCenter)

        self.Pages.addWidget(self.pg_home)
        self.pg_cadastro = QWidget()
        self.pg_cadastro.setObjectName(u"pg_cadastro")
        self.verticalLayout_12 = QVBoxLayout(self.pg_cadastro)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_10 = QLabel(self.pg_cadastro)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_12.addWidget(self.label_10)

        self.frame_5 = QFrame(self.pg_cadastro)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_5)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_11 = QLabel(self.frame_6)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(100, 30))

        self.horizontalLayout_5.addWidget(self.label_11)

        self.txt_nome = QLineEdit(self.frame_6)
        self.txt_nome.setObjectName(u"txt_nome")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(180)
        sizePolicy1.setHeightForWidth(self.txt_nome.sizePolicy().hasHeightForWidth())
        self.txt_nome.setSizePolicy(sizePolicy1)
        self.txt_nome.setMinimumSize(QSize(0, 30))
        font2 = QFont()
        font2.setPointSize(10)
        self.txt_nome.setFont(font2)
        self.txt_nome.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_nome.setStyleSheet(u"QLineEdit {\n"
"        background-color: SkyBlue;\n"
"    }\n"
"    QLineEdit:focus {\n"
"        background-color: SkyBlue;\n"
"    }\n"
"    QLineEdit:disabled {\n"
"        background-color: lightpink; \n"
"   }\n"
"	QLineEdit::placeholder {\n"
"     color: Black;\n"
"    }")

        self.horizontalLayout_5.addWidget(self.txt_nome)


        self.verticalLayout_13.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_12 = QLabel(self.frame_7)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(100, 30))

        self.horizontalLayout_7.addWidget(self.label_12)

        self.txt_user = QLineEdit(self.frame_7)
        self.txt_user.setObjectName(u"txt_user")
        sizePolicy.setHeightForWidth(self.txt_user.sizePolicy().hasHeightForWidth())
        self.txt_user.setSizePolicy(sizePolicy)
        self.txt_user.setMinimumSize(QSize(0, 30))
        self.txt_user.setFont(font2)
        self.txt_user.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_user.setStyleSheet(u"QLineEdit {\n"
"        background-color: SkyBlue;\n"
"    }\n"
"    QLineEdit:focus {\n"
"        background-color: SkyBlue;\n"
"    }\n"
"    QLineEdit:disabled {\n"
"        background-color: lightpink; \n"
"   }\n"
"	QLineEdit::placeholder {\n"
"     color: Black;\n"
"    }")

        self.horizontalLayout_7.addWidget(self.txt_user)


        self.verticalLayout_13.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame_5)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_14 = QLabel(self.frame_8)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(100, 30))

        self.horizontalLayout_9.addWidget(self.label_14)

        self.txt_senha = QLineEdit(self.frame_8)
        self.txt_senha.setObjectName(u"txt_senha")
        self.txt_senha.setMinimumSize(QSize(0, 30))
        self.txt_senha.setFont(font2)
        self.txt_senha.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_senha.setStyleSheet(u"QLineEdit {\n"
"        background-color: SkyBlue;\n"
"    }\n"
"    QLineEdit:focus {\n"
"        background-color: SkyBlue;\n"
"    }\n"
"    QLineEdit:disabled {\n"
"        background-color: lightpink; \n"
"   }\n"
"	QLineEdit::placeholder {\n"
"     color: Black;\n"
"    }")
        self.txt_senha.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_9.addWidget(self.txt_senha)


        self.verticalLayout_13.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.frame_5)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_13 = QLabel(self.frame_9)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(100, 30))

        self.horizontalLayout_8.addWidget(self.label_13)

        self.txt_senha_2 = QLineEdit(self.frame_9)
        self.txt_senha_2.setObjectName(u"txt_senha_2")
        self.txt_senha_2.setMinimumSize(QSize(0, 30))
        self.txt_senha_2.setFont(font2)
        self.txt_senha_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_senha_2.setStyleSheet(u"QLineEdit {\n"
"    background-color: SkyBlue;\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"    color: black; \n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    background-color: SkyBlue;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: lightpink; \n"
"}")
        self.txt_senha_2.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_8.addWidget(self.txt_senha_2)


        self.verticalLayout_13.addWidget(self.frame_9)

        self.frame_10 = QFrame(self.frame_5)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_15 = QLabel(self.frame_10)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMinimumSize(QSize(100, 30))

        self.horizontalLayout_10.addWidget(self.label_15)

        self.cb_perfil = QComboBox(self.frame_10)
        self.cb_perfil.addItem("")
        self.cb_perfil.addItem("")
        self.cb_perfil.addItem("")
        self.cb_perfil.setObjectName(u"cb_perfil")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.cb_perfil.sizePolicy().hasHeightForWidth())
        self.cb_perfil.setSizePolicy(sizePolicy2)
        self.cb_perfil.setMinimumSize(QSize(0, 30))
        font3 = QFont()
        font3.setFamilies([u"Trebuchet MS"])
        self.cb_perfil.setFont(font3)
        self.cb_perfil.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.cb_perfil.setStyleSheet(u"QComboBox{\n"
"        background-color: SkyBlue;\n"
"    }\n"
"    QLineEdit:focus {\n"
"        background-color: SkyBlue;\n"
"    }\n"
"    QLineEdit:disabled {\n"
"        background-color: SkyBlue; \n"
"   }")
        self.cb_perfil.setEditable(False)

        self.horizontalLayout_10.addWidget(self.cb_perfil)


        self.verticalLayout_13.addWidget(self.frame_10)


        self.verticalLayout_12.addWidget(self.frame_5)

        self.btn_cadastrar_usuario = QPushButton(self.pg_cadastro)
        self.btn_cadastrar_usuario.setObjectName(u"btn_cadastrar_usuario")
        self.btn_cadastrar_usuario.setMinimumSize(QSize(180, 30))
        self.btn_cadastrar_usuario.setFont(font1)
        self.btn_cadastrar_usuario.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_cadastrar_usuario.setStyleSheet(u"QPushButton {\n"
"  color: rgb(255, 255, 255);\n"
"  border-radius: 10px;\n"
"  font-size: 16px;\n"
"  background-color: rgb(0, 80, 121);\n"
"  border: 2px solid white; \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #87CEEB;\n"
"  color: black;\n"
"}")

        self.verticalLayout_12.addWidget(self.btn_cadastrar_usuario, 0, Qt.AlignHCenter)

        self.Pages.addWidget(self.pg_cadastro)
        self.pg_moradores = QWidget()
        self.pg_moradores.setObjectName(u"pg_moradores")
        self.verticalLayout_55 = QVBoxLayout(self.pg_moradores)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.tabWidget_7 = QTabWidget(self.pg_moradores)
        self.tabWidget_7.setObjectName(u"tabWidget_7")
        self.tabWidget_7.setStyleSheet(u"QTabWidget::pane {\n"
"  border: 1px solid  white;\n"
"  top:-1px; \n"
"  background: rgb(0, 80, 121);; \n"
"} \n"
"\n"
"QTabBar::tab {\n"
"\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(0, 61, 90, 255));\n"
"  border: 1px solid  rgb(249, 249, 249); \n"
"  padding: 10px;\n"
"color:white ;\n"
"} \n"
"\n"
"\n"
"QTabBar::tab:selected { \n"
"	background-color: SkyBlue; \n"
"  margin-bottom: -1px; \n"
" color: rgb(0, 85, 127);\n"
"	\n"
"}")
        self.tab_13 = QWidget()
        self.tab_13.setObjectName(u"tab_13")
        self.verticalLayout_56 = QVBoxLayout(self.tab_13)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.label_94 = QLabel(self.tab_13)
        self.label_94.setObjectName(u"label_94")

        self.verticalLayout_56.addWidget(self.label_94)

        self.scrollArea_6 = QScrollArea(self.tab_13)
        self.scrollArea_6.setObjectName(u"scrollArea_6")
        self.scrollArea_6.setWidgetResizable(True)
        self.scrollAreaWidgetContents_6 = QWidget()
        self.scrollAreaWidgetContents_6.setObjectName(u"scrollAreaWidgetContents_6")
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, -783, 695, 1278))
        self.verticalLayout_58 = QVBoxLayout(self.scrollAreaWidgetContents_6)
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.frame_45 = QFrame(self.scrollAreaWidgetContents_6)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setFrameShape(QFrame.StyledPanel)
        self.frame_45.setFrameShadow(QFrame.Raised)
        self.verticalLayout_62 = QVBoxLayout(self.frame_45)
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.frame_44 = QFrame(self.frame_45)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setFrameShape(QFrame.StyledPanel)
        self.frame_44.setFrameShadow(QFrame.Raised)
        self.verticalLayout_81 = QVBoxLayout(self.frame_44)
        self.verticalLayout_81.setObjectName(u"verticalLayout_81")
        self.label_65 = QLabel(self.frame_44)
        self.label_65.setObjectName(u"label_65")

        self.verticalLayout_81.addWidget(self.label_65)

        self.txt_apartamento_bloco = QLineEdit(self.frame_44)
        self.txt_apartamento_bloco.setObjectName(u"txt_apartamento_bloco")
        self.txt_apartamento_bloco.setMinimumSize(QSize(0, 30))
        self.txt_apartamento_bloco.setFont(font2)
        self.txt_apartamento_bloco.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_apartamento_bloco.setStyleSheet(u"QLineEdit {\n"
"        background-color: SkyBlue;\n"
"    }\n"
"    QLineEdit:focus {\n"
"        background-color: SkyBlue;\n"
"    }\n"
"    QLineEdit:disabled {\n"
"        background-color: SkyBlue; \n"
"   }\n"
"	QLineEdit::placeholder {\n"
"     color: Black;\n"
"    }")

        self.verticalLayout_81.addWidget(self.txt_apartamento_bloco, 0, Qt.AlignLeft)


        self.verticalLayout_62.addWidget(self.frame_44)

        self.label_67 = QLabel(self.frame_45)
        self.label_67.setObjectName(u"label_67")

        self.verticalLayout_62.addWidget(self.label_67)

        self.txt_nome_completo = QLineEdit(self.frame_45)
        self.txt_nome_completo.setObjectName(u"txt_nome_completo")
        self.txt_nome_completo.setMinimumSize(QSize(0, 30))
        self.txt_nome_completo.setFont(font2)
        self.txt_nome_completo.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_nome_completo.setStyleSheet(u"QLineEdit {\n"
"    background-color: SkyBlue;\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"    color: black; \n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    background-color: SkyBlue;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: SkyBlue; \n"
"}")

        self.verticalLayout_62.addWidget(self.txt_nome_completo)

        self.txt_data_nascimento = QLineEdit(self.frame_45)
        self.txt_data_nascimento.setObjectName(u"txt_data_nascimento")
        self.txt_data_nascimento.setMinimumSize(QSize(0, 30))
        self.txt_data_nascimento.setFont(font2)
        self.txt_data_nascimento.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_data_nascimento.setStyleSheet(u"QLineEdit {\n"
"    background-color: SkyBlue;\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"    color: black; \n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    background-color: SkyBlue;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: SkyBlue; \n"
"}")

        self.verticalLayout_62.addWidget(self.txt_data_nascimento)

        self.txt_nome_completo2 = QLineEdit(self.frame_45)
        self.txt_nome_completo2.setObjectName(u"txt_nome_completo2")
        self.txt_nome_completo2.setMinimumSize(QSize(0, 30))
        self.txt_nome_completo2.setFont(font2)
        self.txt_nome_completo2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_nome_completo2.setStyleSheet(u"QLineEdit {\n"
"    background-color: SkyBlue;\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"    color: black; \n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    background-color: SkyBlue;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: SkyBlue; \n"
"}")

        self.verticalLayout_62.addWidget(self.txt_nome_completo2)

        self.txt_data_nascimento2 = QLineEdit(self.frame_45)
        self.txt_data_nascimento2.setObjectName(u"txt_data_nascimento2")
        self.txt_data_nascimento2.setMinimumSize(QSize(0, 30))
        self.txt_data_nascimento2.setFont(font2)
        self.txt_data_nascimento2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_data_nascimento2.setStyleSheet(u"QLineEdit {\n"
"    background-color: SkyBlue;\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"    color: black; \n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    background-color: SkyBlue;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: SkyBlue; \n"
"}")

        self.verticalLayout_62.addWidget(self.txt_data_nascimento2)

        self.txt_nome_completo3 = QLineEdit(self.frame_45)
        self.txt_nome_completo3.setObjectName(u"txt_nome_completo3")
        self.txt_nome_completo3.setMinimumSize(QSize(0, 30))
        self.txt_nome_completo3.setFont(font2)
        self.txt_nome_completo3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_nome_completo3.setStyleSheet(u"QLineEdit {\n"
"    background-color: SkyBlue;\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"    color: black; \n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    background-color: SkyBlue;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: SkyBlue; \n"
"}")

        self.verticalLayout_62.addWidget(self.txt_nome_completo3)

        self.txt_data_nascimento3 = QLineEdit(self.frame_45)
        self.txt_data_nascimento3.setObjectName(u"txt_data_nascimento3")
        self.txt_data_nascimento3.setMinimumSize(QSize(0, 30))
        self.txt_data_nascimento3.setFont(font2)
        self.txt_data_nascimento3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_data_nascimento3.setStyleSheet(u"QLineEdit {\n"
"    background-color: SkyBlue;\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"    color: black; \n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    background-color: SkyBlue;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: SkyBlue; \n"
"}")

        self.verticalLayout_62.addWidget(self.txt_data_nascimento3)

        self.txt_nome_completo4 = QLineEdit(self.frame_45)
        self.txt_nome_completo4.setObjectName(u"txt_nome_completo4")
        self.txt_nome_completo4.setMinimumSize(QSize(0, 30))
        self.txt_nome_completo4.setFont(font2)
        self.txt_nome_completo4.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_nome_completo4.setStyleSheet(u"QLineEdit {\n"
"    background-color: SkyBlue;\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"    color: black; \n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    background-color: SkyBlue;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: SkyBlue; \n"
"}")

        self.verticalLayout_62.addWidget(self.txt_nome_completo4)

        self.txt_data_nascimento4 = QLineEdit(self.frame_45)
        self.txt_data_nascimento4.setObjectName(u"txt_data_nascimento4")
        self.txt_data_nascimento4.setMinimumSize(QSize(0, 30))
        self.txt_data_nascimento4.setFont(font2)
        self.txt_data_nascimento4.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_data_nascimento4.setStyleSheet(u"QLineEdit {\n"
"    background-color: SkyBlue;\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"    color: black; \n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    background-color: SkyBlue;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: SkyBlue; \n"
"}")

        self.verticalLayout_62.addWidget(self.txt_data_nascimento4)

        self.txt_nome_completo5 = QLineEdit(self.frame_45)
        self.txt_nome_completo5.setObjectName(u"txt_nome_completo5")
        self.txt_nome_completo5.setMinimumSize(QSize(0, 30))
        self.txt_nome_completo5.setFont(font2)
        self.txt_nome_completo5.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_nome_completo5.setStyleSheet(u"QLineEdit {\n"
"    background-color: SkyBlue;\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"    color: black; \n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    background-color: SkyBlue;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: SkyBlue; \n"
"}")

        self.verticalLayout_62.addWidget(self.txt_nome_completo5)

        self.txt_data_nascimento5 = QLineEdit(self.frame_45)
        self.txt_data_nascimento5.setObjectName(u"txt_data_nascimento5")
        self.txt_data_nascimento5.setMinimumSize(QSize(0, 30))
        self.txt_data_nascimento5.setFont(font2)
        self.txt_data_nascimento5.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_data_nascimento5.setStyleSheet(u"QLineEdit {\n"
"    background-color: SkyBlue;\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"    color: black; \n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    background-color: SkyBlue;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: SkyBlue; \n"
"}")

        self.verticalLayout_62.addWidget(self.txt_data_nascimento5)

        self.txt_nome_completo6 = QLineEdit(self.frame_45)
        self.txt_nome_completo6.setObjectName(u"txt_nome_completo6")
        self.txt_nome_completo6.setMinimumSize(QSize(0, 30))
        self.txt_nome_completo6.setFont(font2)
        self.txt_nome_completo6.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_nome_completo6.setStyleSheet(u"QLineEdit {\n"
"    background-color: SkyBlue;\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"    color: black; \n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    background-color: SkyBlue;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: SkyBlue; \n"
"}")

        self.verticalLayout_62.addWidget(self.txt_nome_completo6)

        self.txt_data_nascimento6 = QLineEdit(self.frame_45)
        self.txt_data_nascimento6.setObjectName(u"txt_data_nascimento6")
        self.txt_data_nascimento6.setMinimumSize(QSize(0, 30))
        self.txt_data_nascimento6.setFont(font2)
        self.txt_data_nascimento6.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_data_nascimento6.setStyleSheet(u"QLineEdit {\n"
"    background-color: SkyBlue;\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"    color: black; \n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    background-color: SkyBlue;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: SkyBlue; \n"
"}")

        self.verticalLayout_62.addWidget(self.txt_data_nascimento6)

        self.frame_43 = QFrame(self.frame_45)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setFrameShape(QFrame.StyledPanel)
        self.frame_43.setFrameShadow(QFrame.Raised)
        self.verticalLayout_57 = QVBoxLayout(self.frame_43)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.label_68 = QLabel(self.frame_43)
        self.label_68.setObjectName(u"label_68")

        self.verticalLayout_57.addWidget(self.label_68)

        self.txt_telefone1 = QLineEdit(self.frame_43)
        self.txt_telefone1.setObjectName(u"txt_telefone1")
        self.txt_telefone1.setMinimumSize(QSize(0, 30))
        self.txt_telefone1.setFont(font2)
        self.txt_telefone1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_telefone1.setStyleSheet(u"QLineEdit {\n"
"    background-color: SkyBlue;\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"    color: black; \n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    background-color: SkyBlue;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: SkyBlue; \n"
"}")

        self.verticalLayout_57.addWidget(self.txt_telefone1)

        self.label_69 = QLabel(self.frame_43)
        self.label_69.setObjectName(u"label_69")

        self.verticalLayout_57.addWidget(self.label_69)

        self.txt_telefone2 = QLineEdit(self.frame_43)
        self.txt_telefone2.setObjectName(u"txt_telefone2")
        self.txt_telefone2.setMinimumSize(QSize(0, 30))
        self.txt_telefone2.setFont(font2)
        self.txt_telefone2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_telefone2.setStyleSheet(u"QLineEdit {\n"
"    background-color: SkyBlue;\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"    color: black; \n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    background-color: SkyBlue;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: SkyBlue; \n"
"}")

        self.verticalLayout_57.addWidget(self.txt_telefone2)

        self.label_70 = QLabel(self.frame_43)
        self.label_70.setObjectName(u"label_70")

        self.verticalLayout_57.addWidget(self.label_70)

        self.txt_email1 = QLineEdit(self.frame_43)
        self.txt_email1.setObjectName(u"txt_email1")
        self.txt_email1.setMinimumSize(QSize(0, 30))
        self.txt_email1.setFont(font2)
        self.txt_email1.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_email1.setStyleSheet(u"QLineEdit {\n"
"    background-color: SkyBlue;\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"    color: black; \n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    background-color: SkyBlue;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: SkyBlue; \n"
"}")

        self.verticalLayout_57.addWidget(self.txt_email1)

        self.label_71 = QLabel(self.frame_43)
        self.label_71.setObjectName(u"label_71")

        self.verticalLayout_57.addWidget(self.label_71)

        self.txt_email2 = QLineEdit(self.frame_43)
        self.txt_email2.setObjectName(u"txt_email2")
        self.txt_email2.setMinimumSize(QSize(0, 30))
        self.txt_email2.setFont(font2)
        self.txt_email2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_email2.setStyleSheet(u"QLineEdit {\n"
"    background-color: SkyBlue;\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"    color: black; \n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    background-color: SkyBlue;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: SkyBlue; \n"
"}")

        self.verticalLayout_57.addWidget(self.txt_email2)


        self.verticalLayout_62.addWidget(self.frame_43)

        self.frame_49 = QFrame(self.frame_45)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setFrameShape(QFrame.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_49)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.frame_46 = QFrame(self.frame_49)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setFrameShape(QFrame.StyledPanel)
        self.frame_46.setFrameShadow(QFrame.Raised)
        self.verticalLayout_59 = QVBoxLayout(self.frame_46)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.label_76 = QLabel(self.frame_46)
        self.label_76.setObjectName(u"label_76")

        self.verticalLayout_59.addWidget(self.label_76)

        self.txt_veiculo1_placa = QLineEdit(self.frame_46)
        self.txt_veiculo1_placa.setObjectName(u"txt_veiculo1_placa")
        self.txt_veiculo1_placa.setMinimumSize(QSize(0, 30))
        self.txt_veiculo1_placa.setFont(font2)
        self.txt_veiculo1_placa.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_veiculo1_placa.setStyleSheet(u"QLineEdit {\n"
"    background-color: SkyBlue;\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"    color: Black; \n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    background-color: SkyBlue;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: SkyBlue; \n"
"}")

        self.verticalLayout_59.addWidget(self.txt_veiculo1_placa)

        self.txt_veiculo1_marca = QLineEdit(self.frame_46)
        self.txt_veiculo1_marca.setObjectName(u"txt_veiculo1_marca")
        self.txt_veiculo1_marca.setMinimumSize(QSize(0, 30))
        self.txt_veiculo1_marca.setFont(font2)
        self.txt_veiculo1_marca.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_veiculo1_marca.setStyleSheet(u"QLineEdit {\n"
"    background-color: SkyBlue;\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"    color: black; \n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    background-color: SkyBlue;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: SkyBlue; \n"
"}")

        self.verticalLayout_59.addWidget(self.txt_veiculo1_marca)

        self.txt_veiculo1_modelo = QLineEdit(self.frame_46)
        self.txt_veiculo1_modelo.setObjectName(u"txt_veiculo1_modelo")
        self.txt_veiculo1_modelo.setMinimumSize(QSize(0, 30))
        self.txt_veiculo1_modelo.setFont(font2)
        self.txt_veiculo1_modelo.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_veiculo1_modelo.setStyleSheet(u"QLineEdit {\n"
"    background-color: SkyBlue;\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"    color: black; \n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    background-color: SkyBlue;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: SkyBlue; \n"
"}")

        self.verticalLayout_59.addWidget(self.txt_veiculo1_modelo)

        self.txt_veiculo1_cor = QLineEdit(self.frame_46)
        self.txt_veiculo1_cor.setObjectName(u"txt_veiculo1_cor")
        self.txt_veiculo1_cor.setMinimumSize(QSize(0, 30))
        self.txt_veiculo1_cor.setFont(font2)
        self.txt_veiculo1_cor.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_veiculo1_cor.setStyleSheet(u"QLineEdit {\n"
"    background-color: SkyBlue;\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"    color: black; \n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    background-color: SkyBlue;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: SkyBlue; \n"
"}")

        self.verticalLayout_59.addWidget(self.txt_veiculo1_cor)


        self.horizontalLayout_25.addWidget(self.frame_46)

        self.frame_47 = QFrame(self.frame_49)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setFrameShape(QFrame.StyledPanel)
        self.frame_47.setFrameShadow(QFrame.Raised)
        self.verticalLayout_60 = QVBoxLayout(self.frame_47)
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.label_77 = QLabel(self.frame_47)
        self.label_77.setObjectName(u"label_77")

        self.verticalLayout_60.addWidget(self.label_77)

        self.txt_veiculo2_placa = QLineEdit(self.frame_47)
        self.txt_veiculo2_placa.setObjectName(u"txt_veiculo2_placa")
        self.txt_veiculo2_placa.setMinimumSize(QSize(0, 30))
        self.txt_veiculo2_placa.setFont(font2)
        self.txt_veiculo2_placa.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_veiculo2_placa.setStyleSheet(u"QLineEdit {\n"
"    background-color: SkyBlue;\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"    color: black; \n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    background-color: SkyBlue;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: SkyBlue; \n"
"}")

        self.verticalLayout_60.addWidget(self.txt_veiculo2_placa)

        self.txt_veiculo2_marca = QLineEdit(self.frame_47)
        self.txt_veiculo2_marca.setObjectName(u"txt_veiculo2_marca")
        self.txt_veiculo2_marca.setMinimumSize(QSize(0, 30))
        self.txt_veiculo2_marca.setFont(font2)
        self.txt_veiculo2_marca.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_veiculo2_marca.setStyleSheet(u"QLineEdit {\n"
"    background-color: SkyBlue;\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"    color: black; \n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    background-color: SkyBlue;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: SkyBlue; \n"
"}")

        self.verticalLayout_60.addWidget(self.txt_veiculo2_marca)

        self.txt_veiculo2_modelo = QLineEdit(self.frame_47)
        self.txt_veiculo2_modelo.setObjectName(u"txt_veiculo2_modelo")
        self.txt_veiculo2_modelo.setMinimumSize(QSize(0, 30))
        self.txt_veiculo2_modelo.setFont(font2)
        self.txt_veiculo2_modelo.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_veiculo2_modelo.setStyleSheet(u"QLineEdit {\n"
"    background-color: SkyBlue;\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"    color: black; \n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    background-color: SkyBlue;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: SkyBlue; \n"
"}")

        self.verticalLayout_60.addWidget(self.txt_veiculo2_modelo)

        self.txt_veiculo2_cor = QLineEdit(self.frame_47)
        self.txt_veiculo2_cor.setObjectName(u"txt_veiculo2_cor")
        self.txt_veiculo2_cor.setMinimumSize(QSize(0, 30))
        self.txt_veiculo2_cor.setFont(font2)
        self.txt_veiculo2_cor.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_veiculo2_cor.setStyleSheet(u"QLineEdit {\n"
"    background-color: SkyBlue;\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"    color: black; \n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    background-color: SkyBlue;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: SkyBlue; \n"
"}")

        self.verticalLayout_60.addWidget(self.txt_veiculo2_cor)


        self.horizontalLayout_25.addWidget(self.frame_47)


        self.verticalLayout_62.addWidget(self.frame_49)

        self.frame_48 = QFrame(self.frame_45)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setFrameShape(QFrame.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Raised)
        self.verticalLayout_61 = QVBoxLayout(self.frame_48)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.label_72 = QLabel(self.frame_48)
        self.label_72.setObjectName(u"label_72")

        self.verticalLayout_61.addWidget(self.label_72)

        self.txt_observacoes = QTextEdit(self.frame_48)
        self.txt_observacoes.setObjectName(u"txt_observacoes")
        self.txt_observacoes.setMinimumSize(QSize(0, 50))
        self.txt_observacoes.setStyleSheet(u" QTextEdit {\n"
"        background-color: SkyBlue;\n"
"    }\n"
"    QTextEdit:focus {\n"
"        background-color: SkyBlue; \n"
"    }\n"
"    QTextEdit:read-only {\n"
"        background-color: SkyBlue; \n"
"    }\n"
"")

        self.verticalLayout_61.addWidget(self.txt_observacoes)

        self.btn_cadastrar_morador = QPushButton(self.frame_48)
        self.btn_cadastrar_morador.setObjectName(u"btn_cadastrar_morador")
        self.btn_cadastrar_morador.setMinimumSize(QSize(180, 30))
        self.btn_cadastrar_morador.setFont(font1)
        self.btn_cadastrar_morador.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_cadastrar_morador.setStyleSheet(u"QPushButton {\n"
"  color: rgb(255, 255, 255);\n"
"  border-radius: 10px;\n"
"  font-size: 16px;\n"
"  background-color: rgb(0, 80, 121);\n"
"  border: 2px solid white; \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #87CEEB;\n"
"  color: black;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")

        self.verticalLayout_61.addWidget(self.btn_cadastrar_morador, 0, Qt.AlignHCenter)


        self.verticalLayout_62.addWidget(self.frame_48)


        self.verticalLayout_58.addWidget(self.frame_45)

        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_6)

        self.verticalLayout_56.addWidget(self.scrollArea_6)

        self.tabWidget_7.addTab(self.tab_13, "")
        self.tab_14 = QWidget()
        self.tab_14.setObjectName(u"tab_14")
        self.verticalLayout_53 = QVBoxLayout(self.tab_14)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.frame_34 = QFrame(self.tab_14)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.verticalLayout_63 = QVBoxLayout(self.frame_34)
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.label_48 = QLabel(self.frame_34)
        self.label_48.setObjectName(u"label_48")

        self.verticalLayout_63.addWidget(self.label_48)

        self.frame_41 = QFrame(self.frame_34)
        self.frame_41.setObjectName(u"frame_41")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_41.sizePolicy().hasHeightForWidth())
        self.frame_41.setSizePolicy(sizePolicy3)
        self.frame_41.setFrameShape(QFrame.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_41)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.txt_pesquisa_apartamento_bloco = QLineEdit(self.frame_41)
        self.txt_pesquisa_apartamento_bloco.setObjectName(u"txt_pesquisa_apartamento_bloco")
        self.txt_pesquisa_apartamento_bloco.setMinimumSize(QSize(0, 30))
        self.txt_pesquisa_apartamento_bloco.setFont(font2)
        self.txt_pesquisa_apartamento_bloco.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_pesquisa_apartamento_bloco.setStyleSheet(u"QLineEdit {\n"
"        background-color: #87CEEB;\n"
"    }\n"
"    QLineEdit:focus {\n"
"        background-color: #87CEEB;\n"
"    }\n"
"    QLineEdit:disabled {\n"
"        background-color: #87CEEB; \n"
"   }\n"
"	QLineEdit::placeholder {\n"
"     color: Black;\n"
"    }")
        self.txt_pesquisa_apartamento_bloco.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.txt_pesquisa_apartamento_bloco)

        self.btn_pesquisar_morador = QPushButton(self.frame_41)
        self.btn_pesquisar_morador.setObjectName(u"btn_pesquisar_morador")
        self.btn_pesquisar_morador.setMinimumSize(QSize(100, 30))
        self.btn_pesquisar_morador.setFont(font1)
        self.btn_pesquisar_morador.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_pesquisar_morador.setStyleSheet(u"QPushButton {\n"
"  color: rgb(255, 255, 255);\n"
"  border-radius: 10px;\n"
"  font-size: 16px;\n"
"  background-color: rgb(0, 80, 121);\n"
"  border: 2px solid white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #87CEEB;\n"
"  color: black;\n"
"}")

        self.horizontalLayout_17.addWidget(self.btn_pesquisar_morador)


        self.verticalLayout_63.addWidget(self.frame_41)

        self.tb_moradores = QTableWidget(self.frame_34)
        if (self.tb_moradores.columnCount() < 27):
            self.tb_moradores.setColumnCount(27)
        __qtablewidgetitem = QTableWidgetItem()
        self.tb_moradores.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tb_moradores.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tb_moradores.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tb_moradores.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tb_moradores.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tb_moradores.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tb_moradores.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tb_moradores.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tb_moradores.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tb_moradores.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tb_moradores.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tb_moradores.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tb_moradores.setHorizontalHeaderItem(12, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tb_moradores.setHorizontalHeaderItem(13, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tb_moradores.setHorizontalHeaderItem(14, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tb_moradores.setHorizontalHeaderItem(15, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tb_moradores.setHorizontalHeaderItem(16, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tb_moradores.setHorizontalHeaderItem(17, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tb_moradores.setHorizontalHeaderItem(18, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tb_moradores.setHorizontalHeaderItem(19, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tb_moradores.setHorizontalHeaderItem(20, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tb_moradores.setHorizontalHeaderItem(21, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tb_moradores.setHorizontalHeaderItem(22, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tb_moradores.setHorizontalHeaderItem(23, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tb_moradores.setHorizontalHeaderItem(24, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tb_moradores.setHorizontalHeaderItem(25, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tb_moradores.setHorizontalHeaderItem(26, __qtablewidgetitem26)
        self.tb_moradores.setObjectName(u"tb_moradores")
        self.tb_moradores.setStyleSheet(u"QTableWidget{\n"
"        background-color: #87CEEB;\n"
"    }\n"
"    QLineEdit:focus {\n"
"        background-color: #87CEEB;\n"
"    }\n"
"    QLineEdit:disabled {\n"
"        background-color: #87CEEB; \n"
"   }")

        self.verticalLayout_63.addWidget(self.tb_moradores)


        self.verticalLayout_53.addWidget(self.frame_34)

        self.tabWidget_7.addTab(self.tab_14, "")

        self.verticalLayout_55.addWidget(self.tabWidget_7)

        self.Pages.addWidget(self.pg_moradores)
        self.pg_agendamento = QWidget()
        self.pg_agendamento.setObjectName(u"pg_agendamento")
        self.verticalLayout_48 = QVBoxLayout(self.pg_agendamento)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.tabWidget_6 = QTabWidget(self.pg_agendamento)
        self.tabWidget_6.setObjectName(u"tabWidget_6")
        self.tabWidget_6.setStyleSheet(u"QTabWidget::pane {\n"
"  border: 1px solid  white;\n"
"  top:-1px; \n"
"  background: rgb(0, 80, 121);; \n"
"} \n"
"\n"
"QTabBar::tab {\n"
"\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(0, 61, 90, 255));\n"
"  border: 1px solid  rgb(249, 249, 249); \n"
"  padding: 10px;\n"
"color:white ;\n"
"} \n"
"\n"
"\n"
"QTabBar::tab:selected { \n"
"	background-color: SkyBlue;\n"
"  margin-bottom: -1px; \n"
" color: rgb(0, 85, 127);\n"
"	\n"
"}")
        self.tab_11 = QWidget()
        self.tab_11.setObjectName(u"tab_11")
        self.verticalLayout_50 = QVBoxLayout(self.tab_11)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.scrollArea_5 = QScrollArea(self.tab_11)
        self.scrollArea_5.setObjectName(u"scrollArea_5")
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, -149, 695, 679))
        self.verticalLayout_54 = QVBoxLayout(self.scrollAreaWidgetContents_5)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.frame_30 = QFrame(self.scrollAreaWidgetContents_5)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.verticalLayout_83 = QVBoxLayout(self.frame_30)
        self.verticalLayout_83.setObjectName(u"verticalLayout_83")
        self.label_95 = QLabel(self.frame_30)
        self.label_95.setObjectName(u"label_95")

        self.verticalLayout_83.addWidget(self.label_95)

        self.frame_65 = QFrame(self.frame_30)
        self.frame_65.setObjectName(u"frame_65")
        sizePolicy.setHeightForWidth(self.frame_65.sizePolicy().hasHeightForWidth())
        self.frame_65.setSizePolicy(sizePolicy)
        self.frame_65.setFrameShape(QFrame.StyledPanel)
        self.frame_65.setFrameShadow(QFrame.Raised)
        self.verticalLayout_82 = QVBoxLayout(self.frame_65)
        self.verticalLayout_82.setObjectName(u"verticalLayout_82")
        self.label_66 = QLabel(self.frame_65)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setMinimumSize(QSize(100, 0))

        self.verticalLayout_82.addWidget(self.label_66, 0, Qt.AlignLeft)

        self.txt_ag_apartamento_bloco = QLineEdit(self.frame_65)
        self.txt_ag_apartamento_bloco.setObjectName(u"txt_ag_apartamento_bloco")
        self.txt_ag_apartamento_bloco.setMinimumSize(QSize(100, 30))
        self.txt_ag_apartamento_bloco.setFont(font2)
        self.txt_ag_apartamento_bloco.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_ag_apartamento_bloco.setStyleSheet(u"QLineEdit {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit::placeholder {\n"
"     color: Black;\n"
"    }\n"
"QLineEdit:focus {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit:disabled {\n"
"      background-color:SkyBlue; \n"
"   }\n"
"	")

        self.verticalLayout_82.addWidget(self.txt_ag_apartamento_bloco, 0, Qt.AlignLeft)


        self.verticalLayout_83.addWidget(self.frame_65)

        self.label_58 = QLabel(self.frame_30)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setMinimumSize(QSize(100, 0))

        self.verticalLayout_83.addWidget(self.label_58)

        self.txt_ag_nome_morador = QLineEdit(self.frame_30)
        self.txt_ag_nome_morador.setObjectName(u"txt_ag_nome_morador")
        self.txt_ag_nome_morador.setMinimumSize(QSize(100, 30))
        self.txt_ag_nome_morador.setFont(font2)
        self.txt_ag_nome_morador.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_ag_nome_morador.setStyleSheet(u"QLineEdit {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit::placeholder {\n"
"     color: Black;\n"
"    }\n"
"QLineEdit:focus {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit:disabled {\n"
"      background-color:SkyBlue; \n"
"   }\n"
"	")

        self.verticalLayout_83.addWidget(self.txt_ag_nome_morador)

        self.frame_3 = QFrame(self.frame_30)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_112 = QLabel(self.frame_3)
        self.label_112.setObjectName(u"label_112")

        self.verticalLayout_8.addWidget(self.label_112)

        self.txt_data_agendamento = QLineEdit(self.frame_3)
        self.txt_data_agendamento.setObjectName(u"txt_data_agendamento")
        self.txt_data_agendamento.setMinimumSize(QSize(0, 30))
        self.txt_data_agendamento.setFont(font2)
        self.txt_data_agendamento.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_data_agendamento.setStyleSheet(u"QLineEdit {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit::placeholder {\n"
"     color: Black;\n"
"    }\n"
"QLineEdit:focus {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit:disabled {\n"
"      background-color:SkyBlue; \n"
"   }\n"
"	")

        self.verticalLayout_8.addWidget(self.txt_data_agendamento, 0, Qt.AlignLeft)


        self.verticalLayout_83.addWidget(self.frame_3)

        self.label_61 = QLabel(self.frame_30)
        self.label_61.setObjectName(u"label_61")

        self.verticalLayout_83.addWidget(self.label_61)

        self.cmb_local = QComboBox(self.frame_30)
        self.cmb_local.addItem("")
        self.cmb_local.addItem("")
        self.cmb_local.addItem("")
        self.cmb_local.addItem("")
        self.cmb_local.addItem("")
        self.cmb_local.setObjectName(u"cmb_local")
        self.cmb_local.setMinimumSize(QSize(0, 30))
        self.cmb_local.setFont(font2)
        self.cmb_local.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.cmb_local.setStyleSheet(u"QComboBox{\n"
"        background-color: SkyBlue;\n"
"    }\n"
"QLineEdit:focus {\n"
"        background-color: SkyBlue;\n"
"    }\n"
"QLineEdit:disabled {\n"
"        background-color: SkyBlue; \n"
"   }")

        self.verticalLayout_83.addWidget(self.cmb_local)

        self.label_62 = QLabel(self.frame_30)
        self.label_62.setObjectName(u"label_62")

        self.verticalLayout_83.addWidget(self.label_62)

        self.cmb_periodo = QComboBox(self.frame_30)
        self.cmb_periodo.addItem("")
        self.cmb_periodo.addItem("")
        self.cmb_periodo.addItem("")
        self.cmb_periodo.setObjectName(u"cmb_periodo")
        self.cmb_periodo.setMinimumSize(QSize(0, 30))
        self.cmb_periodo.setFont(font2)
        self.cmb_periodo.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.cmb_periodo.setStyleSheet(u"QComboBox{\n"
"        background-color: SkyBlue;\n"
"    }\n"
"    QLineEdit:focus {\n"
"        background-color: SkyBlue;\n"
"    }\n"
"    QLineEdit:disabled {\n"
"        background-color: SkyBlue; \n"
"   }")

        self.verticalLayout_83.addWidget(self.cmb_periodo)

        self.label_63 = QLabel(self.frame_30)
        self.label_63.setObjectName(u"label_63")

        self.verticalLayout_83.addWidget(self.label_63)

        self.txt_ag_funcionario = QLineEdit(self.frame_30)
        self.txt_ag_funcionario.setObjectName(u"txt_ag_funcionario")
        self.txt_ag_funcionario.setMinimumSize(QSize(0, 30))
        self.txt_ag_funcionario.setFont(font2)
        self.txt_ag_funcionario.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_ag_funcionario.setStyleSheet(u"QLineEdit {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit::placeholder {\n"
"     color: Black;\n"
"    }\n"
"QLineEdit:focus {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit:disabled {\n"
"      background-color:SkyBlue; \n"
"   }\n"
"	")

        self.verticalLayout_83.addWidget(self.txt_ag_funcionario)

        self.frame_42 = QFrame(self.frame_30)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setFrameShape(QFrame.StyledPanel)
        self.frame_42.setFrameShadow(QFrame.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.frame_42)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.label_64 = QLabel(self.frame_42)
        self.label_64.setObjectName(u"label_64")

        self.verticalLayout_38.addWidget(self.label_64)

        self.txt_ag_observacoes = QTextEdit(self.frame_42)
        self.txt_ag_observacoes.setObjectName(u"txt_ag_observacoes")
        self.txt_ag_observacoes.setMinimumSize(QSize(0, 50))
        self.txt_ag_observacoes.setStyleSheet(u"QTextEdit {\n"
"    background-color: SkyBlue;\n"
"    }\n"
"QTextEdit:focus {\n"
"    background-color: SkyBlue; \n"
"    }\n"
"QTextEdit:read-only {\n"
"    background-color: SkyBlue; \n"
"    }")

        self.verticalLayout_38.addWidget(self.txt_ag_observacoes)

        self.btn_registrar_agendamento = QPushButton(self.frame_42)
        self.btn_registrar_agendamento.setObjectName(u"btn_registrar_agendamento")
        self.btn_registrar_agendamento.setMinimumSize(QSize(180, 30))
        self.btn_registrar_agendamento.setFont(font1)
        self.btn_registrar_agendamento.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_registrar_agendamento.setStyleSheet(u"QPushButton {\n"
"  color: rgb(255, 255, 255);\n"
"  border-radius: 10px;\n"
"  font-size: 16px;\n"
"  background-color: rgb(0, 80, 121);\n"
"  border: 2px solid white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #87CEEB;\n"
"  color: black;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")

        self.verticalLayout_38.addWidget(self.btn_registrar_agendamento, 0, Qt.AlignHCenter)


        self.verticalLayout_83.addWidget(self.frame_42)


        self.verticalLayout_54.addWidget(self.frame_30)

        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_5)

        self.verticalLayout_50.addWidget(self.scrollArea_5)

        self.tabWidget_6.addTab(self.tab_11, "")
        self.tab_12 = QWidget()
        self.tab_12.setObjectName(u"tab_12")
        self.verticalLayout_49 = QVBoxLayout(self.tab_12)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.label_97 = QLabel(self.tab_12)
        self.label_97.setObjectName(u"label_97")

        self.verticalLayout_49.addWidget(self.label_97)

        self.frame_37 = QFrame(self.tab_12)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.verticalLayout_52 = QVBoxLayout(self.frame_37)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.frame_38 = QFrame(self.frame_37)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_38)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.frame_39 = QFrame(self.frame_38)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.verticalLayout_51 = QVBoxLayout(self.frame_39)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.frame_40 = QFrame(self.frame_39)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_40)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.txt_pesquisar_agendamentos = QLineEdit(self.frame_40)
        self.txt_pesquisar_agendamentos.setObjectName(u"txt_pesquisar_agendamentos")
        self.txt_pesquisar_agendamentos.setMinimumSize(QSize(0, 30))
        self.txt_pesquisar_agendamentos.setFont(font2)
        self.txt_pesquisar_agendamentos.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_pesquisar_agendamentos.setStyleSheet(u"QLineEdit {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit::placeholder {\n"
"     color: Black;\n"
"    }\n"
"QLineEdit:focus {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit:disabled {\n"
"      background-color:SkyBlue; \n"
"   }")
        self.txt_pesquisar_agendamentos.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_23.addWidget(self.txt_pesquisar_agendamentos)

        self.btn_pesquisar_agendamentos = QPushButton(self.frame_40)
        self.btn_pesquisar_agendamentos.setObjectName(u"btn_pesquisar_agendamentos")
        self.btn_pesquisar_agendamentos.setMinimumSize(QSize(100, 30))
        self.btn_pesquisar_agendamentos.setFont(font1)
        self.btn_pesquisar_agendamentos.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_pesquisar_agendamentos.setStyleSheet(u"QPushButton {\n"
"  color: rgb(255, 255, 255);\n"
"  border-radius: 10px;\n"
"  font-size: 16px;\n"
"  background-color: rgb(0, 80, 121);\n"
"  border: 2px solid white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #87CEEB;\n"
"  color: black;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")

        self.horizontalLayout_23.addWidget(self.btn_pesquisar_agendamentos)


        self.verticalLayout_51.addWidget(self.frame_40)

        self.tb_agendamentos = QTableWidget(self.frame_39)
        if (self.tb_agendamentos.columnCount() < 8):
            self.tb_agendamentos.setColumnCount(8)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tb_agendamentos.setHorizontalHeaderItem(0, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tb_agendamentos.setHorizontalHeaderItem(1, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tb_agendamentos.setHorizontalHeaderItem(2, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tb_agendamentos.setHorizontalHeaderItem(3, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tb_agendamentos.setHorizontalHeaderItem(4, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tb_agendamentos.setHorizontalHeaderItem(5, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tb_agendamentos.setHorizontalHeaderItem(6, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tb_agendamentos.setHorizontalHeaderItem(7, __qtablewidgetitem34)
        self.tb_agendamentos.setObjectName(u"tb_agendamentos")
        self.tb_agendamentos.setStyleSheet(u"QTableWidget{\n"
"        background-color: SkyBlue;\n"
"    }\n"
"    QLineEdit:focus {\n"
"        background-color: SkyBlue;\n"
"    }\n"
"    QLineEdit:disabled {\n"
"        background-color: SkyBlue;\n"
"   }")

        self.verticalLayout_51.addWidget(self.tb_agendamentos)


        self.horizontalLayout_22.addWidget(self.frame_39)


        self.verticalLayout_52.addWidget(self.frame_38)


        self.verticalLayout_49.addWidget(self.frame_37)

        self.tabWidget_6.addTab(self.tab_12, "")

        self.verticalLayout_48.addWidget(self.tabWidget_6)

        self.Pages.addWidget(self.pg_agendamento)
        self.pg_visitantes = QWidget()
        self.pg_visitantes.setObjectName(u"pg_visitantes")
        self.verticalLayout_41 = QVBoxLayout(self.pg_visitantes)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.tabWidget_5 = QTabWidget(self.pg_visitantes)
        self.tabWidget_5.setObjectName(u"tabWidget_5")
        self.tabWidget_5.setStyleSheet(u"QTabWidget::pane {\n"
"  border: 1px solid  white;\n"
"  top:-1px; \n"
"  background: rgb(0, 80, 121);; \n"
"} \n"
"\n"
"QTabBar::tab {\n"
"\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(0, 61, 90, 255));\n"
"  border: 1px solid  rgb(249, 249, 249); \n"
"  padding: 10px;\n"
"color:white ;\n"
"} \n"
"\n"
"\n"
"QTabBar::tab:selected { \n"
"	background-color: SkyBlue;\n"
"  margin-bottom: -1px; \n"
" color: rgb(0, 85, 127);\n"
"	\n"
"}")
        self.tab_9 = QWidget()
        self.tab_9.setObjectName(u"tab_9")
        self.verticalLayout_42 = QVBoxLayout(self.tab_9)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.scrollArea_4 = QScrollArea(self.tab_9)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 695, 968))
        self.verticalLayout_47 = QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.label_98 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_98.setObjectName(u"label_98")

        self.verticalLayout_47.addWidget(self.label_98)

        self.frame_33 = QFrame(self.scrollAreaWidgetContents_4)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.verticalLayout_46 = QVBoxLayout(self.frame_33)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.label_44 = QLabel(self.frame_33)
        self.label_44.setObjectName(u"label_44")

        self.verticalLayout_46.addWidget(self.label_44)

        self.txt_data_visita = QLineEdit(self.frame_33)
        self.txt_data_visita.setObjectName(u"txt_data_visita")
        self.txt_data_visita.setMinimumSize(QSize(0, 30))
        self.txt_data_visita.setFont(font2)
        self.txt_data_visita.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_data_visita.setStyleSheet(u"QLineEdit {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit::placeholder {\n"
"     color: Black;\n"
"    }\n"
"QLineEdit:focus {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit:disabled {\n"
"      background-color:SkyBlue; \n"
"   }")

        self.verticalLayout_46.addWidget(self.txt_data_visita)

        self.label_45 = QLabel(self.frame_33)
        self.label_45.setObjectName(u"label_45")

        self.verticalLayout_46.addWidget(self.label_45)

        self.txt_nome_visitante = QLineEdit(self.frame_33)
        self.txt_nome_visitante.setObjectName(u"txt_nome_visitante")
        self.txt_nome_visitante.setMinimumSize(QSize(0, 30))
        self.txt_nome_visitante.setFont(font2)
        self.txt_nome_visitante.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_nome_visitante.setStyleSheet(u"QLineEdit {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit::placeholder {\n"
"     color: Black;\n"
"    }\n"
"QLineEdit:focus {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit:disabled {\n"
"      background-color:SkyBlue; \n"
"   }")

        self.verticalLayout_46.addWidget(self.txt_nome_visitante)

        self.label_46 = QLabel(self.frame_33)
        self.label_46.setObjectName(u"label_46")

        self.verticalLayout_46.addWidget(self.label_46)

        self.txt_rg_cpf_visitante = QLineEdit(self.frame_33)
        self.txt_rg_cpf_visitante.setObjectName(u"txt_rg_cpf_visitante")
        self.txt_rg_cpf_visitante.setMinimumSize(QSize(0, 30))
        self.txt_rg_cpf_visitante.setFont(font2)
        self.txt_rg_cpf_visitante.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_rg_cpf_visitante.setStyleSheet(u"QLineEdit {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit::placeholder {\n"
"     color: Black;\n"
"    }\n"
"QLineEdit:focus {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit:disabled {\n"
"      background-color:SkyBlue; \n"
"   }")

        self.verticalLayout_46.addWidget(self.txt_rg_cpf_visitante)

        self.label_47 = QLabel(self.frame_33)
        self.label_47.setObjectName(u"label_47")

        self.verticalLayout_46.addWidget(self.label_47)

        self.txt_visitando = QLineEdit(self.frame_33)
        self.txt_visitando.setObjectName(u"txt_visitando")
        self.txt_visitando.setMinimumSize(QSize(0, 30))
        self.txt_visitando.setFont(font2)
        self.txt_visitando.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_visitando.setStyleSheet(u"QLineEdit {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit::placeholder {\n"
"     color: Black;\n"
"    }\n"
"QLineEdit:focus {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit:disabled {\n"
"      background-color:SkyBlue; \n"
"   }")

        self.verticalLayout_46.addWidget(self.txt_visitando)

        self.frame_66 = QFrame(self.frame_33)
        self.frame_66.setObjectName(u"frame_66")
        sizePolicy.setHeightForWidth(self.frame_66.sizePolicy().hasHeightForWidth())
        self.frame_66.setSizePolicy(sizePolicy)
        self.frame_66.setFrameShape(QFrame.StyledPanel)
        self.frame_66.setFrameShadow(QFrame.Raised)
        self.verticalLayout_84 = QVBoxLayout(self.frame_66)
        self.verticalLayout_84.setObjectName(u"verticalLayout_84")
        self.label_113 = QLabel(self.frame_66)
        self.label_113.setObjectName(u"label_113")
        self.label_113.setMinimumSize(QSize(100, 0))

        self.verticalLayout_84.addWidget(self.label_113, 0, Qt.AlignLeft)

        self.txt_apartamento_bloco_visitantes = QLineEdit(self.frame_66)
        self.txt_apartamento_bloco_visitantes.setObjectName(u"txt_apartamento_bloco_visitantes")
        self.txt_apartamento_bloco_visitantes.setMinimumSize(QSize(100, 30))
        self.txt_apartamento_bloco_visitantes.setFont(font2)
        self.txt_apartamento_bloco_visitantes.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_apartamento_bloco_visitantes.setStyleSheet(u"QLineEdit {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit::placeholder {\n"
"     color: Black;\n"
"    }\n"
"QLineEdit:focus {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit:disabled {\n"
"      background-color:SkyBlue; \n"
"   }")

        self.verticalLayout_84.addWidget(self.txt_apartamento_bloco_visitantes, 0, Qt.AlignLeft)


        self.verticalLayout_46.addWidget(self.frame_66)

        self.frame_35 = QFrame(self.frame_33)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_35)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_50 = QLabel(self.frame_35)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_21.addWidget(self.label_50)

        self.txt_hora_entrada_visita = QLineEdit(self.frame_35)
        self.txt_hora_entrada_visita.setObjectName(u"txt_hora_entrada_visita")
        self.txt_hora_entrada_visita.setMinimumSize(QSize(0, 30))
        self.txt_hora_entrada_visita.setFont(font2)
        self.txt_hora_entrada_visita.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_hora_entrada_visita.setStyleSheet(u"QLineEdit {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit::placeholder {\n"
"     color: Black;\n"
"    }\n"
"QLineEdit:focus {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit:disabled {\n"
"      background-color:SkyBlue; \n"
"   }")

        self.horizontalLayout_21.addWidget(self.txt_hora_entrada_visita)

        self.label_51 = QLabel(self.frame_35)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_21.addWidget(self.label_51)

        self.txt_hora_saida_visita = QLineEdit(self.frame_35)
        self.txt_hora_saida_visita.setObjectName(u"txt_hora_saida_visita")
        self.txt_hora_saida_visita.setMinimumSize(QSize(0, 30))
        self.txt_hora_saida_visita.setFont(font2)
        self.txt_hora_saida_visita.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_hora_saida_visita.setStyleSheet(u"QLineEdit {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit::placeholder {\n"
"     color: Black;\n"
"    }\n"
"QLineEdit:focus {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit:disabled {\n"
"      background-color:SkyBlue; \n"
"   }")

        self.horizontalLayout_21.addWidget(self.txt_hora_saida_visita)


        self.verticalLayout_46.addWidget(self.frame_35)

        self.frame_36 = QFrame(self.frame_33)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.verticalLayout_45 = QVBoxLayout(self.frame_36)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.label_52 = QLabel(self.frame_36)
        self.label_52.setObjectName(u"label_52")

        self.verticalLayout_45.addWidget(self.label_52)

        self.txt_quem_autorizou_visita = QLineEdit(self.frame_36)
        self.txt_quem_autorizou_visita.setObjectName(u"txt_quem_autorizou_visita")
        self.txt_quem_autorizou_visita.setMinimumSize(QSize(0, 30))
        self.txt_quem_autorizou_visita.setFont(font2)
        self.txt_quem_autorizou_visita.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_quem_autorizou_visita.setStyleSheet(u"QLineEdit {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit::placeholder {\n"
"     color: Black;\n"
"    }\n"
"QLineEdit:focus {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit:disabled {\n"
"      background-color:SkyBlue; \n"
"   }")

        self.verticalLayout_45.addWidget(self.txt_quem_autorizou_visita)

        self.label_53 = QLabel(self.frame_36)
        self.label_53.setObjectName(u"label_53")

        self.verticalLayout_45.addWidget(self.label_53)

        self.cmb_vaga_utilizada = QComboBox(self.frame_36)
        self.cmb_vaga_utilizada.addItem("")
        self.cmb_vaga_utilizada.addItem("")
        self.cmb_vaga_utilizada.setObjectName(u"cmb_vaga_utilizada")
        self.cmb_vaga_utilizada.setMinimumSize(QSize(0, 30))
        self.cmb_vaga_utilizada.setFont(font2)
        self.cmb_vaga_utilizada.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.cmb_vaga_utilizada.setStyleSheet(u"QComboBox{\n"
"        background-color: SkyBlue;\n"
"    }\n"
"    QLineEdit:focus {\n"
"        background-color: SkyBlue;\n"
"    }\n"
"    QLineEdit:disabled {\n"
"        background-color:SkyBlue;\n"
"   }")

        self.verticalLayout_45.addWidget(self.cmb_vaga_utilizada)

        self.label_54 = QLabel(self.frame_36)
        self.label_54.setObjectName(u"label_54")

        self.verticalLayout_45.addWidget(self.label_54)

        self.txt_placa_visitante = QLineEdit(self.frame_36)
        self.txt_placa_visitante.setObjectName(u"txt_placa_visitante")
        self.txt_placa_visitante.setMinimumSize(QSize(0, 30))
        self.txt_placa_visitante.setFont(font2)
        self.txt_placa_visitante.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_placa_visitante.setStyleSheet(u"QLineEdit {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit::placeholder {\n"
"     color: Black;\n"
"    }\n"
"QLineEdit:focus {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit:disabled {\n"
"      background-color:SkyBlue; \n"
"   }")

        self.verticalLayout_45.addWidget(self.txt_placa_visitante)

        self.label_55 = QLabel(self.frame_36)
        self.label_55.setObjectName(u"label_55")

        self.verticalLayout_45.addWidget(self.label_55)

        self.txt_marca_visitante = QLineEdit(self.frame_36)
        self.txt_marca_visitante.setObjectName(u"txt_marca_visitante")
        self.txt_marca_visitante.setMinimumSize(QSize(0, 30))
        self.txt_marca_visitante.setFont(font2)
        self.txt_marca_visitante.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_marca_visitante.setStyleSheet(u"QLineEdit {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit::placeholder {\n"
"     color: Black;\n"
"    }\n"
"QLineEdit:focus {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit:disabled {\n"
"      background-color:SkyBlue; \n"
"   }")

        self.verticalLayout_45.addWidget(self.txt_marca_visitante)

        self.label_56 = QLabel(self.frame_36)
        self.label_56.setObjectName(u"label_56")

        self.verticalLayout_45.addWidget(self.label_56)

        self.txt_modelo_visitante = QLineEdit(self.frame_36)
        self.txt_modelo_visitante.setObjectName(u"txt_modelo_visitante")
        self.txt_modelo_visitante.setMinimumSize(QSize(0, 30))
        self.txt_modelo_visitante.setFont(font2)
        self.txt_modelo_visitante.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_modelo_visitante.setStyleSheet(u"QLineEdit {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit::placeholder {\n"
"     color: Black;\n"
"    }\n"
"QLineEdit:focus {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit:disabled {\n"
"      background-color:SkyBlue; \n"
"   }")

        self.verticalLayout_45.addWidget(self.txt_modelo_visitante)

        self.label_57 = QLabel(self.frame_36)
        self.label_57.setObjectName(u"label_57")

        self.verticalLayout_45.addWidget(self.label_57)

        self.txt_cor_visitante = QLineEdit(self.frame_36)
        self.txt_cor_visitante.setObjectName(u"txt_cor_visitante")
        self.txt_cor_visitante.setMinimumSize(QSize(0, 30))
        self.txt_cor_visitante.setFont(font2)
        self.txt_cor_visitante.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_cor_visitante.setStyleSheet(u"QLineEdit {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit::placeholder {\n"
"     color: Black;\n"
"    }\n"
"QLineEdit:focus {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit:disabled {\n"
"      background-color:SkyBlue; \n"
"   }")

        self.verticalLayout_45.addWidget(self.txt_cor_visitante)

        self.btn_registrar_visitante = QPushButton(self.frame_36)
        self.btn_registrar_visitante.setObjectName(u"btn_registrar_visitante")
        self.btn_registrar_visitante.setMinimumSize(QSize(180, 30))
        self.btn_registrar_visitante.setFont(font1)
        self.btn_registrar_visitante.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_registrar_visitante.setStyleSheet(u"QPushButton {\n"
"  color: rgb(255, 255, 255);\n"
"  border-radius: 10px;\n"
"  font-size: 16px;\n"
"  background-color: rgb(0, 80, 121);\n"
"  border: 2px solid white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #87CEEB;\n"
"  color: black;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")

        self.verticalLayout_45.addWidget(self.btn_registrar_visitante, 0, Qt.AlignHCenter)


        self.verticalLayout_46.addWidget(self.frame_36)


        self.verticalLayout_47.addWidget(self.frame_33)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_4)

        self.verticalLayout_42.addWidget(self.scrollArea_4)

        self.tabWidget_5.addTab(self.tab_9, "")
        self.tab_10 = QWidget()
        self.tab_10.setObjectName(u"tab_10")
        self.verticalLayout_44 = QVBoxLayout(self.tab_10)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.label_99 = QLabel(self.tab_10)
        self.label_99.setObjectName(u"label_99")

        self.verticalLayout_44.addWidget(self.label_99)

        self.frame_29 = QFrame(self.tab_10)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.frame_31 = QFrame(self.frame_29)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.verticalLayout_43 = QVBoxLayout(self.frame_31)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.frame_32 = QFrame(self.frame_31)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.txt_pesquisa_visitantes = QLineEdit(self.frame_32)
        self.txt_pesquisa_visitantes.setObjectName(u"txt_pesquisa_visitantes")
        self.txt_pesquisa_visitantes.setMinimumSize(QSize(0, 30))
        self.txt_pesquisa_visitantes.setFont(font2)
        self.txt_pesquisa_visitantes.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_pesquisa_visitantes.setStyleSheet(u"QLineEdit {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit::placeholder {\n"
"     color: Black;\n"
"    }\n"
"QLineEdit:focus {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit:disabled {\n"
"      background-color:SkyBlue; \n"
"   }")
        self.txt_pesquisa_visitantes.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_19.addWidget(self.txt_pesquisa_visitantes)

        self.btn_pesquisar_visitantes = QPushButton(self.frame_32)
        self.btn_pesquisar_visitantes.setObjectName(u"btn_pesquisar_visitantes")
        self.btn_pesquisar_visitantes.setMinimumSize(QSize(100, 30))
        self.btn_pesquisar_visitantes.setFont(font1)
        self.btn_pesquisar_visitantes.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_pesquisar_visitantes.setStyleSheet(u"QPushButton {\n"
"  color: rgb(255, 255, 255);\n"
"  border-radius: 10px;\n"
"  font-size: 16px;\n"
"  background-color: rgb(0, 80, 121);\n"
"  border: 2px solid white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #87CEEB;\n"
"  color: black;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")

        self.horizontalLayout_19.addWidget(self.btn_pesquisar_visitantes)


        self.verticalLayout_43.addWidget(self.frame_32)

        self.tb_visitantes = QTableWidget(self.frame_31)
        if (self.tb_visitantes.columnCount() < 14):
            self.tb_visitantes.setColumnCount(14)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tb_visitantes.setHorizontalHeaderItem(0, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tb_visitantes.setHorizontalHeaderItem(1, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tb_visitantes.setHorizontalHeaderItem(2, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tb_visitantes.setHorizontalHeaderItem(3, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tb_visitantes.setHorizontalHeaderItem(4, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tb_visitantes.setHorizontalHeaderItem(5, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.tb_visitantes.setHorizontalHeaderItem(6, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.tb_visitantes.setHorizontalHeaderItem(7, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.tb_visitantes.setHorizontalHeaderItem(8, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.tb_visitantes.setHorizontalHeaderItem(9, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.tb_visitantes.setHorizontalHeaderItem(10, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.tb_visitantes.setHorizontalHeaderItem(11, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.tb_visitantes.setHorizontalHeaderItem(12, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.tb_visitantes.setHorizontalHeaderItem(13, __qtablewidgetitem48)
        self.tb_visitantes.setObjectName(u"tb_visitantes")
        self.tb_visitantes.setStyleSheet(u"QTableWidget{\n"
"        background-color: SkyBlue;\n"
"    }\n"
"    QLineEdit:focus {\n"
"        background-color: SkyBlue;\n"
"    }\n"
"    QLineEdit:disabled {\n"
"        background-color: SkyBlue; \n"
"   }")

        self.verticalLayout_43.addWidget(self.tb_visitantes)


        self.horizontalLayout_18.addWidget(self.frame_31)


        self.verticalLayout_44.addWidget(self.frame_29)

        self.tabWidget_5.addTab(self.tab_10, "")

        self.verticalLayout_41.addWidget(self.tabWidget_5)

        self.Pages.addWidget(self.pg_visitantes)
        self.pg_prestadores = QWidget()
        self.pg_prestadores.setObjectName(u"pg_prestadores")
        self.verticalLayout_34 = QVBoxLayout(self.pg_prestadores)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.tabWidget_4 = QTabWidget(self.pg_prestadores)
        self.tabWidget_4.setObjectName(u"tabWidget_4")
        self.tabWidget_4.setStyleSheet(u"QTabWidget::pane {\n"
"  border: 1px solid  white;\n"
"  top:-1px; \n"
"  background: rgb(0, 80, 121);; \n"
"} \n"
"\n"
"QTabBar::tab {\n"
"\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(0, 61, 90, 255));\n"
"  border: 1px solid  rgb(249, 249, 249); \n"
"  padding: 10px;\n"
"color:white ;\n"
"} \n"
"\n"
"\n"
"QTabBar::tab:selected { \n"
"	background-color: #87CEEB;\n"
"  margin-bottom: -1px; \n"
" color: rgb(0, 85, 127);\n"
"	\n"
"}")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.verticalLayout_4 = QVBoxLayout(self.tab_7)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.scrollArea_3 = QScrollArea(self.tab_7)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 695, 883))
        self.verticalLayout_40 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.label_100 = QLabel(self.scrollAreaWidgetContents_3)
        self.label_100.setObjectName(u"label_100")

        self.verticalLayout_40.addWidget(self.label_100)

        self.frame_28 = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.frame_28)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.label_34 = QLabel(self.frame_28)
        self.label_34.setObjectName(u"label_34")

        self.verticalLayout_39.addWidget(self.label_34)

        self.txt_nome_empresa = QLineEdit(self.frame_28)
        self.txt_nome_empresa.setObjectName(u"txt_nome_empresa")
        self.txt_nome_empresa.setMinimumSize(QSize(0, 30))
        self.txt_nome_empresa.setFont(font2)
        self.txt_nome_empresa.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_nome_empresa.setStyleSheet(u"QLineEdit {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit::placeholder {\n"
"     color: Black;\n"
"    }\n"
"QLineEdit:focus {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit:disabled {\n"
"      background-color:SkyBlue; \n"
"   }")

        self.verticalLayout_39.addWidget(self.txt_nome_empresa)

        self.label_35 = QLabel(self.frame_28)
        self.label_35.setObjectName(u"label_35")

        self.verticalLayout_39.addWidget(self.label_35)

        self.txt_tipo_servico = QLineEdit(self.frame_28)
        self.txt_tipo_servico.setObjectName(u"txt_tipo_servico")
        self.txt_tipo_servico.setMinimumSize(QSize(0, 30))
        self.txt_tipo_servico.setFont(font2)
        self.txt_tipo_servico.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_tipo_servico.setStyleSheet(u"QLineEdit {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit::placeholder {\n"
"     color: Black;\n"
"    }\n"
"QLineEdit:focus {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit:disabled {\n"
"      background-color:SkyBlue; \n"
"   }")

        self.verticalLayout_39.addWidget(self.txt_tipo_servico)

        self.label_36 = QLabel(self.frame_28)
        self.label_36.setObjectName(u"label_36")

        self.verticalLayout_39.addWidget(self.label_36)

        self.txt_data_servico = QLineEdit(self.frame_28)
        self.txt_data_servico.setObjectName(u"txt_data_servico")
        self.txt_data_servico.setMinimumSize(QSize(0, 30))
        self.txt_data_servico.setFont(font2)
        self.txt_data_servico.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_data_servico.setStyleSheet(u"QLineEdit {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit::placeholder {\n"
"     color: Black;\n"
"    }\n"
"QLineEdit:focus {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit:disabled {\n"
"      background-color:SkyBlue; \n"
"   }")

        self.verticalLayout_39.addWidget(self.txt_data_servico)

        self.label_38 = QLabel(self.frame_28)
        self.label_38.setObjectName(u"label_38")

        self.verticalLayout_39.addWidget(self.label_38)

        self.txt_hora_entrada_prestador = QLineEdit(self.frame_28)
        self.txt_hora_entrada_prestador.setObjectName(u"txt_hora_entrada_prestador")
        self.txt_hora_entrada_prestador.setMinimumSize(QSize(0, 30))
        self.txt_hora_entrada_prestador.setFont(font2)
        self.txt_hora_entrada_prestador.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_hora_entrada_prestador.setStyleSheet(u"QLineEdit {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit::placeholder {\n"
"     color: Black;\n"
"    }\n"
"QLineEdit:focus {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit:disabled {\n"
"      background-color:SkyBlue; \n"
"   }")

        self.verticalLayout_39.addWidget(self.txt_hora_entrada_prestador)

        self.label_37 = QLabel(self.frame_28)
        self.label_37.setObjectName(u"label_37")

        self.verticalLayout_39.addWidget(self.label_37)

        self.txt_hora_saida_prestador = QLineEdit(self.frame_28)
        self.txt_hora_saida_prestador.setObjectName(u"txt_hora_saida_prestador")
        self.txt_hora_saida_prestador.setMinimumSize(QSize(0, 30))
        self.txt_hora_saida_prestador.setFont(font2)
        self.txt_hora_saida_prestador.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_hora_saida_prestador.setStyleSheet(u"QLineEdit {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit::placeholder {\n"
"     color: Black;\n"
"    }\n"
"QLineEdit:focus {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit:disabled {\n"
"      background-color:SkyBlue; \n"
"   }")

        self.verticalLayout_39.addWidget(self.txt_hora_saida_prestador)

        self.label_39 = QLabel(self.frame_28)
        self.label_39.setObjectName(u"label_39")

        self.verticalLayout_39.addWidget(self.label_39)

        self.txt_nome_prestador = QLineEdit(self.frame_28)
        self.txt_nome_prestador.setObjectName(u"txt_nome_prestador")
        self.txt_nome_prestador.setMinimumSize(QSize(0, 30))
        self.txt_nome_prestador.setFont(font2)
        self.txt_nome_prestador.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_nome_prestador.setStyleSheet(u"QLineEdit {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit::placeholder {\n"
"     color: Black;\n"
"    }\n"
"QLineEdit:focus {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit:disabled {\n"
"      background-color:SkyBlue; \n"
"   }")

        self.verticalLayout_39.addWidget(self.txt_nome_prestador)

        self.label_40 = QLabel(self.frame_28)
        self.label_40.setObjectName(u"label_40")

        self.verticalLayout_39.addWidget(self.label_40)

        self.txt_rg_cpf_prestador = QLineEdit(self.frame_28)
        self.txt_rg_cpf_prestador.setObjectName(u"txt_rg_cpf_prestador")
        self.txt_rg_cpf_prestador.setMinimumSize(QSize(0, 30))
        self.txt_rg_cpf_prestador.setFont(font2)
        self.txt_rg_cpf_prestador.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_rg_cpf_prestador.setStyleSheet(u"QLineEdit {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit::placeholder {\n"
"     color: Black;\n"
"    }\n"
"QLineEdit:focus {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit:disabled {\n"
"      background-color:SkyBlue; \n"
"   }")

        self.verticalLayout_39.addWidget(self.txt_rg_cpf_prestador)

        self.label_41 = QLabel(self.frame_28)
        self.label_41.setObjectName(u"label_41")

        self.verticalLayout_39.addWidget(self.label_41)

        self.txt_telefone_prestador = QLineEdit(self.frame_28)
        self.txt_telefone_prestador.setObjectName(u"txt_telefone_prestador")
        self.txt_telefone_prestador.setMinimumSize(QSize(0, 30))
        self.txt_telefone_prestador.setFont(font2)
        self.txt_telefone_prestador.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_telefone_prestador.setStyleSheet(u"QLineEdit {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit::placeholder {\n"
"     color: Black;\n"
"    }\n"
"QLineEdit:focus {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit:disabled {\n"
"      background-color:SkyBlue; \n"
"   }")

        self.verticalLayout_39.addWidget(self.txt_telefone_prestador)

        self.label_42 = QLabel(self.frame_28)
        self.label_42.setObjectName(u"label_42")

        self.verticalLayout_39.addWidget(self.label_42)

        self.txt_contratante = QLineEdit(self.frame_28)
        self.txt_contratante.setObjectName(u"txt_contratante")
        self.txt_contratante.setMinimumSize(QSize(0, 30))
        self.txt_contratante.setFont(font2)
        self.txt_contratante.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_contratante.setStyleSheet(u"QLineEdit {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit::placeholder {\n"
"     color: Black;\n"
"    }\n"
"QLineEdit:focus {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit:disabled {\n"
"      background-color:SkyBlue; \n"
"   }")

        self.verticalLayout_39.addWidget(self.txt_contratante)

        self.frame_67 = QFrame(self.frame_28)
        self.frame_67.setObjectName(u"frame_67")
        sizePolicy.setHeightForWidth(self.frame_67.sizePolicy().hasHeightForWidth())
        self.frame_67.setSizePolicy(sizePolicy)
        self.frame_67.setFrameShape(QFrame.StyledPanel)
        self.frame_67.setFrameShadow(QFrame.Raised)
        self.verticalLayout_85 = QVBoxLayout(self.frame_67)
        self.verticalLayout_85.setObjectName(u"verticalLayout_85")
        self.label_114 = QLabel(self.frame_67)
        self.label_114.setObjectName(u"label_114")
        self.label_114.setMinimumSize(QSize(100, 0))

        self.verticalLayout_85.addWidget(self.label_114)

        self.txt_apartamento_bloco_prestador = QLineEdit(self.frame_67)
        self.txt_apartamento_bloco_prestador.setObjectName(u"txt_apartamento_bloco_prestador")
        self.txt_apartamento_bloco_prestador.setMinimumSize(QSize(100, 30))
        self.txt_apartamento_bloco_prestador.setFont(font2)
        self.txt_apartamento_bloco_prestador.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_apartamento_bloco_prestador.setStyleSheet(u"QLineEdit {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit::placeholder {\n"
"     color: Black;\n"
"    }\n"
"QLineEdit:focus {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit:disabled {\n"
"      background-color:SkyBlue; \n"
"   }")

        self.verticalLayout_85.addWidget(self.txt_apartamento_bloco_prestador, 0, Qt.AlignLeft)


        self.verticalLayout_39.addWidget(self.frame_67)

        self.label_43 = QLabel(self.frame_28)
        self.label_43.setObjectName(u"label_43")

        self.verticalLayout_39.addWidget(self.label_43)

        self.txt_autorizou_entrada = QLineEdit(self.frame_28)
        self.txt_autorizou_entrada.setObjectName(u"txt_autorizou_entrada")
        self.txt_autorizou_entrada.setMinimumSize(QSize(0, 30))
        self.txt_autorizou_entrada.setFont(font2)
        self.txt_autorizou_entrada.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_autorizou_entrada.setStyleSheet(u"QLineEdit {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit::placeholder {\n"
"     color: Black;\n"
"    }\n"
"QLineEdit:focus {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit:disabled {\n"
"      background-color:SkyBlue; \n"
"   }")

        self.verticalLayout_39.addWidget(self.txt_autorizou_entrada)

        self.btn_registrar_prestadores = QPushButton(self.frame_28)
        self.btn_registrar_prestadores.setObjectName(u"btn_registrar_prestadores")
        self.btn_registrar_prestadores.setMinimumSize(QSize(180, 30))
        self.btn_registrar_prestadores.setFont(font1)
        self.btn_registrar_prestadores.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_registrar_prestadores.setStyleSheet(u"QPushButton {\n"
"  color: rgb(255, 255, 255);\n"
"  border-radius: 10px;\n"
"  font-size: 16px;\n"
"  background-color: rgb(0, 80, 121);\n"
"  border: 2px solid white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #87CEEB;\n"
"  color: black;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")

        self.verticalLayout_39.addWidget(self.btn_registrar_prestadores, 0, Qt.AlignHCenter)


        self.verticalLayout_40.addWidget(self.frame_28)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_4.addWidget(self.scrollArea_3)

        self.tabWidget_4.addTab(self.tab_7, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.verticalLayout_35 = QVBoxLayout(self.tab_8)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.label_101 = QLabel(self.tab_8)
        self.label_101.setObjectName(u"label_101")

        self.verticalLayout_35.addWidget(self.label_101)

        self.frame_25 = QFrame(self.tab_8)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.frame_26 = QFrame(self.frame_25)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.frame_26)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.frame_27 = QFrame(self.frame_26)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.lineEdit_22 = QLineEdit(self.frame_27)
        self.lineEdit_22.setObjectName(u"lineEdit_22")
        self.lineEdit_22.setMinimumSize(QSize(0, 30))
        self.lineEdit_22.setFont(font2)
        self.lineEdit_22.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.lineEdit_22.setStyleSheet(u"QLineEdit {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit::placeholder {\n"
"     color: Black;\n"
"    }\n"
"QLineEdit:focus {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit:disabled {\n"
"      background-color:SkyBlue; \n"
"   }")
        self.lineEdit_22.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.lineEdit_22)

        self.btn_pesquisar_prestadores = QPushButton(self.frame_27)
        self.btn_pesquisar_prestadores.setObjectName(u"btn_pesquisar_prestadores")
        self.btn_pesquisar_prestadores.setMinimumSize(QSize(100, 30))
        self.btn_pesquisar_prestadores.setFont(font1)
        self.btn_pesquisar_prestadores.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_pesquisar_prestadores.setStyleSheet(u"QPushButton {\n"
"  color: rgb(255, 255, 255);\n"
"  border-radius: 10px;\n"
"  font-size: 16px;\n"
"  background-color: rgb(0, 80, 121);\n"
"  border: 2px solid white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #87CEEB;\n"
"  color: black;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")

        self.horizontalLayout_15.addWidget(self.btn_pesquisar_prestadores)


        self.verticalLayout_36.addWidget(self.frame_27)

        self.tb_prestadores = QTableWidget(self.frame_26)
        if (self.tb_prestadores.columnCount() < 12):
            self.tb_prestadores.setColumnCount(12)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.tb_prestadores.setHorizontalHeaderItem(0, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.tb_prestadores.setHorizontalHeaderItem(1, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.tb_prestadores.setHorizontalHeaderItem(2, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.tb_prestadores.setHorizontalHeaderItem(3, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.tb_prestadores.setHorizontalHeaderItem(4, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        self.tb_prestadores.setHorizontalHeaderItem(5, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        self.tb_prestadores.setHorizontalHeaderItem(6, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        self.tb_prestadores.setHorizontalHeaderItem(7, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        self.tb_prestadores.setHorizontalHeaderItem(8, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        self.tb_prestadores.setHorizontalHeaderItem(9, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        self.tb_prestadores.setHorizontalHeaderItem(10, __qtablewidgetitem59)
        __qtablewidgetitem60 = QTableWidgetItem()
        self.tb_prestadores.setHorizontalHeaderItem(11, __qtablewidgetitem60)
        self.tb_prestadores.setObjectName(u"tb_prestadores")
        self.tb_prestadores.setStyleSheet(u"QTableWidget{\n"
"        background-color: SkyBlue;\n"
"    }\n"
"    QLineEdit:focus {\n"
"        background-color: SkyBlue;\n"
"    }\n"
"    QLineEdit:disabled {\n"
"        background-color: SkyBlue;\n"
"   }")

        self.verticalLayout_36.addWidget(self.tb_prestadores)


        self.horizontalLayout_16.addWidget(self.frame_26)


        self.verticalLayout_35.addWidget(self.frame_25)

        self.tabWidget_4.addTab(self.tab_8, "")

        self.verticalLayout_34.addWidget(self.tabWidget_4)

        self.Pages.addWidget(self.pg_prestadores)
        self.pg_encomendas = QWidget()
        self.pg_encomendas.setObjectName(u"pg_encomendas")
        self.verticalLayout_73 = QVBoxLayout(self.pg_encomendas)
        self.verticalLayout_73.setObjectName(u"verticalLayout_73")
        self.tabWidget_9 = QTabWidget(self.pg_encomendas)
        self.tabWidget_9.setObjectName(u"tabWidget_9")
        self.tabWidget_9.setStyleSheet(u"QTabWidget::pane {\n"
"  border: 1px solid  white;\n"
"  top:-1px; \n"
"  background: rgb(0, 80, 121);; \n"
"} \n"
"\n"
"QTabBar::tab {\n"
"\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(0, 61, 90, 255));\n"
"  border: 1px solid  rgb(249, 249, 249); \n"
"  padding: 10px;\n"
"color:white ;\n"
"} \n"
"\n"
"\n"
"QTabBar::tab:selected { \n"
"	background-color: SkyBlue;\n"
"  margin-bottom: -1px; \n"
" color: rgb(0, 85, 127);\n"
"	\n"
"}")
        self.tab_17 = QWidget()
        self.tab_17.setObjectName(u"tab_17")
        self.verticalLayout_37 = QVBoxLayout(self.tab_17)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.label_102 = QLabel(self.tab_17)
        self.label_102.setObjectName(u"label_102")

        self.verticalLayout_37.addWidget(self.label_102)

        self.scrollArea_8 = QScrollArea(self.tab_17)
        self.scrollArea_8.setObjectName(u"scrollArea_8")
        self.scrollArea_8.setWidgetResizable(True)
        self.scrollAreaWidgetContents_8 = QWidget()
        self.scrollAreaWidgetContents_8.setObjectName(u"scrollAreaWidgetContents_8")
        self.scrollAreaWidgetContents_8.setGeometry(QRect(0, 0, 695, 1045))
        self.verticalLayout_77 = QVBoxLayout(self.scrollAreaWidgetContents_8)
        self.verticalLayout_77.setObjectName(u"verticalLayout_77")
        self.frame_61 = QFrame(self.scrollAreaWidgetContents_8)
        self.frame_61.setObjectName(u"frame_61")
        self.frame_61.setFrameShape(QFrame.StyledPanel)
        self.frame_61.setFrameShadow(QFrame.Raised)
        self.verticalLayout_80 = QVBoxLayout(self.frame_61)
        self.verticalLayout_80.setObjectName(u"verticalLayout_80")
        self.label_81 = QLabel(self.frame_61)
        self.label_81.setObjectName(u"label_81")

        self.verticalLayout_80.addWidget(self.label_81)

        self.txt_numero_protocolo = QLineEdit(self.frame_61)
        self.txt_numero_protocolo.setObjectName(u"txt_numero_protocolo")
        self.txt_numero_protocolo.setMinimumSize(QSize(0, 30))
        self.txt_numero_protocolo.setFont(font2)
        self.txt_numero_protocolo.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_numero_protocolo.setStyleSheet(u"QLineEdit {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit::placeholder {\n"
"     color: Black;\n"
"    }\n"
"QLineEdit:focus {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit:disabled {\n"
"      background-color:SkyBlue; \n"
"   }")

        self.verticalLayout_80.addWidget(self.txt_numero_protocolo)

        self.label_82 = QLabel(self.frame_61)
        self.label_82.setObjectName(u"label_82")

        self.verticalLayout_80.addWidget(self.label_82)

        self.txt_data_hora_recebimento = QLineEdit(self.frame_61)
        self.txt_data_hora_recebimento.setObjectName(u"txt_data_hora_recebimento")
        self.txt_data_hora_recebimento.setMinimumSize(QSize(0, 30))
        self.txt_data_hora_recebimento.setFont(font2)
        self.txt_data_hora_recebimento.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_data_hora_recebimento.setStyleSheet(u"QLineEdit {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit::placeholder {\n"
"     color: Black;\n"
"    }\n"
"QLineEdit:focus {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit:disabled {\n"
"      background-color:SkyBlue; \n"
"   }")

        self.verticalLayout_80.addWidget(self.txt_data_hora_recebimento)

        self.label_83 = QLabel(self.frame_61)
        self.label_83.setObjectName(u"label_83")

        self.verticalLayout_80.addWidget(self.label_83)

        self.txt_nome_destinatario = QLineEdit(self.frame_61)
        self.txt_nome_destinatario.setObjectName(u"txt_nome_destinatario")
        self.txt_nome_destinatario.setMinimumSize(QSize(0, 30))
        self.txt_nome_destinatario.setFont(font2)
        self.txt_nome_destinatario.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_nome_destinatario.setStyleSheet(u"QLineEdit {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit::placeholder {\n"
"     color: Black;\n"
"    }\n"
"QLineEdit:focus {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit:disabled {\n"
"      background-color:SkyBlue; \n"
"   }")

        self.verticalLayout_80.addWidget(self.txt_nome_destinatario)

        self.frame_68 = QFrame(self.frame_61)
        self.frame_68.setObjectName(u"frame_68")
        sizePolicy.setHeightForWidth(self.frame_68.sizePolicy().hasHeightForWidth())
        self.frame_68.setSizePolicy(sizePolicy)
        self.frame_68.setFrameShape(QFrame.StyledPanel)
        self.frame_68.setFrameShadow(QFrame.Raised)
        self.verticalLayout_86 = QVBoxLayout(self.frame_68)
        self.verticalLayout_86.setObjectName(u"verticalLayout_86")
        self.label_115 = QLabel(self.frame_68)
        self.label_115.setObjectName(u"label_115")
        self.label_115.setMinimumSize(QSize(100, 0))

        self.verticalLayout_86.addWidget(self.label_115)

        self.txt_apartamento_bloco_encomendas = QLineEdit(self.frame_68)
        self.txt_apartamento_bloco_encomendas.setObjectName(u"txt_apartamento_bloco_encomendas")
        self.txt_apartamento_bloco_encomendas.setMinimumSize(QSize(100, 30))
        self.txt_apartamento_bloco_encomendas.setFont(font2)
        self.txt_apartamento_bloco_encomendas.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_apartamento_bloco_encomendas.setStyleSheet(u"QLineEdit {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit::placeholder {\n"
"     color: Black;\n"
"    }\n"
"QLineEdit:focus {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit:disabled {\n"
"      background-color:SkyBlue; \n"
"   }")

        self.verticalLayout_86.addWidget(self.txt_apartamento_bloco_encomendas, 0, Qt.AlignLeft)


        self.verticalLayout_80.addWidget(self.frame_68)

        self.label_86 = QLabel(self.frame_61)
        self.label_86.setObjectName(u"label_86")

        self.verticalLayout_80.addWidget(self.label_86)

        self.txt_numero_rastreamento = QLineEdit(self.frame_61)
        self.txt_numero_rastreamento.setObjectName(u"txt_numero_rastreamento")
        self.txt_numero_rastreamento.setMinimumSize(QSize(0, 30))
        self.txt_numero_rastreamento.setFont(font2)
        self.txt_numero_rastreamento.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_numero_rastreamento.setStyleSheet(u"QLineEdit {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit::placeholder {\n"
"     color: Black;\n"
"    }\n"
"QLineEdit:focus {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit:disabled {\n"
"      background-color:SkyBlue; \n"
"   }")

        self.verticalLayout_80.addWidget(self.txt_numero_rastreamento)

        self.label_87 = QLabel(self.frame_61)
        self.label_87.setObjectName(u"label_87")

        self.verticalLayout_80.addWidget(self.label_87)

        self.cmb_tipo_encomenda = QComboBox(self.frame_61)
        self.cmb_tipo_encomenda.addItem("")
        self.cmb_tipo_encomenda.addItem("")
        self.cmb_tipo_encomenda.addItem("")
        self.cmb_tipo_encomenda.setObjectName(u"cmb_tipo_encomenda")
        self.cmb_tipo_encomenda.setMinimumSize(QSize(0, 30))
        self.cmb_tipo_encomenda.setFont(font2)
        self.cmb_tipo_encomenda.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.cmb_tipo_encomenda.setStyleSheet(u"QComboBox{\n"
"        background-color: SkyBlue;\n"
"    }\n"
"    QLineEdit:focus {\n"
"        background-color: SkyBlue;\n"
"    }\n"
"    QLineEdit:disabled {\n"
"        background-color: SkyBlue; \n"
"   }")

        self.verticalLayout_80.addWidget(self.cmb_tipo_encomenda)

        self.frame_63 = QFrame(self.frame_61)
        self.frame_63.setObjectName(u"frame_63")
        self.frame_63.setFrameShape(QFrame.StyledPanel)
        self.frame_63.setFrameShadow(QFrame.Raised)
        self.verticalLayout_78 = QVBoxLayout(self.frame_63)
        self.verticalLayout_78.setObjectName(u"verticalLayout_78")
        self.label_88 = QLabel(self.frame_63)
        self.label_88.setObjectName(u"label_88")

        self.verticalLayout_78.addWidget(self.label_88)

        self.txt_descricao_encomenda = QTextEdit(self.frame_63)
        self.txt_descricao_encomenda.setObjectName(u"txt_descricao_encomenda")
        self.txt_descricao_encomenda.setMinimumSize(QSize(0, 50))
        self.txt_descricao_encomenda.setStyleSheet(u" QTextEdit {\n"
"        background-color: SkyBlue;\n"
"    }\n"
"    QTextEdit:focus {\n"
"        background-color: SkyBlue;\n"
"    }\n"
"    QTextEdit:read-only {\n"
"        background-color: SkyBlue; \n"
"    }")

        self.verticalLayout_78.addWidget(self.txt_descricao_encomenda)


        self.verticalLayout_80.addWidget(self.frame_63)

        self.label_89 = QLabel(self.frame_61)
        self.label_89.setObjectName(u"label_89")

        self.verticalLayout_80.addWidget(self.label_89)

        self.txt_empresa_entrega = QLineEdit(self.frame_61)
        self.txt_empresa_entrega.setObjectName(u"txt_empresa_entrega")
        self.txt_empresa_entrega.setMinimumSize(QSize(0, 30))
        self.txt_empresa_entrega.setFont(font2)
        self.txt_empresa_entrega.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_empresa_entrega.setStyleSheet(u"QLineEdit {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit::placeholder {\n"
"     color: Black;\n"
"    }\n"
"QLineEdit:focus {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit:disabled {\n"
"      background-color:SkyBlue; \n"
"   }")

        self.verticalLayout_80.addWidget(self.txt_empresa_entrega)

        self.frame_64 = QFrame(self.frame_61)
        self.frame_64.setObjectName(u"frame_64")
        self.frame_64.setFrameShape(QFrame.StyledPanel)
        self.frame_64.setFrameShadow(QFrame.Raised)
        self.verticalLayout_79 = QVBoxLayout(self.frame_64)
        self.verticalLayout_79.setObjectName(u"verticalLayout_79")
        self.label_90 = QLabel(self.frame_64)
        self.label_90.setObjectName(u"label_90")

        self.verticalLayout_79.addWidget(self.label_90)

        self.txt_observacoes_encomendas = QTextEdit(self.frame_64)
        self.txt_observacoes_encomendas.setObjectName(u"txt_observacoes_encomendas")
        self.txt_observacoes_encomendas.setMinimumSize(QSize(0, 50))
        self.txt_observacoes_encomendas.setStyleSheet(u" QTextEdit {\n"
"        background-color: SkyBlue;\n"
"    }\n"
"    QTextEdit:focus {\n"
"        background-color: SkyBlue;\n"
"    }\n"
"    QTextEdit:read-only {\n"
"        background-color: SkyBlue; \n"
"    }")

        self.verticalLayout_79.addWidget(self.txt_observacoes_encomendas)


        self.verticalLayout_80.addWidget(self.frame_64)

        self.label_91 = QLabel(self.frame_61)
        self.label_91.setObjectName(u"label_91")

        self.verticalLayout_80.addWidget(self.label_91)

        self.txt_nome_entregador = QLineEdit(self.frame_61)
        self.txt_nome_entregador.setObjectName(u"txt_nome_entregador")
        self.txt_nome_entregador.setMinimumSize(QSize(0, 30))
        self.txt_nome_entregador.setFont(font2)
        self.txt_nome_entregador.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_nome_entregador.setStyleSheet(u"QLineEdit {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit::placeholder {\n"
"     color: Black;\n"
"    }\n"
"QLineEdit:focus {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit:disabled {\n"
"      background-color:SkyBlue; \n"
"   }")

        self.verticalLayout_80.addWidget(self.txt_nome_entregador)

        self.txt_rg_cpf_entregador = QLineEdit(self.frame_61)
        self.txt_rg_cpf_entregador.setObjectName(u"txt_rg_cpf_entregador")
        self.txt_rg_cpf_entregador.setMinimumSize(QSize(0, 30))
        self.txt_rg_cpf_entregador.setFont(font2)
        self.txt_rg_cpf_entregador.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_rg_cpf_entregador.setStyleSheet(u"QLineEdit {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit::placeholder {\n"
"     color: Black;\n"
"    }\n"
"QLineEdit:focus {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit:disabled {\n"
"      background-color:SkyBlue; \n"
"   }")

        self.verticalLayout_80.addWidget(self.txt_rg_cpf_entregador)

        self.label_92 = QLabel(self.frame_61)
        self.label_92.setObjectName(u"label_92")

        self.verticalLayout_80.addWidget(self.label_92)

        self.txt_nome_porteiro = QLineEdit(self.frame_61)
        self.txt_nome_porteiro.setObjectName(u"txt_nome_porteiro")
        self.txt_nome_porteiro.setMinimumSize(QSize(0, 30))
        self.txt_nome_porteiro.setFont(font2)
        self.txt_nome_porteiro.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_nome_porteiro.setStyleSheet(u"QLineEdit {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit::placeholder {\n"
"     color: Black;\n"
"    }\n"
"QLineEdit:focus {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit:disabled {\n"
"      background-color:SkyBlue; \n"
"   }")

        self.verticalLayout_80.addWidget(self.txt_nome_porteiro)

        self.label_93 = QLabel(self.frame_61)
        self.label_93.setObjectName(u"label_93")

        self.verticalLayout_80.addWidget(self.label_93)

        self.txt_nome_retirou = QLineEdit(self.frame_61)
        self.txt_nome_retirou.setObjectName(u"txt_nome_retirou")
        self.txt_nome_retirou.setMinimumSize(QSize(0, 30))
        self.txt_nome_retirou.setFont(font2)
        self.txt_nome_retirou.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_nome_retirou.setStyleSheet(u"QLineEdit {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit::placeholder {\n"
"     color: Black;\n"
"    }\n"
"QLineEdit:focus {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit:disabled {\n"
"      background-color:SkyBlue; \n"
"   }")

        self.verticalLayout_80.addWidget(self.txt_nome_retirou)

        self.btn_registrar_encomendas = QPushButton(self.frame_61)
        self.btn_registrar_encomendas.setObjectName(u"btn_registrar_encomendas")
        self.btn_registrar_encomendas.setMinimumSize(QSize(180, 30))
        self.btn_registrar_encomendas.setFont(font1)
        self.btn_registrar_encomendas.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_registrar_encomendas.setStyleSheet(u"QPushButton {\n"
"  color: rgb(255, 255, 255);\n"
"  border-radius: 10px;\n"
"  font-size: 16px;\n"
"  background-color: rgb(0, 80, 121);\n"
"  border: 2px solid white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #87CEEB;\n"
"  color: black;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")

        self.verticalLayout_80.addWidget(self.btn_registrar_encomendas, 0, Qt.AlignHCenter)


        self.verticalLayout_77.addWidget(self.frame_61)

        self.scrollArea_8.setWidget(self.scrollAreaWidgetContents_8)

        self.verticalLayout_37.addWidget(self.scrollArea_8)

        self.tabWidget_9.addTab(self.tab_17, "")
        self.tab_18 = QWidget()
        self.tab_18.setObjectName(u"tab_18")
        self.verticalLayout_76 = QVBoxLayout(self.tab_18)
        self.verticalLayout_76.setObjectName(u"verticalLayout_76")
        self.label_103 = QLabel(self.tab_18)
        self.label_103.setObjectName(u"label_103")

        self.verticalLayout_76.addWidget(self.label_103)

        self.frame_58 = QFrame(self.tab_18)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setFrameShape(QFrame.StyledPanel)
        self.frame_58.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_58)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.frame_59 = QFrame(self.frame_58)
        self.frame_59.setObjectName(u"frame_59")
        self.frame_59.setFrameShape(QFrame.StyledPanel)
        self.frame_59.setFrameShadow(QFrame.Raised)
        self.verticalLayout_75 = QVBoxLayout(self.frame_59)
        self.verticalLayout_75.setObjectName(u"verticalLayout_75")
        self.frame_60 = QFrame(self.frame_59)
        self.frame_60.setObjectName(u"frame_60")
        self.frame_60.setFrameShape(QFrame.StyledPanel)
        self.frame_60.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_60)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.txt_pesquisar_encomendas = QLineEdit(self.frame_60)
        self.txt_pesquisar_encomendas.setObjectName(u"txt_pesquisar_encomendas")
        self.txt_pesquisar_encomendas.setMinimumSize(QSize(0, 30))
        self.txt_pesquisar_encomendas.setFont(font2)
        self.txt_pesquisar_encomendas.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_pesquisar_encomendas.setStyleSheet(u"QLineEdit {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit::placeholder {\n"
"     color: Black;\n"
"    }\n"
"QLineEdit:focus {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit:disabled {\n"
"      background-color:SkyBlue; \n"
"   }")
        self.txt_pesquisar_encomendas.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_30.addWidget(self.txt_pesquisar_encomendas)

        self.btn_pesquisar_encomendas = QPushButton(self.frame_60)
        self.btn_pesquisar_encomendas.setObjectName(u"btn_pesquisar_encomendas")
        self.btn_pesquisar_encomendas.setMinimumSize(QSize(100, 30))
        self.btn_pesquisar_encomendas.setFont(font1)
        self.btn_pesquisar_encomendas.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_pesquisar_encomendas.setStyleSheet(u"QPushButton {\n"
"  color: rgb(255, 255, 255);\n"
"  border-radius: 10px;\n"
"  font-size: 16px;\n"
"  background-color: rgb(0, 80, 121);\n"
"  border: 2px solid white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #87CEEB;\n"
"  color: black;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")

        self.horizontalLayout_30.addWidget(self.btn_pesquisar_encomendas)


        self.verticalLayout_75.addWidget(self.frame_60)

        self.tb_encomendas = QTableWidget(self.frame_59)
        if (self.tb_encomendas.columnCount() < 14):
            self.tb_encomendas.setColumnCount(14)
        __qtablewidgetitem61 = QTableWidgetItem()
        self.tb_encomendas.setHorizontalHeaderItem(0, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        self.tb_encomendas.setHorizontalHeaderItem(1, __qtablewidgetitem62)
        __qtablewidgetitem63 = QTableWidgetItem()
        self.tb_encomendas.setHorizontalHeaderItem(2, __qtablewidgetitem63)
        __qtablewidgetitem64 = QTableWidgetItem()
        self.tb_encomendas.setHorizontalHeaderItem(3, __qtablewidgetitem64)
        __qtablewidgetitem65 = QTableWidgetItem()
        self.tb_encomendas.setHorizontalHeaderItem(4, __qtablewidgetitem65)
        __qtablewidgetitem66 = QTableWidgetItem()
        self.tb_encomendas.setHorizontalHeaderItem(5, __qtablewidgetitem66)
        __qtablewidgetitem67 = QTableWidgetItem()
        self.tb_encomendas.setHorizontalHeaderItem(6, __qtablewidgetitem67)
        __qtablewidgetitem68 = QTableWidgetItem()
        self.tb_encomendas.setHorizontalHeaderItem(7, __qtablewidgetitem68)
        __qtablewidgetitem69 = QTableWidgetItem()
        self.tb_encomendas.setHorizontalHeaderItem(8, __qtablewidgetitem69)
        __qtablewidgetitem70 = QTableWidgetItem()
        self.tb_encomendas.setHorizontalHeaderItem(9, __qtablewidgetitem70)
        __qtablewidgetitem71 = QTableWidgetItem()
        self.tb_encomendas.setHorizontalHeaderItem(10, __qtablewidgetitem71)
        __qtablewidgetitem72 = QTableWidgetItem()
        self.tb_encomendas.setHorizontalHeaderItem(11, __qtablewidgetitem72)
        __qtablewidgetitem73 = QTableWidgetItem()
        self.tb_encomendas.setHorizontalHeaderItem(12, __qtablewidgetitem73)
        __qtablewidgetitem74 = QTableWidgetItem()
        self.tb_encomendas.setHorizontalHeaderItem(13, __qtablewidgetitem74)
        self.tb_encomendas.setObjectName(u"tb_encomendas")
        self.tb_encomendas.setStyleSheet(u"QTableWidget{\n"
"        background-color: SkyBlue;\n"
"    }\n"
"    QLineEdit:focus {\n"
"        background-color: SkyBlue;\n"
"    }\n"
"    QLineEdit:disabled {\n"
"        background-color: SkyBlue;\n"
"   }")

        self.verticalLayout_75.addWidget(self.tb_encomendas)


        self.horizontalLayout_29.addWidget(self.frame_59)


        self.verticalLayout_76.addWidget(self.frame_58)

        self.tabWidget_9.addTab(self.tab_18, "")

        self.verticalLayout_73.addWidget(self.tabWidget_9)

        self.Pages.addWidget(self.pg_encomendas)
        self.pg_ocorrencias = QWidget()
        self.pg_ocorrencias.setObjectName(u"pg_ocorrencias")
        self.verticalLayout_65 = QVBoxLayout(self.pg_ocorrencias)
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.tabWidget_8 = QTabWidget(self.pg_ocorrencias)
        self.tabWidget_8.setObjectName(u"tabWidget_8")
        self.tabWidget_8.setStyleSheet(u"QTabWidget::pane {\n"
"  border: 1px solid  white;\n"
"  top:-1px; \n"
"  background: rgb(0, 80, 121);; \n"
"} \n"
"\n"
"QTabBar::tab {\n"
"\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(0, 61, 90, 255));\n"
"  border: 1px solid  rgb(249, 249, 249); \n"
"  padding: 10px;\n"
"color:white ;\n"
"} \n"
"\n"
"\n"
"QTabBar::tab:selected { \n"
"	background-color: SkyBlue;\n"
"  margin-bottom: -1px; \n"
" color: rgb(0, 85, 127);\n"
"	\n"
"}\n"
"")
        self.tab_15 = QWidget()
        self.tab_15.setObjectName(u"tab_15")
        self.verticalLayout_67 = QVBoxLayout(self.tab_15)
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")
        self.label_104 = QLabel(self.tab_15)
        self.label_104.setObjectName(u"label_104")

        self.verticalLayout_67.addWidget(self.label_104)

        self.scrollArea_7 = QScrollArea(self.tab_15)
        self.scrollArea_7.setObjectName(u"scrollArea_7")
        self.scrollArea_7.setWidgetResizable(True)
        self.scrollAreaWidgetContents_7 = QWidget()
        self.scrollAreaWidgetContents_7.setObjectName(u"scrollAreaWidgetContents_7")
        self.scrollAreaWidgetContents_7.setGeometry(QRect(0, 0, 695, 528))
        self.verticalLayout_68 = QVBoxLayout(self.scrollAreaWidgetContents_7)
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.frame_53 = QFrame(self.scrollAreaWidgetContents_7)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setFrameShape(QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QFrame.Raised)
        self.verticalLayout_70 = QVBoxLayout(self.frame_53)
        self.verticalLayout_70.setObjectName(u"verticalLayout_70")
        self.label_73 = QLabel(self.frame_53)
        self.label_73.setObjectName(u"label_73")

        self.verticalLayout_70.addWidget(self.label_73)

        self.txt_numero_protocolo_ocorrencias = QLineEdit(self.frame_53)
        self.txt_numero_protocolo_ocorrencias.setObjectName(u"txt_numero_protocolo_ocorrencias")
        self.txt_numero_protocolo_ocorrencias.setMinimumSize(QSize(0, 30))
        self.txt_numero_protocolo_ocorrencias.setFont(font2)
        self.txt_numero_protocolo_ocorrencias.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_numero_protocolo_ocorrencias.setStyleSheet(u"QLineEdit {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit::placeholder {\n"
"     color: Black;\n"
"    }\n"
"QLineEdit:focus {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit:disabled {\n"
"      background-color:SkyBlue; \n"
"   }")

        self.verticalLayout_70.addWidget(self.txt_numero_protocolo_ocorrencias)

        self.label_74 = QLabel(self.frame_53)
        self.label_74.setObjectName(u"label_74")

        self.verticalLayout_70.addWidget(self.label_74)

        self.txt_data_ocorrencia = QLineEdit(self.frame_53)
        self.txt_data_ocorrencia.setObjectName(u"txt_data_ocorrencia")
        self.txt_data_ocorrencia.setMinimumSize(QSize(0, 30))
        self.txt_data_ocorrencia.setFont(font2)
        self.txt_data_ocorrencia.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_data_ocorrencia.setStyleSheet(u"QLineEdit {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit::placeholder {\n"
"     color: Black;\n"
"    }\n"
"QLineEdit:focus {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit:disabled {\n"
"      background-color:SkyBlue; \n"
"   }")

        self.verticalLayout_70.addWidget(self.txt_data_ocorrencia)

        self.label_75 = QLabel(self.frame_53)
        self.label_75.setObjectName(u"label_75")

        self.verticalLayout_70.addWidget(self.label_75)

        self.txt_nome_funcionario = QLineEdit(self.frame_53)
        self.txt_nome_funcionario.setObjectName(u"txt_nome_funcionario")
        self.txt_nome_funcionario.setMinimumSize(QSize(0, 30))
        self.txt_nome_funcionario.setFont(font2)
        self.txt_nome_funcionario.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_nome_funcionario.setStyleSheet(u"QLineEdit {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit::placeholder {\n"
"     color: Black;\n"
"    }\n"
"QLineEdit:focus {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit:disabled {\n"
"      background-color:SkyBlue; \n"
"   }")

        self.verticalLayout_70.addWidget(self.txt_nome_funcionario)

        self.label_78 = QLabel(self.frame_53)
        self.label_78.setObjectName(u"label_78")

        self.verticalLayout_70.addWidget(self.label_78)

        self.txt_hora_registro = QLineEdit(self.frame_53)
        self.txt_hora_registro.setObjectName(u"txt_hora_registro")
        self.txt_hora_registro.setMinimumSize(QSize(0, 30))
        self.txt_hora_registro.setFont(font2)
        self.txt_hora_registro.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_hora_registro.setStyleSheet(u"QLineEdit {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit::placeholder {\n"
"     color: Black;\n"
"    }\n"
"QLineEdit:focus {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit:disabled {\n"
"      background-color:SkyBlue; \n"
"   }")

        self.verticalLayout_70.addWidget(self.txt_hora_registro)

        self.label_79 = QLabel(self.frame_53)
        self.label_79.setObjectName(u"label_79")

        self.verticalLayout_70.addWidget(self.label_79)

        self.txt_data_registro = QLineEdit(self.frame_53)
        self.txt_data_registro.setObjectName(u"txt_data_registro")
        self.txt_data_registro.setMinimumSize(QSize(0, 30))
        self.txt_data_registro.setFont(font2)
        self.txt_data_registro.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_data_registro.setStyleSheet(u"QLineEdit {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit::placeholder {\n"
"     color: Black;\n"
"    }\n"
"QLineEdit:focus {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit:disabled {\n"
"      background-color:SkyBlue; \n"
"   }")

        self.verticalLayout_70.addWidget(self.txt_data_registro)

        self.frame_54 = QFrame(self.frame_53)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setFrameShape(QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QFrame.Raised)
        self.verticalLayout_69 = QVBoxLayout(self.frame_54)
        self.verticalLayout_69.setObjectName(u"verticalLayout_69")
        self.label_80 = QLabel(self.frame_54)
        self.label_80.setObjectName(u"label_80")

        self.verticalLayout_69.addWidget(self.label_80)

        self.txt_descricao = QTextEdit(self.frame_54)
        self.txt_descricao.setObjectName(u"txt_descricao")
        self.txt_descricao.setMinimumSize(QSize(0, 50))
        self.txt_descricao.setStyleSheet(u"QTextEdit {\n"
"        background-color: SkyBlue;\n"
"    }\n"
"    QTextEdit:focus {\n"
"        background-color: SkyBlue;\n"
"    }\n"
"    QTextEdit:read-only {\n"
"        background-color: SkyBlue;\n"
"    }\n"
"")

        self.verticalLayout_69.addWidget(self.txt_descricao)


        self.verticalLayout_70.addWidget(self.frame_54)


        self.verticalLayout_68.addWidget(self.frame_53)

        self.btn_registrar_ocorrencias = QPushButton(self.scrollAreaWidgetContents_7)
        self.btn_registrar_ocorrencias.setObjectName(u"btn_registrar_ocorrencias")
        self.btn_registrar_ocorrencias.setMinimumSize(QSize(180, 30))
        self.btn_registrar_ocorrencias.setFont(font1)
        self.btn_registrar_ocorrencias.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_registrar_ocorrencias.setStyleSheet(u"QPushButton {\n"
"  color: rgb(255, 255, 255);\n"
"  border-radius: 10px;\n"
"  font-size: 16px;\n"
"  background-color: rgb(0, 80, 121);\n"
"  border: 2px solid white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #87CEEB;\n"
"  color: black;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")

        self.verticalLayout_68.addWidget(self.btn_registrar_ocorrencias, 0, Qt.AlignHCenter)

        self.scrollArea_7.setWidget(self.scrollAreaWidgetContents_7)

        self.verticalLayout_67.addWidget(self.scrollArea_7)

        self.tabWidget_8.addTab(self.tab_15, "")
        self.tab_16 = QWidget()
        self.tab_16.setObjectName(u"tab_16")
        self.verticalLayout_66 = QVBoxLayout(self.tab_16)
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.label_105 = QLabel(self.tab_16)
        self.label_105.setObjectName(u"label_105")

        self.verticalLayout_66.addWidget(self.label_105)

        self.frame_55 = QFrame(self.tab_16)
        self.frame_55.setObjectName(u"frame_55")
        self.frame_55.setFrameShape(QFrame.StyledPanel)
        self.frame_55.setFrameShadow(QFrame.Raised)
        self.verticalLayout_72 = QVBoxLayout(self.frame_55)
        self.verticalLayout_72.setObjectName(u"verticalLayout_72")
        self.frame_56 = QFrame(self.frame_55)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setFrameShape(QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QFrame.Raised)
        self.verticalLayout_71 = QVBoxLayout(self.frame_56)
        self.verticalLayout_71.setObjectName(u"verticalLayout_71")
        self.frame_57 = QFrame(self.frame_56)
        self.frame_57.setObjectName(u"frame_57")
        self.frame_57.setFrameShape(QFrame.StyledPanel)
        self.frame_57.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_57)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.txt_pesquisa_ocorrencia = QLineEdit(self.frame_57)
        self.txt_pesquisa_ocorrencia.setObjectName(u"txt_pesquisa_ocorrencia")
        self.txt_pesquisa_ocorrencia.setMinimumSize(QSize(0, 30))
        self.txt_pesquisa_ocorrencia.setFont(font2)
        self.txt_pesquisa_ocorrencia.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_pesquisa_ocorrencia.setStyleSheet(u"QLineEdit {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit::placeholder {\n"
"     color: Black;\n"
"    }\n"
"QLineEdit:focus {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit:disabled {\n"
"      background-color:SkyBlue; \n"
"   }")
        self.txt_pesquisa_ocorrencia.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_28.addWidget(self.txt_pesquisa_ocorrencia)

        self.btn_pesquisar_ocorrencias = QPushButton(self.frame_57)
        self.btn_pesquisar_ocorrencias.setObjectName(u"btn_pesquisar_ocorrencias")
        self.btn_pesquisar_ocorrencias.setMinimumSize(QSize(100, 30))
        self.btn_pesquisar_ocorrencias.setFont(font1)
        self.btn_pesquisar_ocorrencias.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_pesquisar_ocorrencias.setStyleSheet(u"QPushButton {\n"
"  color: rgb(255, 255, 255);\n"
"  border-radius: 10px;\n"
"  font-size: 16px;\n"
"  background-color: rgb(0, 80, 121);\n"
"  border: 2px solid white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #87CEEB;\n"
"  color: black;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")

        self.horizontalLayout_28.addWidget(self.btn_pesquisar_ocorrencias)


        self.verticalLayout_71.addWidget(self.frame_57)

        self.tb_ocorrencias = QTableWidget(self.frame_56)
        if (self.tb_ocorrencias.columnCount() < 7):
            self.tb_ocorrencias.setColumnCount(7)
        __qtablewidgetitem75 = QTableWidgetItem()
        self.tb_ocorrencias.setHorizontalHeaderItem(0, __qtablewidgetitem75)
        __qtablewidgetitem76 = QTableWidgetItem()
        self.tb_ocorrencias.setHorizontalHeaderItem(1, __qtablewidgetitem76)
        __qtablewidgetitem77 = QTableWidgetItem()
        self.tb_ocorrencias.setHorizontalHeaderItem(2, __qtablewidgetitem77)
        __qtablewidgetitem78 = QTableWidgetItem()
        self.tb_ocorrencias.setHorizontalHeaderItem(3, __qtablewidgetitem78)
        __qtablewidgetitem79 = QTableWidgetItem()
        self.tb_ocorrencias.setHorizontalHeaderItem(4, __qtablewidgetitem79)
        __qtablewidgetitem80 = QTableWidgetItem()
        self.tb_ocorrencias.setHorizontalHeaderItem(5, __qtablewidgetitem80)
        __qtablewidgetitem81 = QTableWidgetItem()
        self.tb_ocorrencias.setHorizontalHeaderItem(6, __qtablewidgetitem81)
        self.tb_ocorrencias.setObjectName(u"tb_ocorrencias")
        self.tb_ocorrencias.setStyleSheet(u"QTableWidget{\n"
"        background-color: SkyBlue;\n"
"    }\n"
"    QLineEdit:focus {\n"
"        background-color: SkyBlue;\n"
"    }\n"
"    QLineEdit:disabled {\n"
"        background-color: SkyBlue;\n"
"   }")

        self.verticalLayout_71.addWidget(self.tb_ocorrencias)


        self.verticalLayout_72.addWidget(self.frame_56)


        self.verticalLayout_66.addWidget(self.frame_55)

        self.tabWidget_8.addTab(self.tab_16, "")

        self.verticalLayout_65.addWidget(self.tabWidget_8)

        self.Pages.addWidget(self.pg_ocorrencias)
        self.pg_funcionarios = QWidget()
        self.pg_funcionarios.setObjectName(u"pg_funcionarios")
        self.verticalLayout_28 = QVBoxLayout(self.pg_funcionarios)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.tabWidget_3 = QTabWidget(self.pg_funcionarios)
        self.tabWidget_3.setObjectName(u"tabWidget_3")
        self.tabWidget_3.setStyleSheet(u"QTabWidget::pane {\n"
"  border: 1px solid  white;\n"
"  top:-1px; \n"
"  background: rgb(0, 80, 121);; \n"
"} \n"
"\n"
"QTabBar::tab {\n"
"\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(0, 61, 90, 255));\n"
"  border: 1px solid  rgb(249, 249, 249); \n"
"  padding: 10px;\n"
"color:white ;\n"
"} \n"
"\n"
"\n"
"QTabBar::tab:selected { \n"
"	background-color: SkyBlue;\n"
"  margin-bottom: -1px; \n"
" color: rgb(0, 85, 127);\n"
"	\n"
"}\n"
"")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.verticalLayout_31 = QVBoxLayout(self.tab_5)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.label_106 = QLabel(self.tab_5)
        self.label_106.setObjectName(u"label_106")

        self.verticalLayout_31.addWidget(self.label_106)

        self.frame_20 = QFrame(self.tab_5)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_20)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.label_27 = QLabel(self.frame_20)
        self.label_27.setObjectName(u"label_27")

        self.verticalLayout_29.addWidget(self.label_27)

        self.txt_nome_funcionarios = QLineEdit(self.frame_20)
        self.txt_nome_funcionarios.setObjectName(u"txt_nome_funcionarios")
        self.txt_nome_funcionarios.setMinimumSize(QSize(0, 30))
        self.txt_nome_funcionarios.setFont(font2)
        self.txt_nome_funcionarios.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_nome_funcionarios.setStyleSheet(u"QLineEdit {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit::placeholder {\n"
"     color: Black;\n"
"    }\n"
"QLineEdit:focus {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit:disabled {\n"
"      background-color:SkyBlue; \n"
"   }")

        self.verticalLayout_29.addWidget(self.txt_nome_funcionarios)

        self.label_28 = QLabel(self.frame_20)
        self.label_28.setObjectName(u"label_28")

        self.verticalLayout_29.addWidget(self.label_28)

        self.txt_endereco_funcionario = QLineEdit(self.frame_20)
        self.txt_endereco_funcionario.setObjectName(u"txt_endereco_funcionario")
        self.txt_endereco_funcionario.setMinimumSize(QSize(0, 30))
        self.txt_endereco_funcionario.setFont(font2)
        self.txt_endereco_funcionario.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_endereco_funcionario.setStyleSheet(u"QLineEdit {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit::placeholder {\n"
"     color: Black;\n"
"    }\n"
"QLineEdit:focus {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit:disabled {\n"
"      background-color:SkyBlue; \n"
"   }")

        self.verticalLayout_29.addWidget(self.txt_endereco_funcionario)

        self.frame_21 = QFrame(self.frame_20)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_29 = QLabel(self.frame_21)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_12.addWidget(self.label_29)

        self.txt_bairro_funcionario = QLineEdit(self.frame_21)
        self.txt_bairro_funcionario.setObjectName(u"txt_bairro_funcionario")
        self.txt_bairro_funcionario.setMinimumSize(QSize(0, 30))
        self.txt_bairro_funcionario.setFont(font2)
        self.txt_bairro_funcionario.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_bairro_funcionario.setStyleSheet(u"QLineEdit {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit::placeholder {\n"
"     color: Black;\n"
"    }\n"
"QLineEdit:focus {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit:disabled {\n"
"      background-color:SkyBlue; \n"
"   }")

        self.horizontalLayout_12.addWidget(self.txt_bairro_funcionario)

        self.label_30 = QLabel(self.frame_21)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_12.addWidget(self.label_30)

        self.txt_cep_funcionario = QLineEdit(self.frame_21)
        self.txt_cep_funcionario.setObjectName(u"txt_cep_funcionario")
        self.txt_cep_funcionario.setMinimumSize(QSize(0, 30))
        self.txt_cep_funcionario.setFont(font2)
        self.txt_cep_funcionario.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_cep_funcionario.setStyleSheet(u"QLineEdit {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit::placeholder {\n"
"     color: Black;\n"
"    }\n"
"QLineEdit:focus {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit:disabled {\n"
"      background-color:SkyBlue; \n"
"   }")

        self.horizontalLayout_12.addWidget(self.txt_cep_funcionario)


        self.verticalLayout_29.addWidget(self.frame_21)

        self.frame_22 = QFrame(self.frame_20)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_31 = QLabel(self.frame_22)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_13.addWidget(self.label_31)

        self.txt_telefone_funcionario = QLineEdit(self.frame_22)
        self.txt_telefone_funcionario.setObjectName(u"txt_telefone_funcionario")
        self.txt_telefone_funcionario.setMinimumSize(QSize(0, 30))
        self.txt_telefone_funcionario.setFont(font2)
        self.txt_telefone_funcionario.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_telefone_funcionario.setStyleSheet(u"QLineEdit {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit::placeholder {\n"
"     color: Black;\n"
"    }\n"
"QLineEdit:focus {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit:disabled {\n"
"      background-color:SkyBlue; \n"
"   }")

        self.horizontalLayout_13.addWidget(self.txt_telefone_funcionario)

        self.label_32 = QLabel(self.frame_22)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_13.addWidget(self.label_32)

        self.txt_celular_funcionario = QLineEdit(self.frame_22)
        self.txt_celular_funcionario.setObjectName(u"txt_celular_funcionario")
        self.txt_celular_funcionario.setMinimumSize(QSize(0, 30))
        self.txt_celular_funcionario.setFont(font2)
        self.txt_celular_funcionario.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_celular_funcionario.setStyleSheet(u"QLineEdit {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit::placeholder {\n"
"     color: Black;\n"
"    }\n"
"QLineEdit:focus {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit:disabled {\n"
"      background-color:SkyBlue; \n"
"   }")

        self.horizontalLayout_13.addWidget(self.txt_celular_funcionario)


        self.verticalLayout_29.addWidget(self.frame_22)

        self.label_33 = QLabel(self.frame_20)
        self.label_33.setObjectName(u"label_33")

        self.verticalLayout_29.addWidget(self.label_33)

        self.txt_email_funcionario = QLineEdit(self.frame_20)
        self.txt_email_funcionario.setObjectName(u"txt_email_funcionario")
        self.txt_email_funcionario.setMinimumSize(QSize(0, 30))
        self.txt_email_funcionario.setFont(font2)
        self.txt_email_funcionario.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_email_funcionario.setStyleSheet(u"QLineEdit {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit::placeholder {\n"
"     color: Black;\n"
"    }\n"
"QLineEdit:focus {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit:disabled {\n"
"      background-color:SkyBlue; \n"
"   }")

        self.verticalLayout_29.addWidget(self.txt_email_funcionario)

        self.frame_19 = QFrame(self.frame_20)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_19)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.label_26 = QLabel(self.frame_19)
        self.label_26.setObjectName(u"label_26")

        self.verticalLayout_30.addWidget(self.label_26)

        self.txt_observacao_funcionario = QTextEdit(self.frame_19)
        self.txt_observacao_funcionario.setObjectName(u"txt_observacao_funcionario")
        self.txt_observacao_funcionario.setMinimumSize(QSize(0, 50))
        self.txt_observacao_funcionario.setStyleSheet(u"QTextEdit {\n"
"        background-color: SkyBlue\n"
"    }\n"
"    QTextEdit:focus {\n"
"        background-color: SkyBlue;\n"
"    }\n"
"    QTextEdit:read-only {\n"
"        background-color: SkyBlue;\n"
"    }\n"
"")

        self.verticalLayout_30.addWidget(self.txt_observacao_funcionario)


        self.verticalLayout_29.addWidget(self.frame_19)


        self.verticalLayout_31.addWidget(self.frame_20)

        self.btn_registrar_funcionarios = QPushButton(self.tab_5)
        self.btn_registrar_funcionarios.setObjectName(u"btn_registrar_funcionarios")
        self.btn_registrar_funcionarios.setMinimumSize(QSize(180, 30))
        self.btn_registrar_funcionarios.setFont(font1)
        self.btn_registrar_funcionarios.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_registrar_funcionarios.setStyleSheet(u"QPushButton {\n"
"  color: rgb(255, 255, 255);\n"
"  border-radius: 10px;\n"
"  font-size: 16px;\n"
"  background-color: rgb(0, 80, 121);\n"
"  border: 2px solid white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #87CEEB;\n"
"  color: black;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")

        self.verticalLayout_31.addWidget(self.btn_registrar_funcionarios, 0, Qt.AlignHCenter)

        self.tabWidget_3.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.verticalLayout_33 = QVBoxLayout(self.tab_6)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.label_107 = QLabel(self.tab_6)
        self.label_107.setObjectName(u"label_107")

        self.verticalLayout_33.addWidget(self.label_107)

        self.frame_23 = QFrame(self.tab_6)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_23)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.frame_24 = QFrame(self.frame_23)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.txt_pesquisar_funcionario = QLineEdit(self.frame_24)
        self.txt_pesquisar_funcionario.setObjectName(u"txt_pesquisar_funcionario")
        self.txt_pesquisar_funcionario.setMinimumSize(QSize(0, 30))
        self.txt_pesquisar_funcionario.setFont(font2)
        self.txt_pesquisar_funcionario.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_pesquisar_funcionario.setStyleSheet(u"QLineEdit {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit::placeholder {\n"
"     color: Black;\n"
"    }\n"
"QLineEdit:focus {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit:disabled {\n"
"      background-color:SkyBlue; \n"
"   }")
        self.txt_pesquisar_funcionario.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.txt_pesquisar_funcionario)

        self.btn_pesquisar_funcionarios = QPushButton(self.frame_24)
        self.btn_pesquisar_funcionarios.setObjectName(u"btn_pesquisar_funcionarios")
        self.btn_pesquisar_funcionarios.setMinimumSize(QSize(100, 30))
        self.btn_pesquisar_funcionarios.setFont(font1)
        self.btn_pesquisar_funcionarios.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_pesquisar_funcionarios.setStyleSheet(u"QPushButton {\n"
"  color: rgb(255, 255, 255);\n"
"  border-radius: 10px;\n"
"  font-size: 16px;\n"
"  background-color: rgb(0, 80, 121);\n"
"  border: 2px solid white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #87CEEB;\n"
"  color: black;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")

        self.horizontalLayout_14.addWidget(self.btn_pesquisar_funcionarios)


        self.verticalLayout_32.addWidget(self.frame_24)

        self.tb_funcionarios = QTableWidget(self.frame_23)
        if (self.tb_funcionarios.columnCount() < 9):
            self.tb_funcionarios.setColumnCount(9)
        __qtablewidgetitem82 = QTableWidgetItem()
        self.tb_funcionarios.setHorizontalHeaderItem(0, __qtablewidgetitem82)
        __qtablewidgetitem83 = QTableWidgetItem()
        self.tb_funcionarios.setHorizontalHeaderItem(1, __qtablewidgetitem83)
        __qtablewidgetitem84 = QTableWidgetItem()
        self.tb_funcionarios.setHorizontalHeaderItem(2, __qtablewidgetitem84)
        __qtablewidgetitem85 = QTableWidgetItem()
        self.tb_funcionarios.setHorizontalHeaderItem(3, __qtablewidgetitem85)
        __qtablewidgetitem86 = QTableWidgetItem()
        self.tb_funcionarios.setHorizontalHeaderItem(4, __qtablewidgetitem86)
        __qtablewidgetitem87 = QTableWidgetItem()
        self.tb_funcionarios.setHorizontalHeaderItem(5, __qtablewidgetitem87)
        __qtablewidgetitem88 = QTableWidgetItem()
        self.tb_funcionarios.setHorizontalHeaderItem(6, __qtablewidgetitem88)
        __qtablewidgetitem89 = QTableWidgetItem()
        self.tb_funcionarios.setHorizontalHeaderItem(7, __qtablewidgetitem89)
        __qtablewidgetitem90 = QTableWidgetItem()
        self.tb_funcionarios.setHorizontalHeaderItem(8, __qtablewidgetitem90)
        self.tb_funcionarios.setObjectName(u"tb_funcionarios")
        self.tb_funcionarios.setStyleSheet(u"QTableWidget{\n"
"        background-color: SkyBlue;\n"
"    }\n"
"    QLineEdit:focus {\n"
"        background-color: SkyBlue;\n"
"    }\n"
"    QLineEdit:disabled {\n"
"        background-color: lSkyBlue; \n"
"   }")

        self.verticalLayout_32.addWidget(self.tb_funcionarios)


        self.verticalLayout_33.addWidget(self.frame_23)

        self.tabWidget_3.addTab(self.tab_6, "")

        self.verticalLayout_28.addWidget(self.tabWidget_3)

        self.Pages.addWidget(self.pg_funcionarios)
        self.pg_domesticos = QWidget()
        self.pg_domesticos.setObjectName(u"pg_domesticos")
        self.verticalLayout_23 = QVBoxLayout(self.pg_domesticos)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.tabWidget_2 = QTabWidget(self.pg_domesticos)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.tabWidget_2.setStyleSheet(u"QTabWidget::pane {\n"
"  border: 1px solid  white;\n"
"  top:-1px; \n"
"  background: rgb(0, 80, 121);; \n"
"} \n"
"\n"
"QTabBar::tab {\n"
"\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(0, 61, 90, 255));\n"
"  border: 1px solid  rgb(249, 249, 249); \n"
"  padding: 10px;\n"
"color:white ;\n"
"} \n"
"\n"
"\n"
"QTabBar::tab:selected { \n"
"	background-color: SkyBlue;\n"
"  margin-bottom: -1px; \n"
" color: rgb(0, 85, 127);\n"
"	\n"
"}\n"
"")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.verticalLayout_25 = QVBoxLayout(self.tab_3)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_108 = QLabel(self.tab_3)
        self.label_108.setObjectName(u"label_108")

        self.verticalLayout_25.addWidget(self.label_108)

        self.frame_16 = QFrame(self.tab_3)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_16)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label_20 = QLabel(self.frame_16)
        self.label_20.setObjectName(u"label_20")

        self.verticalLayout_24.addWidget(self.label_20)

        self.txt_nome_domestico = QLineEdit(self.frame_16)
        self.txt_nome_domestico.setObjectName(u"txt_nome_domestico")
        self.txt_nome_domestico.setMinimumSize(QSize(0, 30))
        self.txt_nome_domestico.setFont(font2)
        self.txt_nome_domestico.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_nome_domestico.setStyleSheet(u"QLineEdit {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit::placeholder {\n"
"     color: Black;\n"
"    }\n"
"QLineEdit:focus {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit:disabled {\n"
"      background-color:SkyBlue; \n"
"   }")

        self.verticalLayout_24.addWidget(self.txt_nome_domestico)

        self.label_21 = QLabel(self.frame_16)
        self.label_21.setObjectName(u"label_21")

        self.verticalLayout_24.addWidget(self.label_21)

        self.txt_apartamento_domestico = QLineEdit(self.frame_16)
        self.txt_apartamento_domestico.setObjectName(u"txt_apartamento_domestico")
        self.txt_apartamento_domestico.setMinimumSize(QSize(0, 30))
        self.txt_apartamento_domestico.setFont(font2)
        self.txt_apartamento_domestico.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_apartamento_domestico.setStyleSheet(u"QLineEdit {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit::placeholder {\n"
"     color: Black;\n"
"    }\n"
"QLineEdit:focus {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit:disabled {\n"
"      background-color:SkyBlue; \n"
"   }")

        self.verticalLayout_24.addWidget(self.txt_apartamento_domestico)

        self.label_22 = QLabel(self.frame_16)
        self.label_22.setObjectName(u"label_22")

        self.verticalLayout_24.addWidget(self.label_22)

        self.txt_bloco_domestico = QLineEdit(self.frame_16)
        self.txt_bloco_domestico.setObjectName(u"txt_bloco_domestico")
        self.txt_bloco_domestico.setMinimumSize(QSize(0, 30))
        self.txt_bloco_domestico.setFont(font2)
        self.txt_bloco_domestico.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_bloco_domestico.setStyleSheet(u"QLineEdit {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit::placeholder {\n"
"     color: Black;\n"
"    }\n"
"QLineEdit:focus {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit:disabled {\n"
"      background-color:SkyBlue; \n"
"   }")

        self.verticalLayout_24.addWidget(self.txt_bloco_domestico)

        self.label_23 = QLabel(self.frame_16)
        self.label_23.setObjectName(u"label_23")

        self.verticalLayout_24.addWidget(self.label_23)

        self.txt_funcao_domestico = QLineEdit(self.frame_16)
        self.txt_funcao_domestico.setObjectName(u"txt_funcao_domestico")
        self.txt_funcao_domestico.setMinimumSize(QSize(0, 30))
        self.txt_funcao_domestico.setFont(font2)
        self.txt_funcao_domestico.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_funcao_domestico.setStyleSheet(u"QLineEdit {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit::placeholder {\n"
"     color: Black;\n"
"    }\n"
"QLineEdit:focus {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit:disabled {\n"
"      background-color:SkyBlue; \n"
"   }")

        self.verticalLayout_24.addWidget(self.txt_funcao_domestico)

        self.label_24 = QLabel(self.frame_16)
        self.label_24.setObjectName(u"label_24")

        self.verticalLayout_24.addWidget(self.label_24)

        self.txt_horario_domestico = QLineEdit(self.frame_16)
        self.txt_horario_domestico.setObjectName(u"txt_horario_domestico")
        self.txt_horario_domestico.setMinimumSize(QSize(0, 30))
        self.txt_horario_domestico.setFont(font2)
        self.txt_horario_domestico.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_horario_domestico.setStyleSheet(u"QLineEdit {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit::placeholder {\n"
"     color: Black;\n"
"    }\n"
"QLineEdit:focus {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit:disabled {\n"
"      background-color:SkyBlue; \n"
"   }")

        self.verticalLayout_24.addWidget(self.txt_horario_domestico)

        self.label_25 = QLabel(self.frame_16)
        self.label_25.setObjectName(u"label_25")

        self.verticalLayout_24.addWidget(self.label_25)

        self.txt_telefone_domestico = QLineEdit(self.frame_16)
        self.txt_telefone_domestico.setObjectName(u"txt_telefone_domestico")
        self.txt_telefone_domestico.setMinimumSize(QSize(0, 30))
        self.txt_telefone_domestico.setFont(font2)
        self.txt_telefone_domestico.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_telefone_domestico.setStyleSheet(u"QLineEdit {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit::placeholder {\n"
"     color: Black;\n"
"    }\n"
"QLineEdit:focus {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit:disabled {\n"
"      background-color:SkyBlue; \n"
"   }")

        self.verticalLayout_24.addWidget(self.txt_telefone_domestico)


        self.verticalLayout_25.addWidget(self.frame_16)

        self.btn_registrar_domesticos = QPushButton(self.tab_3)
        self.btn_registrar_domesticos.setObjectName(u"btn_registrar_domesticos")
        self.btn_registrar_domesticos.setMinimumSize(QSize(180, 30))
        self.btn_registrar_domesticos.setFont(font1)
        self.btn_registrar_domesticos.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_registrar_domesticos.setStyleSheet(u"QPushButton {\n"
"  color: rgb(255, 255, 255);\n"
"  border-radius: 10px;\n"
"  font-size: 16px;\n"
"  background-color: rgb(0, 80, 121);\n"
"  border: 2px solid white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #87CEEB;\n"
"  color: black;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")

        self.verticalLayout_25.addWidget(self.btn_registrar_domesticos, 0, Qt.AlignHCenter)

        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout_26 = QVBoxLayout(self.tab_4)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.label_109 = QLabel(self.tab_4)
        self.label_109.setObjectName(u"label_109")

        self.verticalLayout_26.addWidget(self.label_109)

        self.frame_17 = QFrame(self.tab_4)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_17)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.frame_18 = QFrame(self.frame_17)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.txt_pesquisar_domesticos = QLineEdit(self.frame_18)
        self.txt_pesquisar_domesticos.setObjectName(u"txt_pesquisar_domesticos")
        self.txt_pesquisar_domesticos.setMinimumSize(QSize(0, 30))
        self.txt_pesquisar_domesticos.setFont(font2)
        self.txt_pesquisar_domesticos.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_pesquisar_domesticos.setStyleSheet(u"QLineEdit {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit::placeholder {\n"
"     color: Black;\n"
"    }\n"
"QLineEdit:focus {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit:disabled {\n"
"      background-color:SkyBlue; \n"
"   }")
        self.txt_pesquisar_domesticos.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.txt_pesquisar_domesticos)

        self.btn_pesquisar_domesticos = QPushButton(self.frame_18)
        self.btn_pesquisar_domesticos.setObjectName(u"btn_pesquisar_domesticos")
        self.btn_pesquisar_domesticos.setMinimumSize(QSize(100, 30))
        self.btn_pesquisar_domesticos.setFont(font1)
        self.btn_pesquisar_domesticos.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_pesquisar_domesticos.setStyleSheet(u"QPushButton {\n"
"  color: rgb(255, 255, 255);\n"
"  border-radius: 10px;\n"
"  font-size: 16px;\n"
"  background-color: rgb(0, 80, 121);\n"
"  border: 2px solid white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #87CEEB;\n"
"  color: black;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")

        self.horizontalLayout_11.addWidget(self.btn_pesquisar_domesticos)


        self.verticalLayout_27.addWidget(self.frame_18)

        self.tableWidget = QTableWidget(self.frame_17)
        if (self.tableWidget.columnCount() < 7):
            self.tableWidget.setColumnCount(7)
        __qtablewidgetitem91 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem91)
        __qtablewidgetitem92 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem92)
        __qtablewidgetitem93 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem93)
        __qtablewidgetitem94 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem94)
        __qtablewidgetitem95 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem95)
        __qtablewidgetitem96 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem96)
        __qtablewidgetitem97 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem97)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"QTableWidget{\n"
"        background-color: SkyBlue;\n"
"    }\n"
"    QLineEdit:focus {\n"
"        background-color: SkyBlue;\n"
"    }\n"
"    QLineEdit:disabled {\n"
"        background-color: SkyBlue; \n"
"   }")

        self.verticalLayout_27.addWidget(self.tableWidget)


        self.verticalLayout_26.addWidget(self.frame_17)

        self.tabWidget_2.addTab(self.tab_4, "")

        self.verticalLayout_23.addWidget(self.tabWidget_2)

        self.Pages.addWidget(self.pg_domesticos)
        self.pg_mudancas = QWidget()
        self.pg_mudancas.setObjectName(u"pg_mudancas")
        self.verticalLayout_15 = QVBoxLayout(self.pg_mudancas)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.tabWidget = QTabWidget(self.pg_mudancas)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setStyleSheet(u"QTabWidget::pane {\n"
"  border: 1px solid  white;\n"
"  top:-1px; \n"
"  background: rgb(0, 80, 121);; \n"
"} \n"
"\n"
"QTabBar::tab {\n"
"\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(0, 61, 90, 255));\n"
"  border: 1px solid  rgb(249, 249, 249); \n"
"  padding: 10px;\n"
"color:white ;\n"
"} \n"
"\n"
"\n"
"QTabBar::tab:selected { \n"
"	background-color: SkyBlue;\n"
"  margin-bottom: -1px; \n"
" color: rgb(0, 85, 127);\n"
"	\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_14 = QVBoxLayout(self.tab)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_110 = QLabel(self.tab)
        self.label_110.setObjectName(u"label_110")

        self.verticalLayout_14.addWidget(self.label_110)

        self.scrollArea_2 = QScrollArea(self.tab)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, -80, 695, 575))
        self.verticalLayout_20 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.frame_11 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_11.setObjectName(u"frame_11")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy4)
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_11)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_16 = QLabel(self.frame_11)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_16.addWidget(self.label_16)

        self.txt_data_mudanca = QLineEdit(self.frame_11)
        self.txt_data_mudanca.setObjectName(u"txt_data_mudanca")
        self.txt_data_mudanca.setMinimumSize(QSize(0, 30))
        self.txt_data_mudanca.setFont(font2)
        self.txt_data_mudanca.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_data_mudanca.setStyleSheet(u"QLineEdit {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit::placeholder {\n"
"     color: Black;\n"
"    }\n"
"QLineEdit:focus {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit:disabled {\n"
"      background-color:SkyBlue; \n"
"   }\n"
"")

        self.verticalLayout_16.addWidget(self.txt_data_mudanca)


        self.verticalLayout_20.addWidget(self.frame_11)

        self.frame_13 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_13.setObjectName(u"frame_13")
        sizePolicy4.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy4)
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_13)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_18 = QLabel(self.frame_13)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout_18.addWidget(self.label_18)

        self.txt_horario_mudanca = QLineEdit(self.frame_13)
        self.txt_horario_mudanca.setObjectName(u"txt_horario_mudanca")
        self.txt_horario_mudanca.setMinimumSize(QSize(0, 30))
        self.txt_horario_mudanca.setFont(font2)
        self.txt_horario_mudanca.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_horario_mudanca.setStyleSheet(u"QLineEdit {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit::placeholder {\n"
"     color: Black;\n"
"    }\n"
"QLineEdit:focus {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit:disabled {\n"
"      background-color:SkyBlue; \n"
"   }")

        self.verticalLayout_18.addWidget(self.txt_horario_mudanca)


        self.verticalLayout_20.addWidget(self.frame_13)

        self.frame_12 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_12.setObjectName(u"frame_12")
        sizePolicy4.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy4)
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_12)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_17 = QLabel(self.frame_12)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout_17.addWidget(self.label_17)

        self.txt_nome_responsavel = QLineEdit(self.frame_12)
        self.txt_nome_responsavel.setObjectName(u"txt_nome_responsavel")
        self.txt_nome_responsavel.setMinimumSize(QSize(0, 30))
        self.txt_nome_responsavel.setFont(font2)
        self.txt_nome_responsavel.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_nome_responsavel.setStyleSheet(u"QLineEdit {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit::placeholder {\n"
"     color: Black;\n"
"    }\n"
"QLineEdit:focus {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit:disabled {\n"
"      background-color:SkyBlue; \n"
"   }")

        self.verticalLayout_17.addWidget(self.txt_nome_responsavel)

        self.txt_apartamento_mudanca = QLineEdit(self.frame_12)
        self.txt_apartamento_mudanca.setObjectName(u"txt_apartamento_mudanca")
        self.txt_apartamento_mudanca.setMinimumSize(QSize(0, 30))
        self.txt_apartamento_mudanca.setFont(font2)
        self.txt_apartamento_mudanca.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_apartamento_mudanca.setStyleSheet(u"QLineEdit {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit::placeholder {\n"
"     color: Black;\n"
"    }\n"
"QLineEdit:focus {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit:disabled {\n"
"      background-color:SkyBlue; \n"
"   }")

        self.verticalLayout_17.addWidget(self.txt_apartamento_mudanca)

        self.txt_bloco_mudanca = QLineEdit(self.frame_12)
        self.txt_bloco_mudanca.setObjectName(u"txt_bloco_mudanca")
        self.txt_bloco_mudanca.setMinimumSize(QSize(0, 30))
        self.txt_bloco_mudanca.setFont(font2)
        self.txt_bloco_mudanca.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_bloco_mudanca.setStyleSheet(u"QLineEdit {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit::placeholder {\n"
"     color: Black;\n"
"    }\n"
"QLineEdit:focus {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit:disabled {\n"
"      background-color:SkyBlue; \n"
"   }\n"
"")

        self.verticalLayout_17.addWidget(self.txt_bloco_mudanca)


        self.verticalLayout_20.addWidget(self.frame_12)

        self.frame_14 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_14.setObjectName(u"frame_14")
        sizePolicy4.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy4)
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_14)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_19 = QLabel(self.frame_14)
        self.label_19.setObjectName(u"label_19")

        self.verticalLayout_19.addWidget(self.label_19)

        self.txt_nome_enp_mudanca = QLineEdit(self.frame_14)
        self.txt_nome_enp_mudanca.setObjectName(u"txt_nome_enp_mudanca")
        self.txt_nome_enp_mudanca.setMinimumSize(QSize(0, 30))
        self.txt_nome_enp_mudanca.setFont(font2)
        self.txt_nome_enp_mudanca.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_nome_enp_mudanca.setStyleSheet(u"QLineEdit {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit::placeholder {\n"
"     color: Black;\n"
"    }\n"
"QLineEdit:focus {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit:disabled {\n"
"      background-color:SkyBlue; \n"
"   }\n"
"")

        self.verticalLayout_19.addWidget(self.txt_nome_enp_mudanca)


        self.verticalLayout_20.addWidget(self.frame_14)

        self.chk_uso_elevador = QCheckBox(self.scrollAreaWidgetContents_2)
        self.chk_uso_elevador.setObjectName(u"chk_uso_elevador")
        self.chk_uso_elevador.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_20.addWidget(self.chk_uso_elevador)

        self.chk_uso_escada = QCheckBox(self.scrollAreaWidgetContents_2)
        self.chk_uso_escada.setObjectName(u"chk_uso_escada")
        self.chk_uso_escada.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_20.addWidget(self.chk_uso_escada)

        self.chk_icamento = QCheckBox(self.scrollAreaWidgetContents_2)
        self.chk_icamento.setObjectName(u"chk_icamento")
        self.chk_icamento.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout_20.addWidget(self.chk_icamento)

        self.btn_registrar_mudancas = QPushButton(self.scrollAreaWidgetContents_2)
        self.btn_registrar_mudancas.setObjectName(u"btn_registrar_mudancas")
        self.btn_registrar_mudancas.setMinimumSize(QSize(180, 30))
        self.btn_registrar_mudancas.setFont(font1)
        self.btn_registrar_mudancas.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_registrar_mudancas.setStyleSheet(u"QPushButton {\n"
"  color: rgb(255, 255, 255);\n"
"  border-radius: 10px;\n"
"  font-size: 16px;\n"
"  background-color: rgb(0, 80, 121);\n"
"  border: 2px solid white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #87CEEB;\n"
"  color: black;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")

        self.verticalLayout_20.addWidget(self.btn_registrar_mudancas, 0, Qt.AlignHCenter)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_14.addWidget(self.scrollArea_2)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_21 = QVBoxLayout(self.tab_2)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_111 = QLabel(self.tab_2)
        self.label_111.setObjectName(u"label_111")

        self.verticalLayout_21.addWidget(self.label_111)

        self.frame_15 = QFrame(self.tab_2)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(180, 0))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_15)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.txt_data_mudanca_2 = QLineEdit(self.frame_15)
        self.txt_data_mudanca_2.setObjectName(u"txt_data_mudanca_2")
        self.txt_data_mudanca_2.setMinimumSize(QSize(0, 30))
        self.txt_data_mudanca_2.setFont(font2)
        self.txt_data_mudanca_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txt_data_mudanca_2.setStyleSheet(u"QLineEdit {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit::placeholder {\n"
"     color: Black;\n"
"    }\n"
"QLineEdit:focus {\n"
"      background-color: SkyBlue;\n"
"    }\n"
"QLineEdit:disabled {\n"
"      background-color:SkyBlue; \n"
"   }")
        self.txt_data_mudanca_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.txt_data_mudanca_2)

        self.tableWidget_2 = QTableWidget(self.frame_15)
        if (self.tableWidget_2.columnCount() < 10):
            self.tableWidget_2.setColumnCount(10)
        __qtablewidgetitem98 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem98)
        __qtablewidgetitem99 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem99)
        __qtablewidgetitem100 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem100)
        __qtablewidgetitem101 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem101)
        __qtablewidgetitem102 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, __qtablewidgetitem102)
        __qtablewidgetitem103 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, __qtablewidgetitem103)
        __qtablewidgetitem104 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, __qtablewidgetitem104)
        __qtablewidgetitem105 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(7, __qtablewidgetitem105)
        __qtablewidgetitem106 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(8, __qtablewidgetitem106)
        __qtablewidgetitem107 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(9, __qtablewidgetitem107)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setStyleSheet(u"QTableWidget{\n"
"        background-color: SkyBlue;\n"
"    }\n"
"    QLineEdit:focus {\n"
"        background-color: SkyBlue;\n"
"    }\n"
"    QLineEdit:disabled {\n"
"        background-color: SkyBlue; \n"
"   }")

        self.verticalLayout_22.addWidget(self.tableWidget_2)

        self.btn_pesquisar_mudancas = QPushButton(self.frame_15)
        self.btn_pesquisar_mudancas.setObjectName(u"btn_pesquisar_mudancas")
        self.btn_pesquisar_mudancas.setMinimumSize(QSize(180, 30))
        self.btn_pesquisar_mudancas.setFont(font1)
        self.btn_pesquisar_mudancas.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_pesquisar_mudancas.setStyleSheet(u"QPushButton {\n"
"  color: rgb(255, 255, 255);\n"
"  border-radius: 10px;\n"
"  font-size: 16px;\n"
"  background-color: rgb(0, 80, 121);\n"
"  border: 2px solid white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: #D3D3D3;\n"
"  color: black;\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")

        self.verticalLayout_22.addWidget(self.btn_pesquisar_mudancas, 0, Qt.AlignHCenter)


        self.verticalLayout_21.addWidget(self.frame_15)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_15.addWidget(self.tabWidget)

        self.Pages.addWidget(self.pg_mudancas)
        self.pg_sobre = QWidget()
        self.pg_sobre.setObjectName(u"pg_sobre")
        self.horizontalLayout_6 = QHBoxLayout(self.pg_sobre)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.frame_4 = QFrame(self.pg_sobre)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_4)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_8 = QLabel(self.frame_4)
        self.label_8.setObjectName(u"label_8")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy5)

        self.verticalLayout_10.addWidget(self.label_8)

        self.scrollArea = QScrollArea(self.frame_4)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 695, 1062))
        self.verticalLayout_11 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_9 = QLabel(self.scrollAreaWidgetContents)
        self.label_9.setObjectName(u"label_9")
        font4 = QFont()
        font4.setUnderline(False)
        font4.setStrikeOut(False)
        self.label_9.setFont(font4)
        self.label_9.setTabletTracking(False)
        self.label_9.setContextMenuPolicy(Qt.NoContextMenu)
        self.label_9.setAutoFillBackground(False)
        self.label_9.setTextFormat(Qt.RichText)
        self.label_9.setWordWrap(True)

        self.verticalLayout_11.addWidget(self.label_9)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_10.addWidget(self.scrollArea)


        self.horizontalLayout_6.addWidget(self.frame_4)

        self.Pages.addWidget(self.pg_sobre)
        self.pg_contatos = QWidget()
        self.pg_contatos.setObjectName(u"pg_contatos")
        self.verticalLayout_6 = QVBoxLayout(self.pg_contatos)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame = QFrame(self.pg_contatos)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        sizePolicy4.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy4)

        self.verticalLayout_9.addWidget(self.label_5, 0, Qt.AlignHCenter)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_2)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_7.addWidget(self.label_6)

        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_7.addWidget(self.label_7)


        self.verticalLayout_9.addWidget(self.frame_2, 0, Qt.AlignHCenter)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_3)


        self.verticalLayout_6.addWidget(self.frame)

        self.Pages.addWidget(self.pg_contatos)

        self.verticalLayout_74.addWidget(self.Pages)


        self.verticalLayout.addWidget(self.main_frame)

        self.foot_frame = QFrame(self.main_container)
        self.foot_frame.setObjectName(u"foot_frame")
        self.foot_frame.setFrameShape(QFrame.StyledPanel)
        self.foot_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.foot_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.foot_frame)
        self.label_2.setObjectName(u"label_2")
        font5 = QFont()
        font5.setPointSize(9)
        self.label_2.setFont(font5)
        self.label_2.setStyleSheet(u" background-color: rgb(0, 80, 121);")

        self.horizontalLayout_2.addWidget(self.label_2, 0, Qt.AlignVCenter)


        self.verticalLayout.addWidget(self.foot_frame)


        self.horizontalLayout.addWidget(self.main_container)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.Pages.setCurrentIndex(0)
        self.tabWidget_7.setCurrentIndex(0)
        self.tabWidget_6.setCurrentIndex(0)
        self.tabWidget_5.setCurrentIndex(0)
        self.tabWidget_4.setCurrentIndex(0)
        self.tabWidget_9.setCurrentIndex(0)
        self.tabWidget_8.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/_imgs/_imgs/logo_2.jpg\"/></p></body></html>", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_menu_moradores.setText(QCoreApplication.translate("MainWindow", u"Moradores", None))
        self.btn_menu_agendamentos.setText(QCoreApplication.translate("MainWindow", u"Agendamentos", None))
        self.btn_menu_visitantes.setText(QCoreApplication.translate("MainWindow", u"Visitantes", None))
        self.btn_menu_prestadores.setText(QCoreApplication.translate("MainWindow", u"Prestadores", None))
        self.btn_menu_encomendas.setText(QCoreApplication.translate("MainWindow", u"Encomendas", None))
        self.btn_menu_ocorrencias.setText(QCoreApplication.translate("MainWindow", u"Ocorr\u00eancias", None))
        self.btn_menu_funcionarios.setText(QCoreApplication.translate("MainWindow", u"Funcion\u00e1rios", None))
        self.btn_menu_domesticos.setText(QCoreApplication.translate("MainWindow", u"Dom\u00e9sticos", None))
        self.btn_menu_mudancas.setText(QCoreApplication.translate("MainWindow", u"Mudan\u00e7as", None))
        self.btn_menu_sobre.setText(QCoreApplication.translate("MainWindow", u"Sobre", None))
        self.btn_menu_contatos.setText(QCoreApplication.translate("MainWindow", u"Contatos", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:7pt; color:#ffffff;\">GHG</span></p></body></html>", None))
#if QT_CONFIG(whatsthis)
        self.toogle_Button.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/_imgs/_imgs/menu.png\"/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.toogle_Button.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:22pt; font-weight:600; color:#ffffff;\">SISTEMA DE CONDOM\u00cdNIO</span></p></body></html>", None))
        self.lbl_logo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><br/></p><p align=\"center\"><img src=\":/_imgs/_imgs/hero.png\"/></p><p align=\"center\"><span style=\" font-size:22pt; font-weight:600; color:#ffffff;\">VARANDAS DO PRAIA</span></p></body></html>", None))
        self.btn_menu_cadastrar.setText(QCoreApplication.translate("MainWindow", u"Cadastrar Usu\u00e1rio", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/_imgs/_imgs/user_1.png\"/></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Nome:</span></p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Usu\u00e1rio:</span></p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Senha:</span></p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Senha:</span></p></body></html>", None))
        self.txt_senha_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u" Confirme a senha", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#ffffff;\">Perfil:</span></p></body></html>", None))
        self.cb_perfil.setItemText(0, QCoreApplication.translate("MainWindow", u" Administrador", None))
        self.cb_perfil.setItemText(1, QCoreApplication.translate("MainWindow", u" Sindico", None))
        self.cb_perfil.setItemText(2, QCoreApplication.translate("MainWindow", u" Porteiro", None))

        self.btn_cadastrar_usuario.setText(QCoreApplication.translate("MainWindow", u"Cadastrar Usu\u00e1rio", None))
        self.label_94.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">Cadastro de Moradores</span></p></body></html>", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Apartamento/Bloco</span></p></body></html>", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Moradores</span></p></body></html>", None))
        self.txt_nome_completo.setPlaceholderText(QCoreApplication.translate("MainWindow", u" Nome Completo ", None))
        self.txt_data_nascimento.setPlaceholderText(QCoreApplication.translate("MainWindow", u" dd/mm/aaaa", None))
        self.txt_nome_completo2.setPlaceholderText(QCoreApplication.translate("MainWindow", u" Nome Completo ", None))
        self.txt_data_nascimento2.setPlaceholderText(QCoreApplication.translate("MainWindow", u" dd/mm/aaaa", None))
        self.txt_nome_completo3.setPlaceholderText(QCoreApplication.translate("MainWindow", u" Nome Completo ", None))
        self.txt_data_nascimento3.setPlaceholderText(QCoreApplication.translate("MainWindow", u" dd/mm/aaaa", None))
        self.txt_nome_completo4.setPlaceholderText(QCoreApplication.translate("MainWindow", u" Nome Completo ", None))
        self.txt_data_nascimento4.setText("")
        self.txt_data_nascimento4.setPlaceholderText(QCoreApplication.translate("MainWindow", u" dd/mm/aaaa", None))
        self.txt_nome_completo5.setPlaceholderText(QCoreApplication.translate("MainWindow", u" Nome Completo ", None))
        self.txt_data_nascimento5.setPlaceholderText(QCoreApplication.translate("MainWindow", u" dd/mm/aaaa", None))
        self.txt_nome_completo6.setPlaceholderText(QCoreApplication.translate("MainWindow", u" Nome Completo ", None))
        self.txt_data_nascimento6.setPlaceholderText(QCoreApplication.translate("MainWindow", u" dd/mm/aaaa", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Telefone 1</span></p></body></html>", None))
        self.txt_telefone1.setPlaceholderText(QCoreApplication.translate("MainWindow", u" (00) 00000-0000", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Telefone 2</span></p></body></html>", None))
        self.txt_telefone2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(00) 00000-0000", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Email</span></p></body></html>", None))
        self.txt_email1.setPlaceholderText("")
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Email 2</span></p></body></html>", None))
        self.txt_email2.setPlaceholderText("")
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Ve\u00edculo</span></p></body></html>", None))
        self.txt_veiculo1_placa.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Placa", None))
        self.txt_veiculo1_marca.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Marca", None))
        self.txt_veiculo1_modelo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Modelo", None))
        self.txt_veiculo1_cor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Cor", None))
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Ve\u00edculo 2</span></p></body></html>", None))
        self.txt_veiculo2_placa.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Placa", None))
        self.txt_veiculo2_marca.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Marca", None))
        self.txt_veiculo2_modelo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Modelo", None))
        self.txt_veiculo2_cor.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Cor", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Observa\u00e7\u00f5es:</span></p></body></html>", None))
        self.btn_cadastrar_morador.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.tab_13), QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#ffffff;\">Pesquisar Morador</span></p></body></html>", None))
        self.txt_pesquisa_apartamento_bloco.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite um nome ", None))
        self.btn_pesquisar_morador.setText(QCoreApplication.translate("MainWindow", u"Pesquisar", None))
        ___qtablewidgetitem = self.tb_moradores.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Id", None));
        ___qtablewidgetitem1 = self.tb_moradores.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Ap/Bloco", None));
        ___qtablewidgetitem2 = self.tb_moradores.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Nome Completo", None));
        ___qtablewidgetitem3 = self.tb_moradores.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Data Nascimento", None));
        ___qtablewidgetitem4 = self.tb_moradores.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Nome Completo", None));
        ___qtablewidgetitem5 = self.tb_moradores.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Data Nascimento", None));
        ___qtablewidgetitem6 = self.tb_moradores.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Nome Completo", None));
        ___qtablewidgetitem7 = self.tb_moradores.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Data Nascimento", None));
        ___qtablewidgetitem8 = self.tb_moradores.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Nome Completo", None));
        ___qtablewidgetitem9 = self.tb_moradores.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Data Nascimento", None));
        ___qtablewidgetitem10 = self.tb_moradores.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Nome Completo", None));
        ___qtablewidgetitem11 = self.tb_moradores.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Data Nascimento", None));
        ___qtablewidgetitem12 = self.tb_moradores.horizontalHeaderItem(12)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Nome Completo", None));
        ___qtablewidgetitem13 = self.tb_moradores.horizontalHeaderItem(13)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Data Nascimento", None));
        ___qtablewidgetitem14 = self.tb_moradores.horizontalHeaderItem(14)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Telefone1", None));
        ___qtablewidgetitem15 = self.tb_moradores.horizontalHeaderItem(15)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Telefone2", None));
        ___qtablewidgetitem16 = self.tb_moradores.horizontalHeaderItem(16)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Email1", None));
        ___qtablewidgetitem17 = self.tb_moradores.horizontalHeaderItem(17)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Email2", None));
        ___qtablewidgetitem18 = self.tb_moradores.horizontalHeaderItem(18)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Veiculo1 Placa", None));
        ___qtablewidgetitem19 = self.tb_moradores.horizontalHeaderItem(19)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Veiculo1 Marca", None));
        ___qtablewidgetitem20 = self.tb_moradores.horizontalHeaderItem(20)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Veiculo1 Modelo", None));
        ___qtablewidgetitem21 = self.tb_moradores.horizontalHeaderItem(21)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Veiculo1 Cor", None));
        ___qtablewidgetitem22 = self.tb_moradores.horizontalHeaderItem(22)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Veiculo2 Placa", None));
        ___qtablewidgetitem23 = self.tb_moradores.horizontalHeaderItem(23)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Veiculo2 Marca", None));
        ___qtablewidgetitem24 = self.tb_moradores.horizontalHeaderItem(24)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Veiculo2 Modelo", None));
        ___qtablewidgetitem25 = self.tb_moradores.horizontalHeaderItem(25)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Veiculo2 Cor", None));
        ___qtablewidgetitem26 = self.tb_moradores.horizontalHeaderItem(26)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Observa\u00e7\u00f5es", None));
        self.tabWidget_7.setTabText(self.tabWidget_7.indexOf(self.tab_14), QCoreApplication.translate("MainWindow", u"Pesquisa", None))
        self.label_95.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">Agendamentos</span></p></body></html>", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Apartamento/Bloco</span></p></body></html>", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Nome do Morador</span></p></body></html>", None))
        self.label_112.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Data</span></p></body></html>", None))
        self.txt_data_agendamento.setPlaceholderText(QCoreApplication.translate("MainWindow", u" dd/mm/aaaa", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Local</span></p></body></html>", None))
        self.cmb_local.setItemText(0, QCoreApplication.translate("MainWindow", u"Sal\u00e3o de Festas", None))
        self.cmb_local.setItemText(1, QCoreApplication.translate("MainWindow", u"Quiosque Bloco 1", None))
        self.cmb_local.setItemText(2, QCoreApplication.translate("MainWindow", u"Quiosque Bloco 2", None))
        self.cmb_local.setItemText(3, QCoreApplication.translate("MainWindow", u"Quiosque Bloco 3", None))
        self.cmb_local.setItemText(4, QCoreApplication.translate("MainWindow", u"Quiosque Bloco 4", None))

        self.label_62.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Per\u00edodo</span></p></body></html>", None))
        self.cmb_periodo.setItemText(0, QCoreApplication.translate("MainWindow", u"Manh\u00e3", None))
        self.cmb_periodo.setItemText(1, QCoreApplication.translate("MainWindow", u"Tarde", None))
        self.cmb_periodo.setItemText(2, QCoreApplication.translate("MainWindow", u"Noite", None))

        self.label_63.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Funcion\u00e1rio</span></p></body></html>", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Observa\u00e7\u00f5es:</span></p></body></html>", None))
        self.btn_registrar_agendamento.setText(QCoreApplication.translate("MainWindow", u"Agendar", None))
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(self.tab_11), QCoreApplication.translate("MainWindow", u"Agendar", None))
        self.label_97.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">Pesquisa Agendamentos</span></p></body></html>", None))
        self.txt_pesquisar_agendamentos.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite uma data", None))
        self.btn_pesquisar_agendamentos.setText(QCoreApplication.translate("MainWindow", u"Pesquisar", None))
        ___qtablewidgetitem27 = self.tb_agendamentos.horizontalHeaderItem(0)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Id", None));
        ___qtablewidgetitem28 = self.tb_agendamentos.horizontalHeaderItem(1)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Ap/Bloco", None));
        ___qtablewidgetitem29 = self.tb_agendamentos.horizontalHeaderItem(2)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"Nome Morador", None));
        ___qtablewidgetitem30 = self.tb_agendamentos.horizontalHeaderItem(3)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"Local", None));
        ___qtablewidgetitem31 = self.tb_agendamentos.horizontalHeaderItem(4)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"Per\u00edodo", None));
        ___qtablewidgetitem32 = self.tb_agendamentos.horizontalHeaderItem(5)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"Data Agendamento", None));
        ___qtablewidgetitem33 = self.tb_agendamentos.horizontalHeaderItem(6)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"Funcion\u00e1rio", None));
        ___qtablewidgetitem34 = self.tb_agendamentos.horizontalHeaderItem(7)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"Observa\u00e7\u00f5es", None));
        self.tabWidget_6.setTabText(self.tabWidget_6.indexOf(self.tab_12), QCoreApplication.translate("MainWindow", u"Pesquisar", None))
        self.label_98.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">Registro de Visitantes</span></p></body></html>", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Data</span></p></body></html>", None))
        self.txt_data_visita.setPlaceholderText(QCoreApplication.translate("MainWindow", u"   dd/mm/aaaa", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Nome do Visitante</span></p></body></html>", None))
        self.txt_nome_visitante.setPlaceholderText("")
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">RG ou CPF</span></p></body></html>", None))
        self.txt_rg_cpf_visitante.setPlaceholderText("")
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Visitando / Destino</span></p></body></html>", None))
        self.txt_visitando.setPlaceholderText("")
        self.label_113.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Apartamento/Bloco</span></p></body></html>", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Hora de Entrada</span></p></body></html>", None))
        self.txt_hora_entrada_visita.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  -- : --", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Hora da Sa\u00edda</span></p></body></html>", None))
        self.txt_hora_saida_visita.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  -- : --", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Quem Autorizou</span></p></body></html>", None))
        self.txt_quem_autorizou_visita.setPlaceholderText("")
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Vai usar vaga de visitante ou do apartamento?</span></p></body></html>", None))
        self.cmb_vaga_utilizada.setItemText(0, QCoreApplication.translate("MainWindow", u"Visitante", None))
        self.cmb_vaga_utilizada.setItemText(1, QCoreApplication.translate("MainWindow", u"Apartamento", None))

        self.label_54.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Placa</span></p></body></html>", None))
        self.txt_placa_visitante.setPlaceholderText("")
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Marca</span></p></body></html>", None))
        self.txt_marca_visitante.setPlaceholderText("")
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Modelo</span></p></body></html>", None))
        self.txt_modelo_visitante.setPlaceholderText("")
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Cor</span></p></body></html>", None))
        self.txt_cor_visitante.setPlaceholderText("")
        self.btn_registrar_visitante.setText(QCoreApplication.translate("MainWindow", u"Registrar", None))
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_9), QCoreApplication.translate("MainWindow", u"Registrar", None))
        self.label_99.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">Pesquisa Visitantes</span></p></body></html>", None))
        self.txt_pesquisa_visitantes.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite um nome", None))
        self.btn_pesquisar_visitantes.setText(QCoreApplication.translate("MainWindow", u"Pesquisar", None))
        ___qtablewidgetitem35 = self.tb_visitantes.horizontalHeaderItem(0)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"Id", None));
        ___qtablewidgetitem36 = self.tb_visitantes.horizontalHeaderItem(1)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"Data Visita", None));
        ___qtablewidgetitem37 = self.tb_visitantes.horizontalHeaderItem(2)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"Nome Visitante", None));
        ___qtablewidgetitem38 = self.tb_visitantes.horizontalHeaderItem(3)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"RG/CPF", None));
        ___qtablewidgetitem39 = self.tb_visitantes.horizontalHeaderItem(4)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"Visitando", None));
        ___qtablewidgetitem40 = self.tb_visitantes.horizontalHeaderItem(5)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"Ap/Bloco", None));
        ___qtablewidgetitem41 = self.tb_visitantes.horizontalHeaderItem(6)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"Hora Entrada", None));
        ___qtablewidgetitem42 = self.tb_visitantes.horizontalHeaderItem(7)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"Hora Sa\u00edda", None));
        ___qtablewidgetitem43 = self.tb_visitantes.horizontalHeaderItem(8)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"Quem Autorizou", None));
        ___qtablewidgetitem44 = self.tb_visitantes.horizontalHeaderItem(9)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"Vaga Utilizada", None));
        ___qtablewidgetitem45 = self.tb_visitantes.horizontalHeaderItem(10)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"Placa", None));
        ___qtablewidgetitem46 = self.tb_visitantes.horizontalHeaderItem(11)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"Marca", None));
        ___qtablewidgetitem47 = self.tb_visitantes.horizontalHeaderItem(12)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"Modelo", None));
        ___qtablewidgetitem48 = self.tb_visitantes.horizontalHeaderItem(13)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"Cor", None));
        self.tabWidget_5.setTabText(self.tabWidget_5.indexOf(self.tab_10), QCoreApplication.translate("MainWindow", u"Pesquisar", None))
        self.label_100.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">Registro de Prestadores</span></p></body></html>", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Nome da Empresa</span></p></body></html>", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Tipo de Servi\u00e7o</span></p></body></html>", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Data</span></p></body></html>", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Hoda da Entrada</span></p></body></html>", None))
        self.txt_hora_entrada_prestador.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  -- : --", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Hoda da Sa\u00edda</span></p></body></html>", None))
        self.txt_hora_saida_prestador.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  -- : --", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Nome do Prestador</span></p></body></html>", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">RG ou CPF</span></p></body></html>", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Telefone</span></p></body></html>", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Contratante</span></p></body></html>", None))
        self.txt_contratante.setPlaceholderText(QCoreApplication.translate("MainWindow", u" Nome", None))
        self.label_114.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Apartamento/Bloco</span></p></body></html>", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Quem Autorizou a Entrada</span></p></body></html>", None))
        self.btn_registrar_prestadores.setText(QCoreApplication.translate("MainWindow", u"Registrar", None))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_7), QCoreApplication.translate("MainWindow", u"Registrar", None))
        self.label_101.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">Pesquisar Prestadores</span></p></body></html>", None))
        self.lineEdit_22.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite um nome", None))
        self.btn_pesquisar_prestadores.setText(QCoreApplication.translate("MainWindow", u"Pesquisar", None))
        ___qtablewidgetitem49 = self.tb_prestadores.horizontalHeaderItem(0)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"Id", None));
        ___qtablewidgetitem50 = self.tb_prestadores.horizontalHeaderItem(1)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MainWindow", u"Nome Empresa", None));
        ___qtablewidgetitem51 = self.tb_prestadores.horizontalHeaderItem(2)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MainWindow", u"Tipo Servi\u00e7o", None));
        ___qtablewidgetitem52 = self.tb_prestadores.horizontalHeaderItem(3)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("MainWindow", u"Data Servi\u00e7o", None));
        ___qtablewidgetitem53 = self.tb_prestadores.horizontalHeaderItem(4)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("MainWindow", u"Hora Entrada", None));
        ___qtablewidgetitem54 = self.tb_prestadores.horizontalHeaderItem(5)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("MainWindow", u"Hora Sa\u00edda", None));
        ___qtablewidgetitem55 = self.tb_prestadores.horizontalHeaderItem(6)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("MainWindow", u"Nome Prestador", None));
        ___qtablewidgetitem56 = self.tb_prestadores.horizontalHeaderItem(7)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("MainWindow", u"RG/CPF", None));
        ___qtablewidgetitem57 = self.tb_prestadores.horizontalHeaderItem(8)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("MainWindow", u"Telefone", None));
        ___qtablewidgetitem58 = self.tb_prestadores.horizontalHeaderItem(9)
        ___qtablewidgetitem58.setText(QCoreApplication.translate("MainWindow", u"Contratante", None));
        ___qtablewidgetitem59 = self.tb_prestadores.horizontalHeaderItem(10)
        ___qtablewidgetitem59.setText(QCoreApplication.translate("MainWindow", u"Ap/Bloco", None));
        ___qtablewidgetitem60 = self.tb_prestadores.horizontalHeaderItem(11)
        ___qtablewidgetitem60.setText(QCoreApplication.translate("MainWindow", u"Quem Autorizou", None));
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_8), QCoreApplication.translate("MainWindow", u"Pesquisar", None))
        self.label_102.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">Registro de Encomendas</span></p></body></html>", None))
        self.label_81.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">N\u00famero de Protocolo</span></p></body></html>", None))
        self.txt_numero_protocolo.setPlaceholderText(QCoreApplication.translate("MainWindow", u" AUTO GENERATED", None))
        self.label_82.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Data e Hora do Recebimento</span></p></body></html>", None))
        self.txt_data_hora_recebimento.setPlaceholderText(QCoreApplication.translate("MainWindow", u" dd/mm/aaaa  \u00e0s   -- : --", None))
        self.label_83.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Nome do Destinat\u00e1rio</span></p></body></html>", None))
        self.txt_nome_destinatario.setPlaceholderText("")
        self.label_115.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Apartamento/Bloco</span></p></body></html>", None))
        self.label_86.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">N\u00famero de Rastramento</span></p></body></html>", None))
        self.txt_numero_rastreamento.setPlaceholderText("")
        self.label_87.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Tipo de Encomenda</span></p></body></html>", None))
        self.cmb_tipo_encomenda.setItemText(0, QCoreApplication.translate("MainWindow", u"Pacote", None))
        self.cmb_tipo_encomenda.setItemText(1, QCoreApplication.translate("MainWindow", u"Carta", None))
        self.cmb_tipo_encomenda.setItemText(2, QCoreApplication.translate("MainWindow", u"Objeto Grande", None))

        self.label_88.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Descri\u00e7\u00e3o da Encomenda</span></p></body></html>", None))
        self.label_89.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Empresa de Entrega</span></p></body></html>", None))
        self.txt_empresa_entrega.setPlaceholderText("")
        self.label_90.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Observa\u00e7\u00f5es</span></p></body></html>", None))
        self.label_91.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; color:#ffffff;\">Informa\u00e7\u00f5es do Entregador</span></p></body></html>", None))
        self.txt_nome_entregador.setPlaceholderText(QCoreApplication.translate("MainWindow", u" Nome do Entregador", None))
        self.txt_rg_cpf_entregador.setPlaceholderText(QCoreApplication.translate("MainWindow", u" RG ou CPF do Entregador", None))
        self.label_92.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Porteiro</span></p></body></html>", None))
        self.txt_nome_porteiro.setPlaceholderText("")
        self.label_93.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Nome de quem retirou da portaria</span></p></body></html>", None))
        self.txt_nome_retirou.setPlaceholderText("")
        self.btn_registrar_encomendas.setText(QCoreApplication.translate("MainWindow", u"Registrar Encomenda", None))
        self.tabWidget_9.setTabText(self.tabWidget_9.indexOf(self.tab_17), QCoreApplication.translate("MainWindow", u"Registrar", None))
        self.label_103.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">Pesquisar  Encomendas</span></p></body></html>", None))
        self.txt_pesquisar_encomendas.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite um nome", None))
        self.btn_pesquisar_encomendas.setText(QCoreApplication.translate("MainWindow", u"Pesquisar", None))
        ___qtablewidgetitem61 = self.tb_encomendas.horizontalHeaderItem(0)
        ___qtablewidgetitem61.setText(QCoreApplication.translate("MainWindow", u"Id", None));
        ___qtablewidgetitem62 = self.tb_encomendas.horizontalHeaderItem(1)
        ___qtablewidgetitem62.setText(QCoreApplication.translate("MainWindow", u"N\u00famero Protocolo", None));
        ___qtablewidgetitem63 = self.tb_encomendas.horizontalHeaderItem(2)
        ___qtablewidgetitem63.setText(QCoreApplication.translate("MainWindow", u"Data Hora Recebimento", None));
        ___qtablewidgetitem64 = self.tb_encomendas.horizontalHeaderItem(3)
        ___qtablewidgetitem64.setText(QCoreApplication.translate("MainWindow", u"Nome Destinat\u00e1rio", None));
        ___qtablewidgetitem65 = self.tb_encomendas.horizontalHeaderItem(4)
        ___qtablewidgetitem65.setText(QCoreApplication.translate("MainWindow", u"Ap/Bloco", None));
        ___qtablewidgetitem66 = self.tb_encomendas.horizontalHeaderItem(5)
        ___qtablewidgetitem66.setText(QCoreApplication.translate("MainWindow", u"N\u00famero Rastreamento", None));
        ___qtablewidgetitem67 = self.tb_encomendas.horizontalHeaderItem(6)
        ___qtablewidgetitem67.setText(QCoreApplication.translate("MainWindow", u"Tipo Encomenda", None));
        ___qtablewidgetitem68 = self.tb_encomendas.horizontalHeaderItem(7)
        ___qtablewidgetitem68.setText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o Encomenda", None));
        ___qtablewidgetitem69 = self.tb_encomendas.horizontalHeaderItem(8)
        ___qtablewidgetitem69.setText(QCoreApplication.translate("MainWindow", u"Empresa Entrega", None));
        ___qtablewidgetitem70 = self.tb_encomendas.horizontalHeaderItem(9)
        ___qtablewidgetitem70.setText(QCoreApplication.translate("MainWindow", u"Observa\u00e7\u00f5es", None));
        ___qtablewidgetitem71 = self.tb_encomendas.horizontalHeaderItem(10)
        ___qtablewidgetitem71.setText(QCoreApplication.translate("MainWindow", u"Nome Entregador", None));
        ___qtablewidgetitem72 = self.tb_encomendas.horizontalHeaderItem(11)
        ___qtablewidgetitem72.setText(QCoreApplication.translate("MainWindow", u"RG/CPF", None));
        ___qtablewidgetitem73 = self.tb_encomendas.horizontalHeaderItem(12)
        ___qtablewidgetitem73.setText(QCoreApplication.translate("MainWindow", u"Porteiro", None));
        ___qtablewidgetitem74 = self.tb_encomendas.horizontalHeaderItem(13)
        ___qtablewidgetitem74.setText(QCoreApplication.translate("MainWindow", u"Quem Retirou", None));
        self.tabWidget_9.setTabText(self.tabWidget_9.indexOf(self.tab_18), QCoreApplication.translate("MainWindow", u"Pesquisar", None))
        self.label_104.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">Registro de Ocorr\u00eancias</span></p></body></html>", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">N\u00famero da Ocorr\u00eancia</span></p></body></html>", None))
        self.txt_numero_protocolo_ocorrencias.setPlaceholderText(QCoreApplication.translate("MainWindow", u" AUTO GENERATED", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Data da Ocorr\u00eancia</span></p></body></html>", None))
        self.txt_data_ocorrencia.setPlaceholderText(QCoreApplication.translate("MainWindow", u" aa/mm/aaaa", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Nome do Funcion\u00e1rio</span></p></body></html>", None))
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Hora do Registro</span></p></body></html>", None))
        self.txt_hora_registro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  -- : --", None))
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Data do Registro</span></p></body></html>", None))
        self.txt_data_registro.setPlaceholderText(QCoreApplication.translate("MainWindow", u" dd/mm/aaaa", None))
        self.label_80.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Descri\u00e7\u00e3o da Ocorr\u00eancia:</span></p></body></html>", None))
        self.btn_registrar_ocorrencias.setText(QCoreApplication.translate("MainWindow", u"Registrar", None))
        self.tabWidget_8.setTabText(self.tabWidget_8.indexOf(self.tab_15), QCoreApplication.translate("MainWindow", u"Registrar", None))
        self.label_105.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">Pesquisar Ocorr\u00eancias</span></p></body></html>", None))
        self.txt_pesquisa_ocorrencia.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite um nome", None))
        self.btn_pesquisar_ocorrencias.setText(QCoreApplication.translate("MainWindow", u"Pesquisar", None))
        ___qtablewidgetitem75 = self.tb_ocorrencias.horizontalHeaderItem(0)
        ___qtablewidgetitem75.setText(QCoreApplication.translate("MainWindow", u"Id", None));
        ___qtablewidgetitem76 = self.tb_ocorrencias.horizontalHeaderItem(1)
        ___qtablewidgetitem76.setText(QCoreApplication.translate("MainWindow", u"N\u00famero Protocolo", None));
        ___qtablewidgetitem77 = self.tb_ocorrencias.horizontalHeaderItem(2)
        ___qtablewidgetitem77.setText(QCoreApplication.translate("MainWindow", u"Data Ocorr\u00eancia", None));
        ___qtablewidgetitem78 = self.tb_ocorrencias.horizontalHeaderItem(3)
        ___qtablewidgetitem78.setText(QCoreApplication.translate("MainWindow", u"Nome Funcion\u00e1rio", None));
        ___qtablewidgetitem79 = self.tb_ocorrencias.horizontalHeaderItem(4)
        ___qtablewidgetitem79.setText(QCoreApplication.translate("MainWindow", u"Hora Registro", None));
        ___qtablewidgetitem80 = self.tb_ocorrencias.horizontalHeaderItem(5)
        ___qtablewidgetitem80.setText(QCoreApplication.translate("MainWindow", u"Data Registro", None));
        ___qtablewidgetitem81 = self.tb_ocorrencias.horizontalHeaderItem(6)
        ___qtablewidgetitem81.setText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o", None));
        self.tabWidget_8.setTabText(self.tabWidget_8.indexOf(self.tab_16), QCoreApplication.translate("MainWindow", u"Pesquisar", None))
        self.label_106.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">Registrar Funcion\u00e1rios</span></p></body></html>", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Nome</span></p></body></html>", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Endere\u00e7o</span></p></body></html>", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Bairro</span></p></body></html>", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">CEP:</span></p></body></html>", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Telefone</span></p></body></html>", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Celular</span></p></body></html>", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Email</span></p></body></html>", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Observa\u00e7\u00f5es:</span></p></body></html>", None))
        self.btn_registrar_funcionarios.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.label_107.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">Pesquisar Funcion\u00e1rios</span></p></body></html>", None))
        self.txt_pesquisar_funcionario.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite um nome", None))
        self.btn_pesquisar_funcionarios.setText(QCoreApplication.translate("MainWindow", u"Pesquisar", None))
        ___qtablewidgetitem82 = self.tb_funcionarios.horizontalHeaderItem(0)
        ___qtablewidgetitem82.setText(QCoreApplication.translate("MainWindow", u"Id", None));
        ___qtablewidgetitem83 = self.tb_funcionarios.horizontalHeaderItem(1)
        ___qtablewidgetitem83.setText(QCoreApplication.translate("MainWindow", u"Nome Funcion\u00e1rio", None));
        ___qtablewidgetitem84 = self.tb_funcionarios.horizontalHeaderItem(2)
        ___qtablewidgetitem84.setText(QCoreApplication.translate("MainWindow", u"Endere\u00e7o", None));
        ___qtablewidgetitem85 = self.tb_funcionarios.horizontalHeaderItem(3)
        ___qtablewidgetitem85.setText(QCoreApplication.translate("MainWindow", u"Bairro", None));
        ___qtablewidgetitem86 = self.tb_funcionarios.horizontalHeaderItem(4)
        ___qtablewidgetitem86.setText(QCoreApplication.translate("MainWindow", u"Cep", None));
        ___qtablewidgetitem87 = self.tb_funcionarios.horizontalHeaderItem(5)
        ___qtablewidgetitem87.setText(QCoreApplication.translate("MainWindow", u"Telefone", None));
        ___qtablewidgetitem88 = self.tb_funcionarios.horizontalHeaderItem(6)
        ___qtablewidgetitem88.setText(QCoreApplication.translate("MainWindow", u"Celular", None));
        ___qtablewidgetitem89 = self.tb_funcionarios.horizontalHeaderItem(7)
        ___qtablewidgetitem89.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem90 = self.tb_funcionarios.horizontalHeaderItem(8)
        ___qtablewidgetitem90.setText(QCoreApplication.translate("MainWindow", u"Observa\u00e7\u00f5es", None));
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"Pesquisar", None))
        self.label_108.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">Registrar Dom\u00e9sticos</span></p></body></html>", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Nome</span></p></body></html>", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Apartamento</span></p></body></html>", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Bloco</span></p></body></html>", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Fun\u00e7\u00e3o</span></p></body></html>", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Hor\u00e1rio</span></p></body></html>", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Telefone</span></p></body></html>", None))
        self.btn_registrar_domesticos.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.label_109.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">Pesquisar Dom\u00e9sticos</span></p></body></html>", None))
        self.txt_pesquisar_domesticos.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite um nome", None))
        self.btn_pesquisar_domesticos.setText(QCoreApplication.translate("MainWindow", u"Pesquisar", None))
        ___qtablewidgetitem91 = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem91.setText(QCoreApplication.translate("MainWindow", u"Id", None));
        ___qtablewidgetitem92 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem92.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem93 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem93.setText(QCoreApplication.translate("MainWindow", u"Apartamento", None));
        ___qtablewidgetitem94 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem94.setText(QCoreApplication.translate("MainWindow", u"Bloco", None));
        ___qtablewidgetitem95 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem95.setText(QCoreApplication.translate("MainWindow", u"Fun\u00e7\u00e3o", None));
        ___qtablewidgetitem96 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem96.setText(QCoreApplication.translate("MainWindow", u"Hor\u00e1rio", None));
        ___qtablewidgetitem97 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem97.setText(QCoreApplication.translate("MainWindow", u"Telefone", None));
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Pesquisar", None))
        self.label_110.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">Agendar Mudan\u00e7a</span></p></body></html>", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Data da Mudan\u00e7a</span></p></body></html>", None))
        self.txt_data_mudanca.setPlaceholderText(QCoreApplication.translate("MainWindow", u" dd/mm/aaaa", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Hor\u00e1rio</span></p></body></html>", None))
        self.txt_horario_mudanca.setPlaceholderText(QCoreApplication.translate("MainWindow", u"  -- : --", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Respons\u00e1vel</span></p></body></html>", None))
        self.txt_nome_responsavel.setPlaceholderText(QCoreApplication.translate("MainWindow", u" Nome", None))
        self.txt_apartamento_mudanca.setPlaceholderText(QCoreApplication.translate("MainWindow", u" Apartamento", None))
        self.txt_bloco_mudanca.setPlaceholderText(QCoreApplication.translate("MainWindow", u" Bloco", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#ffffff;\">Nome da Empresa Contratada</span></p></body></html>", None))
        self.txt_nome_enp_mudanca.setPlaceholderText("")
        self.chk_uso_elevador.setText(QCoreApplication.translate("MainWindow", u"Uso do Elevador", None))
        self.chk_uso_escada.setText(QCoreApplication.translate("MainWindow", u"Uso da Escada", None))
        self.chk_icamento.setText(QCoreApplication.translate("MainWindow", u"I\u00e7amento", None))
        self.btn_registrar_mudancas.setText(QCoreApplication.translate("MainWindow", u"Agendar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Agendar", None))
        self.label_111.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">Pesquisar Mudan\u00e7a</span></p></body></html>", None))
        self.txt_data_mudanca_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite sua pesquisa", None))
        ___qtablewidgetitem98 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem98.setText(QCoreApplication.translate("MainWindow", u"Id", None));
        ___qtablewidgetitem99 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem99.setText(QCoreApplication.translate("MainWindow", u"Data", None));
        ___qtablewidgetitem100 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem100.setText(QCoreApplication.translate("MainWindow", u"Hor\u00e1rio", None));
        ___qtablewidgetitem101 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem101.setText(QCoreApplication.translate("MainWindow", u"Nome Respons\u00e1vel", None));
        ___qtablewidgetitem102 = self.tableWidget_2.horizontalHeaderItem(4)
        ___qtablewidgetitem102.setText(QCoreApplication.translate("MainWindow", u"Apartamento", None));
        ___qtablewidgetitem103 = self.tableWidget_2.horizontalHeaderItem(5)
        ___qtablewidgetitem103.setText(QCoreApplication.translate("MainWindow", u"Bloco", None));
        ___qtablewidgetitem104 = self.tableWidget_2.horizontalHeaderItem(6)
        ___qtablewidgetitem104.setText(QCoreApplication.translate("MainWindow", u"Nome Empresa", None));
        ___qtablewidgetitem105 = self.tableWidget_2.horizontalHeaderItem(7)
        ___qtablewidgetitem105.setText(QCoreApplication.translate("MainWindow", u"Uso Elevador", None));
        ___qtablewidgetitem106 = self.tableWidget_2.horizontalHeaderItem(8)
        ___qtablewidgetitem106.setText(QCoreApplication.translate("MainWindow", u"Uso Escada", None));
        ___qtablewidgetitem107 = self.tableWidget_2.horizontalHeaderItem(9)
        ___qtablewidgetitem107.setText(QCoreApplication.translate("MainWindow", u"I\u00e7amento", None));
        self.btn_pesquisar_mudancas.setText(QCoreApplication.translate("MainWindow", u"Pesquisar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Pesquisar", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:22pt; font-weight:600; color:#ffffff;\">SOBRE O SISTEMA</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">Funcionalidades:</span></p><p><span style=\" font-size:12pt; color:#ffffff;\">O sistemas para controle de portaria de condom\u00ednio residencial oferece op\u00e7\u00f5es para registro de moradores, ve\u00edculos, registro de visitantes, funcion\u00e1rios e prestadores, registro de ocorr\u00eancias, registro de encomendas, agendamento sal\u00e3o de festas e quiosques.</span></p><p><span style=\" color:#ffffff;\"><br/></span><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">Fun\u00e7\u00e3o de cada bot\u00e3o do menu latel:</span></p><p><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">Home:</span></p><p><span style=\" font-size:12pt; color:#ffffff;\">Possui bot\u00e3o para cadastro de novos usu\u00e1rios, com n\u00edveis de permiss\u00e3o.</span></p><p><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">Moradores:</span></p><p><span style=\" font-size:12pt; color:#ffffff;\">Possui a"
                        "s fun\u00e7\u00f5es para cadastro dos moradores por apartamento e bloco com o bot\u00e3o de cadastrar, tamb\u00e9m a fun\u00e7\u00e3o de pesquisar que pode ser realizada atrav\u00e9s do nome do morador ou pelo numero do apartamento seguido no numero do bloco.</span></p><p><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">Agendamentos:</span></p><p><span style=\" font-size:12pt; color:#ffffff;\">Faz o agendamento do sal\u00e3o de festas e dos quiosques.</span></p><p><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">Prestadores:</span></p><p><span style=\" font-size:12pt; color:#ffffff;\">fun\u00e7\u00e3o para cadastro de prestadores do condom\u00ednio e de apartamentos.</span></p><p><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">Encomendas: </span></p><p><span style=\" font-size:12pt; color:#ffffff;\">Tem a fun\u00e7\u00e3o de fazer o controle e distribui\u00e7\u00e3o das encomendas substituindo o livro de protocolo.</span></p><p><span style=\" font-size:14pt; fon"
                        "t-weight:600; color:#ffffff;\">Ocorr\u00eancias:</span></p><p><span style=\" font-size:12pt; color:#ffffff;\">Para registro geral de ocorr\u00eancias durante o expediente do porteiro.</span></p><p><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">Funcion\u00e1rios:</span></p><p><span style=\" font-size:12pt; color:#ffffff;\">Para registro de contatos dos funcion\u00e1rios do condom\u00ednio.</span></p><p><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">Dom\u00e9sticos:</span></p><p><span style=\" font-size:12pt; color:#ffffff;\">registrar a entrada de funcion\u00e1rios dos apartamentos.</span></p><p><span style=\" font-size:14pt; font-weight:600; color:#ffffff;\">Mudan\u00e7as:</span></p><p><span style=\" font-size:12pt; color:#ffffff;\">Agendamento de entrada e sa\u00edda das mudan\u00e7as e registro de eventuais incidentes durante a mudan\u00e7as.</span></p><p><span style=\" color:#ffffff;\"><br/></span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:22pt; font-weight:600; color:#ffffff;\">CONTATOS</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/_imgs/_imgs/whats.png\"/><span style=\" font-size:18pt; font-weight:600; color:#ffffff; vertical-align:super;\">(34) 99195-7588</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/_imgs/_imgs/email.png\"/><span style=\" font-size:18pt; font-weight:600; color:#ffffff; vertical-align:super;\">gilmargomes12@gmail.com</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600; color:#ffffff; vertical-align:super;\">2024 Copyright GHG</span></p></body></html>", None))
    # retranslateUi

