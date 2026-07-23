valor = float(input('Insira o valor de uma unidade da peça que você deseja comprar: R$'))
qtd = int(input('Insira a quantidade de peças que você deseja: '))
total = valor * qtd
valorfinal = total - (total * 0.12)
print(f'O valor total da sua compra é de R${total:.1f}. Com o desconto de 12%, sua compra vai ficar R${valorfinal:.1f}.')
