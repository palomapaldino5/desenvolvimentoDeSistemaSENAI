#UBER 
class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.saldo = 0
        self.avaliacao = 5
    def adicionarSaldo(self,valor):
        self.saldo += valor
        print(f'O valor de {valor} foi adicionado')
    def removerSaldo(self, valor):
        self.saldo -= valor
        print(f'O valor de {valor} foi debitado')
    def avaliar(self):
        nota = float(input('Qual é a avaliação? (0 a 5 ✨)'))
        self.avaliacao = nota
        print(f'Sua nota atual é de {self.avaliacao}✨')

cliente = Cliente('Victor', 21)
cliente.adicionarSaldo(100)
cliente.removerSaldo(10)
cliente.avaliar()
print(cliente.saldo , cliente.avaliacao)