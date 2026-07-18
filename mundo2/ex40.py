n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))

media = (n1 + n2) / 2

if media >= 7:
    print(f'Tirando {n1} e {n2}, a média do aluno é {media:.2f}')
    print('O aluno está APROVADO.')
elif media < 7 and media >= 5:
    print(f'Tirando {n1} e {n2}, a média do aluno é {media:.2f}')
    print('O aluno está de RECUPERAÇÃO.')
else:
    print(f'Tirando {n1} e {n2}, a média do aluno é {media:.2f}')
    print('O aluno está REPROVADO.')