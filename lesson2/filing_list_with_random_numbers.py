import random


def random_numbers_list(start, end):
    list1 = []
    i = 1
    done = 0
    while done < 1:
        num_of_numbers = int(input('Input how many random numbers you want:'))
        if num_of_numbers >= 1:
            while i <= num_of_numbers:
                list1.append(random.randint(start, end))
                i += 1
                done = 1
            print(list1)
        else:
            print('You entered negative number or zero. Please try again but with positive number')


if __name__ == "__main__":
    print('Input lowest ran number')
    inp_min = int(input())
    print('Input highest ran number')
    inp_max = int(input())
    if inp_min <= inp_max:
        random_numbers_list(inp_min, inp_max)
    else:
        print('Error: first number is larger than second')
