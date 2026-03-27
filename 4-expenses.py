from typing import List, Union

# from sympy import

# Список для хранения расходов, где первый элемент - это строка, которая будет служить заголовком для списка расходов
expenses = ["Список расходов"]
value = 0  # Переменная для хранения значения расхода
index = 0  # Переменная для хранения индекса расхода, который нужно удалить
summa = 0  # Переменная для хранения суммы расходов


def add_expense(expenses: List[Union[int, str]], value: int) -> List[Union[int, str]]:
    """Добавляет строку расхода в конец общего списка"""
    user_input = int(input("Введите расход: ").strip().lower())
    expenses.append(user_input)
    return expenses


def get_total_list(expenses: List[int]):  # Показывает сумму расходов
    """Показывает список расходов"""
    for i, list_expens in enumerate(expenses):  # Печатает все расходы с их индексами
        print(i if i != 0 else "\n", list_expens)
    # Считает сумму всех числовых элементов в списке расходов
    return 0


def get_total(expenses: List[int]):
    """Считает сумму всех числовых элементов в списке расходов, игнорируя строку заголовка"""
    return sum(summa for summa in expenses if isinstance(summa, (int, float)))


def delete_expence(expenses: List[int], index: int):
    """Удаляет строку расхода из списка по номеру"""

    # Печатает все расходы с их индексами, для удобства пользователя
    get_total_list(expenses)
    user_select_index = int(
        input("Введите номер расхода, который нужно удалить: ").strip().lower())
    if 0 < user_select_index < len(expenses):
        expenses.pop(user_select_index)
        print(
            f"Расход удален. Сумма оставшихся расходов: {get_total(expenses)}")
    else:
        print("Некорректный номер расхода. Пожалуйста, попробуйте снова.")
        # Рекурсивный вызов функции для повторного запроса ввода
        delete_expence(expenses, index)


def get_average(expenses: List[int]):  # Показывает средний расход
    """Показывает средний расход"""
    total = get_total(expenses)
    if len(expenses) > 1:
        total_sr = total / (len(expenses) - 1)
    return total_sr

def print_report(expenses: List[int]):  # Печатает красивый отчет
    """Печатает красивый отчет"""
    print("Отчет по расходам:")
    get_total_list(expenses)
    print(f"Сумма: {get_total(expenses)}")
    print(f"Средний расход: {get_average(expenses)}")

menus = (" ", "Добавить расход", "Показать все расходы",
         "Показать сумму", "показать средний расход", "Удалить расход по номеру", "Показать отчет", "Выход")
user_select = None

while user_select not in menus:
    for i, menu in enumerate(menus):
        if i == 0:
            continue
        print(i, menu)
    user_select = str(input("Выберите пункт меню: ").lower())
    match user_select:
        case "1":
            add_expense(expenses, value)  # добавляет расход
        case "2":
            get_total_list(expenses)  # показывает все расходы
        case "3":
            # get_total(expenses)  # возвращает сумму
            print(f"Сумма всех расходов: {get_total(expenses)}")
        case "4":
            get_average(expenses)  # возвращает средний расход
            print(get_average(expenses))
        case "5":
            delete_expence(expenses, index)  # удалить расход
        case "6":
            print_report(expenses)  # печатает красивый отчёт
        case "7":
            break
        case _:
            print("Такого пункта меню нет, повторите ввод!")
