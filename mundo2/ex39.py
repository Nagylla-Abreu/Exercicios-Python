from datetime import datetime
ano = int(input('Ano de nascimento: '))

anoatual = datetime.now().year
idade = anoatual - ano


print(f'Quem nasceu em {ano} tem {idade} anos em {anoatual}.')

if idade > 18:
    saldo = idade - 18
    print(f'Você deveria ter se alistado há {saldo} anos.')
    print(f'Seu alistamento foi em {anoatual - saldo}.')
elif idade < 18:
    saldo = 18 - idade
    print(f'Ainda falta(m) {saldo} ano(s) para o alistamento.')
    print(f'Seu alistamento será em {anoatual + saldo}.')
else:
    print('Você tem que se alistar IMEDIATAMENTE!')