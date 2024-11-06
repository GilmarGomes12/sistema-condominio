from PySide6.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem
from PySide6.QtGui import QIcon
from ui_main import Ui_MainWindow
from database import DataBase
from morador import cadastrar_morador, pesquisar_morador
from agendamento import registrar_agendamento, pesquisar_agendamentos
from visitante import registrar_visitante, pesquisar_visitantes
from prestadores import registrar_prestadores, pesquisar_prestadores
from encomendas import registrar_encomendas, pesquisar_encomendas
from ocorrencias import registrar_ocorrencias, pesquisar_ocorrencias
from funcionarios import registrar_funcionarios, pesquisar_funcionarios
from domesticos import registrar_domesticos, pesquisar_domesticos
from mudancas import registrar_mudancas, pesquisar_mudancas
import uuid

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, user, user_type):
        super(MainWindow, self).__init__()
        self.user_type = user_type
        self.user = user
        self.campo = ""
        self.setupUi(self)
        self.setWindowTitle('Sistema de Gerenciamento - Portaria')
        self.setWindowIcon(QIcon('icon.png'))


    # Gere o número de protocolo ao inicializar
        self.numero_protocolo()
    def numero_protocolo(self):
        numero_protocolo = str(uuid.uuid4())
        print(f"Gerando número de protocolo: {numero_protocolo}")
        self.txt_numero_protocolo.setText(numero_protocolo)


    # Gere o número de protocolo ao inicializar
        self.numero_protocolo_ocorrencias()
    def numero_protocolo_ocorrencias(self):
        numero_protocolo_ocorrencias = str(uuid.uuid4())
        print(f"Gerando número de protocolo: {numero_protocolo_ocorrencias}")
        self.txt_numero_protocolo_ocorrencias.setText(numero_protocolo_ocorrencias)        


        # Verifica o tipo de usuário e habilita as opções
        print(f"Tipo de usuário: {self.user_type}")  
        if self.user_type.lower() == 'porteiro':
            self.btn_menu_cadastrar.setVisible(False)

        # PÁGINAS DO SISTEMA
        self.btn_home.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_home))
        self.btn_menu_cadastrar.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_cadastro))
        self.btn_menu_moradores.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_moradores))
        self.btn_menu_agendamentos.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_agendamento))
        self.btn_menu_visitantes.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_visitantes))
        self.btn_menu_prestadores.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_prestadores))
        self.btn_menu_encomendas.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_encomendas))
        self.btn_menu_ocorrencias.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_ocorrencias))
        self.btn_menu_funcionarios.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_funcionarios))
        self.btn_menu_domesticos.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_domesticos))
        self.btn_menu_mudancas.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_mudancas))
        self.btn_menu_sobre.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_sobre))
        self.btn_menu_contatos.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_contatos))

        self.btn_cadastrar_usuario.clicked.connect(self.cadastrar_usuario)
        self.btn_cadastrar_morador.clicked.connect(lambda: cadastrar_morador(self))
        self.btn_pesquisar_morador.clicked.connect(lambda: pesquisar_morador(self))
        self.btn_registrar_agendamento.clicked.connect(lambda: registrar_agendamento(self))
        self.btn_pesquisar_agendamentos.clicked.connect(lambda: pesquisar_agendamentos(self))
        self.btn_registrar_visitante.clicked.connect(lambda: registrar_visitante(self))
        self.btn_pesquisar_visitantes.clicked.connect(lambda: pesquisar_visitantes)
        self.btn_registrar_prestadores.clicked.connect(lambda: registrar_prestadores(self))
        self.btn_pesquisar_prestadores.clicked.connect(lambda: pesquisar_prestadores(self))
        self.btn_registrar_encomendas.clicked.connect(lambda: registrar_encomendas(self))
        self.btn_pesquisar_encomendas.clicked.connect(lambda: pesquisar_encomendas(self))
        self.btn_registrar_ocorrencias.clicked.connect(lambda: registrar_ocorrencias(self))
        self.btn_pesquisar_ocorrencias.clicked.connect(lambda: pesquisar_ocorrencias(self))
        self.btn_registrar_funcionarios.clicked.connect(lambda: registrar_funcionarios(self))
        self.btn_pesquisar_funcionarios.clicked.connect(lambda: pesquisar_funcionarios(self))
        self.btn_registrar_domesticos.clicked.connect(lambda: registrar_domesticos(self))
        self.btn_pesquisar_domesticos.clicked.connect(lambda: pesquisar_domesticos(self))
        self.btn_registrar_mudancas.clicked.connect(lambda: registrar_mudancas(self))
        self.btn_pesquisar_mudancas.clicked.connect(lambda: pesquisar_mudancas(self))

    def cadastrar_usuario(self):
        if self.txt_senha.text() != self.txt_senha_2.text(): 
            QMessageBox.critical(self, 'ERRO', 'A senha informada não é igual')
            return None     
        nome = self.txt_nome.text()
        user = self.txt_user.text()
        password = self.txt_senha.text()
        acesso = self.cb_perfil.currentText()
        
        db = DataBase()
        db.inserirUsuario(nome, user, password, acesso)
        
        QMessageBox.information(self, 'OK', 'Cadastro realizado com sucesso!', QMessageBox.Ok)
  
        self.txt_nome.setText("")
        self.txt_user.setText("")
        self.txt_senha.setText("")
        self.txt_senha_2.setText("")