def mid(x):
    sum = 0
    quantity = 0
    for i in x:
        sum += int(i)
        quantity += 1
    return sum/quantity


if __name__ == "__main__":
    some_list = [1, 2, 3, 6]
    print(mid(some_list))
