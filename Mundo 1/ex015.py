Km =float(input('Digite a quantidade de Km rodados:'))
dias =int(input('Agora digite a quantidade de dias de aluguel do veículo:'))
preçodia = dias*60
preçokm = Km*0.15
print(f'Seu valor total a pagar é de R${preçodia + preçokm:.2f}, sendo R${preçodia} o valor pelos dias de aluguel e R${preçokm:.2f} o valor pelos Km rodados')
