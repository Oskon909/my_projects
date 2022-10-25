def list_copy(l):
    return [i for i in l]
print(list_copy([1,2,3,4,5]))

def dict_copy(d):
    return {k: v for k, v in d.items()}

dict_copy({'a': 1, 'b': 2, 'c': 3})

def set_copy(s):
    return {i for i in s}

set_copy({1, 2, 3, 4, 5})