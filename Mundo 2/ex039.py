from datetime import date #modulo de data
atual = date.today().year #informa o ano do dia q o programa está sendo usado
nome = str(input('Informe seu nome completo: '))
lista = nome.split() #separa o nome em lista
print(f'Olá, {lista[0]}!') #escreve o primeiro item da lista (primeiro nome)
ano = int(input('Por favor informe seu ano de nascimento: '))
idade = atual - ano
if idade < 18:
    print(f'Ainda faltam {18 - idade} anos para o seu alistamento, {lista[0]}.')
elif idade > 18:
    print(f'Já se passaram {idade - 18} anos do ano do seu alistamento, {lista[0]}.')
elif idade == 18:
    print(f'Está na hora de você se alistar, {lista[0]}!')