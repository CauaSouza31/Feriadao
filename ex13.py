numeros = []

print("Digite 10 números inteiros:")
for i in range(10):
    num = int(input(f"Número {i+1}: "))
    numeros.append(num)

pares = []
for num in numeros:
    if num % 2 == 0:
        pares.append(num)

menor = numeros[0]
maior = numeros[0]

for num in numeros:
    if num < menor:
        menor = num
    if num > maior:
        maior = num

soma = 0
contador = 0
for num in numeros:
    soma += num
    contador += 1

media = soma / contador

maiores_que_media = 0
for num in numeros:
    if num > media:
        maiores_que_media += 1

print("\nNúmeros pares:", pares)
print(f"Menor valor: {menor}")
print(f"Maior valor: {maior}")
print(f"Quantidade de valores maiores que a média ({media:.2f}): {maiores_que_media}")
