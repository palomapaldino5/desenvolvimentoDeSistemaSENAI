"""
1)Peça ao usuário dois números e uma operação matemática (+, -, *, /). 
Execute a operação e trate erros como divisão por zero e operação inválida.
"""

try:
    NUM_1 = 6
    NUM_2 = 5

    NUM_3 = NUM_1 / NUM_2

    print(NUM_3)

    listaBacana = [NUM_3]
    print(listaBacana[0])

    # RAISE - chama um erro para acontecer
    raise Exception

except ZeroDivisionError as erro:
    print('NÃO PODE DIVIDIR POR 0')
    print(erro)
except IndexError as erro:
    print('ELEMENTO NA LISTA NÃO EXISTE!')
    print(erro)
except KeyError as erro:
    print('DICIONÁRIO NÃO EXISTE!')
    print(erro)
except Exception:
    print('ERRO DESCONHECIDO')
finally:
    print('EXECUTEI O PROGRAMA!')