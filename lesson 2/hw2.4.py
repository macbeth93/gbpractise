# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.
user_list = input("Enter the list for my list practise:\n >>>")
work_list = user_list.split()
cycling_number = 0
string_number = 1

while len(work_list) > cycling_number:
    if len(str(work_list)) <= 10:
        print("Строка номер", string_number, ":", work_list[cycling_number])
        cycling_number += 1
        string_number += 1
    else:
        print("Строка номер", string_number, ":", work_list[cycling_number][0:10])
        cycling_number += 1
        string_number += 1
