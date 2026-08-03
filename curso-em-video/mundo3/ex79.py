lista = []

while True:
    valor = (int(input('Digite um valor: ')))

    if valor in lista:
        print('Valor duplicado! Não vou adicionar...')
    else:  
        print('Valor adicionado com sucesso...')
        lista.append(valor)

    decisao = str(input('Quer continuar? [S/N] ')).upper()

    if decisao == 'N':
        break

print(f'Você digitou os valores {sorted(lista)}')