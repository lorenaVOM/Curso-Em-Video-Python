from random import randint
computador = randint (0, 10)
print ('Olá, humano! Eu sou seu computador e estou pensando em um número de 1 a 10.\nSerá que você consegue adivinhar qual número eu estou pensando?')
acertou = False
palpites = 0
while not acertou:
    num = int(input('Dê seu palpite: '))
    palpites = palpites + 1
    if num == computador:
        acertou = True
    else:
        if num > computador:
            print('Menos...Tente novamente!')
        elif num < computador:
            print('Mais...Tente novamente!')
print(f'Parabéns, humano! Você acertou depois de {palpites} palpites!')
