from random import randint
computador = randint (0, 5) # Gera um número inteiro entre um intervalo de números
print ('Vou pensar em número de 0 a 5. Será que você consegue adivinhar em que número eu estou pensando?')
numero = int(input('Em qual número eu pensei? '))
if numero == computador:
    print ('Uau! Você é bom nisso!')
else:
    print (f'GANHEI! Eu pensei no número {computador} e não no {numero}. Tente novamente!')

