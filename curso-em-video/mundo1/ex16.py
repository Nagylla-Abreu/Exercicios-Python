import math
valor = float(input('Digite um valor: '))
arr = math.trunc(valor)
print(f'O valor digitado foi {valor} e a sua porção inteira é {arr}')

# não se usa floor pq haverá um arredondamento. mas com trunc ele irá preservar realmente apenas a parte inteira do número