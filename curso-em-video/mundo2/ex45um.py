from time import sleep
import random

print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

escolhajog = int(input('Qual é a sua jogada? '))
jogadas = [0, 1, 2]
escolhacompt = random.choice(jogadas)

sleep(0.5)
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')

print('-=-' * 10)
if escolhacompt == 0:
    if escolhajog == 0:
        print(f'O computador jogou Pedra')
        print(f'Jogador jogou Pedra')
        print('-=-' * 10)
        print('EMPATE')
    elif escolhajog == 1:
        print(f'O computador jogou Pedra')
        print(f'Jogador jogou Papel')
        print('-=-' * 10)
        print('Jogador VENCE')
    elif escolhajog == 2:
        print(f'O computador jogou Pedra')
        print(f'Jogador jogou Tesoura')
        print('-=-' * 10)
        print('Computador VENCE')
if escolhacompt == 1:
    if escolhajog == 0:
        print(f'O computador jogou Papel')
        print(f'Jogador jogou Pedra')
        print('-=-' * 10)
        print('Jogador VENCE')
    elif escolhajog == 1:
        print(f'O computador jogou Papel')
        print(f'Jogador jogou Papel')
        print('-=-' * 10)
        print('EMPATE')
    elif escolhajog == 2:
        print(f'O computador jogou Papel')
        print(f'Jogador jogou Tesoura')
        print('-=-' * 10)
        print('Computador VENCE')
if escolhacompt == 2:
    if escolhajog == 0:
        print(f'O computador jogou Tesoura')
        print(f'Jogador jogou Pedra')
        print('-=-' * 10)
        print('Jogador VENCE')
    elif escolhajog == 1:
        print(f'O computador jogou Tesoura')
        print(f'Jogador jogou Papel')
        print('-=-' * 10)
        print('Computador VENCE')
    elif escolhajog == 2:
        print(f'O computador jogou Tesoura')
        print(f'Jogador jogou Tesoura')
        print('-=-' * 10)
        print('EMPATE')
    