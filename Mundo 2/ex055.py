maior = 0
menor = 0
for c in range (1, 6):
    peso = float(input(f'Digite o peso da {c}ª pessoa: '))
    if c == 1:
        maior = peso
        menor = peso
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print (f'O maior peso registrado foi de {maior}Kg.\nE o menor foi de {menor}Kg.')
