# Напишите функцию, которая сортирует массив рекурсивно.


def recursive_bubble_sort(numbers):
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:  # if next number is larger than swap
            temp = numbers[i]
            numbers[i] = numbers[i + 1]
            numbers[i + 1] = temp
            recursive_bubble_sort(numbers)


if __name__ == '__main__':
    list1 = [1, 2, 25, 4, 3, 26, 100, -2, 55, 155, 10, 7, -1, 5,
             2010, 0.5, 24, -3, 555, 67, 2003, 0.59, -1.5, -4, -5]
    recursive_bubble_sort(list1)
    print(list1)
