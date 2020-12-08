# 5.Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек,
# или убыток — издержки больше выручки).
# Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

proceeds = input("Введите выручку вашей компании: \n >>>")
expenses = input("Введите расходы вашей компании:\n >>>")
proceeds = int(proceeds)
expenses = int(expenses)

profit = proceeds - expenses  # Прибыль
profitability = profit/expenses  # Рентабельность
profit = int(profit)
profitability = float(profitability)
profitability_percent_value = profitability * 100

if proceeds > expenses:
    print("Фирма отработала с прибылью, рентабельность составила:", profitability_percent_value, "%")
else:
    print("Фирма работает в убыток, завите эффективного менеджера!")
employees_quantity = input("Сообщите количество сотрудников: \n>>>")
employees_quantity = int(employees_quantity)
profit_per_employer = profit/employees_quantity
profit_per_employer = int(profit_per_employer)
print("Целочисленная прибыль на сотрудника составила", profit_per_employer)
