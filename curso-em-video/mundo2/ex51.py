lop = 0
p1 = int(input('Insira o primeiro termo da sua PA: '))
razao = int(input('Insira a razão da sua PA: '))

for c in range(11):
    lop = c - 1
    for pa in range(p1, lop, razao):
        print(pa)