"""
1. Cadastro de Produto
Você precisa criar um programa que armazene informações de um produto em um 
dicionário. As informações devem incluir nome, preço e quantidade em estoque. 
Depois, o programa deve exibir todas as informações do produto.
"""

produto = {
    'nome'  : 'maça',
    'preço' : 'R$4,99',
    'qualidade em estoque' : '100',
    'tipoRed' : True
}


print(produto['nome'])

print(produto, type(produto))
