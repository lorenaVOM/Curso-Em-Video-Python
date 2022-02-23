num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
opção = 0
while opção != 5:
    print ('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior valor
    [ 4 ] novos volares
    [ 5 ] sair do programa''')
    opção = int(input('O que deseja fazer com esses valores? '))
    if opção == 1:
        print(f'{num1} + {num2} = {num1 + num2}')
    if opção == 2:
        print(f'{num1} x {num2} = {num1 * num2}')
    if opção == 3:
        if num1 > num2:
            print(f'{num1} é o maior valor.')
        if num2 > num1:
            print(f'{num2} é o maior valor.')
    if opção == 4:
        print('Digite os novos valores:')
        num1 = int(input('Primeiro valor: '))
        num2 = int(input('Ssegundo valor: '))
    if opção == 5:
        print('Obrigada por usar nosso programa! Volte sempre!')
