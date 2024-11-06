from PySide6.QtWidgets import QMessageBox, QTableWidgetItem
from database import DataBase

def registrar_agendamento(self):
    try:
        ag_apartamento_bloco = self.txt_ag_apartamento_bloco.text()
        ag_nome_morador = self.txt_ag_nome_morador.text()
        local = self.cmb_local.currentText()
        periodo = self.cmb_periodo.currentText()
        data_agendamento = self.txt_data_agendamento.text()
        ag_funcionario = self.txt_ag_funcionario.text()
        ag_observacoes = self.txt_ag_observacoes.toPlainText()

        db = DataBase()
        db.inserir_agendamento(ag_apartamento_bloco, ag_nome_morador, local, periodo, data_agendamento, ag_funcionario, ag_observacoes)

        QMessageBox.information(self, 'OK', 'Agendamento registrado com sucesso!', QMessageBox.Ok)

        self.txt_ag_apartamento_bloco.setText("")
        self.txt_ag_nome_morador.setText("")
        self.cmb_local.setCurrentIndex(0)
        self.cmb_periodo.setCurrentIndex(0)
        self.txt_data_agendamento.setText("")
        self.txt_ag_funcionario.setText("")
        self.txt_ag_observacoes.setPlainText("")
    except AttributeError as e:
        print(f"Erro: {e}")
        QMessageBox.critical(self, 'ERRO', f"Erro ao registrar agendamento: {e}")

def pesquisar_agendamentos(self):
    try:
        ag_apartamento_bloco = self.txt_ag_apartamento_bloco.text()
        ag_nome_morador = self.txt_ag_nome_morador.text()
        local = self.cmb_local.currentText()
        periodo = self.cmb_periodo.currentText()
        data_agendamento = self.txt_data_agendamento.text()
        ag_funcionario = self.txt_ag_funcionario.text()

        db = DataBase()
        resultados = db.pesquisar_agendamentos(ag_apartamento_bloco, ag_nome_morador, local, periodo, data_agendamento, ag_funcionario)

        # Exibir resultados (exemplo: em uma tabela)
        self.tabela_resultados.setRowCount(len(resultados))
        for row_idx, row_data in enumerate(resultados):
            for col_idx, col_data in enumerate(row_data):
                self.tabela_resultados.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))

    except AttributeError as e:
        print(f"Erro: {e}")
        QMessageBox.critical(self, 'ERRO', f"Erro ao pesquisar agendamentos: {e}")