def somarMuitos(*numeros):
    valorTotal = 0

    print(numeros)

    for numero in numeros:
        valorTotal += numero
        print (numero, valorTotal)

somarMuitos(1,2)
somarMuitos(250,901,412,321)
somarMuitos(410, 1203)
somarMuitos(1990283912, 1315789)

print(sum([1,5,7,8,9]))
