nome = str(input('Digite seu nome completo: ')).strip()
divisao = nome.split()
print (f'Seu primeiro nome é: {divisao[0]}')
print ('Seu último nome é: {}'.format(divisao[len(divisao)-1]))