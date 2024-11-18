lista = [5,8,2,9,1]
# c)
lista.append(7)
lista.insert(2,3)
print(lista)

# d)
#del lista[1]
#lista.insert(10,1)

lista[1] = 10
print(lista)

# e)
del lista[4]
del lista[3]
del lista[2]
print(lista)

#2 a)
lista = []

for i in range(4):
    lista = int(input(f'Digite o {i+1}º lista'))
    lista.append (lista)

    #lista > maior

print(lista)
print(max(lista))    
print(min(lista))