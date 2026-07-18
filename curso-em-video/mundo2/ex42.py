l1 = float(input('Primeiro lado: '))
l2 = float(input('Segundo lado: '))
l3 = float(input('Terceiro lado: '))

if l1 < (l2 + l3) and l2 < (l1 + l3) and l3 < (l1 + l2):
    if l1 == l2 == l3:
        print('Os segmentos PODEM FORMAR um triângulo EQUILÁTERO.')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print('Os segmentos PODEM FORMAR um triângulo ISÓSCELES.')
    else:
        print('Os segmentos PODEM FORMAR um triângulo ESCALENO.')
else:
    print('Os segmentos NÃO podem formar um triângulo.')