def max_of_2(number_1, number_2):
    return number_1 if number_1 > number_2 else number_2


def max_of_3(number_1, number_2, number_3):
    return max_of_2(max_of_2(number_1, number_2), number_3)


digit_1 = int(input("Введите первое число: "))
digit_2 = int(input("Введите второе число: "))
digit_3 = int(input("Введите третье число: "))

print("Самое большое число:", max_of_3(digit_1, digit_2, digit_3))
