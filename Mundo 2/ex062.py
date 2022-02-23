print (f'{"10 TERMOS DE UMA PA":=^40}')
termo = int(input('Digite o primeiro termo da sua PA: '))
razão = int(input('Digite a razão da sua PA: '))
primeiro = termo
c = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while c <= total:
        c += 1
        primeiro += razão
        print (f'{primeiro} ➔', end= ' ')
    print ('PAUSA')
    mais = int(input('Quantos termos a mais você deseja visualizar? '))
print (f'Progressão finalizada com {total} termos. Obrigada por usar nosso programa!')