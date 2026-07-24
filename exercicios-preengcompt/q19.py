"""

Faça um programa que leia um número inteiro N e depois imprima os números
naturais ímpares até número digitado.

"""

i = 1
N = int(input('Digite um número inteiro positivo: '))

while i <= N:
    if i % 2 != 0:
        print(i)
    i += 1