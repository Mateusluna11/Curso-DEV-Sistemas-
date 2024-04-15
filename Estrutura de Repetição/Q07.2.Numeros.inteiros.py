#7 - Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

numeros_intervalo = list(range(num1 + 1, num2))
soma_intervalo = sum(numeros_intervalo)

print("Números no intervalo:", numeros_intervalo)
print("Soma dos números no intervalo:", soma_intervalo)
