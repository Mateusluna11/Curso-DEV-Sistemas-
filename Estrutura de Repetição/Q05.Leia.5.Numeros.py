#5 - Faça um programa que leia 5 números e informe a soma e a média dos números.

numeros = [float(input(f"Digite o {i+1}º número: ")) for i in range(5)]
soma = sum(numeros)
media = soma / len(numeros)
print("Soma:", soma)
print("Média:", media)

