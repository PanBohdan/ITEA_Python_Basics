# Разбить строку на группы по 3 числа и посчитать суммы
# каждого первого, второго и третьего


def sum_every_third_number(inp, num_of_line):
    sum_of_nums = 0
    for i1 in range(num_of_line, len(inp), 3):
        if i1 != len(inp)-(3-num_of_line):
            print(inp[i1], end=' + ')
        else:
            print(inp[i1], end=' = ')
        sum_of_nums += inp[i1]
    return sum_of_nums


if __name__ == '__main__':
    data = """
    0.00002640
    23174.4902
    0.61180654
    0.00002599
    8434.0130
    0.21919999
    0.00002000
    52622.1944
    1.05244388
    0.00001599
    13708.5678
    0.21919999
    0.00001500
    100232.3673
    1.50348550
    """

    data = data.split('\n')
    data.remove('')
    data.remove('    ')
    for i in range(len(data)):
        data[i] = float(data[i])
    print(sum_every_third_number(data, 0))
    print(sum_every_third_number(data, 1))
    print(sum_every_third_number(data, 2))
