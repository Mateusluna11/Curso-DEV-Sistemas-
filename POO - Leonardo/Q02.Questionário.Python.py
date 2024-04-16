#Faça um Programa que exiba de 1 a 10
print("Números primos até", limite," ":)
for num in range(2, limite +1):
  if eh_primo(num):
    print (num)
elif comando.lower() == 'para':
    print("Programa encerrado!")
  break
else:
   try:
      numero = int(comando)
  if numero <= 0
      print("Por favor, digita um valor positivo maior que zero!")
else:
   for i in range(1, numero + 1):
     print(1)
except ValeuError:
  print("Entrada inválida. Por favor, digite 'p' para imprimir de 1 até 10, 'primo' para imprimir números primos até o valor fornecido.")
 def eh_primo(num):
   if num <= 1:
     return False
   for i in range (2, int(num ** 0.5) + 1):
     if num % i == 0
      return False 
return True

Wile True:
      comando = input("Digite 'p' para imprimir de 1 até 10,\nou digite um número para imprimir até esse valor.")
      if comando.lower() == 'p':
        for i in range(1, 11):
            print(i)
      elif comando.lower() == 'primo':
        limite = int(input("Digite o valor limite para imprimir os números primos: )
       print("Números primos até", limite, ":")
          for num in range(2, limite + 1)
                 if eh_primo(num) :
                      print(num)
          elif comando.lower() == 'parar':
              print("Programa encerrado!")
        break
else:

    try:
          numero = int(comando)
          if numero <= 0
               print("Por favor, digite um valor positivo maior que zero!")
