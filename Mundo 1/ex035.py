lado1 = float(input('Digite o comprimento da primeira reta: '))
lado2 = float(input('Digite o comprimento da segunda reta: '))
lado3 = float(input('Digite o comprimento da terceira reta: '))
print('Aanalisando triângulo...')
if lado1 > ((lado2 - lado3) * -1) and lado1 < (lado2 + lado3): # condição de existência para a formação de um triângulo
    print(f'Os lados {lado1}, {lado2} e {lado3} FORMAM um triângulo!')
else:
    print(f'Os lados {lado1}, {lado2} e {lado3} NÃO FORMAM um triângulo!')
