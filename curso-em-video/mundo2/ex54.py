# fazer um for perguntando 7 vezes
# importar datetime do ano de hoje
# if para checar se a idade da pessoa, em razão do ano atual é >= 18
# se sim, adicionar +1 para soma de maiores
# se nao, adicionar +1 para soma de menores

from datetime import date

ano_atual = date.today().year
maioridade = 0
minoridade = 0

for i in range(1, 8):
    anonasc = int(input(f'Em que ano a {i}ª pessoa nasceu? '))
    if ano_atual - anonasc >= 18:
        maioridade += 1
    else:
        minoridade += 1
print(f'Ao todo tivemos {maioridade} pessoas maiores de idade')
print(f'E também tivemos {minoridade} pessoas menores de idade')