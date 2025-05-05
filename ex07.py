numeros=[]
for i in range(5):
    num=int(input(f"Digite o {i+1}º número: "))
    numeros.append(num)

print("numros na ordem inversa: ")
for i in range(len(numeros)-4,-1,-1):
    print(numeros[i])
