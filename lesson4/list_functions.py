def insert(inp_list, inp_index, inp_str):
    new_list = inp_list[:inp_index] + [inp_str] + inp_list[inp_index:]
    return new_list


def remove(inp_list, inp_str):
    index = 0
    for i in inp_list:
        if i == inp_str:
            break
        index += 1
    new_list = inp_list[:index] + inp_list[index+1:]
    return new_list


if __name__ == '__main__':
    list1 = ['Hello', 'Max', 'and', 'How do you guys feel today?',
             'Fine?', 'Ok', 'Bye.']
    list1 = insert(list1, 3, 'Victor')
    print(list1)

    list2 = ['Hello', 'Hell', 'world!', 'Hurray!']
    list2 = remove(list2, 'Hell')
    print(list2)
