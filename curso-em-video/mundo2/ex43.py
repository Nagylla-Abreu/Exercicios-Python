peso = float(input('Qual é seu peso? (Kg) '))
altura = float(input('Qual é sua altura? (m) '))

IMC = peso / (altura ** 2)

if IMC < 18.5:
    print(f'Seu IMC é de {IMC:.2f} e você está ABAIXO DO PESO normal')
elif IMC >= 18.5 and IMC < 25:
    print(f'Seu IMC é de {IMC:.2f} e você está no PESO IDEAL')
elif IMC >= 25 and IMC < 30:
    print(f'Seu IMC é de {IMC:.2f} e você está com SOBREPESO')
elif IMC >=30 and IMC < 40:
    print(f'Seu IMC é de {IMC:.2f} e você está com OBESIDADE')
else:
    print(f'Seu IMC é de {IMC:.2f} e você está com OBESIDADE MÓRBIDA')