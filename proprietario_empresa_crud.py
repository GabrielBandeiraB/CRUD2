import psycopg2

class ProprietarioEmpresaCRUD:
    def __init__(self):
        self.conn = psycopg2.connect(
            host="localhost",
            database="trabalho",
            user="postgres",
            password="0134"
        )
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.cursor.close()
        self.conn.close()

    def inserir_proprietario_empresa(self, nome_empresa, razao_social, cnpj, inscricao_estadual, telefone1, telefone2, telefone3):
        query = "INSERT INTO ProprietarioEmpresa (nome_empresa, razao_social, cnpj, inscricao_estadual, telefone1, telefone2, telefone3) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (nome_empresa, razao_social, cnpj, inscricao_estadual, telefone1, telefone2, telefone3)
        self.cursor.execute(query, values)
        self.conn.commit()
        print("Dados inseridos na tabela ProprietarioEmpresa com sucesso!")

    def ler_proprietario_empresa(self):
        query = "SELECT * FROM ProprietarioEmpresa"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)

    def atualizar_proprietario_empresa(self, id_proprietario, nome_empresa, razao_social, cnpj, inscricao_estadual, telefone1, telefone2, telefone3):
        query = "UPDATE ProprietarioEmpresa SET nome_empresa = %s, razao_social = %s, cnpj = %s, inscricao_estadual = %s, telefone1 = %s, telefone2 = %s, telefone3 = %s WHERE id_proprietario = %s"
        values = (nome_empresa, razao_social, cnpj, inscricao_estadual, telefone1, telefone2, telefone3, id_proprietario)
        self.cursor.execute(query, values)
        self.conn.commit()
        print("Dados atualizados na tabela ProprietarioEmpresa com sucesso!")

    def excluir_proprietario_empresa(self, id_proprietario):
        query = "DELETE FROM ProprietarioEmpresa WHERE id_proprietario = %s"
        values = (id_proprietario,)
        self.cursor.execute(query, values)
        self.conn.commit()
        print("Dados excluídos da tabela ProprietarioEmpresa com sucesso!")