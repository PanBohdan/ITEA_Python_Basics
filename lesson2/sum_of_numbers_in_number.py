if __name__ == '__main__':
    number = 12345

    sum_of_nums_in_num = 0
    for i in str(number):
        sum_of_nums_in_num += int(i)
    print(sum_of_nums_in_num)
    sum_of_nums_in_num = 0

    while number != 0:
        sum_of_nums_in_num += number % 10
        number = number // 10
    print(sum_of_nums_in_num)
