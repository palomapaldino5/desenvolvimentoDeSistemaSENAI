"""
1)(timer)Crie um cronômetro reverso com uma mensagem final personalizada usando o módulo time.
"""

import time
from time import sleep as timer

segundo = float(input('Quantod segundos tem o timer: '))

for i in range(segundo,0,-1):
   timer(1)
   print(f'{i} segundo')

print('TEMPO ESGOTADO!')


#import um_modulo_tempo
#from um_modulo_tempo import time

#print(um_modulo_tempo)
#print(time)
