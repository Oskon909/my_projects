a=[1,2,3,4,5,6,7,8,9,10]

for i in range(len(a),1):
    print(a[i])


# list comprehension
def list_copy(l):
    return [i for i in l]