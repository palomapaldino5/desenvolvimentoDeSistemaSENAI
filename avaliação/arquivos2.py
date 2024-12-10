"""
2)Escreva um programa para um sistema de controle de estoque de uma loja. O programa deve:Usar um para armazenar os itens no estoque, onde as chaves são os nomes dos produtos e os valores são as quantidades disponíveis.Permitir que o usuário escolha uma das opções:
Adicionar um novo produto ao estoque.
Atualizar a quantidade de um produto existente.
Verificar se um produto está disponível (quantidade maior que 0).
Continuar exibindo o menu até que o usuário escolha sair.
"""
loja = ['paloma','Alan', 'Bruna']
teste = ['texto',123, True,[]]
clientesAlt = list()
print(type(loja))
print(teste)

lista = ['Copo', 'Banana','KitKat', 'Bebida']

lista.append('VideoGame')

lista.pop() 
print(lista)

lista.insert(2,'TV')
print(lista)

del lista[1] 
print(lista)

print(lista[1]) 
lista.remove('Bebida') 
print(lista)

lista.clear() 
print(lista)
