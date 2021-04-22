# sum -> soma
# len -> tamanho

def soma(numero_1, numero_2):
    return numero_1 + numero_2

def media(lista_de_numeros):
   return sum(lista_de_numeros) / len(lista_de_numeros)

def imprime(nome, cpf, telefone):
    return f"""
    Relatório parcial

    {nome}, portador do cpf {cpf}, com telefone {telefone}

    Está oficialmente de férias.
    Ass, Direção.
    """   

    print(imprime('Beatriz Snichelotto', '10521587905', '45999628373'))