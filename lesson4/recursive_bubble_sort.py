def recursive_bubble_sort(numbers):
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            temp = numbers[i]
            numbers[i] = numbers[i + 1]
            numbers[i + 1] = temp
            recursive_bubble_sort(numbers)


if __name__ == '__main__':
    list1 = [1, 2, 25, 4, 3, 26, 100, -2, 55, 155, 10, 1, -1, 5, 2010, 0.5]
    recursive_bubble_sort(list1)
    print(list1)
