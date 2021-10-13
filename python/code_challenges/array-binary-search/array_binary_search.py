# pylint: disable=invalid-name
# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring


def binary_search(arrlist, checkkey):
    start = 0
    end = len(arrlist)
    while start < end:
        mid = (start + end)//2
        if arrlist[mid] > checkkey:
            end = mid
        elif arrlist[mid] < checkkey:
            start = mid + 1
        else:
            return mid
    return -1


print(binary_search([11, 22, 33, 44, 55, 66, 77], 44))
print(binary_search([1, 2, 3, 5, 6, 7], 4))
