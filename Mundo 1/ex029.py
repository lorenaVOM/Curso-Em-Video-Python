velocidade = float(input('Qual é a velocidade atual do carro? '))
multa = 7 * (velocidade - 80)
if velocidade > 80.0:
    print (f'Você ultrapassou o limite de velocidade de 80Km/h! Você deverá pagar uma multa no valor de R${multa:.2f}.')
else:
    print ('Você está dentro do limite de velocidade de 80Km/h.')
print ('Tenha um bom dia! Dirija com segurança!')
