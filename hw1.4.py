# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = input("Введите целое, положительное число:\n>>>")
number = int(number)
answer_number = number
max_number = 0
interval = 1
while number > 0:
    print("Loop number", interval, ":", number, max_number)
    interval = interval + 1
    if max_number < number % 10:
        max_number = number % 10
        number = number // 10
    else:
        number = number // 10

print("Наибольшей цифрой в числе", answer_number, "будет цифра:", max_number)
