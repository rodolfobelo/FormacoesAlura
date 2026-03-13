

# 1 - Crie um dicionário representando informações sobre uma pessoa, como nome, idade e cidade.
pessoas = [{'nome':'Rodolfo', 'idade':39, 'cidade':'maranguape'},
          {'nome':'Yara', 'idade':39, 'cidade':'capital'},
          {'nome':'José Igor', 'idade':7, 'cidade':'capital'},
          {'nome':'Ícaro', 'idade':7, 'cidade':'capital'}
          ]
# 2 - Utilizando o dicionário criado no item 1:

# Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
for pessoa in pessoas:
    print(f'{pessoa['nome']} | {pessoa['idade']} | {pessoa['cidade']}')
nome = input('De quem você deseja atualizar a idade? ')
idade = int(input('Entre com a idade atualizada: '))
pessoas['nome':f'{nome}']
# Adicione um campo de profissão para essa pessoa;
# Remova um item do dicionário.
# 3 - Crie um dicionário que relacione os números de 1 a 5 aos seus respectivos quadrados.

# 4 - Crie um dicionário e verifique se uma chave específica existe dentro desse dicionário.

# 5 - Escreva um código que conte a frequência de cada palavra em uma frase utilizando um dicionário.