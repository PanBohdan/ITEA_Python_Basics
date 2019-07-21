import pickle
from test2 import sum_of_squares_of_list


def find_arithmetic_mean(inp_list):
    final_sum = 0
    for j in inp_list:
        final_sum += int(j)
    return final_sum/len(inp_list)


def find_arithmetic_means_of_txt_file():
    with open('test5_3', 'rb') as f:
        tmp = pickle.load(f)
        output_list = []
        for j in tmp:
            output_list.append(find_arithmetic_mean(j))
        print(sum_of_squares_of_list(output_list))


if __name__ == '__main__':
    find_arithmetic_means_of_txt_file()
