numeros= []
for i in range(10):
    numero=int(input(f"Digite um numero {i+1}: "))
    numeros.append(numero)

numero_busa = int(input("/n Digite um número para verificar quantas  vez aparece: "))
quantidade = numeros.count(numero_busa)

print(f"/nO numero {numero_busa} aprace {quantidade} vezes no vetor.")