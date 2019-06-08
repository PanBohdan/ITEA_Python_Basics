if __name__ == '__main__':
    fib = [0]
    i = 0
    n = int(input('Input how many Fibonacci numbers you want:'))
    if n == 1:
        print(fib)
    else:
        fib.append(1)
    while i <= n-3:
        i1 = i+1
        fib.append(int(fib[i]) + int(fib[i1]))
        i += 1
    if n != 1:
        print(fib)
