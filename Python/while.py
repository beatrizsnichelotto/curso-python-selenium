# while = Enquanto
# Break = Parar

resposta = input ('Vamos sair hoje [s/n]?? ')

n = 1

while resposta != 's':
    resposta = input (f'Vamo{"o" * n} [s/n]?? ')
    n += 1
    if 'chato' in resposta or 'chata' in resposta:
        print('Sorry')
        break

else:
    print('Lets go')

