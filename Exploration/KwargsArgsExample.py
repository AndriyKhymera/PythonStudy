# coding=utf-8
def anyArgumentsAmountPrint(*args):
    """
    It initialize an empty tuple(кортеж)
    Tuple differs from list by the fact that it's objects are immutable
    """
    print (type(args))
    print(args)

def sum(x, y):
    print ("Sum :".format(x+y))

def anyKeyValueArgumentsAmountPrint(**kwargs):
    """
    Key
    """
    print (type(kwargs))
    print(kwargs)

# using Examples
anyArgumentsAmountPrint()
anyArgumentsAmountPrint(1, 2, 3)

list = [1, 2]
anyArgumentsAmountPrint(list)
anyArgumentsAmountPrint(*list)
# We can use * to pass a list
sum(*list)


dict = {
    "key1": "val1",
    "key2": "val2",
    "key3": "val3"
}

anyKeyValueArgumentsAmountPrint()
anyKeyValueArgumentsAmountPrint(key1="val1", key2="val2")
anyKeyValueArgumentsAmountPrint(**{"key3":"val3", "key4":"val4"})
anyKeyValueArgumentsAmountPrint(**dict)
