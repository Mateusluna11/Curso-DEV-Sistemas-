#10 - Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares.

numeros = [int(input(f"Digite o {i+1}º número: ")) for i in range(10)]

pares = sum(1 for num in numeros if num % 2 == 0)
impares = sum(1 for num in numeros if num % 2 != 0)

print("Quantidade de números pares:", pares)
print("Quantidade de números ímpares:", impares)
