print('=' * 20)
print('10 TERMOS DE UMA PA')
print('=' * 20)

p1 = int(input('Insira o primeiro termo da sua PA: '))
razao = int(input('Insira a razão da sua PA: '))

termo = p1

for i in range(10):
    print(f'{termo} > ', end='')
    termo += razao
print('ACABOU')