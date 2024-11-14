print('----CATALOGO----')
print('A) PAMONHA - R$ 7,00')
print('B) CALDO - R$ 4,00')
print('C) PASTEL - R$ 6,99')
print('D) CAFÉ - R$ 3,00')
print('E) CANCELAR')
print('F) FINALIZAR')

adicionar ='sim'

while adicionar == 'sim':

    opcao = input('Qual opcao desejada: ')
    valorTotal =float


    valorTotal = float

    match opcao:
        case 'a':
            print("Você escolheu pamonha")
            valorTotal = 7.00
        case 'b':
            print("Você escolheu caldo")
            valorTotal = 4.00
        case 'c':
            print("Você escolheu pastel")
            valorTotal = 6.99
        case 'd':
            print("Você escolheu café")
            valorTotal = 3.00
        case 'e':
            print("Pedido cancelado!")
        case 'f':
            print("Total do pedido: ",valorTotal)

            adicionar = input('Desejar adicionar algo? (sim ou nao)')

    if adicionar == 'nao':
        break
            
print(valorTotal)