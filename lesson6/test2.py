import math


def sum_of_squares_of_list(inp_list):
    fin_sum = 0
    for j in inp_list:
        fin_sum += math.sqrt(j)
    return fin_sum
