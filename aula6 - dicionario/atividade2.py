"""
2. Agenda de Contatos
Crie um programa para armazenar números de telefone. 
O usuário deve poder adicionar novos contatos (nome como chave e número como valor). 
Depois, o programa deve exibir todos os contatos cadastrados. 
Obs: O salvamento deverá parar apenas quando o usuário digitar "finalizar"
"""

usuario = {
    'nome' : 'Paloma',
    'telefone' : '(11) 5656468446',
    'nome' : 'Marcelo',
    'telefone' : '(61) 545486478',
}

print(len(usuario))
print(list(usuario.keys()))
print(list(usuario.values()))