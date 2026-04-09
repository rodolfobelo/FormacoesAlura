from models.restaurante import Restaurante

restaurante_coxinhas = Restaurante('Coxinhas Gourmet', 'Salgados', 1000)
restaurante_docinhos = Restaurante('Docinhos da Vovó', 'Doces')
restaurante_coxinhas._ativo = True

Restaurante.listar_restaurantes()

restaurante_docinhos.altera_situacao()
Restaurante.listar_restaurantes()



def main():
    pass

if __name__ == '__main__':
    main()
