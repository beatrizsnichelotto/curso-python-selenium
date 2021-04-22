lista_compras = []
resposta = ''

while resposta != 'acabou':
    resposta = input('O que temos que comprar? ')
    if resposta != 'acabou':
        lista_compras.append(resposta)
    
print(lista_compras)