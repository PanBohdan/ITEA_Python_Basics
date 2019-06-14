# Print all capital letters
if __name__ == '__main__':
    inp = 'WHO CAPS loCKed'
    for i in inp:
        if i.istitle():
            print(i, end=' ')
