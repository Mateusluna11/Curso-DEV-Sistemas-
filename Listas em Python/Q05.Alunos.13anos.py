#5 - Foram anotadas as idades e alturas de 10 alunos.
#Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.

idades = []
alturas = []

for i in range(10):
  idade = int(input("Informe a idade do " + str(i + 1) + "º aluno: "))
  altura = float(input("Informe a altura do " + str(i + 1) + "º aluno (cm): "))
  idades.append(idade)
  alturas.append(altura)

media_altura = sum(alturas) / len(alturas)

alunos_acima_13_baixos = 0
for i in range(len(idades)):
  if idades[i] > 13 and alturas[i] < media_altura:
    alunos_acima_13_baixos += 1
