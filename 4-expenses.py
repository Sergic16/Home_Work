# Создать список из трат за неделю(7 чисел)

# Посчитать сумму, среднее, минимум и максимум.

# Сохранить в кортеже(минимум, максимум, сумма) и вывести его
expenses = [100, 150, 200, 250, 300, 350, 400]
total = sum(expenses)
average = total / len(expenses)
minimum = min(expenses)
maximum = max(expenses)
result = (minimum, maximum, total)
print(result)
