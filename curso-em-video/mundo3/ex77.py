palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')

for i in range(len(palavras)):
    print(f'Na palavra {palavras[i]} temos ', end='')   
    if 'A' in palavras[i]:
        print('a ' * palavras[i].count('A'), end='')
    if 'E' in palavras[i]:
        print('e ' * palavras[i].count('E'), end='')
    if 'I' in palavras[i]:
        print('i ' * palavras[i].count('I'), end='')
    if 'O' in palavras[i]:
        print('o ' * palavras[i].count('O'), end='')
    if 'U' in palavras[i]:
        print('u ' * palavras[i].count('U'), end='')
    print(' ')