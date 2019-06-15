def insert(inp_list, inp_index, inp_str):
    inp_list = inp_list + ['temp']
    if inp_index >= len(inp_list)-1:
        inp_list[len(inp_list)-1] = inp_str
        return inp_list

    if inp_index > -1:
        for i in range(len(inp_list)-1):
            if i == inp_index:
                temp = inp_list[i]
                inp_list[i] = inp_str
            if i > inp_index:
                temp_temp = temp
                temp = inp_list[i]
                inp_list[i] = temp_temp
        temp_temp = temp
        inp_list[i+1] = temp_temp
        return inp_list

    if -inp_index >= len(inp_list)-1:
        for i in range(len(inp_list)-1):
            if i == 0:
                temp = inp_list[i]
                inp_list[i] = inp_str
            if i > 0:
                temp_temp = temp
                temp = inp_list[i]
                inp_list[i] = temp_temp
        temp_temp = temp
        inp_list[i+1] = temp_temp
        return inp_list

    if inp_index <= -1:
        for i in range(len(inp_list)-1):
            if i == inp_index+len(inp_list)-1:
                temp = inp_list[i]
                inp_list[i] = inp_str
            if i > inp_index+len(inp_list)-1:
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
        if i == inp_str and first_run:
            inp_list[index] = ''
            first_run = False
            continue
        new_list = new_list + [i]
        index += 1
    return new_list


if __name__ == '__main__':
    list1 = ['Hello', 'Max', 'and', 'How do you guys feel today?', 'Fine?', 'Ok', 'Bye.']
    list1 = insert(list1, 3, 'Victor')
    print(list1)

    list2 = ['Hello', 'Hell', 'world!', 'Hurray!']
    list2 = remove(list2, 'Hell')
    print(list2)
