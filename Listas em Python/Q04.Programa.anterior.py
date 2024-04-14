#4 - Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.

def intercalar_vetores(vetor1, vetor2, vetor3):
    vetor_intercalado = []

    for elemento1, elemento2, elemento3 in zip(vetor1, vetor2, vetor3):
        vetor_intercalado.extend([elemento1, elemento2, elemento3])

    return vetor_intercalado

def ler_vetor(tamanho):
    vetor = [int(input(f"Digite o elemento {i+1}: ")) for i in range(tamanho)]
    return vetor

vetor1 = ler_vetor(5)
vetor2 = ler_vetor(5)
vetor3 = ler_vetor(5)

vetor_intercalado = intercalar_vetores(vetor1, vetor2, vetor3)
print("\nVetor intercalado:")
print(vetor_intercalado)
