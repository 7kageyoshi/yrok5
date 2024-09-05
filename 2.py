import random


def rock_paper_scissors():
    player = int(input("1 - камень, 2 - ножницы, 3 - бумага. Введите ваш выбор: "))
    computer = random.randint(1, 3)

    if player == computer:
        print("Ничья!")
    elif (
        (player == 1 and computer == 2)
        or (player == 2 and computer == 3)
        or (player == 3 and computer == 1)
    ):
        print("Вы выиграли!")
    else:
        print("Вы проиграли!")


def guess_the_number():
    number = random.randint(1, 100)
    while True:
        guess_num = int(input("Введите число: "))
        if guess_num > number:
            print("Число больше, чем нужно. Попробуйте ещё раз!")
        elif guess_num < number:
            print("Число меньше, чем нужно. Попробуйте ещё раз!")
        else:
            print("Поздравляю, вы угадали!")
            break


def main_menu():
    while True:
        game = int(input("1 - Камень, ножницы, бумага; 2 - Угадай число; 3 - Выйти: "))
        if game == 1:
            rock_paper_scissors()
        elif game == 2:
            guess_the_number()
        elif game == 3:
            break
        else:
            print("Неверная команда.")


main_menu()
