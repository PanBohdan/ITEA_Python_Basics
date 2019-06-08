if __name__ == '__main__':
    summ = 0;
    print('Enter numbers that you want to add in one line dividing them with spaces')
    inp = input()
    if inp.find(' ')>0:
        o = inp.split(' ')
        for i in range(len(o)):
            summ += int(o[i])
        print('Your sum is ', summ)
    else:
        print('You entered numbers wrong. Try again but with spaces')
