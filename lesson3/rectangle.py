# Вывести прямоугольник со сторонами a,b


def print_rectangle(a, b):
    a = round(a)
    b = round(b)
    if a <= 0 or b <= 0:
        print("Height or width can't be zero or less")
        return
    for i in range(0, a):
        print('*'*b)


if __name__ == '__main__':
    print_rectangle(5, 13)
