# 6.Спортсмен занимается ежедневными пробежками.
# В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
first_day = input("Введите результат первого дня\n>>>")
first_day = int(first_day)
exhaust = input("Введите крайний день\n>>>")  # День, когда закончит бегать.
exhaust = float(exhaust)
day_number = 1
day_number = int(day_number)  # Стартовый день
while first_day <= 1.05*exhaust:
    day_number += 1
    first_day = first_day*1.1
    first_day = float("%.2f" % first_day)
    print(day_number, "-й день", ":", first_day, sep="")

print("Ответ: на", day_number, "-й день", "спортсмен достиг результата — не менее", exhaust, "км.")
