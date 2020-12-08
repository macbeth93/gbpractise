# 0 - 100
# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = input("Введите целое, положительное число:\n>>>")
number = int(number)
answer_number = number
max_number = 0
interval = 1

while 100 > number > 0:
    print("Loop number", interval, ":", number)
    two = number / 2
    three = number / 3
    five = number / 5
    two_two = number % 2
    three_three = number % 3
    five_five = number % 5

    if two_two == 0:
        print("Четное")
        number += 1
    elif three_three == 0:
        print("Нечетное")
        number += 1
    elif five_five == 0:
        print("Кратно пяти")
        number += 1
    else:
        print("Простое")
        number += 1
