class Restaurante:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False


restaurante_nome = 'testeNome'
restaurante_1_categoria = 'testeCategoria'

restaurante_1 = Restaurante(restaurante_nome, restaurante_1_categoria)

print(restaurante_1.nome)
print(restaurante_1.categoria)