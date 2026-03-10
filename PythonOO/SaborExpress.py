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
    print('3. Alternar restaurante')
    print('4. Sair\n')
    
def finalizar_app():
    print('Finalizando app!\n')

def limpar_terminal():
    # os.system('cls') #Windows
    os.system('clear') #mac

def voltar_main():
    input('Digite um tecla para voltar ao menu principal.\n')
    main()

def opcao_invalida():
    input('Opção inválida!\nDigite uma tecla para voltar ao menu principal.\n')
    main()

def cadastrar_novo_restaurante():
    limpar_terminal()
    print(f'A opção escolhida foi: Cadastrar restaurante!\n')
    nome_restaurante = input('Digite o nome do restaurante que você deseja cadastrar:\n')
    categoria_restaurante = input(f'Digite a categoria do restaurante {nome_restaurante}:\n')
    ativo_restaurante = False
    dados_restaurante = {'nome':nome_restaurante, 'categoria':categoria_restaurante, 'ativo':ativo_restaurante}
    restaurantes.append(dados_restaurante)
    print(f'Seu restaurante {nome_restaurante}, de categoria {categoria_restaurante} foi cadastrado com sucesso e se encontra desativado.\n')
    voltar_main()

def listar_restaurante():
    limpar_terminal()
    print(f'A opção escolhida foi: Listar restaurante!\nSegue lista de restaurante(s) cadastrado(s).')
    for restaurante in restaurantes:
        nome_restaurante      = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        ativo_restaurante     = restaurante['ativo']
        if ativo_restaurante == True:
            print(f'- {nome_restaurante} | ativo!')
        elif ativo_restaurante == False:
            print(f'- {nome_restaurante} | desativado!')
    voltar_main()

def alternar_estado_restaurante():
    limpar_terminal()
    print(f'A opção escolhida foi: Alternar estado do restaurante!\n')
    nome_restaurante = input('Qual restaurante você deseja alternar o estado:\n')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if restaurante['nome'] == nome_restaurante:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {restaurante["nome"]} foi ativado com sucesso!' if restaurante['ativo'] else f'O restaurante {restaurante["nome"]} foi desativado com sucesso!'
            print(mensagem)
    if not restaurante_encontrado:
        print(f'Restaurante não encontrado')
    voltar_main()

def escolher_opcao_app():
    try:
        opcao_escolhida = int(input('Escolha uma opção:'))
        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurante()
        elif opcao_escolhida == 3:
            alternar_estado_restaurante()
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