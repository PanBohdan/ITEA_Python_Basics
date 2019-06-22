from is_matrix_square import square_checker


def sum_of_diagonals_of_matrix(matrix):
    if square_checker(matrix):
        sum_of_diagonals = 0
        length = len(matrix)
        for i in range(length):  # sum of diagonal
            sum_of_diagonals += matrix[i][i]

        matrix.reverse()

        for i in range(length):  # sum of other diagonal
            sum_of_diagonals += matrix[i][i]

        matrix.reverse()  # returning matrix to original form
        return sum_of_diagonals
    else:
        print('Error. Matrix must be square')


def sum_of_diagonal_of_matrix(matrix):
    if square_checker(matrix):
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
    print(sum_of_diagonals_of_matrix(matrix1))
    print(sum_of_diagonal_of_matrix(matrix1))
