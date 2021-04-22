2 > 3 #falso
3 > 2 #true


type(True) #boolean
type(False) #boolean


#Compara se iguais ou diferentes

nome_1 = 'Fausto'
idade_1 = 5
nome_2 = 'Joao'
idade_2 = 7
nome_3 = 'Fausto'
idade_3 = 65


nome_1 == nome_2 #False

nome_1 == nome_2 #True

nome_1 != nome_2 #True

nome_1 != nome_3 #False


# Compara nome e idade com 'AND'

nome_1 == nome_3 and idade_1 == idade_3 #False (Mesmo tendo uma informação verdadeira, se uma for falsa retorna FALSE)
nome_1 == nome_3 and idade_1 == idade_1 #True (Ambas são verdadeiras)


# Compara nome e idade com 'OR'

nome_1 == nome_3 or idade_1 == idade_3 #True (Mesmo contendo uma informação falsa, retorna TRUE)


# Compara nome e idade com 'NOT'

not nome_1 == nome_3 # False (Mesmo sendo verdadeiro, com a expressão NOT na frente, traz resultado FALSE)












