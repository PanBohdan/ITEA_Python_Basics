# print factorial of given number
def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x - 1)


if __name__ == '__main__':
    print(factorial(6))
