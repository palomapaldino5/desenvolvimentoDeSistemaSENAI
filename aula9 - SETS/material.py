"""
SETS - CONJUNTOS

 - 1 º NÃO TEM INDICE (NÃO GARANTE ORDEM)
 - 2 º NÃO ACEITA CONTEUDO REPITIDO
"""



#CRIANDO SET 
a = set('VICTOR')
teste = ['OI', 'OI' , 'OI']
print(a)
print(set(teste))

b = {'Victor'}
print(b)

c = set()
print(c ,  type(c))
# metodos uteis
conjunto = set()
conjunto.add(10)
conjunto.add(8)

conjunto.update(( 3,5,6, 'BOM DIA'))

conjunto.discard(5)

print("*"*20)
print(conjunto)

#UNIÃO (union) - une dois
#INTERSECÇÃO (instersection) - comum nos dois
#DIFERENÇA - item presentes apenas em um conjunto

conjuntoA = {1,2,3,4,5}
conjuntoB = {5,6,7,8,9}
conjuntoC = set()

# | union 
conjuntoC = conjuntoA | conjuntoB
# & intersection
conjuntoC = conjuntoA & conjuntoB
# - diference = difrença em relação ao
#conjunto da esquerda
conjuntoC = conjuntoB - conjuntoA
# ^ diference = diferença em relação a ambos os conjuntos
conjuntoC = conjuntoA ^ conjuntoB

for elemento in conjuntoC:
    print(elemento)


print(conjuntoC)
 

