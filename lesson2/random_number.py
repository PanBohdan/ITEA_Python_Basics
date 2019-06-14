# print random number in the range that user inputs
import random
if __name__ == '__main__':
    print('Input lowest random number')
    inp1 = int(input())
    print('Input highest random number')
    inp2 = int(input())
    if inp1 < inp2:
        num = random.randint(inp1, inp2)
        print(num)
    else:
        print('Error: first number is larger than second')
