import sqlite3

class DataBase():
    def __init__(self, name='system.db') -> None:
        self.name = name

    def connect(self):    
        self.connection = sqlite3.connect(self.name)

    def close_connection(self):
        try:
            self.connection.close()
        except Exception as e:
            print(e)


    def criar_tabela_usuarios(self):
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    usuario TEXT NOT NULL UNIQUE,
                    senha TEXT NOT NULL,
                    tipo_user TEXT NOT NULL
                );
            """)
            self.connection.commit()
            print("Tabela 'users' criada com sucesso")
        except Exception as e:
            print(e)
        finally:
            self.close_connection()


    def criar_tabela_moradores(self):
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS moradores (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    apartamento_bloco TEXT NOT NULL,
                    nome_completo TEXT,
                    data_nascimento TEXT,
                    nome_completo2 TEXT,
                    data_nascimento2 TEXT,
                    nome_completo3 TEXT,
                    data_nascimento3 TEXT,
                    nome_completo4 TEXT,
                    data_nascimento4 TEXT,
                    nome_completo5 TEXT,
                    data_nascimento5 TEXT,
                    nome_completo6 TEXT,
                    data_nascimento6 TEXT,
                    telefone1 TEXT,
                    telefone2 TEXT,
                    email1 TEXT,
                    email2 TEXT,
                    veiculo1_placa TEXT,
                    veiculo1_marca TEXT,
                    veiculo1_modelo TEXT,
                    veiculo1_cor TEXT,
                    veiculo2_placa TEXT,
                    veiculo2_marca TEXT,
                    veiculo2_modelo TEXT,
                    veiculo2_cor TEXT,
                    observacoes TEXT
                );
            """)
            self.connection.commit()
            print("Tabela 'moradores' criada com sucesso")
        except Exception as e:
            print(e)
        finally:
            self.close_connection()


    def criar_tabela_agendamentos(self):
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS agendamentos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    apartamento_bloco TEXT NOT NULL,
                    nome_morador TEXT NOT NULL,
                    local TEXT NOT NULL,
                    periodo TEXT NOT NULL,
                    data_agendamento TEXT NOT NULL,       
                    funcionario TEXT NOT NULL,
                    observacoes TEXT
                );
            """)
            self.connection.commit()
            print("Tabela 'agendamentos' criada com sucesso")
        except Exception as e:
            print(e)
        finally:
            self.close_connection()


    def criar_tabela_visitantes(self):
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS visitantes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    data_visita TEXT NOT NULL,
                    nome_visitante TEXT NOT NULL,
                    rg_cpf_visitante TEXT NOT NULL,
                    visitando TEXT NOT NULL,
                    apartamento_bloco_visitantes TEXT NOT NULL,
                    hora_entrada_visita TEXT NOT NULL,
                    hora_saida_visita TEXT,
                    quem_autorizou_visita TEXT NOT NULL,
                    vaga_utilizada TEXT NOT NULL,
                    placa_visitante TEXT,
                    marca_visitante TEXT,
                    modelo_visitante TEXT,
                    cor_visitante TEXT
                );
            """)
            self.connection.commit()
            print("Tabela 'visitantes' criada com sucesso")
        except Exception as e:
            print(e)
        finally:
            self.close_connection()


    def criar_tabela_prestadores(self):
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS prestadores (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome_empresa TEXT NOT NULL,
                    tipo_servico TEXT NOT NULL,
                    data_servico TEXT NOT NULL,
                    hora_entrada_prestador TEXT NOT NULL,
                    hora_saida_prestador TEXT,
                    nome_prestador TEXT NOT NULL,
                    rg_cpf_prestador TEXT NOT NULL,
                    telefone TEXT,
                    contratante TEXT NOT NULL,
                    apartamento_bloco_prestador TEXT NOT NULL,
                    quem_autorizou_prestador TEXT NOT NULL
                );
            """)
            self.connection.commit()
            print("Tabela 'prestadores' criada com sucesso")
        except Exception as e:
            print(e)
        finally:
            self.close_connection()


    def criar_tabela_encomendas(self):
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS encomendas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    numero_protocolo TEXT NOT NULL,
                    data_hora_recebimento TEXT NOT NULL,
                    nome_destinatario TEXT NOT NULL,
                    apartamento_bloco_encomendas TEXT NOT NULL,
                    numero_rastreamento TEXT,
                    tipo_encomenda TEXT,
                    descricao_encomenda TEXT,
                    empresa_entrega TEXT,
                    observacoes_encomendas TEXT,
                    nome_entregador TEXT,
                    rg_cpf_entregador TEXT,
                    nome_porteiro TEXT,
                    nome_retirou TEXT
                );
            """)
            self.connection.commit()
            print("Tabela 'encomendas' criada com sucesso")
        except Exception as e:
            print(e)
        finally:
            self.close_connection()


    def criar_tabela_ocorrencias(self):
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS ocorrencias (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    numero_protocolo_ocorrencias TEXT NOT NULL,
                    data_ocorrencia TEXT NOT NULL,
                    nome_funcionario TEXT NOT NULL,
                    hora_registro TEXT NOT NULL,
                    data_registro TEXT NOT NULL,
                    descricao TEXT NOT NULL
                );
            """)
            self.connection.commit()
            print("Tabela 'ocorrencias' criada com sucesso")
        except Exception as e:
            print(e)
        finally:
            self.close_connection()


    def criar_tabela_funcionarios(self):
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS funcionarios (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome_funcionarios TEXT NOT NULL,
                    endereco_funcionario TEXT NOT NULL,
                    bairro_funcionario TEXT NOT NULL,
                    cep_funcionario TEXT NOT NULL,
                    telefone_funcionario TEXT NOT NULL,
                    celular_funcionario TEXT NOT NULL,
                    email_funcionario TEXT NOT NULL,
                    observacao_funcionario TEXT
                );
            """)
            self.connection.commit()
            print("Tabela 'funcionarios' criada com sucesso")
        except Exception as e:
            print(e)
        finally:
            self.close_connection()


    def criar_tabela_domesticos(self):
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS domesticos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    apartamento TEXT NOT NULL,
                    bloco TEXT NOT NULL,
                    funcao TEXT NOT NULL,
                    horario TEXT NOT NULL,
                    telefone TEXT NOT NULL
                )
            ''')
            self.connection.commit()
            print("Tabela 'domésticos' criada com sucesso")
        except Exception as e:
            print(e)
        finally:
            self.close_connection()


    def criar_tabela_mudancas(self):
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS mudancas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    data TEXT NOT NULL,
                    horario TEXT NOT NULL,
                    nome_responsavel TEXT NOT NULL,
                    apartamento TEXT NOT NULL,
                    bloco TEXT NOT NULL,
                    nome_enp TEXT NOT NULL,
                    uso_elevador BOOLEAN NOT NULL,
                    uso_escada BOOLEAN NOT NULL,
                    icamento BOOLEAN NOT NULL
                )
            ''')
            self.connection.commit()
            print("Tabela 'mudança' criada com sucesso")
        except Exception as e:
            print(e)
        finally:
            self.close_connection()                                                   


    def inserirUsuario(self, nome, user, password, acesso):
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute("""
                INSERT INTO users (nome, usuario, senha, tipo_user)
                VALUES (?, ?, ?, ?)
            """, (nome, user, password, acesso))
            self.connection.commit()
            print("valores inseridos sucesso")
        except Exception as e:
            print(e)
        finally:
            self.close_connection()  


    def checkUser(self, usuario, senha):
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute("""
                SELECT * FROM users;
            """)
            for linha in cursor.fetchall():
                user = linha[2]
                password = linha[3]
                tipo_user = linha[4].strip()
                print(f"Verificando usuário: {user}, tipo: {tipo_user}")
                if user.upper() == usuario.upper() and password == senha:
                    if tipo_user == "Administrador":
                        return "Administrador"
                    elif tipo_user == "Sindico":
                        return 'Sindico'
                    elif tipo_user == "Porteiro":
                        return 'Porteiro'
            return 'sem acesso'
        except Exception as e:
            print(e)
        finally:
            self.close_connection()

    def inserir_morador(self, apartamento_bloco, moradores, telefone1, telefone2, email1, email2, veiculo1, veiculo2, observacoes):
        try:
            self.connect()
            cursor = self.connection.cursor()
            for nome_completo, data_nascimento in moradores:
                cursor.execute("""
                    INSERT INTO moradores (
                        apartamento_bloco, nome_completo, data_nascimento, telefone1, telefone2, email1, email2, 
                        veiculo1_placa, veiculo1_marca, veiculo1_modelo, veiculo1_cor, 
                        veiculo2_placa, veiculo2_marca, veiculo2_modelo, veiculo2_cor, observacoes
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    apartamento_bloco, nome_completo, data_nascimento, telefone1, telefone2, email1, email2, 
                    veiculo1['placa'], veiculo1['marca'], veiculo1['modelo'], veiculo1['cor'], 
                    veiculo2['placa'], veiculo2['marca'], veiculo2['modelo'], veiculo2['cor'], observacoes
                ))
            self.connection.commit()
            print("Moradores inseridos com sucesso")
        except Exception as e:
            print(e)
        finally:
            self.close_connection()


    def inserir_agendamento(self, ag_apartamento_bloco, ag_nome_morador, cmb_local, cmb_periodo, data_agendamento, ag_funcionario, ag_observacoes):
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute("""
                INSERT INTO agendamentos (apartamento_bloco, nome_morador, local, periodo, data_agendamento, funcionario, observacoes)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (ag_apartamento_bloco, ag_nome_morador, cmb_local, cmb_periodo, data_agendamento, ag_funcionario, ag_observacoes))
            self.connection.commit()
            print("Agendamento inserido com sucesso")
        except Exception as e:
            print(e)
        finally:
            self.close_connection()


    def inserir_visitante(self, nome_visitante, rg_cpf_visitante, visitando, apartamento_bloco_visitantes, data_visita, hora_entrada_visita, hora_saida_visita, quem_autorizou_visita, vaga_utilizada, placa_visitante, marca_visitante, modelo_visitante, cor_visitante):
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute("""
                INSERT INTO visitantes (data_visita, nome_visitante, rg_cpf_visitante, visitando, apartamento_bloco_visitantes, hora_entrada_visita, hora_saida_visita, quem_autorizou_visita, vaga_utilizada, placa_visitante, marca_visitante, modelo_visitante, cor_visitante)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (data_visita, nome_visitante, rg_cpf_visitante, visitando, apartamento_bloco_visitantes, hora_entrada_visita, hora_saida_visita, quem_autorizou_visita, vaga_utilizada, placa_visitante, marca_visitante, modelo_visitante, cor_visitante))
            self.connection.commit()
            print("Visitante inserido com sucesso")
        except Exception as e:
            print(e)
        finally:
            self.close_connection()

            
    def inserir_prestadores(self, nome_empresa, tipo_servico, data_servico, hora_entrada_prestador, hora_saida_prestador, nome_prestador, rg_cpf_prestador, telefone, contratante, apartamento_bloco_prestador, quem_autorizou_prestador):
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute("""
                INSERT INTO prestadores (nome_empresa, tipo_servico, data_servico, hora_entrada_prestador, hora_saida_prestador, nome_prestador, rg_cpf_prestador, telefone, contratante, apartamento_bloco_prestador, quem_autorizou_prestador)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (nome_empresa, tipo_servico, data_servico, hora_entrada_prestador, hora_saida_prestador, nome_prestador, rg_cpf_prestador, telefone, contratante, apartamento_bloco_prestador, quem_autorizou_prestador))
            self.connection.commit()
            print("Prestador inserido com sucesso")
        except Exception as e:
            print(e)
        finally:
            self.close_connection()


    def inserir_encomendas(self, numero_protocolo, data_hora_recebimento, nome_destinatario, apartamento_bloco_encomendas, numero_rastreamento, tipo_encomenda, descricao_encomenda, empresa_entrega, observacoes_encomendas, nome_entregador, rg_cpf_entregador, nome_porteiro, nome_retirou):
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute("""
                INSERT INTO encomendas (numero_protocolo, data_hora_recebimento, nome_destinatario, apartamento_bloco_encomendas, numero_rastreamento, tipo_encomenda, descricao_encomenda, empresa_entrega, observacoes_encomendas, nome_entregador, rg_cpf_entregador, nome_porteiro, nome_retirou)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (numero_protocolo, data_hora_recebimento, nome_destinatario, apartamento_bloco_encomendas, numero_rastreamento, tipo_encomenda, descricao_encomenda, empresa_entrega, observacoes_encomendas, nome_entregador, rg_cpf_entregador, nome_porteiro, nome_retirou))
            self.connection.commit()
            print("Encomenda inserida com sucesso")
            print(f"Encomenda inserida com sucesso! Protocolo: {numero_protocolo}")
        except Exception as e:
            print(e)
        finally:
            self.close_connection()


    def inserir_ocorrencias(self, numero_protocolo_ocorrencias, data_ocorrencia, nome_funcionario, hora_registro, data_registro, descricao):
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute("""
                INSERT INTO ocorrencias (numero_protocolo_ocorrencias, data_ocorrencia, nome_funcionario, hora_registro, data_registro, descricao)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (numero_protocolo_ocorrencias, data_ocorrencia, nome_funcionario, hora_registro, data_registro, descricao))
            self.connection.commit()
            print(f"Ocorrência inserida com sucesso! Protocolo: {numero_protocolo_ocorrencias}")
        except Exception as e:
            print(e)
        finally:
            self.close_connection()


    def inserir_funcionarios(self, nome_funcionarios, endereco_funcionario, bairro_funcionario, cep_funcionario, telefone_funcionario, celular_funcionario, email_funcionario, observacao_funcionario):
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute("""
                INSERT INTO funcionarios (nome_funcionarios, endereco_funcionario, bairro_funcionario, cep_funcionario, telefone_funcionario, celular_funcionario, email_funcionario, observacao_funcionario)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (nome_funcionarios, endereco_funcionario, bairro_funcionario, cep_funcionario, telefone_funcionario, celular_funcionario, email_funcionario, observacao_funcionario))
            self.connection.commit()
            print("Funcionário inserido com sucesso")
        except Exception as e:
            print(e)
        finally:
            self.close_connection()


    def inserir_domesticos(self, nome, apartamento, bloco, funcao, horario, telefone):
        try:    
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute('''
            INSERT INTO domesticos (nome, apartamento, bloco, funcao, horario, telefone)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (nome, apartamento, bloco, funcao, horario, telefone))
            self.connection.commit()
            print("doméstico inserido com sucesso")
        except Exception as e:
            print(e)
        finally:
            self.close_connection()


    def inserir_mudancas(self, data, horario, nome_responsavel, apartamento, bloco, nome_enp, uso_elevador, uso_escada, icamento):
        try:    
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute('''
                INSERT INTO mudancas (data, horario, nome_responsavel, apartamento, bloco, nome_enp, uso_elevador, uso_escada, icamento)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (data, horario, nome_responsavel, apartamento, bloco, nome_enp, uso_elevador, uso_escada, icamento))
            self.connection.commit()
            print("mudança inserido com sucesso")
        except Exception as e:
            print(e)
        finally:
            self.close_connection()                                                        


    def pesquisar_moradores(self, apartamento_bloco=None):
        try:
            self.connect()
            cursor = self.connection.cursor()
            query = "SELECT * FROM moradores WHERE 1=1"
            params = []
            if apartamento_bloco:
                query += " AND apartamento_bloco = ?"
                params.append(apartamento_bloco)
            cursor.execute(query, params)
            resultados = cursor.fetchall()
            return resultados
        except Exception as e:
            print(e)
        finally:
            self.close_connection()


    def pesquisar_agendamentos(self, ag_apartamento_bloco, ag_nome_morador, local, periodo, data_agendamento, ag_funcionario):
        query = """
        SELECT * FROM agendamentos
        WHERE (ag_apartamento_bloco = ? OR ? = '')
        AND (ag_nome_morador = ? OR ? = '')
        AND (local = ? OR ? = '')
        AND (periodo = ? OR ? = '')
        AND (data_agendamento = ? OR ? = '')
        AND (ag_funcionario = ? OR ? = '')
        """
        params = (ag_apartamento_bloco, ag_apartamento_bloco, ag_nome_morador, ag_nome_morador, local, local, periodo, periodo, data_agendamento, data_agendamento, ag_funcionario, ag_funcionario)
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        return cursor.fetchall()

    def pesquisar_visitantes(self, data=None, nome_visitante=None, rg_cpf=None, apartamento_bloco=None):
        try:
            self.connect()
            cursor = self.connection.cursor()
            query = "SELECT * FROM visitantes WHERE 1=1"
            params = []
            if data:
                query += " AND data = ?"
                params.append(data)
            if nome_visitante:
                query += " AND nome_visitante LIKE ?"
                params.append(f"%{nome_visitante}%")
            if rg_cpf:
                query += " AND rg_cpf = ?"
                params.append(rg_cpf)
            if apartamento_bloco:
                query += " AND apartamento_bloco = ?"
                params.append(apartamento_bloco)
            cursor.execute(query, params)
            resultados = cursor.fetchall()
            return resultados
        except Exception as e:
            print(e)
        finally:
            self.close_connection()

    def pesquisar_prestadores(self, data_servico=None, nome_prestador=None, rg_cpf_prestador=None, apartamento_bloco_prestador=None):
        try:
            self.connect()
            cursor = self.connection.cursor()
            query = "SELECT * FROM prestadores WHERE 1=1"
            params = []
            if data_servico:
                query += " AND data_servico = ?"
                params.append(data_servico)
            if nome_prestador:
                query += " AND nome_prestador LIKE ?"
                params.append(f"%{nome_prestador}%")
            if rg_cpf_prestador:
                query += " AND rg_cpf_prestador = ?"
                params.append(rg_cpf_prestador)
            if apartamento_bloco_prestador:
                query += " AND apartamento_bloco_prestador = ?"
                params.append(apartamento_bloco_prestador)
            cursor.execute(query, params)
            resultados = cursor.fetchall()
            return resultados
        except Exception as e:
            print(e)
        finally:
            self.close_connection()


    def pesquisar_encomendas(self, numero_protocolo=None, data_hora_recebimento=None, nome_destinatario=None, apartamento_bloco_encomendas=None, numero_rastreamento=None, tipo_encomenda=None, descricao_encomenda=None, empresa_entrega=None, observacoes_encomendas=None, nome_entregador=None, rg_cpf_entregador=None, nome_porteiro=None, nome_retirou=None):
        try:
            self.connect()
            cursor = self.connection.cursor()
            query = "SELECT * FROM encomendas WHERE 1=1"
            params = []
            if numero_protocolo:
                query += " AND numero_protocolo = ?"
                params.append(numero_protocolo)
            if data_hora_recebimento:
                query += " AND data_hora_recebimento = ?"
                params.append(data_hora_recebimento)
            if nome_destinatario:
                query += " AND nome_destinatario LIKE ?"
                params.append(f"%{nome_destinatario}%")
            if apartamento_bloco_encomendas:
                query += " AND apartamento_bloco_encomendas = ?"
                params.append(apartamento_bloco_encomendas)
            if numero_rastreamento:
                query += " AND numero_rastreamento = ?"
                params.append(numero_rastreamento)
            if tipo_encomenda:
                query += " AND tipo_encomenda = ?"
                params.append(tipo_encomenda)
            if descricao_encomenda:
                query += " AND descricao_encomenda LIKE ?"
                params.append(f"%{descricao_encomenda}%")
            if empresa_entrega:
                query += " AND empresa_entrega LIKE ?"
                params.append(f"%{empresa_entrega}%")
            if observacoes_encomendas:
                query += " AND observacoes_encomendas LIKE ?"
                params.append(f"%{observacoes_encomendas}%")
            if nome_entregador:
                query += " AND nome_entregador LIKE ?"
                params.append(f"%{nome_entregador}%")
            if rg_cpf_entregador:
                query += " AND rg_cpf_entregador = ?"
                params.append(rg_cpf_entregador)
            if nome_porteiro:
                query += " AND nome_porteiro LIKE ?"
                params.append(f"%{nome_porteiro}%")
            if nome_retirou:
                query += " AND nome_retirou LIKE ?"
                params.append(f"%{nome_retirou}%")
            cursor.execute(query, params)
            resultados = cursor.fetchall()
            return resultados
        except Exception as e:
            print(e)
        finally:
            self.close_connection()


    def pesquisar_ocorrencias(self, data_ocorrencia=None, nome_funcionario=None, hora_registro=None, data_registro=None, descricao=None):
        try:
            self.connect()
            cursor = self.connection.cursor()
            query = "SELECT * FROM ocorrencias WHERE 1=1"
            params = []
            if data_ocorrencia:
                query += " AND data_ocorrencia = ?"
                params.append(data_ocorrencia)
            if nome_funcionario:
                query += " AND nome_funcionario LIKE ?"
                params.append(f"%{nome_funcionario}%")
            if hora_registro:
                query += " AND hora_registro = ?"
                params.append(hora_registro)
            if data_registro:
                query += " AND data_registro = ?"
                params.append(data_registro)
            if descricao:
                query += " AND descricao LIKE ?"
                params.append(f"%{descricao}%")
            cursor.execute(query, params)
            resultados = cursor.fetchall()
            return resultados
        except Exception as e:
            print(e)
        finally:
            self.close_connection()


    def pesquisar_funcionarios(self, nome_funcionarios=None, endereco_funcionario=None, bairro_funcionario=None, cep_funcionario=None, telefone_funcionario=None, celular_funcionario=None, email_funcionario=None, observacao_funcionario=None):
        try:
            self.connect()
            cursor = self.connection.cursor()
            query = "SELECT * FROM funcionarios WHERE 1=1"
            params = []
            if nome_funcionarios:
                query += " AND nome_funcionarios LIKE ?"
                params.append(f"%{nome_funcionarios}%")
            if endereco_funcionario:
                query += " AND endereco_funcionario LIKE ?"
                params.append(f"%{endereco_funcionario}%")
            if bairro_funcionario:
                query += " AND bairro_funcionario LIKE ?"
                params.append(f"%{bairro_funcionario}%")
            if cep_funcionario:
                query += " AND cep_funcionario = ?"
                params.append(cep_funcionario)
            if telefone_funcionario:
                query += " AND telefone_funcionario = ?"
                params.append(telefone_funcionario)
            if celular_funcionario:
                query += " AND celular_funcionario = ?"
                params.append(celular_funcionario)
            if email_funcionario:
                query += " AND email_funcionario LIKE ?"
                params.append(f"%{email_funcionario}%")
            if observacao_funcionario:
                query += " AND observacao_funcionario LIKE ?"
                params.append(f"%{observacao_funcionario}%")
            cursor.execute(query, params)
            resultados = cursor.fetchall()
            return resultados
        except Exception as e:
            print(e)
        finally:
            self.close_connection()


    def pesquisar_domesticos(self, nome, apartamento, bloco, funcao, horario, telefone):
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute('''
                SELECT * FROM domesticos
                WHERE nome LIKE ? AND apartamento LIKE ? AND bloco LIKE ? AND funcao LIKE ? AND horario LIKE ? AND telefone LIKE ?
            ''', (f'%{nome}%', f'%{apartamento}%', f'%{bloco}%', f'%{funcao}%', f'%{horario}%', f'%{telefone}%'))
            resultados = cursor.fetchall()
            return resultados
        except Exception as e:
            print(e)
        finally:
            self.close_connection()


    def pesquisar_mudancas(self, data, horario, nome_responsavel, apartamento, bloco, nome_enp, uso_elevador, uso_escada, icamento):
        try:
            self.connect()
            cursor = self.connection.cursor()
            cursor.execute('''
                SELECT * FROM mudancas
                WHERE data LIKE ? AND horario LIKE ? AND nome_responsavel LIKE ? AND apartamento LIKE ? AND bloco LIKE ? AND nome_enp LIKE ? AND uso_elevador = ? AND uso_escada = ? AND icamento = ?
            ''', (f'%{data}%', f'%{horario}%', f'%{nome_responsavel}%', f'%{apartamento}%', f'%{bloco}%', f'%{nome_enp}%', uso_elevador, uso_escada, icamento))                                               
            resultados = cursor.fetchall()
            return resultados
        except Exception as e:
            print(e)
        finally:
            self.close_connection()

if __name__ == '__main__':
    db = DataBase()
    db.criar_tabela_usuarios()
    db.criar_tabela_moradores()
    db.criar_tabela_agendamentos()
    db.criar_tabela_visitantes()
    db.criar_tabela_prestadores()
    db.criar_tabela_encomendas()
    db.criar_tabela_ocorrencias()
    db.criar_tabela_funcionarios()
    db.criar_tabela_domesticos()
    db.criar_tabela_mudancas()
    db.inserirUsuario()
    print("valores inseridos sucesso")