valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
if valor1 > valor2:
    print(f'O primeiro valor ({valor1}) é maior que o segundo valor ({valor2}).')
elif valor2 > valor1:
    print(f'O segundo valor ({valor2}) é maior que o primeiro valor ({valor1}).')
elif valor1 == valor2:
    print(f'Não existe valor maior, os valores 1 e 2 são iguais!')