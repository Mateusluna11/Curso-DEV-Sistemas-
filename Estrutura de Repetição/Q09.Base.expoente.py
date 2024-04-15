#9 - Faça um programa que peça dois números, base e expoente

base = float(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))

resultado = 1
for _ in range(expoente):
    resultado *= base

print(f"{base} elevado a {expoente} é igual a {resultado}")
