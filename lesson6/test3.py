import random


def generate_and_write_five_random_nums():
    with open('test3_result.txt', 'a') as f:
        temp_str = ''
        for j in range(5):
            if not j == 4:
                temp_str += str(random.randint(0, 11))+' '
            else:
                temp_str += str(random.randint(0, 11))+' \n'
        f.write(temp_str)


if __name__ == '__main__':
    for j in range(100):
        generate_and_write_five_random_nums()
