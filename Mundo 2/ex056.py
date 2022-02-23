somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomehomem = ''
contmulher = 0
for c in range (1, 5):
    print (f'-------- {c}ª PESSOA --------')
    nome = str(input(f'Nome: ')).strip()
    idade = int(input(f'Idade: '))
    sexo = str(input(f'Sexo(M/F): ')).strip().upper()
    somaidade = somaidade + idade
    if c == 1 and sexo == 'M':
        maioridadehomem = idade
        nomehomem = nome
    if idade > maioridadehomem and sexo == 'M':
        maioridadehomem = idade
        nomehomem = nome
    if sexo == 'F' and idade < 20:
        contmulher = contmulher + 1
mediaidade = somaidade / 4
print (f'A média das idades registradas foi {mediaidade}.')
print (f'O homem mais velho tem {maioridadehomem} anos e se chama {nomehomem}.')
print (f'{contmulher} mulheres possuem MENOS de 20 anos.')
