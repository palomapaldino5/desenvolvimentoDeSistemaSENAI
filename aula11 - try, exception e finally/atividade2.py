"""
2)Crie um dicionário com informações sobre um aluno (por exemplo, nome, idade, notas). 
Em seguida, solicite ao usuário uma chave para acessar no dicionário. Caso a chave não exista, 
trate o erro e informe quais chaves estão disponíveis.
"""

try:
    NOME = 15
    IDADE = 5

    NOTAS = NOME / IDADE

    print(NOTAS)

    listaBacana = [NOTAS]
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