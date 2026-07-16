num = int(input('Informe um número: '))
print(f'Analisando o número {num}...')

milhar = num // 1000
centena = (num // 100) % 10
dezena = (num // 10) % 10
unidade = num % 10

print(f'Unidade: {unidade}')
print(f'Dezena: {dezena}')
print(f'Centena: {centena}')
print(f'Milhar: {milhar}')
