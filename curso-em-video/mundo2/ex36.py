casa = float(input('Qual o valor da casa? '))
salario = float(input('Qual o seu salário? '))
anos = float(input('Em quantos anos você pretende pagar a casa? '))

prestacao = casa / (anos*12)
porc = salario * 0.3

print(f'Para pagar uma casa de R${casa:.2f} em {anos:.0f} anos a prestação será de R${prestacao:.2f}')

if prestacao <= porc:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')