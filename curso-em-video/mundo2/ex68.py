# sempre q o jogador vencer, contar
# lista com os valores aleatorios de 1 a 10
# somar a escolha da maquina com a do jogador e fzr um if pra ver se é par ou impar
# analisar se o jogador escolheu par ou impar para comparação
# atribuir vencer = 1 e perder = 0 // nao foi necessario já que o while é true...

import random

print('=-' * 15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 15)

total = 0

while True:
    compt = random.randint(1, 10)
    jogador = int(input('Digite um valor: '))
    parimpar = str(input('Par ou Ímpar [P/I]: ')).upper()
    juncao = jogador + compt
    if parimpar == 'I' and juncao % 2 != 0:
        print('--' * 15)
        print(f'Você jogou {jogador} e o computador {compt}. Total de {juncao}')
        print('--' * 15)
        print('Você VENCEU!')
        print('Vamos jogar novamente...')  
        print('=-' * 15)      
        total += 1        
    elif parimpar == 'P'  and juncao % 2 == 0:
        print('--' * 15)
        print(f'Você jogou {jogador} e o computador {compt}. Total de {juncao}')
        print('--' * 15)
        print('Você VENCEU!')
        print('Vamos jogar novamente...')
        print('=-' * 15)
        total += 1
    else:
        break
print('--' * 15)
print(f'Você jogou {jogador} e o computador {compt}. Total de {juncao}')
print('--' * 15)
print('Você PERDEU!')
print('=-' * 15)
print(f'GAME OVER! Você venceu {total} vezes')

