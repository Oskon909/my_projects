
def inner(func):
    def pr(*args,**kwargs):
        print('Hello')
        print(args)
        func(*args)
        print('bye') # typo
    return pr
@inner
def foo(name,lname):
    print(name)
    print(lname)

# foo=inner(foo)
foo('Oskon','rich')