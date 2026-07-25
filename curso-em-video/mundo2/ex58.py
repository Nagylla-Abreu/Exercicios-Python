# o usuario vai digitar um numero entre 0 a 10
# usar comando random para o computador escolher um numero e guardar em um variável
# parametro if para checar se o numero q o usuario chutou é menor ou maior que o numero que a maquina pensou.
# a maquina tem que sinalizar se é mais ou menos
# sempre q o usuario tentar acerta e n conseguir, somar o número de tentativas.

import random

print('Sou seu computador...\nAcabei de pensar em um número de 0 a 10.\nSerá que você consegue adivinhar qual foi?')
palpite = int(input('Qual é seu palpite? '))

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
escolha_pc = random.choice(nums)

tentativas = 1

while palpite != escolha_pc:
    if escolha_pc > palpite:
        print(f'Mais... Tente mais uma vez.')
        palpite = int(input('Qual é seu palpite? '))
        tentativas += 1
    else:
        print(f'Menos... Tente mais uma vez.')
        palpite = int(input('Qual é seu palpite? '))
        tentativas += 1
print(f'Acertou com {tentativas} tentativa(s). Parabéns!')

