carteira = int(input('Quanto eu tenho?  '))
produto = int(input('Quanto custa?  '))
necessidade = input('Preciso mesmo disso[s/n]?  ')

if carteira >= produto and necessidade == 's':
    print('Eba, posso comprar!')
else:
    print('Poxa, deixa pro próximo mes!')