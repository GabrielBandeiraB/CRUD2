import psycopg2

class EmpregadoCRUD:
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

    def inserir_empregado(self, id_propriedade, nome, data_nascimento):
        query = "INSERT INTO Empregado (id_propriedade, nome, data_nascimento) VALUES (%s, %s, %s)"
        values = (id_propriedade, nome, data_nascimento)
        self.cursor.execute(query, values)
        self.conn.commit()
        print("Dados inseridos na tabela Empregado com sucesso!")

    def ler_empregado(self):
        query = "SELECT * FROM Empregado"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)

    def atualizar_empregado(self, id_empregado, id_propriedade, nome, data_nascimento):
        query = "UPDATE Empregado SET id_propriedade = %s, nome = %s, data_nascimento = %s WHERE id_empregado = %s"
        values = (id_propriedade, nome, data_nascimento, id_empregado)
        self.cursor.execute(query, values)
        self.conn.commit()
        print("Dados atualizados na tabela Empregado com sucesso!")

    def excluir_empregado(self, id_empregado):
        query = "DELETE FROM Empregado WHERE id_empregado = %s"
        values = (id_empregado,)
        self.cursor.execute(query, values)
        self.conn.commit()
        print("Dados excluídos da tabela Empregado com sucesso!")