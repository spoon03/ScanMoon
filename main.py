def open_file(name: str) -> list:
    text = []
    row = []
    i = 0
    with open(name, 'r') as f:
        for ch in f.read():
            if ch != '\n':
                row.append(ch)
            else:
                text.append(row)
                row = []
    text.append(row)
    return text


def calculate(photo: str):
    data = open_file(photo)
    line_max = len(data)
    colum_max = len(data[0])
    count = 0
    for d in data:
        print(d)
    print('===============')
    for x in range(line_max):
        for y in range(colum_max):
            el = data[x][y]
            print(f'Элемент с координатой {x + 1}{y + 1}={el}')
            if el == '1':
                data = scan(x, y, data, line_max, colum_max)
                count += 1
    return count

def scan(x: int, y: int, data: list, x_max, y_max):
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
    for d in data:
        print(d)
    print('===============')
    return data


print(calculate('photo.txt'))
