"""
2) Crie uma função fala se um número é par ou ímpar. Retorne se o número é par ou ímpar.
"""

def parImpar(numero):

    if numero % 2==0:
        return'Par'
    else:
        return'Impar'
    
print(parImpar(2))
print(parImpar(3))