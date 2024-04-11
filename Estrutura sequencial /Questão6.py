#6-)Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

import math

print('Descubra a área do círculo apenas com o raio!')
raio = float(input('Diga o valor do raio: '))
area = math.pi * (raio ** 2)
print(f"Área do círculo: {area:.2f}")
