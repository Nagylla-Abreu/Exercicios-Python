valores = []

for i in range(0, 5):
    valores.append(int(input(f'Digite um valor na posição {i}: ')))

print(f'Você digitou os valores {valores}')

maior = max(valores)
print(f'O maior digitado encontrado foi {maior} nas posições ', end='')
for pos, valor in enumerate(valores):
    if valor == maior:
        print(f'{pos}... ', end='')

menor = min(valores)
print(f'\nO menor digitado encontrado foi {menor} nas posições ', end='')
for pos, valor in enumerate(valores):
    if valor == menor:
        print(f'{pos}... ', end='')