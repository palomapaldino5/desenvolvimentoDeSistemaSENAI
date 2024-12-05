"""
ENCAPSULAMENTO
(SEM UNDERLINE) = PUBLIC (PUBLICO)
(UMA UNDERLINE) =  PROTECTED (NÃO DEVE FORA DA CLASSE)
(DOIS UNDERLINES) = PRIVATE  (NÃO É ACESSADO POR OUTRAS PARTES)
"""

class Carro:
    def __init__(self, nome,cor,placa,peso,marca):
        self.nome = nome
        self.cor = cor
        self.placa = placa
        self.peso = peso
        self.marca = marca
        self.km_atual = 0
    
    def alterarPlaca(self,placa ):
        self.placa = placa
        print(f'Alterei a placa para {self.placa}')


carro1 = Carro('fiat uno','Branco', 'FIATOP', 20, 'Fiat')
print(carro1)
print(vars(carro1))
carro1.alterarPlaca('')
print(carro1.__dict__)