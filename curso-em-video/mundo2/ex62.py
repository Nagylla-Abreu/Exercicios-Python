print('Gerador de PA')
print('=-=' * 5)
termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))

i = 0
cont = 10
qtd = 10

while cont != 0:
    while i < cont:
        print(f'{termo} → ', end='')
        termo += razao
        i+=1
    print('PAUSA')
    i = 0
    cont = int(input('Quantos termos você quer mostrar a mais? '))
    qtd += cont
print(f'Progressão finalizada com {qtd} termos mostrados.')



