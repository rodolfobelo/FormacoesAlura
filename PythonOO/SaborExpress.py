import os

def exibir_nome_programa():
    print('''
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
''')

def exibir_opcoes_app():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')
    
def finalizar_app():
    print('Finalizando app!\n')

def limpar_terminal():
    os.system('cls') #Windows
    # os.system('clear') #mac

def escolher_opcao_app():
    opcao_escolhida = int(input('Escolha uma opção:'))
    if opcao_escolhida == 1:
        print(f'A opção escolhida foi: {opcao_escolhida}. Cadastrar restaurante!\n')
    elif opcao_escolhida == 2:
        print(f'A opção escolhida foi: {opcao_escolhida}. Listar restaurante!\n')
    elif opcao_escolhida == 3:
        print(f'A opção escolhida foi: {opcao_escolhida}. Ativar restaurante!\n')
    else:
        limpar_terminal()
        finalizar_app()

def main():
    limpar_terminal()
    exibir_nome_programa()
    exibir_opcoes_app()
    escolher_opcao_app()

if __name__ == '__main__':
    main()