#3 - Faça um Programa que leia dois vetores com 10 elementos cada.
#Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.

def intercalar_vetores(vetor1, vetor2):
    vetor_intercalado = []

    for elemento1, elemento2 in zip(vetor1, vetor2):
        vetor_intercalado.extend([elemento1, elemento2])

    return vetor_intercalado

def ler_vetor(tamanho):
    vetor = [int(input(f"Digite o elemento {i+1}: ")) for i in range(tamanho)]
    return vetor

vetor1 = ler_vetor(5)
vetor2 = ler_vetor(5)

vetor_intercalado = intercalar_vetores(vetor1, vetor2)
print("\nVetor intercalado:")
print(vetor_intercalado)
