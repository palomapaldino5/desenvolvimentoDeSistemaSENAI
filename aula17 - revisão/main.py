"""
4)Crie uma classe Aluno que tenha os atributos nome, 
notas (uma lista) e métodos para calcular a média 
e verificar se o aluno foi aprovado (média >= 7). 
Todo aluno criado deverá ser adicionado a um Json

1- criar o aluno (objeto) nome e notas
2- metodo do aluno calcular media
3- verificar se ele passou ou não
4- calcular a media, criar objetos
5- verificar se existe alunos anteriores
6- exportar para um json 
"""

#sem under - publico
#com um under - protegido
#com dois under - privado

import json
import os

class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self._notas = []

    def adicionarNota(self,nota):
        #nota = int(input('Qual é a nota'))
        self._notas.append(nota)
    
    def calcularMedia(self):
        if self._notas:
            return sum(self._notas) / len(self._notas)
        else:
            return 0

    def verificarAprovacao(self):
        media = self.calcularMedia()

        if media >= 7:
            print(f'Aluno(a) {self.nome} está a´rovado')
        else:
            print(f'Aluno(a) {self.nome} está reprovado')

    def exportarAluno(self):
        dados_alunos = {
            'nome' : self.nome,
            'notas' : self._notas,
            'media' : self.calcularMedia(),
            'aprovacao' : self.verificarAprovacao()
        }              
        
        # se o arquivos existe! Se sim salva em dados
        # se não dados vazio []
        if os.path.exists('dados.json'):
            with open ('dados.json' , 'r', encoding='utf8') as f:
                try:
                    dados = json.load(f)
                except json.JSONDecodeError:
                    dados = []
        
        else:
            dados = []
        
        dados.append(dados_alunos)

        with open('dados.json','w', encoding='utf8') as f:
            json.dump(dados,f,indent=2)

aluno1 = Aluno('victor')
aluno1.adicionarNota(8)
aluno1.adicionarNota(7)
print(aluno1._notas)
aluno1.verificarAprovacao()

aluno2 = Aluno('Bruna')
aluno2.verificarAprovacao()

aluno3 = Aluno('Pedro')
aluno3.adicionarNota(5)
aluno3.adicionarNota(6)
aluno3.verificarprovacao()

aluno4 = Aluno('joão')

aluno1.exportarAluno()
aluno2.exportarAluno()
aluno3.exportarAluno()
aluno4.exportarAluno()

print(vars(aluno1))
print(aluno2.__dict__)
print(aluno3.__dict__)