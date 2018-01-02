#TODO read about @list_decorator
#TODO read about enumerate, dict, zip, filter and reduce
def my_zip_function(arr1, arr2):
    len1 = len(arr1)
    len2 = len(arr2)

    if (len1 > len2):
        limit = len2
    else:
        limit = len1

    dict = {}
    for i in range(0, limit):
        dict[i] = {arr1[1], arr2[2]}


    return dict


arr1 = [1, 2, 3]
arr2 = [4, 5, 6]
dict = my_zip_function(arr1, arr2)
print (dict)

