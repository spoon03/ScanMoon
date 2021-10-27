def open_file():
    text = []
    row = []
    i=0
    with open('photo.txt', 'r') as f:
        for ch in f.read():
            if ch != '\n':
                row.append(ch)
            else:
                text.append(row)
                row = []
    text.append(row)
    return text

def calculate():
    print(open_file())


calculate()


