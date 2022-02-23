nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
if media < 5.0:
    print(f'Sua média final: {media}\nSituação final: REPROVADO') #\n pula para a linha de baixo
elif media >= 5.0 and media <= 6.9:
    print(f'Sua média final: {media}\nSituação final: EM PROVA FINAL')
elif media >= 7.0:
    print(f'Sua média final: {media}\nSituação final: APROVADO\nMeus parabéns!')