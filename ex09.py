nomes = ["Ana", "Carlos", "Beatriz", "Lucas", "Mariana"]
senhas = ["1234", "senha123", "abcde", "xyz789", "mariana123"]

for i in range(5):
    nome = input(f"Digite o nome do usuário {i+1}: ")
    senha = input(f"Digite a senha do usuário {i+1}: ")
    nomes.append(nome)
    senhas.append(senha)

print("\n--- LOGIN ---")
senha_digitada = input("Digite sua senha: ")

if senha_digitada in senhas:
    indice = senhas.index(senha_digitada)
    print(f"Login efetuado com sucesso!Bem-vindo, {nomes[indice]}.")
else:
    print("Senha incorreta. Tente novamente.")