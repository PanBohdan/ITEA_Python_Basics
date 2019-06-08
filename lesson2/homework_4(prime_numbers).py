import math
if __name__ == '__main__':
    inp = int(input('Enter number:'))
    if inp > 1:
        for i in range(2, inp):
            if math.sqrt(inp) % i == 0:
                print(inp, ' is not a prime number')
                break
        else:
            print(inp, ' is a prime number')
    else:
        print(inp, ' is not a prime number')
