from PySide6.QtWidgets import QMessageBox, QTableWidgetItem
from database import DataBase
from validators import validar_cpf, validar_rg
from datetime import datetime
import uuid

def obter_data_hora_atual():
    return datetime.now().strftime('%d/%m/%Y %H:%M:%S')

def gerar_numero_protocolo():
    return str(uuid.uuid4())

def registrar_encomendas(self):
    try:
        numero_protocolo = self.txt_numero_protocolo.text()
        data_hora_recebimento = obter_data_hora_atual()
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

        db = DataBase()
        db.inserir_encomendas(numero_protocolo, data_hora_recebimento, nome_destinatario, apartamento_bloco_encomendas, numero_rastreamento, tipo_encomenda, descricao_encomenda, empresa_entrega, observacoes_encomendas, nome_entregador, rg_cpf_entregador, nome_porteiro, nome_retirou)

        # Verificar se os dados foram inseridos corretamente
        db.listar_todas_encomendas()

        QMessageBox.information(self, 'OK', f'Encomenda registrada com sucesso! Protocolo: {numero_protocolo}', QMessageBox.Ok)

        self.txt_numero_protocolo.setText("")
        self.txt_data_hora_recebimento.setText("")
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

        novo_protocolo = gerar_numero_protocolo()
        self.txt_numero_protocolo.setText(novo_protocolo)

        nova_data_hora_recebimento = obter_data_hora_atual()
        self.txt_data_hora_recebimento.setText(nova_data_hora_recebimento)

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

        print(f"Parâmetros de pesquisa: {numero_protocolo}, {data_hora_recebimento}, {nome_destinatario}, {apartamento_bloco_encomendas}, {numero_rastreamento}, {tipo_encomenda}, {descricao_encomenda}, {empresa_entrega}, {observacoes_encomendas}, {nome_entregador}, {rg_cpf_entregador}, {nome_porteiro}, {nome_retirou}")

        db = DataBase()
        resultados = db.pesquisar_encomendas(numero_protocolo, data_hora_recebimento, nome_destinatario, apartamento_bloco_encomendas, numero_rastreamento, tipo_encomenda, descricao_encomenda, empresa_entrega, observacoes_encomendas, nome_entregador, rg_cpf_entregador, nome_porteiro, nome_retirou)
        
        if resultados:
            print(f"Resultados encontrados: {resultados}")
            self.tb_encomendas.setRowCount(len(resultados))
            self.tb_encomendas.setColumnCount(len(resultados[0]) if resultados else 0)
            for row_idx, row_data in enumerate(resultados):
                for col_idx, col_data in enumerate(row_data):
                    self.tb_encomendas.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))
        else:
            print("Nenhum resultado encontrado.")
            QMessageBox.information(self, 'Pesquisa', 'Nenhum resultado encontrado.', QMessageBox.Ok)

    except AttributeError as e:
        print(f"Erro: {e}")
        QMessageBox.critical(self, 'ERRO', f"Erro ao pesquisar encomenda: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")
        QMessageBox.critical(self, 'ERRO', f"Erro inesperado ao pesquisar encomenda: {e}")