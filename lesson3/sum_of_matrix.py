if __name__ == '__main__':
    matrix1 = [[4, 6, 5], [9, 5, 7], [4, 5, 2, 3]]
    sum_of_matrix = 0
    for i in matrix1:
        for j in i:
            sum_of_matrix += j
    print(sum_of_matrix)
