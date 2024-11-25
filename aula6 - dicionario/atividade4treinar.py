"""
4)Implemente uma lojinha virtual simples! 
Onde possamos ter um catálogo com 5 produtos e nesse podemos adicionar ao carrinho ou visualizar-lo. 
Até chegarmos na finalização do qual mostrará o valor total
"""
produtos = ['maguaiagem','condicionador', 'shampoo','mascara','pincel']
teste = ['texto',123, True,[2]]
produtosAlt = list()
print(type(produtos))
print(teste)

# metodos de uma lista
produtos = ['maguaiagem','condicionador', 'shampoo','mascara','pincel']

produtos.append('mascara') # adicionar no final

produtos.pop() # remover no final
print(produtos)

produtos.insert(2,'maquiagem') # inserir em um indice
print(produtos)

del produtos[1] #deletar em um indice
print(produtos)



# indice 0 1 2 3 4 / -5 -4 -3 -2 -1
print(produtos[1]) # puxar por um indice

produtos.remove('pincel') # deletar pelo valor
print(produtos)

produtos.clear() # deletar tudo da lista
print(produtos)

