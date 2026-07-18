from time import sleep
import random

print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

escolhajog = int(input('Qual é a sua jogada? '))
jogadas = ['PEDRA', 'PAPEL', 'TESOURA']
escolhacompt = random.randint(0, 2)

sleep(0.5)
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')

print('-=-' * 10)

if escolhajog >= 0 and escolhajog <= 2:
    print(f'Computador jogou {jogadas[escolhacompt]}')
    print(f'Jogador jogou {jogadas[escolhajog]}')
    if escolhajog == escolhacompt:
        print('EMPATE')
    elif escolhajog == 0 and escolhacompt == 1:
        print('Jogador PERDE')
    elif escolhajog == 0 and escolhacompt == 2:
        print('Jogador GANHA')
    elif escolhajog == 1 and escolhacompt == 0:
        print('Jogador GANHA')
    elif escolhajog == 1 and escolhacompt == 2:
        print('Jogador PERDE')
    elif escolhajog == 2 and escolhacompt == 0:  
        print('Jogador PERDE')
    elif escolhajog == 2 and escolhacompt == 1:
        print('Jogador GANHA')
else:
    print('Jogada Inválida!')    

print('-=-' * 10)