nomes = []

print("Digite 5 nomes:")
for i in range(5):
    nome = input(f"Nome {i+1}: ")
    nomes.append(nome)

print("\nLista de nomes:")
for nome in nomes:
    print(nome)

print("\nLista de nomes na ordem inversa:")
for nome in reversed(nomes):
    print(nome)
