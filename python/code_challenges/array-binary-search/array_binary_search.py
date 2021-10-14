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


print(binary_search(range(44, 100), 55))
print(binary_search([1, 2, 3, 5, 2, 7], 2))
