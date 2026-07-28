numext = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

num = int(input('Digite um número entre 0 e 20: ')) 

while True:   
    if num <= 20:
            break
    elif num > 20 or num < 0:
        print('Tente novamente. ', end='')
        num = int(input('Digite um número entre 0 e 20: '))       
print(f'Você digitou o número {numext[num]}')

