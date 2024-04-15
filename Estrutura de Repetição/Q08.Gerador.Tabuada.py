#8 - Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10.

numero_tabuada = int(input("Digite um número para a tabuada: "))

print(f"Tabuada de {numero_tabuada}:")
for i in range(1, 11):
    resultado = numero_tabuada * i
  print(f"{numero_tabuada} X {i} = {resultado}")
