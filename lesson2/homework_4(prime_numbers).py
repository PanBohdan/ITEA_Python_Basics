# print is inp a prime number
import math


def is_number_prime(inp):
    if inp > 1:
        for i in range(int(round(math.sqrt(inp))), inp-1):
            if inp % i == 0:
                return False
        else:
            return True
    else:
        return False


if __name__ == '__main__':
    inp = input('Enter number:')
    if inp.isdigit():
        if is_number_prime(int(inp)):
            print('Number is prime')
        else:
            print('Number is not prime')

    else:
        print('Error')
