numero = int(input("Digite um número inteiro: "))
fibonacci = [0, 1]
while fibonacci[-1] < numero:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

if fibonacci[-1] == numero:
    print(f"{numero} pertence à sequência de Fibonnacci.")
  
else:
    print(f"{numero} não pertence à sequência de Fibonnacci.")

print("A sequência de Fibonacci é: ", fibonacci)


