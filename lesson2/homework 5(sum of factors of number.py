if __name__ == '__main__':
    inp=int(input('Enter number: '))
    nums=[]
    sum=0
    for i in range(1, inp+1):
        if inp%i == 0:
            nums.append(i)
    for o in range(len(nums)):
        sum+=int(nums[o])
    print ('sum is ',sum)


