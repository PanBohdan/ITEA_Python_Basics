# Пользователь задает случайное число n.
# Сгенерировать список этой длины и заполнить его 0 и 1 случайным образом.
# Найти самую длинную цепочку из подряд идущих 0 или 1. Вывести эту длину.
# Для какого максимального значения n, ваш алгоритм будет работать меньше чем 1 секунда?


import random


def number_of_zeros_and_ones_in_a_row(n):
    list_of_numbers = []
    number_of_numbers_in_a_row = 1
    list_of_quantities_of_numbers_in_a_row = []
    for i in range(n):
        list_of_numbers.append(random.randint(0, 1))
    list_of_numbers.append(' ')
    # print(list_of_numbers) # for testing
    for i in range(len(list_of_numbers)-1):

        if list_of_numbers[i] == list_of_numbers[i+1]:
            number_of_numbers_in_a_row += 1

        if list_of_numbers[i] != list_of_numbers[i+1]:
            list_of_quantities_of_numbers_in_a_row.append(number_of_numbers_in_a_row)
            number_of_numbers_in_a_row = 1
    # print(list_of_quantities_of_numbers_in_a_row) # for testing
    list_of_quantities_of_numbers_in_a_row.sort()
    list_of_quantities_of_numbers_in_a_row.reverse()
    # print(list_of_quantities_of_numbers_in_a_row) # for testing
    return list_of_quantities_of_numbers_in_a_row[0]


def menu_function():
    n = input('Enter how many zeros and ones you want:')
    if n.isdigit():
        print('There is', number_of_zeros_and_ones_in_a_row(int(n)),
              'numbers in a row')
    else:
        print('Error number must be integer!')
        menu_function()


if __name__ == '__main__':
    menu_function()  # max number in 1 second is 800000
