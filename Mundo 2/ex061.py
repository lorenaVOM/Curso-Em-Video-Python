print (f'{"10 TERMOS DE UMA PA":=^40}')
termo = int(input('Digite o primeiro termo da sua PA: '))
razão = int(input('Digite a razão da sua PA: '))
primeiro = termo
c = 1
while c <= 10:
    c += 1
    primeiro += razão
    print (f'{primeiro} ➔', end= ' ')
print ('FIM')