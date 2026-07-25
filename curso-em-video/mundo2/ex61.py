print('Gerador de PA')
print('=-=' * 5)
termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))

i = 1

while i <= 10:
    print(f'{termo} → ', end='')
    termo = termo + razao
    i+=1
print('FIM')