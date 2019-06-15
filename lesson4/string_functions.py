def find(inp_data, what_to_find):
    index = 0
    if what_to_find in inp_data:
        c = what_to_find[0]
        for ch in inp_data:
            if ch == c:
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


if __name__ == '__main__':
    data = 'Hey! Hello world. Help! 1 2 3'
    print(find(data, 'Hello'))
    print(split(data, ' '))
