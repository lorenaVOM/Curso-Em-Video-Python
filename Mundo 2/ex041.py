from datetime import date #modulo de data
atual = date.today().year #informa o ano do dia q o programa está sendo usado
ano = int(input('Informe o ano de nascimento do atleta: '))
idade = atual - ano
if idade <= 9:
    print('Este atleta se encontra na categoria MIRIM.\nCrianças de até 9 anos.')
elif idade >= 10 and idade <= 14:
    print('Este atleta se encontra na categoria INFANTIL.\nCrianças de 10 a 14 anos.')
elif idade >= 15 and idade <= 19:
    print('Este atleta se encontra na categoria JUNIOR.\nDe 15 a 19 anos.')
elif idade == 20:
    print('Este atleta se encontra na categoria SÊNIOR.\n20 anos.')
else:
    print('Este atleta se encontra na categoria MASTER.\nAcima de 20 anos.')
