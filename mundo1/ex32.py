ano = int(input('Insira o ano que você está: '))

if ano % 4 == 0 and ano % 400 == 0:
    print(f'O ano {ano} é BISSEXTO.')
else:
    print(f'O ano {ano} NÃO é BISSEXTO.')