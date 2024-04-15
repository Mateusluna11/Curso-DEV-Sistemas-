#4 - Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno apresentar

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2

print("Média:", media)

if media == 10:
    print("Aprovado com Distinção.")
elif media >= 7:
    print("Aprovado.")
else:
    print("Reprovado.")
