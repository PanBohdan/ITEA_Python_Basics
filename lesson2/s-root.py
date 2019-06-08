if __name__ == '__main__':
    import math
    sqrnotrdy=float(input('Enter number '))
    sqr=math.sqrt(sqrnotrdy)
    print('Square root of ', sqrnotrdy, ' is ', sqr)
    while sqr > 10:
        sqrnotrdy = float(input('Enter number '))
        sqr = math.sqrt(sqrnotrdy)
        print('Square root of ',sqrnotrdy, ' is ',sqr)