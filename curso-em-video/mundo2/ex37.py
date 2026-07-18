num = int(input('Insira um número qualquer: '))

print('''Selecione qual será a base para conversão:
[1] Binário
[2] Octal
[3] Hexadecimal''')
escolha = int(input('Sua opção: '))

if escolha == 1:
    print(f'{num} convertido para BINÁRIO é igual a {bin(num)[2:]}')
elif escolha == 2:
    print(f'{num} convertido para OCTAL é igual a {oct(num)[2:]}')
elif escolha == 3:
    print(f'{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}')
else:
    print('Escolha inválida!')