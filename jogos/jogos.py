import adivinhacao
import forca

print("====================")
print("   Escolha o jogo   ")
print("====================")

print("\n(1) Adivinhação (2) Forca")

jogo = int(input("Qual jogo? "))

if jogo == 1:
    adivinhacao.jogar()
elif jogo == 2:
    forca.jogar()

