n = int(input('Digite um número[999 para parar]: '))
cont = 0
soma = 0
while n != 999:
    n = int(input('Digite um número[999 para parar]: '))
    cont += 1
    soma += n
print(f'Você digitou {cont} números e a soma deles é igual a {soma}.')