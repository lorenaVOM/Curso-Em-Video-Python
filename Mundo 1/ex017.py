import math
catoposto = float(input('Comprimento do cateto oposto: '))
catadjascente = float(input('Comprimento do cateto adjascente: '))
h = math.hypot(catoposto, catadjascente)
print(f'O comprimento da hipotenusa é {h}')



