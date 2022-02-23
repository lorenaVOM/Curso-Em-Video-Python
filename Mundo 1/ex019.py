from random import choice
a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))
a5 = str(input('Quinto aluno: '))
alunos = [a1, a2, a3, a4, a5]
sorteio = choice(alunos) # choice escolhe um item aleatório da lista
print(f'O aluno sorteado foi: {sorteio}')
