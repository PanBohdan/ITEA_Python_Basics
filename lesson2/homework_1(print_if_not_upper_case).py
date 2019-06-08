if __name__ == '__main__':
    data = 'o hello There'
    for i in data:
        if not i.isupper():
            print(i, end = "")
        else:
            break
