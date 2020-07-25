import guessing
import hangman

print("************ Menu ************")
print()
print("Escolha o jogo que quer jogar:")
print("[1] Adivinhação [2] Forca")
print()

selected_game = int(input("Digite o número do jogo: "))
selected_is_guessing = selected_game == 1

print("---------------------------------")

if (selected_is_guessing):
    guessing.start()
else:
    hangman.start()
