from PySide6.QtWidgets import QMessageBox, QTableWidgetItem
from database import DataBase
from validators import validar_cpf, validar_rg


def registrar_visitante(self):
    try:
        nome_visitante = self.txt_nome_visitante.text()
        rg_cpf_visitante = self.txt_rg_cpf_visitante.text()
        apartamento_bloco_visitantes = self.txt_apartamento_bloco_visitantes.text() 
        data_visita = self.txt_data_visita.text()
        visitando = self.txt_visitando.text()
        hora_entrada_visita = self.txt_hora_entrada_visita.text()
        hora_saida_visita = self.txt_hora_saida_visita.text()
        quem_autorizou_visita = self.txt_quem_autorizou_visita.text()
        vaga_utilizada = self.cmb_vaga_utilizada.currentText()
        placa_visitante = self.txt_placa_visitante.text()
        marca_visitante = self.txt_marca_visitante.text()
        modelo_visitante = self.txt_modelo_visitante.text()
        cor_visitante = self.txt_cor_visitante.text()

        if not (validar_cpf(rg_cpf_visitante) or validar_rg(rg_cpf_visitante)):
            QMessageBox.critical(self, 'ERRO', 'RG ou CPF inválido!')
            return

        db = DataBase()
        db.inserir_visitante(nome_visitante, rg_cpf_visitante, visitando, apartamento_bloco_visitantes, data_visita, hora_entrada_visita, hora_saida_visita, quem_autorizou_visita, vaga_utilizada, placa_visitante, marca_visitante, modelo_visitante, cor_visitante)

        QMessageBox.information(self, 'OK', 'Visitante registrado com sucesso!', QMessageBox.Ok)

        self.txt_nome_visitante.setText("")
        self.txt_rg_cpf_visitante.setText("")
        self.txt_apartamento_bloco_visitantes.setText("")
        self.txt_data_visita.setText("")
        self.txt_visitando.setText("")
        self.txt_hora_entrada_visita.setText("")
        self.txt_hora_saida_visita.setText("")
        self.txt_quem_autorizou_visita.setText("")
        self.cmb_vaga_utilizada.setCurrentIndex(0)
        self.txt_placa_visitante.setText("")
        self.txt_marca_visitante.setText("")
        self.txt_modelo_visitante.setText("")
        self.txt_cor_visitante.setText("")

    except AttributeError as e:
        print(f"Erro: {e}")
        QMessageBox.critical(self, 'ERRO', f"Erro ao registrar visitante: {e}")


def pesquisar_visitantes(self):
    try:
        nome = self.txt_nome_visitante.text()
        rg_cpf = self.txt_rg_cpf_visitante.text()
        apartamento_bloco = self.txt_apartamento_bloco.text()
        data_visita = self.txt_data_visita.text()
        hora_entrada_visita = self.txt_hora_entrada_visita.text()
        hora_saida_visita = self.txt_hora_saida_visita.text()
        quem_autorizou_visita = self.txt_quem_autorizou_visita.text()
        vaga_utilizada = self.cmb_vaga_utilizada.setCurrentIndex()
        placa_visitante = self.txt_placa_visitante.text()
        marca_visitante = self.txt_marca_visitante.text()
        modelo_visitante = self.txt_modelo_visitante.text()
        cor_visitante = self.txt_cor_visitante.text()

        db = DataBase()
        resultados = db.pesquisar_visitantes(nome, rg_cpf, apartamento_bloco, data_visita, hora_entrada_visita, hora_saida_visita, quem_autorizou_visita, vaga_utilizada, placa_visitante, marca_visitante, modelo_visitante, cor_visitante)

        # Exibir resultados (exemplo: em uma tabela)
        self.tabela_resultados.setRowCount(len(resultados))
        for row_idx, row_data in enumerate(resultados):
            for col_idx, col_data in enumerate(row_data):
                self.tabela_resultados.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))

    except AttributeError as e:
        print(f"Erro: {e}")
        QMessageBox.critical(self, 'ERRO', f"Erro ao pesquisar visitantes: {e}")     