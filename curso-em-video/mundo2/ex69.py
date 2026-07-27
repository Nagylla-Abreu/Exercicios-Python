totalhomens = 0
totalmaiores = 0
mulhermenor = 0

while True:
    print('--' * 15)
    print('CADASTRE UMA PESSOA')
    print('--' * 15)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()
    print('--' * 15)
    decisao = str(input('Quer continuar? [S/N] ')).upper()
    if idade > 18:
        totalmaiores += 1
    if sexo == 'M':
        totalhomens += 1
    if sexo == 'F' and idade < 20:
        mulhermenor += 1
    if decisao == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {totalmaiores}')
print(f'Ao todo temos {totalhomens} homem(ns) cadastrado(s)')
print(f'E temos {mulhermenor} mulher(es) com menos de 20 anos')

