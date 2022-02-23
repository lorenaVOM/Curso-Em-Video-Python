frase = str(input('Digite uma frase: ')).lower()
print ('Quantas letras A existem na sua frase? {}'.format(frase.count('a')))
print ('A primeira letra A apareceu na posição: {}'.format(frase.find('a')+1))
print ('A última letra A apareceu na posição: {}'.format(frase.rfind('a')+1))

