# for para imprimir o questionário 4 vezes
# if e usar soma += mulheres_menores para mulheres menores de 20 anos
# if para verificar homem mais velho e armazenar sua idade e nome

total_idades = 0
mulheres_menores = 0

print(f'---- 1ª PESSOA ----')
nome = input('Nome: ')
idade = int(input('Idade: '))
sexo = input('Sexo [M/F]: ')
total_idades += idade

if sexo == 'M':
    mais_velho = nome
    maior = idade
if sexo == 'F':
    if idade < 20:
        mulheres_menores += 1
    

for i in range(2, 5):
    print(f'---- {i}ª PESSOA ----')
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ')
    total_idades += idade
    if sexo == 'M':
        if idade > maior:
            mais_velho = nome
            maior = idade
    if sexo == 'F':
        if idade < 20:
            mulheres_menores += 1
    
        
media = total_idades / 4
print(f'A média de idade do grupo é de {media} anos.')
print(f'O homem mais velho tem {maior} anos e se chama {mais_velho}.')
print(f'Ao todo são {mulheres_menores} mulheres com menos de 20 anos.')

