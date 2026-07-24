"""
Faça um Programa que peça um número correspondente a um
determinado ano e em seguida informe se este ano é ou não bissexto.
"""

# o ano tem que ser divisivel por 4
# se terminar com 00 TAMBEM tem q ser divisivel por 400

ano = int(input('Insira um ano para verificar se ele é bissexto: '))

if ano % 4 == 0 and ano % 100 != 0:
    print(f'O ano de {ano} é BISSEXTO.')
elif ano % 4 == 0 and ano % 400 == 0:
    print(f'O ano de {ano} é BISSEXTO.')
else:
    print(f'O ano de {ano} NÃO é bissexto.')