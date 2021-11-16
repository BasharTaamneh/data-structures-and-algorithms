def mergeSort(arr):

    if len(arr) > 1:
        # Finding the mid of the array
        mid = len(arr)//2
        # Dividing the array elements  into 2 halves
        left = arr[:mid]
        right = arr[mid:]
        # Sorting the first half
        mergeSort(left)
        # Sorting the second half
        mergeSort(right)

        merge(left, right, arr)

    return arr


def merge(left, right, arr):
    i = j = k = 0
    # Copy data to temp arrays left[] and right[]
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # Checking if any element was left
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    # Checking if any element was right
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


arr = [2, 3, 5, 7, 13, 11]
print(mergeSort(arr))
