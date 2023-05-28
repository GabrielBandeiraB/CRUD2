import psycopg2

class MunicipioCRUD:
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

    def inserir_municipio(self, nome_municipio):
        query = "INSERT INTO Municipio (nome_municipio) VALUES (%s)"
        values = (nome_municipio,)
        self.cursor.execute(query, values)
        self.conn.commit()
        print("Dados inseridos na tabela Municipio com sucesso!")

    def ler_municipio(self):
        query = "SELECT * FROM Municipio"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)

    def atualizar_municipio(self, id_municipio, nome_municipio):
        query = "UPDATE Municipio SET nome_municipio = %s WHERE id_municipio = %s"
        values = (nome_municipio, id_municipio)
        self.cursor.execute(query, values)
        self.conn.commit()
        print("Dados atualizados na tabela Municipio com sucesso!")

    def excluir_municipio(self, id_municipio):
        query = "DELETE FROM Municipio WHERE id_municipio = %s"
        values = (id_municipio,)
        self.cursor.execute(query, values)
        self.conn.commit()
        print("Dados excluídos da tabela Municipio com sucesso!")