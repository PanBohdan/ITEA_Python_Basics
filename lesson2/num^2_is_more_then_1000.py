# print squares of numbers until square is more than 1000
if __name__ == '__main__':
    i = 0
    while i*i < 1000:
        print (i)
        print(i ** 2)
        i += 1
    print (i)
    print(i ** 2)