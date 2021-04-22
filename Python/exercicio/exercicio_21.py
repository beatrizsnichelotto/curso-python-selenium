
def quadrado(lista_de_numeros):
    lista_resposta = []
    for numero in lista_de_numeros:
        lista_resposta.append(numero ** 2)

    return lista_resposta

def cubo(lista_de_numeros):
    lista_resposta = []
    for numero in lista_de_numeros:
        lista_resposta.append(numero ** 3)

    return lista_resposta

lista_valores = []

for valor in range(10):
    lista_valores.append(
        int(input('Digite um numero:    '))
        )

dicionario = {
    'lista padrao' : lista_valores,
    'lista quadrada' : quadrado(lista_valores),
    'lista cúbica': cubo(lista_valores)
}

print(dicionario)