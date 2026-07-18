nome = input('Digite seu nome completo: ')
print('Muito prazer em te conhecer!')

nomediv = nome.split()

primeiro = nomediv[0]
ultimo = nomediv[-1]

print(f'Seu primeiro nome é {primeiro}') 
print(f'Seu último nome é {ultimo}')
