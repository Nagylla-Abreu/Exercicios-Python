num = int(input('Digite um número para\ncalcular seu fatorial: '))

i = 1
fatorial = 1
nums = num

print(f'Calculando {num}! = ', end='')
while nums >= 1:    
    print(f'{nums}', end='')
    print(' x ' if nums > 1 else ' = ', end='')
    fatorial = fatorial * nums
    nums-=1    
print(fatorial)

