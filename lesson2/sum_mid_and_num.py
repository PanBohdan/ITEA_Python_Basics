# print arithmetic means, sum and number of numbers when user enters 0
if __name__ == '__main__':
    sum_of_num = 0
    i = float(input('Input number end press Enter: '))
    counter = 0
    while i != 0:
        counter += 1
        sum_of_num += i
        i = float(input('Input number end press Enter: '))
    mid = sum_of_num / 2
    print('Sum is', sum_of_num)
    print('mid is', mid)
    print('You entered', counter, 'numbers')
