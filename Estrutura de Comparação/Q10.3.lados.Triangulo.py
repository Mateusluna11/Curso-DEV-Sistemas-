#10 - Faça um Programa que peça os 3 lados de um triângulo.

lado1 = float(input("Digite o comprimento do primeiro lado: "))
lado2 = float(input("Digite o comprimento do segundo lado: "))
lado3 = float(input("Digite o comprimento do terceiro lado: "))

if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    if lado1 == lado2 == lado3:
        print("Triângulo Equilátero.")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Triângulo Isósceles.")
    else:
        print("Triângulo Escaleno.")
else:
    print("Esses lados não formam um triângulo.")
