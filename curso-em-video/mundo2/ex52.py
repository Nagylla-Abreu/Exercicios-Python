num = int(input('Insira um número inteiro: '))
divisoes = 0
for i in range(1, num+1):
    if num % i == 0:
        divisoes += 1
print(f'O número {num} foi divisível {divisoes} vezes')
if divisoes == 2:
    print('O número É PRIMO!')
else:
    print('E por isso o número NÃO É PRIMO!')