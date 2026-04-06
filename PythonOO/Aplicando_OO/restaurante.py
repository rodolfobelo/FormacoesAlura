class Restaurante:
<<<<<<< HEAD
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
=======
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
>>>>>>> c659c34e207acf6e68d45fa5d551501eab917e0d


restaurante_1 = Restaurante('testeNome1', 'testeCategoria1', False)
restaurante_1 = Restaurante('testeNome2', 'testeCategoria2', True)

<<<<<<< HEAD
Restaurante.listar_restaurantes()
=======
restaurante_1 = Restaurante(restaurante_nome, restaurante_1_categoria)

print(restaurante_1.nome)
print(restaurante_1.categoria)
>>>>>>> c659c34e207acf6e68d45fa5d551501eab917e0d
