# pylint: disable=invalid-name
# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring

def insertShift_Array(arrlist, n):
    '''
    BIG O:
    -------------
    time <== O(n)

    space <== O(n)
    '''
    idx = int((len(arrlist)+1)/2)
    arrlist.insert(idx, n)
    return arrlist


print(insertShift_Array([2, 4, 6, -8], 5))
print(insertShift_Array([42, 8, 15, 23, 42], 16))
