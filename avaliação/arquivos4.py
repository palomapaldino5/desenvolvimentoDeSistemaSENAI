"""
4)Crie duas classes:
1 Autor, com os atributos:  Nome, nacionalidade e livros
2 Livro, com os atributos: titulo, ano e autor
Depois, escreva um programa que:Crie um autor e dois livros associados a ele.
Imprima o nome do autor e a lista dos seus livros.
"""

nome = None
nacionalidade = []
livro = 0

def carregarCatalogo():
    print('1 - R$59,50 Vigiar e punir')
    print('2 - R$100.50  LDB fácil')
    print('3 - R$50.50 S10 lições sobre Santo Agostinho')
    print('4 - R$18.99 Exercícios práticos para estimular a memória Vol. 1')
    print('5 - R$99.99 A vida que vale a pena ser vivida')
    print('6 - MOSTRAR CARRINHO')
    print('7 - FINALIZAR')
 
    global escolha
    escolha = input('Digite a opção desejada: ')

def adicionarCarrinho(nome,valor):
    livro.append(nome)
    global valorTotal
    valorTotal += valor
    print(f'{nome} adicionado efetuado com sucesso!')

while True:
    carregarCatalogo()

    if escolha == '1':
        adicionarCarrinho('Vigiar e punir', 59.50)
    elif escolha == '2':
        adicionarCarrinho('LDB fácil', 100.50)
    elif escolha == '3':
        adicionarCarrinho('S10 lições sobre Santo Agostinho', 50.50)
    elif escolha == '4':
        adicionarCarrinho('Exercícios práticos para estimular a memória Vol. 1', 18.99)
    elif escolha == '5':
        adicionarCarrinho('A vida que vale a pena ser vivida', 99.99)
    elif escolha == '6':
        print(livro)
    elif escolha == '7':
        break
    else:
         print('Opção inválida! Tente novamente!')
print(f'Valor total da compra é de : {livro}')