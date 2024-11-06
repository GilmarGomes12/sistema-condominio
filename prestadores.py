from PySide6.QtWidgets import QMessageBox, QTableWidgetItem
from database import DataBase
from validators import validar_cpf, validar_rg


def registrar_prestadores(self):
    try:
        nome_empresa = self.txt_nome_empresa.text()
        tipo_servico = self.txt_tipo_servico.text()
        data_servico = self.txt_data_servico.text() 
        hora_entrada_prestador = self.txt_hora_entrada_prestador.text()
        hora_saida_prestador = self.txt_hora_saida_prestador.text()
        nome_prestador = self.txt_nome_prestador.text()
        rg_cpf_prestador = self.txt_rg_cpf_prestador.text()
        telefone_prestador = self.txt_telefone_prestador.text()
        contratante = self.txt_contratante.text()
        apartamento_bloco_prestador = self.txt_apartamento_bloco_prestador.text()
        autorizou_entrada = self.txt_autorizou_entrada.text()

        if not (validar_cpf(rg_cpf_prestador) or validar_rg(rg_cpf_prestador)):
            QMessageBox.critical(self, 'ERRO', 'RG ou CPF inválido!')
            return

        db = DataBase()
        db.inserir_prestadores(nome_empresa, tipo_servico, data_servico, hora_entrada_prestador, hora_saida_prestador, nome_prestador, rg_cpf_prestador, telefone_prestador, contratante, apartamento_bloco_prestador, autorizou_entrada)

        QMessageBox.information(self, 'OK', 'Prestador registrado com sucesso!', QMessageBox.Ok)

        self.txt_nome_empresa.setText("")
        self.txt_tipo_servico.setText("")
        self.txt_data_servico.setText("")
        self.txt_hora_entrada_prestador.setText("")
        self.txt_hora_saida_prestador.setText("")
        self.txt_nome_prestador.setText("")
        self.txt_rg_cpf_prestador.setText("")
        self.txt_telefone_prestador.setText("")
        self.txt_contratante.setText("")
        self.txt_apartamento_bloco_prestador.setText("")
        self.txt_autorizou_entrada.setText("")

    except AttributeError as e:
        print(f"Erro: {e}")
        QMessageBox.critical(self, 'ERRO', f"Erro ao registrar prestador: {e}")


def pesquisar_prestadores(self):
    try:
        nome_empresa = self.txt_nome_empresa.text()
        tipo_servico = self.txt_tipo_servico.text()
        data_servico = self.txt_data_servico.text() 
        hora_entrada_prestador = self.txt_hora_entrada_prestador.text()
        hora_saida_prestador = self.txt_hora_saida_prestador.text()
        nome_prestador = self.txt_nome_prestador.text()
        rg_cpf_prestador = self.txt_rg_cpf_prestador.text()
        telefone_prestador = self.txt_telefone_prestador.text()
        contratante = self.txt_contratante.text()
        apartamento_bloco_prestador = self.txt_apartamento_bloco_prestador.text()
        autorizou_entrada = self.txt_autorizou_entrada.text()

        db = DataBase()
        resultados = db.pesquisar_prestadores(nome_empresa, tipo_servico, data_servico, hora_entrada_prestador, hora_saida_prestador, nome_prestador, rg_cpf_prestador, telefone_prestador, contratante, apartamento_bloco_prestador, autorizou_entrada)

        # Exibir resultados (exemplo: em uma tabela)
        self.tabela_resultados.setRowCount(len(resultados))
        for row_idx, row_data in enumerate(resultados):
            for col_idx, col_data in enumerate(row_data):
                self.tabela_resultados.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))

    except AttributeError as e:
        print(f"Erro: {e}")
        QMessageBox.critical(self, 'ERRO', f"Erro ao pesquisar prestadores: {e}")     