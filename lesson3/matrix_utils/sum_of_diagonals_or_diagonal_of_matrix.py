# Найти сумму верхней диагонали матрицы
# Найти сумму диагональных элементов матрицы


from is_matrix_square import is_square_matrix


def sum_diagonals_of_matrix(matrix):
    if is_square_matrix(matrix):
        sum_of_diagonals = 0
        length = len(matrix)
        for i in range(length):  # sum of diagonal
            sum_of_diagonals += matrix[i][i]

        for i in range(length-1, -1, -1):
            sum_of_diagonals += matrix[i][-i-1]

        return sum_of_diagonals
    else:
        print('Error. Matrix must be square')


def sum_diagonal_of_matrix(matrix):
    if is_square_matrix(matrix):
        sum_of_diagonal = 0
        length = len(matrix)
        for i in range(length):  # sum of diagonal
            sum_of_diagonal += matrix[i][i]
        return sum_of_diagonal
    else:
        print('Error. Matrix must be square')


if __name__ == '__main__':
    matrix1 = [[-2, 5, 3, 2, 1.5],
               [9, -6, 5, 1, 6],
               [3, 2, 0.5,  3, 2],
               [-1, 8, -4, 8, 1],
               [2, -25, -1, 5, 2]]
    print(sum_diagonals_of_matrix(matrix1))
    print(sum_diagonal_of_matrix(matrix1))
