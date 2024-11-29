#MODULOS PADRÃO DO PYTHON
# https://docs.python.org/3/py-modindex.html
#dicas úteis
# 1 - EVITE USAR NOMES DE VARIAVEIS
# IGUAIS A IMPORTAÇÃO

#AS APELIDO = ADICIONA APELIDO NO IMPORT
#obs : evite colocar apedidos que não sejam
#descritivos

#metodo 1 - puxa todo o mettodo
import  sys as sistema
#metodos 2 - puxa só uma função
from sys import exit as sair
#metodo 3 - Puxa um arquivo
import um_modulo_balacubaco
from um_modulo_balacubaco import nome

print (sistema.platform)
print(um_modulo_balacubaco.msg())
print(nome)
sair