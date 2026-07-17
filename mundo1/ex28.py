import random
from time import sleep

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)

num = int(input('Em que número eu pensei? '))

print('PROCESSANDO...')
sleep(2)

nums = [0, 1, 2, 3, 4, 5]
numrand = random.choice(nums)

if num == numrand:
    print('PARABÉNS! Você adivinhou o número!')
else:
    print(f'GANHEI! Eu pensei no número {numrand} e não em {num}')