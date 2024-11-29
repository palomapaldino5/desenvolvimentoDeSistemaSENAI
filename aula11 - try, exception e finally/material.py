# LINKS DOS ERROS
# 1 - https://docs.python.org/3/library/exceptions.html
# 2 - https://www.w3schools.com/python/python_ref_exceptions.asp

# print( 10 / 0) ZeroDivisionError

# lista = [0,1,2,3] IndexError
# print(lista[4])

# dicinario = {'chave':'valor'} KeyError
# print(dicinario['VICTOR'])

try:
    NUM_1 = 15
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
# TRY - tenta rodar o codigo
# EXCEPT - caso dê um erro espefico
# FINALLY - ultimo codigo a ser executado

