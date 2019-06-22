# Найти сумму элементов матрицы


def sum_of_matrix(matrix):
    sum_of_m = 0
    for i in matrix:
        for j in i:
            sum_of_m += j
    return sum_of_m


if __name__ == '__main__':
    matrix1 = [[4, 6, 5], [9, 5, 7], [4, 5, 2, 3]]
    print(sum_of_matrix(matrix1))
