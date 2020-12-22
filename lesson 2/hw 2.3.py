# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.


while True:
    user_month_number = (input("Введите номер месяца целым числом: \n >>>"))
    if user_month_number.isdigit():
        user_month_number = int(user_month_number)
        break
    print("Введите номер месяца целым числом ")
season_list = dict([(1, "Зима"), (2,"Весна"), (3, "Лето"), (4, "Осень")])
month_list = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь",
              "Декабрь"]
if user_month_number == 12 or user_month_number <= 3:
    print(season_list[1])
elif user_month_number == 3 or user_month_number == 4 or user_month_number == 5:
    print(season_list[2])
elif user_month_number == 6 or user_month_number == 7 or user_month_number == 8:
    print(season_list[3])
else:
    print(season_list[4])

print(month_list[user_month_number - 1])


