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

    sum_of_nums = 0
    data = data.split('\n')
    data.remove('')
    data.remove('    ')
    for i in range(len(data)):
        data[i] = float(data[i])

    for i in range(0, len(data), 3):
        if i != len(data)-3:
            print(data[i], end=' + ')
        else:
            print(data[i], end=' = ')
        sum_of_nums += data[i]
    print(sum_of_nums)

    sum_of_nums = 0
    for i in range(1, len(data), 3):
        if i != len(data)-2:
            print(data[i], end=' + ')
        else:
            print(data[i], end=' = ')
        sum_of_nums += data[i]
    print(sum_of_nums)

    sum_of_nums = 0
    for i in range(2, len(data), 3):
        if i != len(data)-1:
            print(data[i], end=' + ')
        else:
            print(data[i], end=' = ')
        sum_of_nums += data[i]
    print(sum_of_nums)
