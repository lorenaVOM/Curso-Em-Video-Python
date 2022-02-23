distancia = float(input('Digite a distância do seu local de partida até o seu destino: '))
preço1 = distancia * 0.50
preço2 = distancia * 0.45
if distancia <= 200.0:
    print (f'O valor é de R${preço1:.2f} por passagem!')
else:
    print (f'O valor é de R${preço2:.2f} por passagem!')