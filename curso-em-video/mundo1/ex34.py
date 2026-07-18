salario = float(input('Qual é o salário do funcionário? R$'))

if salario <= 1250:
    novo = (salario * 0.15) + salario
else:
    novo = (salario * 0.10) + salario

print(f'Quem ganhava R${salario} passa a ganhar R${novo:.2f} agora.')