def insert(inp_list, inp_index, inp_str):
    inp_list = inp_list + ['temp']
    if inp_index >= len(inp_list)-1:  # for indexes that larger than length of input list
        inp_list[len(inp_list)-1] = inp_str  # insert at last index of list
        return inp_list

    if inp_index > -1:  # for positive indexes
        for i in range(len(inp_list)-1):
            if i == inp_index:  # inserting input_str
                temp = inp_list[i]
                inp_list[i] = inp_str
            if i > inp_index:  # moving all of the other objects in the list
                temp_temp = temp
                temp = inp_list[i]
                inp_list[i] = temp_temp
        temp_temp = temp
        inp_list[i+1] = temp_temp
        return inp_list

    if -inp_index >= len(inp_list)-1:   # for negative indexes that larger then length of input list
        for i in range(len(inp_list)-1):  # moving back in cycle of length of input list
            if i == 0:  # inserting at the index of beginning
                temp = inp_list[i]
                inp_list[i] = inp_str
            if i > 0:
                temp_temp = temp  # moving all of objects by one index
                temp = inp_list[i]
                inp_list[i] = temp_temp
        temp_temp = temp
        inp_list[i+1] = temp_temp
        return inp_list

    if inp_index <= -1:  # for negative indexes
        for i in range(len(inp_list)-1):
            if i == inp_index+len(inp_list)-1:  # inserting at the index
                temp = inp_list[i]
                inp_list[i] = inp_str
            if i > inp_index+len(inp_list)-1:  # moving objects
                temp_temp = temp
                temp = inp_list[i]
                inp_list[i] = temp_temp
        temp_temp = temp
        inp_list[i+1] = temp_temp
        return inp_list


def remove(inp_list, inp_str):
    index = 0
    first_run = True
    new_list = []
    for i in inp_list:
        if i == inp_str and first_run:  # removing
            inp_list[index] = ''
            first_run = False
            continue
        new_list = new_list + [i]  # moving along
        index += 1
    return new_list


if __name__ == '__main__':
    list1 = ['Hello', 'Max', 'and', 'How do you guys feel today?', 'Fine?', 'Ok', 'Bye.']
    list1 = insert(list1, 3, 'Victor')
    print(list1)

    list2 = ['Hello', 'Hell', 'world!', 'Hurray!']
    list2 = remove(list2, 'Hell')
    print(list2)
