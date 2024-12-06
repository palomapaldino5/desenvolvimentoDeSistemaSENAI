"""
Crie um class motorista e um class carro, 
associe o carro ao motorista e possibilite que ele acelere o carro e também acrescente algo ao porta malas
"""

class motorista:
   def __init__(self, nome):
      self.nome = nome

class Carro:
    def __init__(self,cor,placa,peso,marca):
        self.cor = cor
        self.placa = placa
        self.peso = peso
        self.marca = marca
        self.km_atual = 0
    
    def alterarPlaca(self,placa ):
        self.placa = placa
        print(f'Alterei a placa para {self.placa}')

    @property
    def carroAdd(self):
        return(Carro)

    @carroAdd.setter
    def carroAdd(self, carroAdd):
        self.carro = carroAdd

carro1 = Carro('Branco', 'FIATOP', 20, 'Fiat')
print(carro1)
print(vars(carro1))
carro1.alterarPlaca('')
print(carro1.__dict__)

class carro1:
    def __init__(self, peso, mala):
        self.peso = peso
        self.mala = mala
    
    def mostrarMala(self):
        return self.mala
        