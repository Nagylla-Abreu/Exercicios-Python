print('--' * 18)
print('\tLOJA SUPER BARATÃO')
print('--' * 18)

menor = 0
barato = ''
total = 0
totalmil = 0
decisao = 'S'

produto = str(input('Nome do Produto: '))
preco = float(input('Preço: R$'))
total += preco
menor = preco
barato = produto

if preco >= 1000:
    totalmil += 1

while True:
    decisao = str(input('Quer continuar? [S/N] ')).upper()   
    if decisao == 'N':
        break
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))
    total += preco
        
    if preco < menor:
        menor = preco
        barato = produto

    if preco >= 1000:
        totalmil += 1

print('------ FIM DO PROGRAMA ------')
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totalmil} produto(s) custando mais de R$1000.00')
print(f'O produto mais barato foi {barato} e custa R${menor:.2f}')


