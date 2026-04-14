from models.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria, capacidade=10, ativo=False):
        self._nome = nome.title()
        self.categoria = categoria.title()
        self._ativo = ativo
        self._avaliacao = []
        self.capacidade = capacidade
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self.categoria}'
    
    @classmethod
    def listar_restaurantes(cls):        
        print(f'{'Nome'.ljust(20)} | {'Categoria'.ljust(20)} | {'Capacidade'.ljust(20)} | {'Avaliação'.ljust(20)} | {'Situação'}')
        print(len(f'{'Nome'.ljust(20)} | {'Categoria'.ljust(20)} | {'Capacidade'.ljust(20)} | {'Avaliação'.ljust(20)} | {'Situação'}') * '*')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(20)} | {restaurante.categoria.ljust(20)} | {str(restaurante.capacidade).ljust(20)} | {str(restaurante.media_avaliacoes()).ljust(20)} | {restaurante.ativo.ljust(20)}')

    def altera_situacao(self):
        self._ativo = not self._ativo

    @property
    def ativo(self):
        return '✅' if self._ativo else '❎'

    def receber_avaliacao(self, cliente, nota):
        if nota > 5:
            nota = nota / 2        
        elif 0 < nota <= 5:
            nota = nota
        self._avaliacao.append(Avaliacao(cliente, nota))

    def media_avaliacoes(self):
        if not self._avaliacao:
            return 'Sem avaliação!'
        soma_notas = sum(av._nota for av in self._avaliacao)
        quantidade_notas = len(self._avaliacao)
        media = round(soma_notas / quantidade_notas, 1)
        return media