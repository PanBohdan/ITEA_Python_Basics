# Как передать копию списка или словаря в функцию?


def test_function(x):
    x.clear()
    return x


if __name__ == '__main__':
    dict1 = {'Hello': 'World'}
    list1 = ['Hello', 'World']
    print(test_function(list1.copy()))
    print(list1)
    print(test_function(dict1.copy()))
    print(dict1)
