from PySide6.QtWidgets import QMainWindow, QMessageBox
import sys
from ui_login import Ui_LoginWindow
from database import DataBase
from main_window import MainWindow

class LoginWindow(QMainWindow, Ui_LoginWindow):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.setupUi(self)
        self.tentativas = 0

        self.btn_login.clicked.connect(self.check_Login)

    def check_Login(self):
        self.usuarios = DataBase()
        autenticado = self.usuarios.checkUser(self.txt_user.text(), self.txt_password.text())
        print(f"Tipo de usuário autenticado: {autenticado}") 
        if autenticado in ["Administrador", "Sindico", "Porteiro"]:
            user = self.txt_user.text().upper()
            self.userTyper = autenticado
            self.MainProgram = MainWindow(user, autenticado)
            self.MainProgram.show()
            self.close()
        else:
            if self.tentativas < 3:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle("Erro ao acessar")
                msg.setText(f'Login ou senha incorreto \n \nTentativa:{self.tentativas + 1} de 3 ')
                msg.exec()
                self.tentativas += 1

                if self.tentativas >= 3:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Warning)
                    msg.setWindowTitle("Número de tentativas excedido")
                    msg.setText(f'Você excedeu o número de tentativas \n O programa será encerrado.')
                    msg.exec()
                    sys.exit(0)