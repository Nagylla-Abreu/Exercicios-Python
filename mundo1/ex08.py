dist = float(input('Uma distância em metros: '))

print(f'A medida de {dist}m corresponde a')
print(f'{dist/1000}km')
print(f'{dist/100}hm')
print(f'{dist/10}dam')
print(f'{dist*10:.0f}dm')
print(f'{dist*100:.0f}cm')
print(f'{dist*1000:.0f}mm')