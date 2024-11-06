from PySide6.QtWidgets import QMessageBox, QTableWidgetItem
from database import DataBase
from validators import validar_cpf, validar_rg
from datetime import datetime


def obter_data_hora_atual():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def registrar_encomendas(self):
    try:
        numero_protocolo = self.txt_numero_protocolo.text()
        data_hora_recebimento = datetime.now().isoformat() 
        self.txt_data_hora_recebimento.setText(data_hora_recebimento)
        nome_destinatario = self.txt_nome_destinatario.text() 
        apartamento_bloco_encomendas = self.txt_apartamento_bloco_encomendas.text()
        numero_rastreamento = self.txt_numero_rastreamento.text()
        tipo_encomenda = self.cmb_tipo_encomenda.currentText()
        descricao_encomenda = self.txt_descricao_encomenda.toPlainText()
        empresa_entrega = self.txt_empresa_entrega.text()
        observacoes_encomendas = self.txt_observacoes_encomendas.toPlainText()
        nome_entregador = self.txt_nome_entregador.text()
        rg_cpf_entregador = self.txt_rg_cpf_entregador.text()
        nome_porteiro = self.txt_nome_porteiro.text()
        nome_retirou = self.txt_nome_retirou.text()

        if not (validar_cpf(rg_cpf_entregador) or validar_rg(rg_cpf_entregador)):
            QMessageBox.critical(self, 'ERRO', 'RG ou CPF inválido!')
            return

        db = DataBase()
        db.inserir_encomendas(numero_protocolo, data_hora_recebimento, nome_destinatario, apartamento_bloco_encomendas, numero_rastreamento, tipo_encomenda, descricao_encomenda, empresa_entrega, observacoes_encomendas, nome_entregador, rg_cpf_entregador, nome_porteiro, nome_retirou)

        QMessageBox.information(self, 'OK', f'Encomenda registrada com sucesso! Protocolo: {numero_protocolo}', QMessageBox.Ok)

        self.txt_numero_protocolo.setText("")
        self.txt_data_hora_recebimento.setText("")
        self.txt_nome_destinatario.setText("")
        self.txt_nome_destinatario.setText("")
        self.txt_apartamento_bloco_encomendas.setText("")
        self.txt_numero_rastreamento.setText("")
        self.cmb_tipo_encomenda.setCurrentIndex(0)
        self.txt_descricao_encomenda.setText("")
        self.txt_empresa_entrega.setText("")
        self.txt_observacoes_encomendas.setText("")
        self.txt_nome_entregador.setText("")
        self.txt_rg_cpf_entregador.setText("")
        self.txt_nome_porteiro.setText("")
        self.txt_nome_retirou.setText("")

    except AttributeError as e:
        print(f"Erro: {e}")
        QMessageBox.critical(self, 'ERRO', f"Erro ao registrar encomenda: {e}")


def pesquisar_encomendas(self):
    try:
        numero_protocolo = self.txt_numero_protocolo.text()
        data_hora_recebimento = self.txt_data_hora_recebimento.text()
        nome_destinatario = self.txt_nome_destinatario.text() 
        apartamento_bloco_encomendas = self.txt_apartamento_bloco_encomendas.text()
        numero_rastreamento = self.txt_numero_rastreamento.text()
        tipo_encomenda = self.cmb_tipo_encomenda.currentText()
        descricao_encomenda = self.txt_descricao_encomenda.toPlainText()
        empresa_entrega = self.txt_empresa_entrega.text()
        observacoes_encomendas = self.txt_observacoes_encomendas.toPlainText()
        nome_entregador = self.txt_nome_entregador.text()
        rg_cpf_entregador = self.txt_rg_cpf_entregador.text()
        nome_porteiro = self.txt_nome_porteiro.text()
        nome_retirou = self.txt_nome_retirou.text()

        db = DataBase()
        resultados = db.pesquisar_encomendas(numero_protocolo, data_hora_recebimento, nome_destinatario, apartamento_bloco_encomendas, numero_rastreamento, tipo_encomenda, descricao_encomenda, empresa_entrega, observacoes_encomendas, nome_entregador, rg_cpf_entregador, nome_porteiro, nome_retirou)
        # Exibir resultados (exemplo: em uma tabela)
        self.tabela_resultados.setRowCount(len(resultados))
        for row_idx, row_data in enumerate(resultados):
            for col_idx, col_data in enumerate(row_data):
                self.tabela_resultados.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))

    except AttributeError as e:
        print(f"Erro: {e}")
        QMessageBox.critical(self, 'ERRO', f"Erro ao pesquisar encomenda: {e}")     