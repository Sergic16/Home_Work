price = input("Введите стоимость товара: ")
discount = input("Введите размер скидки (%): ")

discount_price = int(price) * (1 - (int(discount) / 100))

print("Стоимость товра:", price)
print("Стоимость товара со скидкой:", discount_price)

