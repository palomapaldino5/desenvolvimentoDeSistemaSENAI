"""
3)(calendar)Use o módulo calendar para exibir o calendário completo do ano atual
"""
import calendar
from datetime import datetime

ano_atual = datetime.now().year
dia_atual = datetime.now().day
mes_atual = datetime.now().month
hora_atual = datetime.now().hour

print(f'Você está no ano de {ano_atual} \n mês: {mes_atual} \n dia: {dia_atual} \n hora: {hora_atual}')
print(calendar.calendar(ano_atual))

#from calendar import exit as sair 

#import um_modulo_caledario
#print(um_modulo_caledario)
#print(calendar)