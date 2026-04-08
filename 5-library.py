# Создай словарь books, где ключ — название книги, значение — автор.
# Добавь несколько записей. При этом может быть у одного автора несколько книг
# Вывести: список всех книг, список всех уникальных авторов.
import sys
# books = {"Руслан и Людмила": "А.С.Пушкин",
#          "Горе от ума": "И.Тургенев", "Царевна лягушка": "А.С.Пушкин"}
# autor = set()
# for key, value in books.items():
#     print(key)
#     autor.add(value)
# print(autor)


books = {
    "Руслан и Людмила": "А.С.Пушкин",
    "Горе от ума": "И.Тургенев",
    "Царевна лягушка": "А.С.Пушкин"
}

action = sys.argv[1]

if action == "filter":
    # Получаем критерий фильтрации из аргументов командной строки
    filter_by = sys.argv[2]

    # Фильтруем книги: ищем совпадения либо в названиях, либо в авторах
    filtered_books = filter(
        lambda title: filter_by in title or filter_by in books[title],
        books.keys()
    )

    # Создаём список строк формата "Книга — Автор" для отфильтрованных книг
    result = map(lambda title: f"{title} — {books[title]}", filtered_books)

    # Выводим результат
    print(list(result))

elif action == "sort":
    # Получаем параметр сортировки из аргументов командной строки (author или book)
    sort_by = sys.argv[2].lower()

    # Подготавливаем список строк "Книга — Автор"
    book_author_list = list(
        map(lambda title: f"{title} — {books[title]}", books.keys())
    )

    if sort_by == "author":
        # Сортируем по имени автора (извлекаем автора из строки "Книга — Автор")
        sorted_books = sorted(
            book_author_list, key=lambda item: item.split(" — ")[1]
        )
    elif sort_by == "book":
        # Сортируем по названию книги (извлекаем название из строки "Книга — Автор")
        sorted_books = sorted(
            book_author_list, key=lambda item: item.split(" — ")[0]
        )
    else:
        print("Ошибка: допустимые значения для сортировки — 'author' или 'book'")
        sys.exit(1)

    # Выводим отсортированный список
    print(sorted_books)

else:
    print("Ошибка: допустимые действия — 'filter' или 'sort'")
    sys.exit(1)
