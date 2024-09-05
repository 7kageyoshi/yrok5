def digits_summ(num):
    summ = 0
    while num > 0:
        digit = num % 10
        summ += digit
        num //= 10
    print("Сумма цифр:", summ)


def max_digit(num):
    maximum = 0
    while num > 0:
        digit = num % 10
        if digit > maximum:
            maximum = digit
        num //= 10
    print("Максимальная цифра:", maximum)


def min_digit(num):
    minimum = num % 10
    while num > 0:
        digit = num % 10
        if digit < minimum:
            minimum = digit
        num //= 10
    print("Минимальная цифра:", minimum)


while True:
    num = int(input("Введите число: "))
    action = int(
        input(
            "Введите номер действия: 1 - сумма цифр, 2 - максимальная цифра, 3 - минимальная цифра: "
        )
    )
    if action == 1:
        digits_summ(num)
    elif action == 2:
        max_digit(num)
    elif action == 3:
        min_digit(num)
    else:
        print("Ошибка: неверная команда.")
