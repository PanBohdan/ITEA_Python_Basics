def sort(x):
    x.sort()
    return x


def sum_of_num(x):
    temp_list = []
    for i in x:
        sum = 0
        for y in str(i):
            sum += int(y)
        temp_list.append(sum)
    return temp_list


if __name__ == "__main__":
    list = [125, 22, 51, 41, 625, 123, 1]
    print(sort(list))
    print('Sum of numbers in numbers is:', sum_of_num(list))
