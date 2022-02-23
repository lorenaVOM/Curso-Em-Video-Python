lado1 = float(input('Digite o comprimento da primeira reta: '))
lado2 = float(input('Digite o comprimento da segunda reta: '))
lado3 = float(input('Digite o comprimento da terceira reta: '))
print('Aanalisando triângulo...')
if lado1 > ((lado2 - lado3) * -1) and lado1 < (lado2 + lado3): # condição de existência para a formação de um triângulo
    print(f'Os lados {lado1}, {lado2} e {lado3} FORMAM um triângulo!')
    if lado1 == lado2 == lado3: # condição dentro da condição
        print('O triângulo que será formado com esses segmentos será um triângulo EQUILÁTERO.')
    elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
        print('O triângulo que será formado com esses segmentos será um triângulo ISÓSCILES.')
    else:
        print('O triângulo que será formado com esses segmentos será um triângulo ESCALENO.')
else:
    print(f'Os lados {lado1}, {lado2} e {lado3} NÃO FORMAM um triângulo!')