def mid(x):
    sum_of_num = 0
    quantity = 0
    for i in x:
        sum_of_num += int(i)
        quantity += 1
    return sum_of_num/quantity


if __name__ == "__main__":
    some_list = [1, 2, 3, 6]
    print(mid(some_list))
