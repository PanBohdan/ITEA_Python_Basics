# print sum of all the factors of a number
if __name__ == '__main__':
    inp = int(input('Enter number: '))
    sum = 0
    for i in range(1, inp+1):
        if inp % i == 0:
            sum += i
    print('sum is ', sum)
