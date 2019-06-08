if __name__ == '__main__':
    strn='o hello There'
    for i in strn:
        if not i.isupper():
            print(i, end='')
        else: break
