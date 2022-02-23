salario = float(input('Digite seu salário: '))
aumento1 = salario + salario * (10/100)
aumento2 = salario + salario * (15/100)
if salario > 1250.0:
    print (f'Seu salário atual é de R${salario:.2f}, com o aumento você receberá R${aumento1:.2f}.')
else:
    print (f'Seu salário atual é de R${salario:.2f}, com o aumento você receberá R${aumento2:.2f}.')
