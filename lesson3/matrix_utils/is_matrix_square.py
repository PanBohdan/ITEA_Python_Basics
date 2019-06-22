def square_checker(matrix):
    return all(len(row) == len(matrix) for row in matrix)


if __name__ == '__main__':
    matrix1 = [[-2, 5, 3, 2, 1.5],
               [9, -6, 5, 1, 6],
               [3, 2, 0.5, 3, 2],
               [-1, 8, -4, 8, 1],
               [2, -25, -1, 5, 2]]
    print(square_checker(matrix1))
    matrix2 = [[-2, 5, 3, 2, 1.5],
               [9, -6, 5, 1, 6],
               [3, 2, 0.5, 3, 2, 3],
               [-1, 8, -4, 8, 1],
               [2, -25, -1, 5, 2]]
    print(square_checker(matrix2))
