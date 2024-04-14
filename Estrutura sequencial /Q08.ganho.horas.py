#8-) Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

print ("Cálculo do salário")
ganhoPorHora = float(input("Ganho por hora: "))
horasTrabalhadas = float(input("Horas trabalhadas: "))

salario = ganhoPorHora * horasTrabalhadas
print (f"Seu salário é de R${salario}")
