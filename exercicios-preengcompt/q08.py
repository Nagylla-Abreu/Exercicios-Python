#  A condição física de uma pessoa pode ser medida com base no cálculo do Índice de
#  Massa Corporal (IMC). O mesmo é calculado dividindo-se a massa dessa pessoa em
#  quilogramas pelo quadrado de sua altura em metros. Calcule e mostre o IMC. Se as
#  entradas fossem 70kg e 1,80m a saída seria aproximadamente 21,60

alt = float(input('Insira a sua altura em metros: '))
massa = float(input('Insira seu peso em quilos: '))
IMC = massa / (alt ** 2)
print(f'Seu IMC é igual a {IMC:.2f}')