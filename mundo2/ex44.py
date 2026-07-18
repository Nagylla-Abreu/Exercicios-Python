print('======== LOJAS NAJOLA ========')

preco = float(input('Preço das compras: R$'))

print('FORMAS DE PAGAMENTO')
print('''[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
opcao = int(input('Qual é a opção? '))

if opcao == 1:
    valornovo = preco - (preco * 0.1)
if opcao == 2:
    valornovo = preco - (preco * 0.05)
if opcao == 3:
    valornovo = preco
    qtd = valornovo / 2
    print(f'Sua compra será parcelada em 2x de R${qtd:.2f} COM JUROS')
if opcao == 4:
    parcela = int(input('Quantas parcelas? '))
    valornovo = preco + (preco * 0.2)
    qtd = valornovo / parcela
    print(f'Sua compra será parcelada em {parcela}x de R${qtd:.2f} COM JUROS')

print(f'Sua compra de R${preco} vai custar R${valornovo:.2f} no final.')