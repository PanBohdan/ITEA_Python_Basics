# Exponentiation with cycle
if __name__ == '__main__':
    x = 25
    power_of = 5
    num = 1
    for i in range(power_of):
        num = num * x
    print(num, ' is a', x, '^', power_of)
