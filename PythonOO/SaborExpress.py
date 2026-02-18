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
    # os.system('clr') #Windows
    os.system('clear') #mac
    print('Finalizando app!\n')

def escolher_opcao_app():
    opcao_escolhida = int(input('Escolha uma opção:'))
    if opcao_escolhida == 1:
        print(f'A opção escolhida foi: {opcao_escolhida}. Cadastrar restaurante')
    elif opcao_escolhida == 2:
        print(f'A opção escolhida foi: {opcao_escolhida}. Listar restaurante')
    elif opcao_escolhida == 3:
        print(f'A opção escolhida foi: {opcao_escolhida}. Ativar restaurante')
    else:
        finalizar_app()

def main():
    exibir_nome_programa()
    exibir_opcoes_app()
    escolher_opcao_app()

if __name__ == '__main__':
    main()