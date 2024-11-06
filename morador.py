from PySide6.QtWidgets import QMessageBox, QTableWidgetItem
from PySide6.QtCore import Qt
from database import DataBase

def cadastrar_morador(self):
    try:
        apartamento_bloco = self.txt_apartamento_bloco.text()
        moradores = [
            (self.txt_nome_completo.text(), self.txt_data_nascimento.text()),
            (self.txt_nome_completo2.text(), self.txt_data_nascimento2.text()),
            (self.txt_nome_completo3.text(), self.txt_data_nascimento3.text()),
            (self.txt_nome_completo4.text(), self.txt_data_nascimento4.text()),
            (self.txt_nome_completo5.text(), self.txt_data_nascimento5.text()),
            (self.txt_nome_completo6.text(), self.txt_data_nascimento6.text())
        ]
        telefone1 = self.txt_telefone1.text()
        telefone2 = self.txt_telefone2.text()
        email1 = self.txt_email1.text()
        email2 = self.txt_email2.text()
        veiculo1 = {
            'placa': self.txt_veiculo1_placa.text(),
            'marca': self.txt_veiculo1_marca.text(),
            'modelo': self.txt_veiculo1_modelo.text(),
            'cor': self.txt_veiculo1_cor.text()
        }
        veiculo2 = {
            'placa': self.txt_veiculo2_placa.text(),
            'marca': self.txt_veiculo2_marca.text(),
            'modelo': self.txt_veiculo2_modelo.text(),
            'cor': self.txt_veiculo2_cor.text()
        }
        observacoes = self.txt_observacoes.toPlainText()

        db = DataBase()
        db.inserir_morador(apartamento_bloco, moradores, telefone1, telefone2, email1, email2, veiculo1, veiculo2, observacoes)

        QMessageBox.information(self, 'OK', 'Morador cadastrado com sucesso!', QMessageBox.Ok)

        self.txt_apartamento_bloco.setText("")
        self.txt_nome_completo.setText("")
        self.txt_data_nascimento.setText("")
        self.txt_nome_completo2.setText("")
        self.txt_data_nascimento2.setText("")
        self.txt_nome_completo3.setText("")
        self.txt_data_nascimento3.setText("")
        self.txt_nome_completo4.setText("")
        self.txt_data_nascimento4.setText("")
        self.txt_nome_completo5.setText("")
        self.txt_data_nascimento5.setText("")
        self.txt_nome_completo6.setText("")
        self.txt_data_nascimento6.setText("")
        self.txt_telefone1.setText("")
        self.txt_telefone2.setText("")
        self.txt_email1.setText("")
        self.txt_email2.setText("")
        self.txt_veiculo1_placa.setText("")
        self.txt_veiculo1_marca.setText("")
        self.txt_veiculo1_modelo.setText("")
        self.txt_veiculo1_cor.setText("")
        self.txt_veiculo2_placa.setText("")
        self.txt_veiculo2_marca.setText("")
        self.txt_veiculo2_modelo.setText("")
        self.txt_veiculo2_cor.setText("")
        self.txt_observacoes.setPlainText("")
    except AttributeError as e:
        print(f"Erro: {e}")
        QMessageBox.critical(self, 'ERRO', f"Erro ao cadastrar morador: {e}")
        

def pesquisar_morador(self):
    apartamento_bloco = self.txt_pesquisa_apartamento_bloco.text()

    db = DataBase() 

    try:
        resultados = db.pesquisar_moradores(apartamento_bloco)

        self.tableWidget.setRowCount(0) 

        for row_number, row_data in enumerate(resultados):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                item = QTableWidgetItem(str(data))

                item.setFlags(item.flags() ^ Qt.ItemIsEditable) 
                self.tableWidget.setItem(row_number, column_number, item)

    except Exception as e:  
        QMessageBox.critical(self, "Erro", f"Erro ao pesquisar: {e}")
        print(f"Erro na pesquisa: {e}")
        return     