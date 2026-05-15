from pathlib import Path
import pandas as pd
import shutil

class Ler_planilhas:

    def Carregar_planilhas(self):
        pasta_entrada = Path(r"C:\GitHub\FormacoesAlura\PythonOO\Planillhas_oferta\Matriculas_Entrada")
        pasta_processadas = Path(r"C:\GitHub\FormacoesAlura\PythonOO\Planillhas_oferta\Matriculas_Processadas")

        pasta_processadas.mkdir(parents=True, exist_ok=True)

        lista_planilhas = []

        arquivos = list(pasta_entrada.glob("*.xlsx"))

        if not arquivos:
            print("Nenhuma planilha encontrada na pasta de entrada")

        for arquivo in arquivos:
            df = pd.read_excel(arquivo)

        df["NOME_ARQUIVO"] = arquivo.name
        df["PERIODO_LETIVO"] = '20262'

        lista_planilhas.append(df)

        destino = pasta_processadas / arquivo.name
        shutil.move(str(arquivo), str(destino))

        planilha_unica = pd.concat(lista_planilhas, ignore_index=True)

        return planilha_unica