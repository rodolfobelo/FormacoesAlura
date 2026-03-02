import os

restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False}, 
                {'nome':'Pizza Suprema', 'categoria':'Pizza', 'ativo':True},
                {'nome':'Cantina', 'categoria':'Italiano', 'ativo':True}
                ]

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

def voltar_main():
    input('Digite um tecla para voltar ao menu principal.\n')
    main()

def opcao_invalida():
    input('Opção inválida!\nDigite uma tecla para voltar ao menu principal.\n')
    main()

def cadastrar_novo_restaurante(opcao_escolhida):
    limpar_terminal()
    print(f'A opção escolhida foi {opcao_escolhida}. Cadastrar restaurante!\n')
    nome_restaurante = input('Digite o nome do restaurante que você deseja cadastrar:\n')
    categoria_restaurante = input(f'Digite a categoria do restaurante {nome_restaurante}:\n')
    ativo_restaurante = False
    dados_restaurante = {'nome':nome_restaurante, 'categoria':categoria_restaurante, 'ativo':ativo_restaurante}
    restaurantes.append(dados_restaurante)
    print(f'Seu restaurante {nome_restaurante}, de categoria {categoria_restaurante} foi cadastrado com sucesso e se encontra desativado.\n')
    voltar_main()

def listar_restaurante(opcao_escolhida):
    limpar_terminal()
    print(f'A opção escolhida foi {opcao_escolhida}. Listar restaurante!\nSegue lista de restaurante(s) cadastrado(s).')
    for restaurante in restaurantes:
        nome_restaurante      = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        ativo_restaurante     = restaurante['ativo']
        if ativo_restaurante == True:
            print(f'- {nome_restaurante} se encontra ativo!')
        elif ativo_restaurante == False:
            print(f'- {nome_restaurante} se encontra desativado!')
    voltar_main()

def alterar_estado_restaurante(opcao_escolhida):
    limpar_terminal()
    print(f'A opção escolhida foi: {opcao_escolhida}. Ativar restaurante!\n')

    voltar_main()

def escolher_opcao_app():
    try:
        opcao_escolhida = int(input('Escolha uma opção:'))
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante(opcao_escolhida)
        elif opcao_escolhida == 2:
            listar_restaurante(opcao_escolhida)
        elif opcao_escolhida == 3:
            alterar_estado_restaurante(opcao_escolhida)
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