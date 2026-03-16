# Список квадратов первых 10-ти натуральных чисел
from math import factorial

squares = [n**2 for n in range(1,11)]
print(squares)

# Словарь, содержащий названия дней недели с порядковыми номерами
days = ['Monday', "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
days_dict = {day: i+1 for i, day in enumerate(days)}
print(days_dict)

# Множество, содержащее теги библиотек в нижнем регистре
tags = ["Django", "FastAPI", "Numpy", "PYTHON", "Pandas", "FASTAPI", "Python", "random"]
tags_set = {tag.lower() for tag in tags}
print(tags_set)

# Список, содержащий только чётные числа из исходного списка
numbers = [1, 3, 4, 87, 98, 15, 7, 4]
numbers_list = [i for i in numbers if i%2==0]
print(numbers_list)

# Словарь, где ключи - числа от 1-5, а значения - их факториал
def fact(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

factorials = {n: fact(n) for n in range(1, 6)}
print(factorials)