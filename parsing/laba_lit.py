import datetime
import time
import asyncio
def foo():
    print('foo')
    time.sleep(2)
    print('foo2')

def bar():
    print('bar')
    time.sleep(5)
    print('bar2')

def main():
    foo()
    bar()

start_time = datetime.datetime.now()
# do your work here
print(start_time.time())

main()
end_time = datetime.datetime.now()
print(end_time.time())


