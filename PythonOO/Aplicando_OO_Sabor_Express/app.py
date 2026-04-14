from models.restaurante import Restaurante

restaurante_coxinhas = Restaurante('Coxinhas Gourmet', 'Salgados', 1000)
Restaurante.altera_situacao(restaurante_coxinhas)

restaurante_docinhos = Restaurante('Docinhos da Vovó', 'Doces')

restaurante_pizza = Restaurante('Pizza do Dino', 'Massas')


restaurante_coxinhas.receber_avaliacao('Rodolfo', 8)
restaurante_coxinhas.receber_avaliacao('Yara', 10)
restaurante_docinhos.receber_avaliacao('Rodolfo', 9)
restaurante_docinhos.receber_avaliacao('Yara', 10)
# restaurante_coxinhas.receber_avaliacao('Rodolfo', 7)
# restaurante_coxinhas.receber_avaliacao('Yara', 9)


Restaurante.listar_restaurantes()

# restaurante_docinhos.altera_situacao()
# Restaurante.listar_restaurantes()



def main():
    pass

if __name__ == '__main__':
    main()
