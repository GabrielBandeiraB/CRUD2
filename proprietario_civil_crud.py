import psycopg2

class ProprietarioCivilCRUD:
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

    def inserir_proprietario_civil(self, nome, carteira_identidade, cpf, data_nascimento, telefone1, telefone2, telefone3):
        query = "INSERT INTO ProprietarioCivil (nome, carteira_identidade, cpf, data_nascimento, telefone1, telefone2, telefone3) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (nome, carteira_identidade, cpf, data_nascimento, telefone1, telefone2, telefone3)
        self.cursor.execute(query, values)
        self.conn.commit()
        print("Dados inseridos na tabela ProprietarioCivil com sucesso!")

    def ler_proprietario_civil(self):
        query = "SELECT * FROM ProprietarioCivil"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)

    def atualizar_proprietario_civil(self, id_proprietario, nome, carteira_identidade, cpf, data_nascimento, telefone1, telefone2, telefone3):
        query = "UPDATE ProprietarioCivil SET nome = %s, carteira_identidade = %s, cpf = %s, data_nascimento = %s, telefone1 = %s, telefone2 = %s, telefone3 = %s WHERE id_proprietario = %s"
        values = (nome, carteira_identidade, cpf, data_nascimento, telefone1, telefone2, telefone3, id_proprietario)
        self.cursor.execute(query, values)
        self.conn.commit()
        print("Dados atualizados na tabela ProprietarioCivil com sucesso!")

    def excluir_proprietario_civil(self, id_proprietario):
        query = "DELETE FROM ProprietarioCivil WHERE id_proprietario = %s"
        values = (id_proprietario,)
        self.cursor.execute(query, values)
        self.conn.commit()
        print("Dados excluídos da tabela ProprietarioCivil com sucesso!")