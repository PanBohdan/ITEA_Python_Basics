if __name__ == '__main__':
    matrix = [[-2, 5, 3, 2, 1.5],
              [9, -6, 5, 1, 6],
              [3, 2, 0.5,  3, 2],
              [-1, 8, -4, 8, 1],
              [2, -25, -1, 5, 2]]

    sum_of_diagonal = 0
    length = len(matrix)
    for i in range(length):  # sum of diagonal
        sum_of_diagonal += matrix[i][i]
    print(sum_of_diagonal)

    matrix.reverse()

    sum_of_diagonal_reversed = 0
    for i in range(length):  # sum of other diagonal
        sum_of_diagonal_reversed += matrix[i][i]

    print(sum_of_diagonal_reversed)
    print(sum_of_diagonal+sum_of_diagonal_reversed)
