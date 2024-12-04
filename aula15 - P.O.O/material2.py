#UBER 
class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.saldo = 0
        self.valiacao = 5
    def adicionarSaldo(self,valor):
        self.saldo += valor
        print(f'Ovalor de {valor} foi adicionado')

cliente = Cliente('Victor', 21)
cliente.adicionarSaldo(100)
print(cliente.saldo , cliente.avaliacao)