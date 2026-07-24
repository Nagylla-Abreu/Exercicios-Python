num = int(input('Insira um número inteiro: '))

primo = 1

for i in range(1, num):
    resto = num % i
    if resto == 0:
        primo = 0
        break

if primo == 1:
    print(f'{num} é primo')
else:
    print(f'{num} NÃO é primo')