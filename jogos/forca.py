def jogar():
    print('=================================')
    print('   Bem vindo ao jogo da forca!   ')
    print('=================================')

    palavra_secreta = "banana".upper()
    letras_certas = ["_", "_", "_", "_", "_", "_"]
    enforcou = False
    ganhou   = False
    erros    = 0

    print(letras_certas)

    while not enforcou and not ganhou:
        chute = input("Qual letra? ").strip().upper()
        index = 0

        if chute not in palavra_secreta:
            erros += 1
        else:
            for letra in palavra_secreta:  # Loop para iterar a string
                if chute == letra:
                    letras_certas[index] = letra
                index += 1  # Acrescenta uma posição no index para cada letra

        enforcou = erros == 6
        print(letras_certas)

    print("Fim de jogo")

if __name__ == "__main__":
    jogar()
