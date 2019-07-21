import pickle
import random


def generate_and_pickle_list_of_five_ran_nums():
    list_of_lists_of_random_nums = []
    for j in range(100):
        temp_list = []
        for i in range(5):
            temp_list.append(random.randint(0, 11))
        list_of_lists_of_random_nums.append(temp_list)
    with open('test5_3', 'wb') as f:
        pickle.dump(list_of_lists_of_random_nums, f)


if __name__ == '__main__':
    generate_and_pickle_list_of_five_ran_nums()
