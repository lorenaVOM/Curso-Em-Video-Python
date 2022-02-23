soma = 0 #acumulador
contador = 0 #contador
for c in range (1, 500+1, 2):
    if c % 3 == 0: #se a divisão por 3 for igual a 0
        contador = contador + 1
        soma = soma + c
print (f'A soma de todos os {contador} valores solicitados é {soma}.')