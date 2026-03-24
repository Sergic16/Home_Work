# Домашнее задание Строки
# Задача 4. Вводим сумму в виде строки, например, "100 руб 10 коп".

user_input = input("Введите сумму (например, 100 руб 10 коп): ")
# Убираем пробелы и приводим к нижнему регистру
user_input1 = user_input.strip().lower()
# Разделяем строку на части
user_input_mod = user_input1.split()
# Ищем рубли и копейки
rubles = 0
kopecks = 0
# Проверяем корректность значений
if len(user_input_mod) == 4:
    rubles = int(user_input_mod[0])
    kopecks = int(user_input_mod[2])
elif len(user_input_mod) == 2:
    if user_input_mod[1] in ['руб', 'рубль', 'рублей']:
        rubles = int(user_input_mod[0])
    elif user_input_mod[1] in ['коп', 'копейка', 'копеек']:
        kopecks = int(user_input_mod[0])
total_amount = rubles + kopecks / 100
# Выводим результат
print(f"{total_amount:.2f} ₽")
