PP = int(input('Posição da porta P(0 ou 1): '))
RR = int(input('Posição da porta R(0 ou 1): '))

if PP == 0:
    caminho = 'C'
elif PP == 1 and RR == 0:
    caminho = 'B'
else:
    caminho = 'A'

print(f'A sua bolinha caiu no caminho {caminho}!')