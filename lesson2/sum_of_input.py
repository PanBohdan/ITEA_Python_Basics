if __name__ == '__main__':
    sum = 0
    print('Enter numbers that you want to add in one line dividing them with spaces')
    inp = input()
    if inp.find(' ') > 0:
        o = inp.split(' ')
        for i in o:
            sum += int(i)
        print('Your sum is ', sum)
    else:
        print('You entered numbers wrong. Try again but with spaces')
