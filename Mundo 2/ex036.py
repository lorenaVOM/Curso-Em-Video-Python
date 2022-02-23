valor = float(input('Digite o valor da casa: R$'))
salario = float(input('Qual é o seu salário? R$'))
anos = int(input('Em quantos anos você quer pagar o imóvel? '))
preço = valor / (anos * 12)
print(f'Para pagar uma casa de R${valor}, em {anos} anos a prestação será de R${preço:.2f}.')
if preço > (30/100 * salario):
    print('EMPRÉSTIMO NEGADO!')
else:
    print('EMPRÉSTIMO ACEITO!')