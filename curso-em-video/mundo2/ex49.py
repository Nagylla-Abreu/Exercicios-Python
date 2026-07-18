n = int(input('Escolha um número para ver a tabuada: '))
print('-=-' * 10)
print(f'TABUADA DO {n}')
for c in range(0, 11):
    mult = n * c
    print(f'{n} x {c} = {mult}')
print('-=-' * 10)