def find_arithmetic_mean(x):
    sum_of_num = 0
    for i in x:
        sum_of_num += int(i)
    return sum_of_num/len(x)


if __name__ == "__main__":
    some_list = [1, 2, 3, 6]
    print(find_arithmetic_mean(some_list))
