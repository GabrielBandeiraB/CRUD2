import psycopg2

class PropriedadeCRUD:
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

    def inserir_propriedade(self, id_proprietario, nome_propriedade, data_aquisicao, area_hectares, municipio_id, preco_aquisicao, distancia_municipio):
        query = "INSERT INTO Propriedade (id_proprietario, nome_propriedade, data_aquisicao, area_hectares, municipio_id, preco_aquisicao, distancia_municipio) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (id_proprietario, nome_propriedade, data_aquisicao, area_hectares, municipio_id, preco_aquisicao, distancia_municipio)
        self.cursor.execute(query, values)
        self.conn.commit()
        print("Dados inseridos na tabela Propriedade com sucesso!")

    def ler_propriedade(self):
        query = "SELECT * FROM Propriedade"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)

    def atualizar_propriedade(self, id_propriedade, id_proprietario, nome_propriedade, data_aquisicao, area_hectares, municipio_id, preco_aquisicao, distancia_municipio):
        query = "UPDATE Propriedade SET id_proprietario = %s, nome_propriedade = %s, data_aquisicao = %s, area_hectares = %s, municipio_id = %s, preco_aquisicao = %s, distancia_municipio = %s WHERE id_propriedade = %s"
        values = (id_proprietario, nome_propriedade, data_aquisicao, area_hectares, municipio_id, preco_aquisicao, distancia_municipio, id_propriedade)
        self.cursor.execute(query, values)
        self.conn.commit()
        print("Dados atualizados na tabela Propriedade com sucesso!")

    def excluir_propriedade(self, id_propriedade):
        query = "DELETE FROM Propriedade WHERE id_propriedade = %s"
        values = (id_propriedade,)
        self.cursor.execute(query, values)
        self.conn.commit()
        print("Dados excluídos da tabela Propriedade com sucesso!")