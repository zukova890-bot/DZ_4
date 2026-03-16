def append_to_file(text: str, namefile: str) -> None:
    # добавляем строку в конец файла
    with open(namefile, 'a', encoding='utf-8') as file:
        file.write(text + '\n')

    with open(namefile, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for index, line in enumerate(lines, 1):
        # проверка на чётность строки
        if index % 2 == 0:
            # выводим нужные строки и удаляем \n в конце строки
            print(line, end='')

if __name__ == '__main__':
    # сосдаём текстовый документ
    with open("example_4_3.txt", 'w', encoding='utf-8') as f:
        f.write("Первая строка\n")
        f.write("Вторая строка\n")
        f.write("Третья строка\n")
        f.write("Четвертая строка\n")

    # вызываем функцию для добавления строки в конец текстового документа
    append_to_file("Пятая строчка", "example_4_3.txt")
