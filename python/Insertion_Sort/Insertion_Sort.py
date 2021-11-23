def InsertionSort(arr):
    """
    InsertionSort function --> sort an array of size n in ascending order
    """
    for i in range(1, len(arr)):
        prev = i - 1
        curr = arr[i]
        while prev >= 0 and curr < arr[prev]:
            arr[prev + 1] = arr[prev]
            prev -= 1
            arr[prev + 1] = curr
    return arr


print(InsertionSort([2, 3, 5, 7, 13, 11]))

