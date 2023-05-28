import psycopg2

class ProducaoCRUD:
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

    def inserir_producao(self, id_propriedade, produto, periodo_colheita_previsto, quantidade_colher_prevista, quantidade_colhida_efetiva, periodo_colheita_efetivo):
        query = "INSERT INTO Producao (id_propriedade, produto, periodo_colheita_previsto, quantidade_colher_prevista, quantidade_colhida_efetiva, periodo_colheita_efetivo) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (id_propriedade, produto, periodo_colheita_previsto, quantidade_colher_prevista, quantidade_colhida_efetiva, periodo_colheita_efetivo)
        self.cursor.execute(query, values)
        self.conn.commit()
        print("Dados inseridos na tabela Producao com sucesso!")

    def ler_producao(self):
        query = "SELECT * FROM Producao"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        for row in rows:
            print(row)

    def atualizar_producao(self, id_producao, id_propriedade, produto, periodo_colheita_previsto, quantidade_colher_prevista, quantidade_colhida_efetiva, periodo_colheita_efetivo):
        query = "UPDATE Producao SET id_propriedade = %s, produto = %s, periodo_colheita_previsto = %s, quantidade_colher_prevista = %s, quantidade_colhida_efetiva = %s, periodo_colheita_efetivo = %s WHERE id_producao = %s"
        values = (id_propriedade, produto, periodo_colheita_previsto, quantidade_colher_prevista, quantidade_colhida_efetiva, periodo_colheita_efetivo, id_producao)
        self.cursor.execute(query, values)
        self.conn.commit()
        print("Dados atualizados na tabela Producao com sucesso!")

    def excluir_producao(self, id_producao):
        query = "DELETE FROM Producao WHERE id_producao = %s"
        values = (id_producao,)
        self.cursor.execute(query, values)
        self.conn.commit()
        print("Dados excluídos da tabela Producao com sucesso!")