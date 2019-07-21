from test2 import sum_of_squares_of_list


def find_arithmetic_mean(inp_list):
    final_sum = 0
    for j in inp_list:
        final_sum += int(j)
    return final_sum/len(inp_list)


def find_arithmetic_means_of_txt_file():
    temp_output_list = []
    final_output_list = []
    with open('test3_result.txt', 'r') as f:
        for line in f:
            temp_str = line
            temp_list = temp_str.split(' ')
            temp_list.remove('\n')
            temp_output_list.append(temp_list)
    for x in temp_output_list:
        final_output_list.append(find_arithmetic_mean(x))
    print(sum_of_squares_of_list(final_output_list))


if __name__ == '__main__':
    find_arithmetic_means_of_txt_file()
