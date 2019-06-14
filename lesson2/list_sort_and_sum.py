def sort(x):
    x.sort()
    return x


def sum_of_num(x):
    temp_list = []
    for i in x:
        sum_of_numbers = 0
        for y in str(i):
            sum_of_numbers += int(y)
        temp_list.append(sum_of_numbers)
    return temp_list


if __name__ == "__main__":
    input_list = [125, 22, 51, 41, 625, 123, 1]
    print(input_list, 'Unsorted list')
    print(sort(input_list), 'Sorted list')
    print('Sum of numbers in numbers in list is:', sum_of_num(input_list))
