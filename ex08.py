nomes = []
senhas = []

for i in range(5):
    nome=input(f"Digite o nome do usuario {i+1}:")
    senha=input(f"Digite a senha do usuario {i+1}:")
    nomes.append(nome)
    senhas.append(senha)

print("/n Dados armazenados:")
for i in range(5):
    print(f"Posição {i}: Nome - {nomes[i]}, Senha - {senhas[i]}")