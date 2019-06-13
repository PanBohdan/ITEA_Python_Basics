def telephone_directory(telephone_list):
    print('Please select what you want to do: \n 1-Add phone and name to the book')
    print(' 2-Search phone by name or name by phone \n 3-Remove name and phone \n 4-Redact phone and name')
    print(' 5-Check how many phone numbers have three or more same numbers in a row \n 6-Stop the program')
    inp = input(' ')

    if inp.isdigit():
        inp = int(inp)
        if inp == 6:  # stopping program
            print('Shutting down')
        elif inp == 1:  # Adding number and phone
            inp = input('Input phone and name ')
            telephone_list.append(inp)
            telephone_directory(telephone_list)

        elif inp == 2:  # searching name by phone or phone by name
            search_phone_and_number(telephone_list)
            telephone_directory(telephone_list)

        elif inp == 3:  # removing phone and name by phone or name
            remove_phone_and_name(telephone_list)
            telephone_directory(telephone_list)

        elif inp == 4:  # changing phone and name
            change_phone_and_name(telephone_list)
            telephone_directory(telephone_list)

        elif inp == 5:  # searching how many phones have three numbers in a row
            three_numbers_in_a_row(telephone_list)
            telephone_directory(telephone_list)

    else:
        print('Error! Please try again. Number must be integer. (And number must be number, not a name)\n')
        telephone_directory(telephone_list)


def remove_phone_and_name(x):
    inp = input('Enter phone or name you want to remove ')
    for i in x:
        if i.find(inp) >= 0:
            print('Do you want this phone and name to be removed? -', i, ' Y-Yes, N-No')
            inp_yes_or_no = input()
            if inp_yes_or_no == 'Y':
                x.remove(i)
                print('Successfully removed!')
            elif inp_yes_or_no == 'N':
                print('Ok. Please try again')
                continue
            else:
                print('Error! You entered wrong letter or number.')
                break


def change_phone_and_name(x):
    inp = input('Enter phone or name you want to change ')
    for i in x:
        if i.find(inp) >= 0:
            print('Do you want this phone and name to be changed? -', i, ' Y-Yes, N-No')
            inp_yes_or_no = input()
            if inp_yes_or_no == 'Y':
                x.append(input('What do you want this to be changed for? '))
                x.remove(i)
                print('Successfully changed!')
            elif inp_yes_or_no == 'N':
                print('Ok. Please try again')
                continue
            else:
                print('Error! You entered wrong letter or number.')
                break


def three_numbers_in_a_row(x):
    same_numbers_counter = 0
    for i in x:
        i = i.split('+')
        triplets = [i[1][x:x + 3] for x in range(len(i[1]) - 2)]
        for j in triplets:
            if j[0] == j[1] and j[1] == j[2]:
                same_numbers_counter += 1
                break

    print(same_numbers_counter)


def search_phone_and_number(x):
    inp = input('Enter phone or name you want to search ')
    for i in x:
        if i.find(inp) >= 0:
            print(i)


if __name__ == '__main__':
    telephone_directory([])
