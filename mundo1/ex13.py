salario = float(input('Qual é o salário do Funcionário? R$'))

aumento = salario * 0.15
salariofinal = salario + aumento

print(f'Um funcionário que ganhava R${salario}, com 15% de aumento, passa a receber R${salariofinal:.2f}')