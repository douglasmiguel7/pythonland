import random


def show_welcome_message():
    print("Bem vindo ao jogo da forca!")
    print()


def get_secret_word():
    file = open("fruits.txt", mode="r", encoding="UTF-8")

    secret_words = []

    for line in file:
        line = line.upper()
        line = line.strip()
        secret_words.append(line)

    file.close()

    secret_word_number = random.randrange(0, len(secret_words))

    secret_word = secret_words[secret_word_number]

    return secret_word


def show_handman_state(amount_errors, correct_letters):
    if (amount_errors == 0):
        print("  _______   ")
        print(" |       !  ")
        print(" |          ")
        print(" |          ")
        print(" |          ")
        print(" |          ")
        print(" |          ")

    elif (amount_errors == 1):
        print("  _______   ")
        print(" |       !  ")
        print(" |      (_) ")
        print(" |          ")
        print(" |          ")
        print(" |          ")
        print(" |          ")

    elif (amount_errors == 2):
        print("  _______   ")
        print(" |       !  ")
        print(" |      (_) ")
        print(" |       |  ")
        print(" |       |  ")
        print(" |          ")
        print(" |          ")

    elif (amount_errors == 3):
        print("  _______   ")
        print(" |       !  ")
        print(" |      (_) ")
        print(" |      /|  ")
        print(" |       |  ")
        print(" |          ")
        print(" |          ")

    elif (amount_errors == 4):
        print("  _______   ")
        print(" |       !  ")
        print(" |      (_) ")
        print(" |      /|\ ")
        print(" |       |  ")
        print(" |          ")
        print(" |          ")

    elif (amount_errors == 5):
        print("  _______   ")
        print(" |       !  ")
        print(" |      (_) ")
        print(" |      /|\ ")
        print(" |       |  ")
        print(" |      /   ")
        print(" |          ")

    elif (amount_errors == 6):
        print("  _______   ")
        print(" |       !  ")
        print(" |      (_) ")
        print(" |      /|\ ")
        print(" |       |  ")
        print(" |      / \ ")
        print(" |          ")

    correct_word = ""

    for correct_letter in correct_letters:
        correct_word = correct_word + correct_letter + " "

    print(" | {}".format(correct_word))
    print()


def show_tip(secret_word):
    print("Dica: é uma fruta com {} letras".format(len(secret_word)))


def request_user_guess():
    user_guess = input("Digite uma letra: ")
    user_guess = user_guess.upper()
    print()

    return user_guess


def start():
    show_welcome_message()

    secret_word = get_secret_word()

    correct_letters = ["_" for secret_letter in secret_word]

    hanged = False
    won = False
    amount_errors = 0

    show_handman_state(amount_errors, correct_letters)

    while (not hanged and not won):
        show_tip(secret_word)

        user_guess = request_user_guess()

        if (not user_guess in secret_word):
            amount_errors = amount_errors + 1

        letter_position = 0
        for letter in secret_word:
            user_guess_is_correct = user_guess == letter

            if (user_guess_is_correct):
                correct_letters[letter_position] = letter

            letter_position = letter_position + 1

        show_handman_state(amount_errors, correct_letters)

        won = not "_" in correct_letters
        hanged = amount_errors == 6

    if (won):
        print("Você venceu!")
    elif (hanged):
        print("Você perdeu!")

    print("Fim do jogo")


if (__name__ == "__main__"):
    start()
