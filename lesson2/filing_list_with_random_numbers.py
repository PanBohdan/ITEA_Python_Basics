import random


def create_list_with_random_numbers(start, end, num_of_numbers):
    list1 = []
    if num_of_numbers >= 1:
        for i in range(num_of_numbers):
            list1.append(random.randint(start, end))
        return list1
    else:
        return ('You entered negative number or zero. '
                'Please try again but with positive number')


if __name__ == "__main__":
    print('Input lowest random number')
    inp_min = int(input())
    print('Input highest ran number')
    inp_max = int(input())
    if inp_min <= inp_max:
        n = int(input('Input how many random numbers you want:'))
        print(create_list_with_random_numbers(inp_min, inp_max, n))
    else:
        print('Error: first number is larger than second')
