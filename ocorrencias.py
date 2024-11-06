from PySide6.QtWidgets import QMessageBox, QTableWidgetItem
from database import DataBase
import uuid


def registrar_ocorrencias(self):
    try:     
        numero_protocolo_ocorrencias = self.txt_numero_protocolo_ocorrencias.text()       
        data_ocorrencia = self.txt_data_ocorrencia.text()
        nome_funcionario = self.txt_nome_funcionario.text() 
        hora_registro = self.txt_hora_registro.text()
        data_registro = self.txt_data_registro.text()
        descricao = self.txt_descricao.toPlainText()

        db = DataBase()
        db.inserir_ocorrencias(numero_protocolo_ocorrencias, data_ocorrencia, nome_funcionario, hora_registro, data_registro, descricao)

        QMessageBox.information(self, 'OK', f'Ocorrência registrada com sucesso! Protocolo: {numero_protocolo_ocorrencias}', QMessageBox.Ok)

        self.txt_numero_protocolo_ocorrencias.setText("")
        self.txt_data_ocorrencia.setText("")
        self.txt_nome_funcionario.setText("")
        self.txt_hora_registro.setText("")
        self.txt_data_registro.setText("")
        self.txt_descricao.setText("")

    except AttributeError as e:
        print(f"Erro: {e}")
        QMessageBox.critical(self, 'ERRO', f"Erro ao registrar ocorrência: {e}")


def pesquisar_ocorrencias(self):
    try:
        data_ocorrencia = self.txt_data_ocorrencia.text()
        nome_funcionario = self.txt_nome_funcionario.text() 
        hora_registro = self.txt_hora_registro.text()
        data_registro = self.txt_data_registro.text()
        descricao = self.txt_descricao.toPlainText()

        db = DataBase()
        resultados = db.pesquisar_ocorrencias(data_ocorrencia, nome_funcionario, hora_registro, data_registro, descricao)
        # Exibir resultados (exemplo: em uma tabela)
        self.tabela_resultados.setRowCount(len(resultados))
        for row_idx, row_data in enumerate(resultados):
            for col_idx, col_data in enumerate(row_data):
                self.tabela_resultados.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))

    except AttributeError as e:
        print(f"Erro: {e}")
        QMessageBox.critical(self, 'ERRO', f"Erro ao pesquisar ocorrência: {e}")