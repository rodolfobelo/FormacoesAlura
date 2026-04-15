from models.cardapio.item_cardapio import ItemCardapio

class Prato(ItemCardapio):
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco)
        self._descricao = descricao

    def __str__(self):
        return f'*****__Prato__*****\n{'Nome'.ljust(20)} | {'Preço'.ljust(20)} | {'Descrição'}\n{len(f'{'Nome'.ljust(20)} | {'Preço'.ljust(20)} | {'Descrição'}') * '*'}\n{self._nome.ljust(20)} | {str(self._preco).ljust(20)} | {self._descricao}'