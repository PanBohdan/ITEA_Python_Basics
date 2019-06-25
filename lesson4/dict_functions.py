# Без использования методов словарей(кроме items),
# напишите  функцию remove по ключу и remove по значению


def remove_with_key(inp_dict, key):
    if key in inp_dict:
        del inp_dict[key]
    else:
        return


def remove_with_value(inp_dict, value):
    for x in inp_dict:
        if inp_dict[x] == value:
            del inp_dict[x]
            break


if __name__ == '__main__':
    dict1 = {'Hello': 'World', 'Hi': 'Max', 'Brand': 'Ford'}
    remove_with_key(dict1, 'Hello')
    print(dict1)

    dict2 = {'Hello': 'Max', 'Good': 'morning', 'Brand': 'Audi'}
    remove_with_value(dict2, 'Max')
    print(dict2)
