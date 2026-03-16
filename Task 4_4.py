def decorator(func):

    def wrapper(*args, **kwargs):
        print(f'Функция {func.__name__} вызвана с аршументами')
        # выводим все позиционные аргументы
        print(f"Позиционные аргументы: {args}")
        # выводим все именнованные аргументы
        print(f"Именнованые аргументы: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Площадь прямоугольника: {result}")
        # возвращаем результат исходной функции
        return result
    # возвращаем обёрнутую функцию
    return wrapper

# применяем декоратор к функции calculate_area
@decorator
def calculate_area(length: float, width: float) -> float:
    return length * width

if __name__ == '__main__':
    calculate_area(5, 10)