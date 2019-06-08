if __name__ == '__main__':

    summ = 0
    i=float(input('Input number end press Enter: '))
    num = []
    counter=0
    while i!=0:
       counter+=1
       num.append(i)
       i = float(input('Input number end press Enter: '))
    for a in range(len(num)):
       summ+=float(num[a])
    mid=summ/2
    if i == 0:
       #print(num)#for testing
       print('Sum is',summ)
       print('mid is',mid)
       print('You entered',counter,'numbers')