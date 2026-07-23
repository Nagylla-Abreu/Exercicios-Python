# Escreva um programa em Python que recebe um inteiro e diga se é par ou ímpar.
# Use o operador matemático % (resto da divisão) e o teste condicional if.

num = int(input('Insira um número inteiro positivo: '))

if num % 2 == 0:
    print(f'{num} é par.')
else:
    print(f'{num} é ímpar.')