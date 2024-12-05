"""
AGREGAÇÃO - "FORMA MAIS ESPECIALIZADA DE ASSOCOAÇÃO"
"""

class Carrinho:
    def __init__(self):
        self.produto =[]

    def inserirProduto(self,*produto):
        for p in produto:
            self.produto.append(p)

    def listarProduto(self):
        for produto in self.produto:
            print(produto.nome)
            print(produto.preco)

class Produto:
    def __init__(self,nome,preco):
        self.nome = nome
        self.preco = preco

carrinho = Carrinho()
p1 = Produto('Relogio do Ben 10',350)
p2 = Produto('Hotwheels',10)

carrinho.inserirProduto(p1,p2)
carrinho.listarProduto()
print(carrinho.__dict__)