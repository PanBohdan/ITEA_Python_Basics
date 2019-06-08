if __name__ == '__main__':
    def build_eqtringle(h):
        for i in range(h):
            rows = [(h - i) * ' ' + i * 2 * '^' + '^']
            for i in rows:
                print (i)
    h1=int(input('Input height of triangle '))
    build_eqtringle(h1)

