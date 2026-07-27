contador = 0
soma = 0
while True:
    num = int(input('Digite um valor [999 para parar]: '))   
    if num == 999:
        break   
    soma += num
    contador += 1 
print(f'A soma dos {contador} valores foi {soma}!')