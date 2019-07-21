telephone_directory = []


class Person:
    def __init__(self, name, phone, info):
        self.name = name
        self.phone = phone
        self.info = info

    def change_name(self, new_name):
        self.name = new_name

    def change_phone(self, new_phone):
        self.phone = new_phone

    def change_info(self, new_info):
        self.info = new_info


def main_menu():
    main_menu_dict = {'1': add_person, '2': get_phone_by_name,
                      '3': get_name_by_phone, '4': remove_by_name,
                      '5': remove_by_phone, '6': change_name,
                      '7': change_info, '8': change_phone,
                      '9': same_numbers, '0': print_directory}
    inp_select = input('Select what you want to do:\n'
                       '0-Print directory\n'
                       '1-Add person to a directory\n'
                       '2-Get phone by name\n'
                       '3-Get name by phone\n'
                       '4-Remove person from a directory by name\n'
                       '5-Remove person from a directory by phone\n'
                       '6-Change name of person\n'
                       '7-Change info of person\n'
                       '8-Change phone of person\n'
                       '9-How many phones have same three numbers\n'
                       '10-Close program\n')
    main_menu_dict.get(inp_select, do_nothing)(telephone_directory)
    if inp_select != '10':
        main_menu()


def print_directory(inp_list):
    for i in inp_list:
        print(i.name, i.phone, i.info)


def do_nothing(inp):
    None


def add_person(inp_list):
    inp_name = input('Input name: ')
    inp_phone = input('Input phone: ')
    inp_info = input('Input info: ')
    inp_list.append(Person(inp_name, inp_phone, inp_info))


def get_phone_by_name(inp_list):
    search_name = input('Input name you want to search: ')
    for i in inp_list:
        if i.name == search_name:
            print(i.name, i.phone, i.info)


def get_name_by_phone(inp_list):
    search_phone = input('Input phone you want to search: ')
    for i in inp_list:
        if i.phone == search_phone:
            print(i.name, i.phone, i.info)


def remove_by_name(inp_list):
    name_to_remove = input('Input name you want to remove: ')
    index = 0
    for i in inp_list:
        if i.name == name_to_remove:
            print(i.name, i.phone, i.info)
            inp = input('Do you want this person to get removed? Yes-Y, No-N'
                        '\n')
            if inp == 'Y':
                inp_list.pop(index)
                break
            else:
                index += 1
        else:
            index += 1


def remove_by_phone(inp_list):
    phone_to_remove = input('Input phone you want to remove: ')
    index = 0
    for i in inp_list:
        if i.phone == phone_to_remove:
            print(i.name, i.phone, i.info)
            inp = input('Do you want this person to get removed? Yes-Y, No-N'
                        '\n')
            if inp == 'Y':
                inp_list.pop(index)
                break
            else:
                index += 1
        else:
            index += 1


def change_name(inp_list):
    name_to_change = input('Input name you want to be changed: ')
    for i in inp_list:
        if i.name == name_to_change:
            print(i.name, i.phone, i.info)
            inp = input('Do you want to change this person name? Yes-Y, No-N'
                        '\n')
            if inp == 'Y':
                inp_name = input('Input new name: ')
                i.change_name(inp_name)


def change_phone(inp_list):
    phone_to_change = input('Input phone you want to be changed: ')
    for i in inp_list:
        if i.phone == phone_to_change:
            print(i.name, i.phone, i.info)
            inp = input('Do you want to change this person phone? Yes-Y, No-N'
                        '\n')
            if inp == 'Y':
                inp_phone = input('Input new phone: ')
                i.change_phone(inp_phone)


def change_info(inp_list):
    name_to_change = input('Input name in which you want to change info: ')
    for i in inp_list:
        if i.name == name_to_change:
            print(i.name, i.phone, i.info)
            inp = input('Do you want to change this person info? Yes-Y, No-N'
                        '\n')
            if inp == 'Y':
                inp_info = input('Input new info: ')
                i.change_info(inp_info)


def same_numbers(inp_list):
    list_of_numbers = []
    for j in inp_list:
        list_of_numbers.append(j.phone)
    same_numbers_counter = 0
    for i in list_of_numbers:
        triplets = [i[x:x + 3] for x in range(len(i) - 2)]
        for j in triplets:
            if j[0] == j[1] and j[1] == j[2]:
                same_numbers_counter += 1
                break
    print(same_numbers_counter)


if __name__ == '__main__':
    main_menu()
