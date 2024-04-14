#4- Faça um programa, utilizando Dicionários, que:
#1° Passo: Peça para o usuário inserir quatro coisas em uma “Caixa Misteriosa” .
#2° Passo: Peça para o usuário inserir um número.
#3° Passo: Mostre na tela o que foi inserido na posição do número inserido pelo usuário.

caixa_misteriosa = {}
for i in range(1, 5):
    item = input(f"Insira o {i} item na Caixa Misteriosa: ")
    caixa_misteriosa[i] = item

numero = int(input("Agora, insira um número de 1 a 4: "))

if numero in caixa_misteriosa:
    print(f"Na posição {numero} da Caixa Misteriosa, temos: {caixa_misteriosa[numero]}")
else:
    print("Número inválido. Por favor, insira um número de 1 a 4.")

