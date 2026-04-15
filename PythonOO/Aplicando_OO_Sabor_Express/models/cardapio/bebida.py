from models.cardapio.item_cardapio import ItemCardapio

class Bebida(ItemCardapio):
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco)
        self._tamanho = tamanho
    
    def __str__(self):
        tam = len(f'{'Nome'.ljust(20)} | {'Preço'.ljust(20)} | {'Tamanho'}')
        return f'{'Nome'.ljust(20)} | {'Preço'.ljust(20)} | {'Tamanho'}\n{tam * '*'}\n{self._nome.ljust(20)} | {str(self._preco).ljust(20)} | {self._tamanho}'
                 
        