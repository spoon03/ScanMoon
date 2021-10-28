"""Поиск кратеров на луне."""


def open_file(name: str) -> list:
    """
    Читаем из файла карту луны.

    :param name:Имя файла.
    :return: Матрица.
    """
    text = []
    row = []
    with open(name, 'r') as f:
        for ch in f.read():
            if ch != '\n':
                row.append(ch)
            else:
                text.append(row)
                row = []
    text.append(row)
    return text


def scan(x: int, y: int, data: list, x_max: int, y_max: int) -> list:
    """
    Сканирование кратера.

    :param x: Координата части кратера
    :param y: Координата части кратера
    :param data: Снимок луны
    :param x_max: Макс размер x
    :param y_max: Макс размер y
    :return: Снимок с отмеченным кратером
    """
    data[x][y] = 'x'
    if x + 1 < x_max:
        el = data[x + 1][y]
        if el == '1':
            data[x + 1][y] = 'x'
            scan(x + 1, y, data, x_max, y_max)
    if y + 1 < y_max:
        el = data[x][y + 1]
        if el == '1':
            data[x][y + 1] = 'x'
            scan(x, y + 1, data, x_max, y_max)
    if x - 1 > -1:
        el = data[x - 1][y]
        if el == '1':
            data[x - 1][y] = 'x'
            scan(x - 1, y, data, x_max, y_max)
    if y - 1 > -1:
        el = data[x][y - 1]
        if el == '1':
            data[x][y - 1] = 'x'
            scan(x, y - 1, data, x_max, y_max)
    return data


def calculate(data: list) -> int:
    """
    Подсчет кол-ва кратеров.

    :param data: Снимок луны
    :return: Кол-во кратеров
    """
    line_max = len(data)
    colum_max = len(data[0])
    count = 0
    for x in range(line_max):
        for y in range(colum_max):
            el = data[x][y]
            if el == '1':
                data = scan(x, y, data, line_max, colum_max)
                count += 1
    return count


print(calculate(open_file('photo.txt')))
