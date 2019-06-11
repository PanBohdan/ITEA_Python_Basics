# print triangle with the height of h
def build_triangle(h):
    for i in range(h):
        rows = [(h - i) * ' ' + i * 2 * '^' + '^']
        for i1 in rows:
            print(i1)


if __name__ == '__main__':
    h1 = int(input('Input height of triangle '))
    build_triangle(h1)
