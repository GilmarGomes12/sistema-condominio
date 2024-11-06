from PySide6.QtWidgets import QMessageBox, QTableWidgetItem
from database import DataBase


def registrar_funcionarios(self):
    try:    
        nome_funcionarios = self.txt_nome_funcionarios.text()       
        endereco_funcionario = self.txt_endereco_funcionario.text()
        bairro_funcionario = self.txt_bairro_funcionario.text() 
        cep_funcionario = self.txt_cep_funcionario.text()
        telefone_funcionario = self.txt_telefone_funcionario.text()
        celular_funcionario = self.txt_celular_funcionario.text()
        email_funcionario = self.txt_email_funcionario.text()
        observacao_funcionario = self.txt_observacao_funcionario.toPlainText()

        db = DataBase()
        db.inserir_funcionarios(nome_funcionarios, endereco_funcionario, bairro_funcionario, cep_funcionario, telefone_funcionario, celular_funcionario, email_funcionario, observacao_funcionario)

        QMessageBox.information(self, 'OK', f'Funcionário registrada com sucesso!', QMessageBox.Ok)

        self.txt_nome_funcionarios.setText("")
        self.txt_endereco_funcionario.setText("")
        self.txt_bairro_funcionario.setText("")
        self.txt_cep_funcionario.setText("")
        self.txt_telefone_funcionario.setText("")
        self.txt_celular_funcionario.setText("")
        self.txt_email_funcionario.setText("")
        self.txt_observacao_funcionario.setText("")

    except AttributeError as e:
        print(f"Erro: {e}")
        QMessageBox.critical(self, 'ERRO', f"Erro ao registrar funcionário: {e}")


def pesquisar_funcionarios(self):
    try:
        nome_funcionarios = self.txt_nome_funcionarios.text()
        endereco_funcionario = self.txt_endereco_funcionario.text() 
        bairro_funcionario = self.txt_bairro_funcionario.text()
        cep_funcionario = self.txt_cep_funcionario.text()
        telefone_funcionario = self.txt_telefone_funcionario.text()
        celular_funcionario = self.txt_celular_funcionario.text()
        email_funcionario = self.txt_email_funcionario.text()
        observacao_funcionario = self.txt_observacao_funcionario.toPlainText()

        db = DataBase()
        resultados = db.pesquisar_funcionarios(nome_funcionarios, endereco_funcionario, bairro_funcionario, cep_funcionario, celular_funcionario, email_funcionario, observacao_funcionario)
        # Exibir resultados (exemplo: em uma tabela)
        self.tabela_resultados.setRowCount(len(resultados))
        for row_idx, row_data in enumerate(resultados):
            for col_idx, col_data in enumerate(row_data):
                self.tabela_resultados.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))

    except AttributeError as e:
        print(f"Erro: {e}")
        QMessageBox.critical(self, 'ERRO', f"Erro ao pesquisar funcionário: {e}")