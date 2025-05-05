palavra = "python"
tentativas = 6
letras_adivinhadas = []
palavra_oculta = ["_" for _ in palavra]

print("Bem-vindo ao Jogo da Forca!")

while tentativas > 0:
    print("\nPalavra:", " ".join(palavra_oculta))
    print("Tentativas restantes:", tentativas)

    letra = input("Digite uma letra: ").lower()

    if letra in letras_adivinhadas:
        print("Você já tentou essa letra. Tente outra.")
        continue

    letras_adivinhadas.append(letra)

    acertou = False
    for i in range(len(palavra)):
        if palavra[i] == letra:
            palavra_oculta[i] = letra
            acertou = True

    if acertou:
        print("Boa! Você acertou uma letra.")
    else:
        tentativas -= 1
        print("Letra incorreta!")

    if "_" not in palavra_oculta:
        print("\nParabéns! Você adivinhou a palavra:", palavra)
        break

if tentativas == 0:
    print("\nVocê perdeu! A palavra era:", palavra)