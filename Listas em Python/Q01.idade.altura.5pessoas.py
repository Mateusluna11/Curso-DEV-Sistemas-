#1 - Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor.
#Imprima a idade e a altura na ordem inversa a ordem lida

idades = []
alturas = []

for i in range(5):
  idade = int(input("Informe a idade da pessoa " + str(i + 1) + ": "))
  altura = float(input("Informe a altura da pessoa " + str(i + 1) + " (cm): "))
  idades.append(idade)
  alturas.append(altura)

print("\nIdades na ordem inversa:")
for i in range(len(idades) - 1, -1, -1):
  print(idades[i])

print("\nAlturas na ordem inversa:")
for i in range(len(alturas) - 1, -1, -1):
  print(alturas[i])
