# print triangle with the height of h
def build_tringle(h):
    for i in range(h):
        rows = [(h - i) * ' ' + i * 2 * '^' + '^']
        for i in rows:
            print(i)


if __name__ == '__main__':
    h1 = int(input('Input height of triangle '))
    build_tringle(h1)
