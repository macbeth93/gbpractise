#2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.
user_seconds = input("Введите секунды:")
if user_seconds.isdigit():
    user_seconds = int(user_seconds)
else:
    print("Введите секунды в формате целого числа")
    exit()

hours = user_seconds//3600
minutes = user_seconds//60
print(hours, minutes, user_seconds, sep=":")
