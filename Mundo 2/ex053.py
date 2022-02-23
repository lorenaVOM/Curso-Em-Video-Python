frase = str(input('Digite uma frase: ')).strip().upper() #remove os espaços e deixa em letras maiúsculas
palavras = frase.split() #separa as palavras da frase
junto = ''.join(palavras) #junta as palavras da frase
inverso = ''
for letra in range(len(junto) -1, -1, -1): #len contagem de letras, 1(-1) última letra, 2(-1) primeira letra, 3(-1) conta ao contrário
    inverso = inverso + junto[letra] #inverte a frase
if inverso == junto:
    print ('Sua frase É um palíndromo!')
else:
    print ('Sua frase NÃO É um palíndromo!')
