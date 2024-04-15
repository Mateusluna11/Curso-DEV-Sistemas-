#2 - Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

GENERO = input("Digite uma letra (F/M): ").upper()
if GENERO == 'F':
    print("Feminino.")
elif GENERO == 'M':
    print("Masculino.")
else:
    print("Sexo Inválido.")
