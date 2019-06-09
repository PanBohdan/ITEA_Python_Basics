# print square roots of number until square root is less then 11
import math
if __name__ == '__main__':
    sqr_not_ready = float(input('Enter number '))
    sqr = math.sqrt(sqr_not_ready)
    print('Square root of ', sqr_not_ready, ' is ', sqr)
    while sqr > 10:
        sqr_not_ready = float(input('Enter number '))
        sqr = math.sqrt(sqr_not_ready)
        print('Square root of ', sqr_not_ready, ' is ', sqr)
