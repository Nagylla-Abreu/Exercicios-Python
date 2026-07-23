"""
Escreva um programa utilizando if que, dada a idade de um nadador, o classifique
em uma das seguintes categorias e, caso a idade inserida seja inferior a 5 anos, mostre
um aviso de "idade inválida".

Infantil A - 5 a 7
Infantil B - 8 a 10
Juvenil A - 11 a 13
Junvenil B - 14 a 17
Senior 18+
"""

idade = int(input('Insira a idade do nadador: '))

if idade >= 5 and idade <= 7:
    print('O nadador pertence a categoria Infantil A.')
elif idade >= 8 and idade <= 10:
    print('O nadador pertence a categoria Infantil B.')
elif idade >= 11 and idade <= 13:
    print('O nadador pertence a categoria Juvenil A.')
elif idade >= 14 and idade <= 17:
    print('O nadador pertence a categoria Juvenil B.')
elif idade >= 18:
    print('O nadador pertence a categoria Sênior.')
else:
    print('Idade inválida.')