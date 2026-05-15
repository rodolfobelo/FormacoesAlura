from Ler_planilhas import Ler_planilhas
from Controller_Planilha import Controller_Planilha

def main():
    df = Ler_planilhas().Carregar_planilhas()

    if df is not None:
        banco = Controller_Planilha()
        banco.inserir_planilha(df)

if __name__ == '__main__':
    main()