# será mantido os nomes das variáveis apesar de serem confusos...

print('-' * 25)
print('Sequência de Fibonacci')
print('-' * 25)

qtd = int(input('Quantos termos quer mostrar? '))

i = 0
n1 = 0
n2 = 1

print('~~~' * 15)
while i < qtd:
    print(f'{n1} → ', end='')
    result = n2 + n1
    n1 = n2    
    n2 = result                  
    i+=1
print('FIM')
print('~~~' * 15)

