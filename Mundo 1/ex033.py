primeiro = int(input('Digite o primeiro valor: '))
segundo = int(input('Digite o segundo valor: '))
terceiro = int(input('Digite o terceiro valor: '))
# verificando o maior
if primeiro > segundo and primeiro > terceiro:
    print (f'O maior valor é o {primeiro}.')
if segundo > primeiro and segundo > terceiro:
    print (f'O maior valor é o {segundo}.')
if terceiro > primeiro and terceiro > segundo:
    print (f'O maior valor é o {terceiro}.')
# verificando o menor
if primeiro < segundo and primeiro < terceiro:
    print (f'O menor valor é o {primeiro}.')
if segundo < primeiro and segundo < terceiro:
    print (f'O menor valor é o {segundo}.')
if terceiro < primeiro and terceiro < segundo:
    print (f'O menor valor é o {terceiro}.')
