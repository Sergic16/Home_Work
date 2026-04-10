import sys

# Кастомные исключения
class MissingArgumentError(Exception):
    """Исключение для случая отсутствия обязательных аргументов"""
    pass

class InvalidActionError(Exception):
    """Исключение для недопустимого действия"""
    pass

class InvalidSortCriteriaError(Exception):
    """Исключение для недопустимого критерия сортировки"""
    pass

books = {
    "Руслан и Людмила": "А.С.Пушкин",
    "Горе от ума": "И.Тургенев",
    "Царевна лягушка": "А.С.Пушкин"
}

def main():
    try:
        # Проверка наличия хотя бы одного аргумента (действия)
        if len(sys.argv) < 2:
            raise MissingArgumentError("Не указано действие. Используйте 'filter' или 'sort'.")

        action = sys.argv[1]

        if action == "filter":
            # Проверка, что передан второй аргумент (название книги для фильтрации)
            if len(sys.argv) < 3:
                raise MissingArgumentError("Для действия 'filter' необходимо указать название книги.")

            book_to_filter = sys.argv[2]
            filtered_books = filter(lambda title: title == book_to_filter, books.keys())
            result = map(lambda title: f"{title} — {books[title]}", filtered_books)
            print(list(result))

        elif action == "sort":
            # Проверка, что передан второй аргумент (критерий сортировки)
            if len(sys.argv) < 3:
                raise MissingArgumentError("Для действия 'sort' необходимо указать критерий ('author' или 'book').")

            sort_by = sys.argv[2].lower()
            book_author_list = list(map(lambda title: f"{title} — {books[title]}", books.keys()))

            if sort_by == "author":
                sorted_books = sorted(book_author_list, key=lambda item: item.split(" — ")[1])
            elif sort_by == "book":
                sorted_books = sorted(book_author_list, key=lambda item: item.split(" — ")[0])
            else:
                raise InvalidSortCriteriaError("Допустимые значения для сортировки — 'author' или 'book'")

            print(sorted_books)

        else:
            raise InvalidActionError("Допустимые действия — 'filter' или 'sort'")


    except MissingArgumentError as e:
        print(f"Ошибка: {e}")
        print("\nПримеры использования:")
        print("  python new.py filter 'Руслан и Людмила'")
        print("  python new.py sort author")
        sys.exit(1)

    except InvalidActionError as e:
        print(f"Ошибка: {e}")
        print("\nДоступные действия: 'filter', 'sort'")
        print("Примеры:")
        print("  python new.py filter 'Горе от ума'")
        print("  python new.py sort book")
        sys.exit(1)

    except InvalidSortCriteriaError as e:
        print(f"Ошибка: {e}")
        print("\nДопустимые критерии сортировки: 'author', 'book'")
        print("Пример:")
        print("  python new.py sort author")
        sys.exit(1)

    except IndexError as e:
        print(f"Неожиданная ошибка с аргументами: {e}")
        print("Проверьте правильность передачи аргументов.")
        sys.exit(1)

    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()