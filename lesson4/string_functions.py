def find(inp_data, what_to_find):
    index = 0
    if what_to_find in inp_data:
        c = what_to_find[0]
        for i in inp_data:
            if i == c:
                if inp_data[index:index+len(what_to_find)] == what_to_find:
                    return index
            index += 1
    return -1


def split(inp_data, splitter):
    list_of_data = []
    temp_string = ''
    for i in inp_data:
        if i == splitter:
            list_of_data.append(temp_string)
            temp_string = ''
        else:
            temp_string += i
    if temp_string:
        list_of_data.append(temp_string)
    return list_of_data


def replace(inp_data, what_to_replace, replace_with):
    new_data = ''
    index = 0
    temp_index = 0
    temp_list = []
    for i in inp_data:
        temp_list.append(i)
    final_destination = len(what_to_replace)
    for i in range(len(inp_data)-len(what_to_replace)+1):
        temp_index += 1
        for j in what_to_replace:
            if inp_data[index+i] == j:
                index += 1
                if index >= final_destination:
                    if len(what_to_replace) == len(replace_with):
                        for l in range(final_destination):
                            temp_list[temp_index+l-1] = replace_with[l]
                        for temp in temp_list:
                            new_data += temp
                        return new_data
                    if len(what_to_replace) > len(replace_with):
                        for l in range(final_destination):
                            if l < len(replace_with):
                                temp_list[temp_index+l-1] = replace_with[l]
                            else:
                                temp_list.pop(l+index)
                        for temp in temp_list:
                            new_data += temp
                        return new_data
                    if len(what_to_replace) < len(replace_with):
                        for k in range(len(replace_with)):
                            if k < final_destination:
                                temp_list[temp_index+k-1] = replace_with[k]
                            elif k >= final_destination:
                                temp_list.insert(k+temp_index-1,
                                                 replace_with[k])
                        for temp in temp_list:
                            new_data += temp
                        return new_data
            elif inp_data[index+i] != j:
                index = 0
                break
    return new_data


if __name__ == '__main__':
    data = 'Hey! Hello world. Help! 1 2 3'
    print(find(data, 'Hello'))
    print(split(data, ' '))
    print(replace(data, 'Hey!', 'Hello!'))
