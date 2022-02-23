from math import factorial
num = int(input('Digite um número para calcular seu fatorial: '))
fat = factorial(num)
c = num
print (f'{num}! = ', end='')
while c > 0:
    c -= 1
    print (f'{c}', end='')
    print (' x 'if c > 0 else ' = ' f'{fat}', end='')