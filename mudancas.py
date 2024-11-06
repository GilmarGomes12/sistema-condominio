from PySide6.QtWidgets import QMessageBox, QTableWidgetItem
from database import DataBase


def registrar_mudancas(self):
    try:    
        data_mudanca = self.txt_data_mudanca.text()       
        horario_mudanca = self.txt_horario_mudanca.text()
        nome_responsavel = self.txt_nome_responsavel.text() 
        apartamento_mudanca = self.txt_apartamento_mudanca.text()
        bloco_mudanca = self.txt_bloco_mudanca.text()
        nome_enp_mudanca = self.txt_nome_enp_mudanca.text()
        uso_elevador = self.chk_uso_elevador.isChecked()
        uso_escada = self.chk_uso_escada.isChecked()
        icamento = self.chk_icamento.isChecked()

        db = DataBase()
        db.inserir_mudancas(data_mudanca, horario_mudanca, nome_responsavel, apartamento_mudanca, bloco_mudanca, nome_enp_mudanca, uso_elevador, uso_escada, icamento)

        QMessageBox.information(self, 'OK', f'Mudança registrada com sucesso!', QMessageBox.Ok)

        self.txt_data_mudanca.setText("")
        self.txt_horario_mudanca.setText("")
        self.txt_nome_responsavel.setText("")
        self.txt_apartamento_mudanca.setText("")
        self.txt_bloco_mudanca.setText("")
        self.txt_nome_enp_mudanca.setText("")
        self.chk_uso_elevador.setChecked(False)
        self.chk_uso_escada.setChecked(False)
        self.chk_icamento.setChecked(False)

    except AttributeError as e:
        print(f"Erro: {e}")
        QMessageBox.critical(self, 'ERRO', f"Erro ao registrar mudança: {e}")


def pesquisar_mudancas(self):
    try:
        data_mudanca = self.txt_data_mudanca.text()
        horario_mudanca = self.txt_horario_mudanca.text() 
        nome_responsavel = self.txt_nome_responsavel.text()
        apartamento_mudanca = self.txt_apartamento_mudanca.text()
        bloco_mudanca = self.txt_bloco_mudanca.text()
        nome_enp_mudanca = self.txt_nome_enp_mudanca.text()
        uso_elevador = self.chk_uso_elevador.isChecked()
        uso_escada = self.chk_uso_escada.isChecked()
        icamento = self.chk_icamento.isChecked()

        db = DataBase()
        resultados = db.pesquisar_mudancas(data_mudanca, horario_mudanca, nome_responsavel, apartamento_mudanca , bloco_mudanca , nome_enp_mudanca, uso_elevador, uso_escada, icamento)
        # Exibir resultados (exemplo: em uma tabela)
        self.tabela_resultados.setRowCount(len(resultados))
        for row_idx, row_data in enumerate(resultados):
            for col_idx, col_data in enumerate(row_data):
                self.tabela_resultados.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))

    except AttributeError as e:
        print(f"Erro: {e}")
        QMessageBox.critical(self, 'ERRO', f"Erro ao pesquisar mudança: {e}")