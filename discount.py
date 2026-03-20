price = input("Введите стоимость товара: ")
discount = input("Введите размер скидки (%): ")

discount_price = int(price) * (1 - (int(discount) / 100))

print("Стоимость товара:", price)
print("Стоимость товара со скидкой:", discount_price)

