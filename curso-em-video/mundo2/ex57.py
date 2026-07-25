sexo = str(input('Insira seu sexo: ')).upper()

while sexo != 'M' and sexo != 'F':
    sexo = str(input('Dados inválidos. Informe seu sexo [M/F]: ')).upper()
print(f'Sexo {sexo} registrado com sucesso.')