palavra = 'abracadabra'
vogais = 'aeiou'


#for letra in palavra:
#    if letra == 'a':
#        print('Bea')
#    elif letra == 'e':
#        print('Bea')
#    elif letra == 'i':
#        print('Bea')
#    elif letra == 'o':
#        print('Bea')
#    elif letra == 'u':
#        print('Bea')
#    else:
#       print(letra)

for letra in palavra:
    if letra in vogais:
        print('Bea')
    else:
        print(letra)        

