nome = str(input('Digite seu nome completo: ').strip ())
divisao = nome.upper().split()
print ('Seu nome tem Silva? {}'.format('SILVA' in divisao))
