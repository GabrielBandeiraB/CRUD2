import psycopg2

class EsposaCRUD:
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

    def inserir_esposa(self, id_proprietario, nome, cpf, data_nascimento, data_casamento, carteira_identidade):
        query = "INSERT INTO Esposa (id_proprietario, nome, cpf, data_nascimento, data_casamento, carteira_identidade) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (id_proprietario, nome, cpf, data_nascimento, data_casamento, carteira_identidade)
        self.cursor.execute(query, values)
        self.conn.commit()
        print("Dados inseridos na tabela Esposa com sucesso!")

    def ler_esposa(self):
        query = "SELECT * FROM Esposa"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)

    def atualizar_esposa(self, id_esposa, id_proprietario, nome, cpf, data_nascimento, data_casamento, carteira_identidade):
        query = "UPDATE Esposa SET id_proprietario = %s, nome = %s, cpf = %s, data_nascimento = %s, data_casamento = %s, carteira_identidade = %s WHERE id_esposa = %s"
        values = (id_proprietario, nome, cpf, data_nascimento, data_casamento, carteira_identidade, id_esposa)
        self.cursor.execute(query, values)
        self.conn.commit()
        print("Dados atualizados na tabela Esposa com sucesso!")

    def excluir_esposa(self, id_esposa):
        query = "DELETE FROM Esposa WHERE id_esposa = %s"
        values = (id_esposa,)
        self.cursor.execute(query, values)
        self.conn.commit()
        print("Dados excluídos da tabela Esposa com sucesso!")