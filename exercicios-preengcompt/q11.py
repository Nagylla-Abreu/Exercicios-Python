"""
Faça um programa para ler um número inteiro. Imprima a mensagem "positivo" se
o valor for positivo. Imprima a mensagem "negativo" caso o valor seja negativo.
Imprima a mensagem "nulo" se o valor for zero.
"""

valor = int(input('Insira um número inteiro positivo ou negativo: '))

if valor > 0:
    print(f'O número {valor} é positivo.')
elif valor < 0:
    print(f'O número {valor} é negativo.')
else:
    print(f'O número {valor} é nulo.')