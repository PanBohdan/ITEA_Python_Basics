# print is inp a prime number
import math


def is_number_prime(inp_local):
    for i in range(int(round(math.sqrt(inp_local))), inp_local-1):
        if inp % i == 0:
            return False
        else:
            return True


if __name__ == '__main__':
    inp = input('Enter number:')
    if inp.isdigit():
        inp = int(inp)
        if inp > 0:
            if is_number_prime(inp):
                print('Number is prime')
            else:
                print('Number is not prime')
        else:
            print('Error')
    else:
        print('Error')
