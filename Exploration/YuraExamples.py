import sys


def decorator(func):
    def warappr(*args,**kwargs):
        print (args)
        print (kwargs)
        print ("call function {}".format(func.__name__))
        return func(*args,**kwargs)

    return warappr

@decorator
def func(a):
    print (a)

if __name__ == "__main__":
    func(1)
    func(a=1)
    print(sys.argv)