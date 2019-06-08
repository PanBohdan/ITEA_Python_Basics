if __name__ == '__main__':
    import math
    sqr_not_ready = float(input('Enter number '))
    sqr = math.sqrt(sqr_not_ready)
    print('Square root of ', sqr_not_ready, ' is ', sqr)
    while sqr > 10:
        sqr_not_ready = float(input('Enter number '))
        sqr = math.sqrt(sqr_not_ready)
        print('Square root of ', sqr_not_ready, ' is ', sqr)
