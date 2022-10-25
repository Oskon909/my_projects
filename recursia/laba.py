# decarator for laba

def laba(func):
    def wrapper(*args, **kwargs):
        print("Laba")
        return func(*args, **kwargs)
    return wrapper

@laba
def countdown(n):
    if n <= 0:
        print("LIFTOFF!")
    else:
        print(n)
        countdown(n - 1)


print(countdown(10))