if __name__ == '__main__':
    o='WHO Togled CAPS loCK'
    for i in range(len(o)):
        if o[i].istitle():
            print(o[i],end=' ')