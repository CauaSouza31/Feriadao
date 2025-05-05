N = int(input("Digite o tamanho dos vetores: "))

A = []
B = []
Soma = []

print("Digite os valores para o vetor A:")
for i in range(N):
    A.append(int(input(f"A[{i}]: ")))

print("Digite os valores para o vetor B:")
for i in range(N):
    B.append(int(input(f"B[{i}]: ")))

for i in range(N):
    Soma.append(A[i] + B[i])

print("\nVetor Soma:")
for i in range(N):
    print(f"Soma[{i}] = {Soma[i]}")