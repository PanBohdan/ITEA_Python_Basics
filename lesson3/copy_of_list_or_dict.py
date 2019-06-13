def function(x):
    x.clear()
    print(x)


if __name__ == '__main__':
    dict1 = {'Hello': 'World'}
    list1 = ['Hello', 'World']
    function(list1.copy())
    print(list1)
    function(dict1.copy())
    print(dict1)
