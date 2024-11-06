from PySide6.QtWidgets import QMessageBox, QTableWidgetItem
from database import DataBase


def registrar_domesticos(self):
    try:    
        nome_domestico = self.txt_nome_domestico.text()       
        apartamento_domestico = self.txt_apartamento_domestico.text()
        bloco_domestico = self.txt_bloco_domestico.text() 
        funcao_domestico = self.txt_funcao_domestico.text()
        horario_domestico = self.txt_horario_domestico.text()
        telefone_domestico = self.txt_telefone_domestico.text()

        db = DataBase()
        db.inserir_domesticos(nome_domestico, apartamento_domestico, bloco_domestico, funcao_domestico, horario_domestico, telefone_domestico)

        QMessageBox.information(self, 'OK', f'Doméstico registrada com sucesso!', QMessageBox.Ok)

        self.txt_nome_domestico.setText("")
        self.txt_apartamento_domestico.setText("")
        self.txt_bloco_domestico.setText("")
        self.txt_funcao_domestico.setText("")
        self.txt_horario_domestico.setText("")
        self.txt_telefone_domestico.setText("")

    except AttributeError as e:
        print(f"Erro: {e}")
        QMessageBox.critical(self, 'ERRO', f"Erro ao registrar doméstico: {e}")


def pesquisar_domesticos(self):
    try:
        nome_domestico = self.txt_nome_domestico.text()
        apartamento_domestico = self.txt_apartamento_domestico.text() 
        bloco_domestico = self.txt_bloco_domestico.text()
        funcao_domestico = self.txt_funcao_domestico.text()
        horario_domestico = self.txt_horario_domestico.text()
        telefone_domestico = self.txt_telefone_domestico.text()

        db = DataBase()
        resultados = db.pesquisar_domesticos(nome_domestico, apartamento_domestico, bloco_domestico, funcao_domestico , horario_domestico ,telefone_domestico)
        # Exibir resultados (exemplo: em uma tabela)
        self.tabela_resultados.setRowCount(len(resultados))
        for row_idx, row_data in enumerate(resultados):
            for col_idx, col_data in enumerate(row_data):
                self.tabela_resultados.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))

    except AttributeError as e:
        print(f"Erro: {e}")
        QMessageBox.critical(self, 'ERRO', f"Erro ao pesquisar doméstico: {e}")