perg = 'S'
soma = 0
cont = 0


num = int(input('Digite um número: '))
maior = num
menor = num
soma += num
cont+=1

while perg != 'N':
    perg = str(input('Quer continuar? [S/N] ')).upper()                   
    if perg == 'S':
        num = int(input('Digite um número: '))

        if num > maior:
            maior = num
        elif num < menor:
            menor = num
            
        soma += num
        cont+=1
        
media = soma / cont
print(f'Você digitou {cont} números e a média foi {media:.2f}')
print(f'O maior valor foi {maior} e o menor foi {menor}')



