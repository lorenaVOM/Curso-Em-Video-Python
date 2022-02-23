cont = 0
num = int (input('Digite um número: '))
for c in range (1, num + 1):
    if num % c == 0:
        print ('\033[32m', end= '')
        cont = cont + 1
    else:
        print ('\033[31m', end= '')
    print (f'{c} ', end= '')
print (f'\n\033[mO número é divisível por {cont} números.')
if cont == 2:
    print (f'O número {num} É PRIMO.')
else:
    print (f'O número {num} NÃO É PRIMO.')
