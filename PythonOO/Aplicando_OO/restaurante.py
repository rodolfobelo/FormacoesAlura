class Restaurante:
    def __init__(self, nome, categoria, ativo):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo


restaurante_nome = 'testeNome'
restaurante_1_categoria = 'testeCategoria'

restaurante_1 = Restaurante(restaurante_nome, restaurante_1_categoria, False)

print(restaurante_1.nome)