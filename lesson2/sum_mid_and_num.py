# print arithmetic means, sum and number of numbers when user enters 0
if __name__ == '__main__':
    sum = 0
    i = float(input('Input number end press Enter: '))
    counter = 0
    while i != 0:
        counter += 1
        sum += i
        i = float(input('Input number end press Enter: '))
    mid = sum / 2
    print('Sum is', sum)
    print('mid is', mid)
    print('You entered', counter, 'numbers')
