# numero = int(input('Entre com um numero: '))
# if numero % 2 == 0:
#     print(f'Número {numero} é par.')
# else:
#     print(f'Número {numero} é impar')



numeros = [1,2,3,4,5,6,7,8,9,10]
nomes = ['Rodolfo', 'Yara', 'José Igor', 'Ícaro']
data_nascimento = ['1987', '2026']

# for numero in numeros:
#     print(numero)
# for nome in nomes:
#     print(nome)
# for datas in data_nascimento:
#     print(datas)

cont_impar = 0
for numero in numeros:
    if numero%2 != 0:
        cont_impar = cont_impar + numero
print(f'{cont_impar} é a soma dos numeros impares de 1 a 10')

i = 0
numero_tabuada = int(input('Entre com o numero para montar a tabuada\n'))
while i <= 10:
    print( f'{i}*{numero_tabuada} = {i*numero_tabuada}\n')
    i = i +1