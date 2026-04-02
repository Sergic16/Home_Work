# import re


# def normalize_money():
#     # Читаем ввод и очищаем от лишних пробелов, приводим к нижнему регистру
#     user_input = input(
#         "Введите сумму (например, 100 руб 10 коп): ").strip().lower()

#     # Проверка на пустую строку
#     if not user_input:
#         print("Некорректный формат суммы")
#         return

#     # Регулярное выражение для формата с рублями и копейками
#     # Поддерживает: «X руб Y коп», с любым количеством пробелов
#     pattern_with_kopecks = r'^(\d+)\s+руб\s+(\d+)\s+коп$'
#     match_with_kopecks = re.match(pattern_with_kopecks, user_input)

#     if match_with_kopecks:
#         rubles_str, kopecks_str = match_with_kopecks.groups()
#         rubles = int(rubles_str)
#         kopecks = int(kopecks_str)

#         # Проверки корректности значений
#         if kopecks >= 100:
#             print("Некорректный формат суммы")
#             return
#         if rubles < 0 or kopecks < 0:
#             print("Некорректный формат суммы")
#             return

#         # Форматируем вывод: рубли + копейки с двумя знаками после запятой
#         total = f"{rubles}.{kopecks:02d} ₽"
#         print(total)
#         return

#     # Регулярное выражение для формата только с рублями
#     # Поддерживает: «X руб», с любым количеством пробелов
#     pattern_only_rubles = r'^(\d+)\s+руб$'
#     match_only_rubles = re.match(pattern_only_rubles, user_input)

#     if match_only_rubles:
#         rubles_str = match_only_rubles.group(1)
#         rubles = int(rubles_str)

#         if rubles < 0:
#             print("Некорректный формат суммы")
#             return

#         # Форматируем вывод с двумя нулями после запятой
#         total = f"{rubles}.00 ₽"
#         print(total)
#         return

#     # Если ни один шаблон не подошёл — некорректный формат
#     print("Некорректный формат суммы")


# # Вызов функции
# normalize_money()
# Добавить расход
# Показать все расходы
# Показать сумму и средний расход
# Удалить расход по номеру
# Выход
menus = (" ", "Добавить расход", "Показать все расходы",
         "Показать сумму и средний расход", "Удалить расход по номеру", "Выход")
user_select = ""

while user_select not in menus:
    for i, menu in enumerate(menus):
        if i == 0:
            continue
        print(i, menu)
    user_select = input("Выберите пункт меню: ").lower()
    match user_select:
        case "добавить расход":
            rashod()
        case "показать все раходы":
            rashod_list()
        case "показать сумму и средний расход":
            rashod_summ()
        case "удалить расход по номеру":
            rashod_delete()
        case "выход":
            break
        case _:
            print("Такого пункта меню нет, повторите ввод!")
