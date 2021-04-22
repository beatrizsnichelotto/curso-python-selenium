
# IF = SE
# "Pai, você comprou pão"
# Resposta == sim ou == não
# Se comprou, ele vai agradecer
# Se não comprou, ele vai chorar
# ELIF = else if - Se não, outra coisa
# ELSE = se não, sem resposta


resposta = input ('Pai, você comprou pão?      ')

if resposta == 'sim':
    print ('Obrigado Pai')

elif resposta == 'nao':
    print ('Chorando')

else:
    print('Não foi o que eu perguntei')