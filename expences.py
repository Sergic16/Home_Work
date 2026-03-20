food = input("Введите расходы на еду: ")
taxi = input("Введите расходы на транспорт: ")
dosug = input("Введите расходы на развлечения: ")

sum = int(food) + int(taxi) + int(dosug)
sum_sr = sum / 3

print("Общая сумма расходов:", sum)
print("Средний расход на категорию:", sum_sr)
