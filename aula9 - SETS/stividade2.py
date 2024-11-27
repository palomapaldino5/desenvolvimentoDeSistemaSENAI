"""
2)Duas lojas possuem estoques diferentes de produtos. Encontre os produtos disponíveis em ambas e os exclusivos de cada loja.
"""
lojaA = {1,2,3,4,5}
lojaB = {5,6,7,8,9}
lojaC = set(lojaA ^ lojaB)

lojaC = lojaA ^ lojaB
