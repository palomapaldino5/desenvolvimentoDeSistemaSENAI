# 98 POP
#nome_motorista1 = 'Geraldo'
#carro_motorista1 = 'Renault Kwid'

#class - 'molde ddo objeto'
#def __init__() - função construtora
#self - 'o proprio objeto"
#PascalCase - primeira letra de todas as palavras maiusculo 
#obs : Cam

class Motorista:
    def __init__(self,nome,carro, corCarro, placa):
        self.nome = nome
        self.carro = carro
        self.corCarro = corCarro
        self.placa = placa


motorista1 = Motorista('Geraldo', 'Renault Kwid','rosa pink','1234-top')
motorista2 = Motorista('Victor', 'Camaro','Preto supreme','camaro-2')
# motorista1.nome = 'Geraldo'
# motorista1.carro = 'Renault Kwid'
print(motorista1.carro)
print(motorista2.carro)

print(motorista1, type(motorista1))