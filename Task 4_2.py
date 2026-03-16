def prime_generator():
    number = 2
    while True:
        is_prime = True

        # оптимизированная проверка до n**0.5
        # если число составное, то у него есть некий делитель, который не превыщает кввадратный корень числа
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                # число составное, найден делитель
                is_prime = False
                break

        # делители не найдены - число простое
        if is_prime:
            # возвращаем промежуточный результат
            yield number

        number += 1

if __name__ == "__main__":
    generator = prime_generator()

    # выводим результат
    for _ in range(10):
        print(next(generator))