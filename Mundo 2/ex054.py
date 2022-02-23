from datetime import date
atual = date.today().year
cont1 = 0
cont2 = 0
for c in range (1, 8):
    ano = int(input(f'Digite o ano de nascimento da {c}ª pessoa: '))
    idade = atual - ano
    if idade >= 18:
        cont1 = cont1 + 1
    else:
        cont2 = cont2 + 1
print (f'Ao todo, {cont1} pessoas já atingiram a maioridade e {cont2} ainda são de menor.')


