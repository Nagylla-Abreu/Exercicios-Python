# variaveis maior e menor vão receber o primeiro valor logo de cara
# for para ler o peso de 5 pessoas
# if para fazer checagem e atualizar qual o novo maior e maior peso

peso = float(input('Peso da 1ª pessoa: '))

maior = peso
menor = peso

for i in range(2, 6):
    peso = float(input(f'Peso da {i}ª pessoa: '))
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print(f'O maior peso lido foi de {maior}Kg.')
print(f'O menor peso lido foi de {menor}Kg.')