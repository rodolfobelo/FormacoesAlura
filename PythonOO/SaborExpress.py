import os

restaurantes = ['Pizza', 'Sushi']

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

def opcao_invalida():
    input('Opção inválida!\nDigite uma tecla para voltar ao menu principal.\n')
    main()

def cadastrar_novo_restaurante(opcao_escolhida):
    limpar_terminal()
    print(f'A opção escolhida foi {opcao_escolhida}. Cadastrar restaurante!\n')
    nome_restaurante = input('Digite o nome do restaurante que você deseja cadastrar:\n')
    restaurantes.append(nome_restaurante)
    print(f'Seu restaurante {nome_restaurante}, foi cadastrado com sucesso.\n')
    input('Digite um tecla para voltar ao menu principal.\n')
    main()

def listar_restaurante(opcao_escolhida):
    limpar_terminal()
    print(f'A opção escolhida foi {opcao_escolhida}. Listar restaurante!\nSegue lista de restaurante(s) cadastrado(s).')
    for i, restaurante in enumerate(restaurantes):
        print(f'{i}.{restaurante}')
    input('Digite um tecla para voltar ao menu principal.\n')
    main()


def escolher_opcao_app():
    try:
        opcao_escolhida = int(input('Escolha uma opção:'))
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante(opcao_escolhida)
        elif opcao_escolhida == 2:
            listar_restaurante(opcao_escolhida)
        elif opcao_escolhida == 3:
            print(f'A opção escolhida foi: {opcao_escolhida}. Ativar restaurante!\n')
        elif opcao_escolhida == 4:
            limpar_terminal()
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    limpar_terminal()
    exibir_nome_programa()
    exibir_opcoes_app()
    escolher_opcao_app()

if __name__ == '__main__':
    main()