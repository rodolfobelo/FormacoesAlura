class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria, ativo):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}')


restaurante_1 = Restaurante('testeNome1', 'testeCategoria1', False)
restaurante_1 = Restaurante('testeNome2', 'testeCategoria2', True)

Restaurante.listar_restaurantes()