def reversal(x):
    revers_x = 0
    while x > 0:
        revers_x = revers_x * 10 + x % 10
        x //= 10
    return revers_x


num_1 = int(input("Введите первое число: "))
num_2 = int(input("Введите второе число: "))

revers_num1 = reversal(num_1)
revers_num2 = reversal(num_2)

print("\nПервое число наоборот:", revers_num1)
print("Второе число наоборот:", revers_num2)

amount = revers_num1 + revers_num2
revers_summ = reversal(amount)

print("\nСумма:", amount)
print("Сумма наоборот:", revers_summ)
