from Conexao import Conexao_Banco
import pandas as pd

class Controller_Planilha:
    def inserir_planilha(self, df):
        banco = Conexao_Banco()
        conexao = banco.conectar()

        if conexao is None:
            return "Erro na conexao!"

        try:
            cursor = conexao.cursor()

            sql = """
                INSERT INTO dbo.Z_MATRICULAS_OFERTA
                (
                    RA,
                    SEGUNDA,
                    TERCA,
                    QUARTA,
                    QUINTA,
                    SEXTA,
                    PROJETO,
                    ESTAGIO,
                    EAD,
                    NOME_PLANILHA,
                    PERIODO_LETIVO
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """

            registros = []

            for _, linha in df.iterrows():
                registros.append((
                    str(linha["RA"]) if pd.notna(linha["RA"]) else None,
                    int(linha["SEGUNDA-FEIRA - CÓDIGO"]) if pd.notna(linha["SEGUNDA-FEIRA - CÓDIGO"]) else None,
                    int(linha["TERÇA-FEIRA - CÓDIGO"]) if pd.notna(linha["TERÇA-FEIRA - CÓDIGO"]) else None,
                    int(linha["QUARTA-FEIRA - CÓDIGO"]) if pd.notna(linha["QUARTA-FEIRA - CÓDIGO"]) else None,
                    int(linha["QUINTA-FEIRA - CÓDIGO"]) if pd.notna(linha["QUINTA-FEIRA - CÓDIGO"]) else None,
                    int(linha["SEXTA-FEIRA - CÓDIGO"]) if pd.notna(linha["SEXTA-FEIRA - CÓDIGO"]) else None,
                    int(linha["PROJETO - CÓDIGO"]) if pd.notna(linha["PROJETO - CÓDIGO"]) else None,
                    int(linha["CÓDIGO ESTÁGIO"]) if pd.notna(linha["CÓDIGO ESTÁGIO"]) else None,
                    int(linha["EAD - CÓDIGO"]) if pd.notna(linha["EAD - CÓDIGO"]) else None,
                    str(linha["NOME_ARQUIVO"]) if pd.notna(linha["NOME_ARQUIVO"]) else None,
                    str(linha["PERIODO_LETIVO"]) if pd.notna(linha["PERIODO_LETIVO"]) else None,
                ))

            cursor.executemany(sql, registros)
            conexao.commit()

            print(f"{len(registros)} registros inseridos com sucesso.")

        except Exception as erro:
            conexao.rollback()
            print(f"Erro ao inserir dados: {erro}")

        finally:
            conexao.close()