class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria, nota=5.00, capacidade=10, ativo=False):
        self.nome = nome
        self.categoria = categoria
        self._ativo = ativo
        self.nota = nota
        self.capacidade = capacidade
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
    def listar_restaurantes():        
        print(f'{'Nome'.ljust(20)} | {'Categoria'.ljust(20)} | {'Nota'.ljust(20)} | {'Capacidade'.ljust(20)} | {'Situação'}')
        print(len(f'{'Nome'.ljust(20)} | {'Categoria'.ljust(20)} | {'Nota'.ljust(20)} | {'Capacidade'.ljust(20)} | {'Situação'}') * '*')
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome.ljust(20)} | {restaurante.categoria.ljust(20)} | {str(restaurante.nota).ljust(20)} | {str(restaurante.capacidade).ljust(20)} | {restaurante.ativo.ljust(20)}')

    @property
    def ativo(self):
        return '✅' if self._ativo else '❎'        


restaurante_1 = Restaurante('Coxinhas Gourmet', 'Salgados', 7.00, 1000, True)
restaurante_1 = Restaurante('Docinhos da Vovó', 'Doces')

Restaurante.listar_restaurantes()