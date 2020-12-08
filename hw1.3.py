# 3.Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
solo = input("Введите число:\n>>>")
solo = str(solo)
double = solo + solo
triple = solo + solo + solo
total = int(solo) + int(double) + int(triple)
answer = "{solo}+{double}+{triple}={total}".format(solo=solo, double=double, triple=triple, total=total)
print(answer)
