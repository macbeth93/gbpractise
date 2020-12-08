# 1. Поработайте с переменными, создайте несколько,
# 2 выведите на экран,
# 3 запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.

# 1 Пришла в голову идея калькулятора для работы(менеджер закупок)

print("Рассчет цены на товар")
cost_price = input("Введи себестоимость:\n>>>")
cost_price = float(cost_price)
minimum_price = cost_price*1.24
market_price = minimum_price*1.05
wholesale_price = market_price*1.12
retail_price = market_price*1.18
float(minimum_price)
print("Минимальная цена:", "%.2f" % minimum_price)
print("Рыночная цена:", "%.2f" % market_price)
print("Оптовая цена:", "%.2f" % wholesale_price)
print("Розничная цена:", "%.2f" % retail_price)
