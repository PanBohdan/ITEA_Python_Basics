if __name__ == '__main__':
    string='o hello There'
    for i in string:
        if not i.isupper():
            print(i, end='')
        else: break
