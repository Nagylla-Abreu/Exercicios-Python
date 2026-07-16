import math

angg = float(input('Digite um ângulo que você deseja: '))

angr = math.radians(angg) #tem q converter graus em radianos

sen = math.sin(angr)
cos = math.cos(angr)
tg = math.tan(angr)

print(f'O ângulo de {angg} tem o SENO de {sen:.2f}')
print(f'O ângulo de {angg} tem o COSSENO de {cos:.2f}')
print(f'O ângulo de {angg} tem a TANGENTE de {tg:.2f}')

