class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria, nota=5.00, capacidade=10, ativo=False):
        self._nome = nome.title()
        self.categoria = categoria.title()
        self._ativo = ativo
        self.nota = nota
        self.capacidade = capacidade
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self.categoria}'
    
    @classmethod
    def listar_restaurantes(cls):        
        print(f'{'Nome'.ljust(20)} | {'Categoria'.ljust(20)} | {'Nota'.ljust(20)} | {'Capacidade'.ljust(20)} | {'Situação'}')
        print(len(f'{'Nome'.ljust(20)} | {'Categoria'.ljust(20)} | {'Nota'.ljust(20)} | {'Capacidade'.ljust(20)} | {'Situação'}') * '*')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(20)} | {restaurante.categoria.ljust(20)} | {str(restaurante.nota).ljust(20)} | {str(restaurante.capacidade).ljust(20)} | {restaurante.ativo.ljust(20)}')

    def altera_situacao(self):
        self._ativo = not self._ativo

    @property
    def ativo(self):
        return '✅' if self._ativo else '❎'        



restaurante_1 = Restaurante('Coxinhas Gourmet', 'Salgados', 7.00, 1000)
restaurante_2 = Restaurante('Docinhos da Vovó', 'Doces')
restaurante_1._ativo = True

Restaurante.listar_restaurantes()

restaurante_1._nome = 'alterado coxinhas gourmet'
restaurante_2.altera_situacao()
Restaurante.listar_restaurantes()