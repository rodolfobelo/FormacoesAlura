from models.restaurante import Restaurante
from models.cardapio.bebida import Bebida
from models.cardapio.prato import Prato

restaurante_coxinhas = Restaurante('Coxinhas Gourmet', 'Salgados', 1000)
bebida_suco = Bebida('Suco de Melancia', 7.00, '500 ml')
prato_pao_alho = Prato('Pao de alho', 7.00, 'Pão carioquinha recheado com uma incrivel maionese temperada com sabor de alho.')
# Restaurante.altera_situacao(restaurante_coxinhas)

# restaurante_docinhos = Restaurante('Docinhos da Vovó', 'Doces')

# restaurante_pizza = Restaurante('Pizza do Dino', 'Massas')


# restaurante_coxinhas.receber_avaliacao('Rodolfo', 8)
# restaurante_coxinhas.receber_avaliacao('Yara', 10)
# restaurante_docinhos.receber_avaliacao('Rodolfo', 9)
# restaurante_docinhos.receber_avaliacao('Yara', 10)


def main():
    Restaurante.listar_restaurantes()
    print(bebida_suco)
    # pass

if __name__ == '__main__':
    main()
