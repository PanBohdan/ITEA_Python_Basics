import random


def number_of_zeros_and_ones_in_a_row(n):
    list_of_numbers = []
    number_of_numbers_in_a_row = 1
    list_of_counters_of_numbers_in_a_row = []
    for i in range(n):
        list_of_numbers.append(random.randint(0, 1))
    list_of_numbers.append(' ')
    # print(list_of_numbers) # for testing
    for i in range(len(list_of_numbers)-1):

        if list_of_numbers[i] == list_of_numbers[i+1]:
            number_of_numbers_in_a_row += 1

        if list_of_numbers[i] != list_of_numbers[i+1]:
            list_of_counters_of_numbers_in_a_row.append(number_of_numbers_in_a_row)
            number_of_numbers_in_a_row = 1
    # print(list_of_counters_of_numbers_in_a_row) # for testing
    list_of_counters_of_numbers_in_a_row.sort()
    list_of_counters_of_numbers_in_a_row.reverse()
    # print(list_of_counters_of_numbers_in_a_row) # for testing
    print(list_of_counters_of_numbers_in_a_row[0])


def input_function():
    n = input('Enter how many zeros and ones you want:')
    if n.isdigit():
        number_of_zeros_and_ones_in_a_row(int(n))
    else:
        print('Error number must be integer!')
        input_function()


if __name__ == '__main__':
    input_function()  # max number in 1 second is 900000
