

# 1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.
pessoas = [{'nome':'Rodolfo', 'idade':39, 'cidade':'maranguape'},
          {'nome':'Yara', 'idade':39, 'cidade':'capital'},
          {'nome':'José Igor', 'idade':7, 'cidade':'capital'},
          {'nome':'Ícaro', 'idade':7, 'cidade':'capital'}
          ]
# 2 - Utilizando o dicionário criado no item 1:

# Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
def lista_pessoas():
    print('Nome'.ljust(20), '| Idade '.ljust(12), '| Cidade')
    for pessoa in pessoas:
        nome = pessoa['nome']
        idade = pessoa['idade']
        cidade = pessoa['cidade']
        print(f'{nome.ljust(20)} | {str(idade).ljust(10)} | {cidade}')

def atualiza_idade(busca_nome, idade_atualizada):
    for pessoa in pessoas:
        if busca_nome == pessoa['nome']:
            pessoa['idade'] = idade_atualizada
    print(f'Idade atualizada para o {busca_nome}')
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