import random

def start():
    print("Bem vindo ao jogo de adivinhação!")
    print()
    print("Escolha o nível de dificuldade:")
    print("[1] Bebe chorão (Fácil) [2] QI elevado (Normal) [3] Akinator (Difícil)")
    print()

    level = int(input("Digite o número do nível: "))
    level_is_easy = level == 1
    level_is_normal = level == 2

    if (level_is_easy):
        print("Modo de jogo selecionado: Fácil")
        total_attempts = 5
        max_range = 10
    elif (level_is_normal):
        print("Modo de jogo selecionado: Normal")
        total_attempts = 7
        max_range = 100
    else:
        print("Modo de jogo selecionado: Difícil")
        total_attempts = 10
        max_range = 150

    secret_number = random.randrange(1, max_range + 1)
    points = 1000

    for current_game_round in range(1, total_attempts + 1):
        print()
        print("********* Rodada {} de {} *********".format(current_game_round, total_attempts))

        user_guess = int(input("Digite um número entre 1 e {}: ".format(max_range)))
        user_guess_is_greater_than_max_range = user_guess > max_range
        user_guess_is_less_than_min_range = user_guess < 1
        user_guess_is_correct = secret_number == user_guess
        user_guess_is_greater = user_guess > secret_number

        if (user_guess_is_greater_than_max_range or user_guess_is_less_than_min_range):
            continue

        if (user_guess_is_correct):
            print("Você acertou!")
            break
        else:
            print("Você errou!")

            if (user_guess_is_greater):
                print("Dica: o seu palpite é maior que o número secreto")
            else:
                print("Dica: o seu palpite é menor que o número secreto")

            lost_points = abs(user_guess - secret_number)
            points = points - lost_points

    print()
    print("Você fez {} pontos".format(points))
    print("Fim do jogo")

if (__name__ == "__main__"):
    start()
