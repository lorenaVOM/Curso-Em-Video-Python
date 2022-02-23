nome = str(input('Digite seu nome completo: ')).strip() # strip retira os espaços indesejados
print ('Estamos analisando seu nome...')
print (f'Seu nome, em letras maiúsculas, é: {nome.upper()}')
print (f'Seu nome, em minúsculas minúsculas, é {nome.lower()}')
print (f'Seu nome tem ao todo {len(nome.strip())} letras.') # len faz a contagem de caraceteres
separa = nome.split() # split separa as palavras em lista
print (f'Seu primeiro nome, {separa[0]}, tem {len(separa[0])} letras.')




