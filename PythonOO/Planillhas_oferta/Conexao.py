import pyodbc
import pandas as pd

class Conexao_Banco:

    def conectar(self):
        try:
            conexao = pyodbc.connect(
                "Driver={ODBC Driver 17 for SQL Server};"
                "Server=localhost;"
                "Database=EXEMPLO_1212602;"
                "UID=rm;"
                "PWD=rm;"
            )

            print("Conectado com sucesso!")
            return conexao

        except Exception as erro:
            print(f"Erro ao conectar: {erro}")