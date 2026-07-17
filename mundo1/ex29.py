v = int(input('Qual a velocidade atual do carro? '))

multa = float((v-80) * 7)

if v <= 80:
    print('Tenha um bom dia! Dirija com segurança!')
else:
    print(f'MULTADO! Você excedeu o limite permitido que é de 80Km/h\nVocê deve pagar uma multa de R${multa:.2f}!')