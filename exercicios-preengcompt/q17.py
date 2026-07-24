salario = float(input('Insira o valor do salário: '))

if salario <= 900:
    print('Você está Isento!')
elif salario > 900 and salario <= 1500:
    desconto = salario * 0.08
    salariodesc = salario - desconto
    print(f'Será descontado R${desconto:.2f} do seu salário. Você vai receber {salariodesc:.2f}')
elif salario > 1500 and salario <= 2500:
    desconto = salario * 0.10
    salariodesc = salario - desconto
    print(f'Será descontado R${desconto:.2f} do seu salário. Você vai receber {salariodesc:.2f}')
else:
    desconto = salario * 0.12
    salariodesc = salario - desconto
    print(f'Será descontado R${desconto:.2f} do seu salário. Você vai receber {salariodesc:.2f}')


