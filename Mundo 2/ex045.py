from random import randint
from time import sleep
opções = ('Pedra', 'Papel', 'Tesoura')
computador = randint (0, 2) #computador escolhe um item aleatório das opções
print ('''Vamos brincar de Pedra, Papel e Tesoura!
Jogue uma das opções abaixo:
- Pedra
- Papel
- Tesoura''')
opção = str (input('Sua jogada: ')).strip().title()
print ('JO')
sleep(.5)
print ('KEN')
sleep(.5)
print ('PO')
sleep(.5)
if opção == 'Pedra' and computador == 2:
    print ('Tesoura!\nDroga... você me venceu! Parabéns, humano! Melhor de 3?')
elif opção == 'Pedra' and computador == 1:
    print ('Papel!\nGANHEI! Meu papel cobre sua pedra! Mais sorte na próxima vez, humano.')
elif opção == 'Pedra' and computador == 0:
    print ('Pedra!\nOps...Vamos tentar mais uma vez!')
elif opção == 'Papel' and computador == 0:
    print ('Pedra!\nDroga... você me venceu! Parabéns, humano! Melhor de 3?')
elif opção == 'Papel' and computador == 2:
    print ('Tesoura!\nGANHEI! Minha tesoura corta seu papel! Mais sorte na próxima vez, humano.')
elif opção == 'Papel' and computador == 1:
    print ('Papel!\nOps...Vamos tentar mais uma vez!')
elif opção == 'Tesoura' and computador == 1:
    print ('Papel!\nDroga... você me venceu! Parabéns, humano! Melhor de 3?')
elif opção == 'Tesoura' and computador == 0:
    print('Pedra!\nGANHEI! Minha pedra esmaga sua tesoura! Mais sorte na próxima vez, humano.')
elif opção == 'Tesoura' and computador == 2:
    print ('Tesoura!\nOps...Vamos tentar mais uma vez!')