#equanto condição for true, farei de novo
#break - quebra a repetição

condicao = True

# while condicao:
#     pergunta = input('DESEJA REPETIR DE NOVO')

#    if pergunta == 'nao':
#     break

contador = 0
while contador <= 10:
   
    #contador = contador + 1
    contador += 1

    if contador == 5:
        print('NÃO VOU MOSTRAR O 5 :(')
        continue

print(contador)
# contador = contador  + 1