# print sum of input
if __name__ == '__main__':
    sum_of_inp = 0
    print('Enter numbers that you want to add in one line dividing them with spaces')
    inp = input()
    if inp.find(' ') > 0:
        o = inp.split(' ')
        for i in o:
            sum_of_inp += int(i)
        print('Your sum is ', sum_of_inp)
    else:
        print('You entered numbers wrong. Try again but with spaces')
