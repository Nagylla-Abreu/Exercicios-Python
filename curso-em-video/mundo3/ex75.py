v1 = int(input('Digite um número: '))
v2 = int(input('Digite outro número: ')) 
v3 = int(input('Digite mais um número: '))
v4 = int(input('Digite o último número: '))

tupla = (v1, v2, v3, v4)
qtdnove = 0
posicao = 0
par = 0

print(f'Você digitou os númeoros {tupla}')

for c in range(4):
    if tupla[c] == 9:
        qtdnove += 1
print(f'O valor 9 apareceu {qtdnove} vezes')

if 3 in tupla:
    posicao = tupla.index(3)
    print(f'O valor 3 aparece na {posicao+1}ª posição')
else:        
     print(f'O valor 3 não aparece')

print(f'Os valores pares são ', end='')
for c in range(4):
    if tupla[c] % 2 == 0:
        par = tupla[c]
        print(f'{par} ', end='')


