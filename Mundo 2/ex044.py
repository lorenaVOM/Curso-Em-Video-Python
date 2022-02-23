print(f'{"LOJAS GUANABARA":=^40}') #centraliza a frase em 40 =
valor = float(input('Digite o valor total da sua compra: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] À vista com dinheiro/cheque
[ 2 ] À vista com cartão
[ 3 ] 2x SEM juros no cartão
[ 4 ] 3x ou mais no cartão''')
res = int(input('Qual opção deseja selecionar? '))
certeza = str(input(f'Você selecionou a opção [ {res} ]. Deseja prosseguir para o pagamento? '))
if certeza == 'não' or certeza == 'nao':
    res2 = int(input('Qual opção deseja selecionar? '))
    if res2 == 1:
        print(f'Sua compra de R${valor:.2f} sairá por R${valor - (valor * (10 / 100)):.2f}.\nVocê será transferido para a página de pagamento em um momento.\nObrigado por comprar conosco! Volte sempre!')
    elif res2 == 2:
        print(f'Sua compra de R${valor:.2f} sairá por R${valor - (valor * (5 / 100)):.2f}.\nVocê será transferido para a página de pagamento em um momento.\nObrigado por comprar conosco! Volte sempre!')
    elif res2 == 3:
        print(f'Sua compra foi no valor de R${valor:.2f}.\nVocê será transferido para a página de pagamento em um momento.\nObrigado por comprar conosco! Volte sempre!')
    elif res2 == 4:
        print(f'Sua compra de R${valor:.2f}, com juros, sairá por R${valor + (valor * (20 / 100))}.\nVocê será transferido para a página de pagamento em um momento.\nObrigado por comprar conosco! Volte sempre!')
else:
    if res == 1:
        print(f'Sua compra de R${valor:.2f} sairá por R${valor - (valor * (10 / 100)):.2f}.\nVocê será transferido para a página de pagamento em um momento.\nObrigado por comprar conosco! Volte sempre!')
    elif res == 2:
        print(f'Sua compra de R${valor:.2f} sairá por R${valor - (valor * (5 / 100)):.2f}.\nVocê será transferido para a página de pagamento em um momento.\nObrigado por comprar conosco! Volte sempre!')
    elif res == 3:
        print(f'Sua compra foi no valor de R${valor:.2f}.\nVocê será transferido para a página de pagamento em um momento.\nObrigado por comprar conosco! Volte sempre!')
    elif res == 4:
        print(f'Sua compra de R${valor:.2f}, com juros, sairá por R${valor + (valor * (20 / 100))}.\nVocê será transferido para a página de pagamento em um momento.\nObrigado por comprar conosco! Volte sempre!')
