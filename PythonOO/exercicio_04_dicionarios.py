

# 1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.
pessoas = [{'nome':'Rodolfo', 'idade':39, 'cidade':'maranguape', 'profissao':''},
          {'nome':'Yara', 'idade':39, 'cidade':'capital', 'profissao':''},
          {'nome':'José Igor', 'idade':7, 'cidade':'capital', 'profissao':''},
          {'nome':'Ícaro', 'idade':7, 'cidade':'capital', 'profissao':''}
          ]
# 2 - Utilizando o dicionário criado no item 1:

# Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
def lista_pessoas():
    print('Nome'.ljust(20), '| Idade '.ljust(12), '| Cidade'.ljust(22), '| Profissâo')
    print(len('Nome'.ljust(20) + '| Idade '.ljust(12) + '| Cidade'.ljust(20) + '| Profissâo'.ljust(20)) * '-')
    for pessoa in pessoas:
        nome = pessoa['nome']
        idade = pessoa['idade']
        cidade = pessoa['cidade']
        profissao = pessoa['profissao']
        print(f'{nome.ljust(20)} | {str(idade).ljust(10)} | {cidade.ljust(20)} | {profissao}')

def atualiza_idade(busca_nome, idade_atualizada):
    i = 0
    for pessoa in pessoas:
        if busca_nome == pessoa['nome']:
            pessoa['idade'] = idade_atualizada
            i = i + 1
    if i > 0:
        print(f'\nIdade atualizada para o {busca_nome}.\n')
    else:
        print(f'\nIdade não atualizada, o nome {busca_nome} não foi encontrado.\n')
    lista_pessoas()

def main():
    lista_pessoas()
    busca_nome = input('De quem você deseja atualizar a idade? ')
    idade_atualizada = int(input('Entre com a idade atualizada: '))
    atualiza_idade(busca_nome, idade_atualizada)

if __name__ == '__main__':
    main()

# Adicione um campo de profissão para essa pessoa;
# Remova um item do dicionário.
# 3 - Crie um dicionário que relacione os números de 1 a 5 aos seus respectivos quadrados.

# 4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.

# 5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.