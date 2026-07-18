soma = 0
for c in range(3, 501, 3):
    if c % 2 != 0:
        soma = soma + c
print(f'{soma}')