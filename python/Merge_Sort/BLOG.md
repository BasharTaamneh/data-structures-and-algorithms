# Challenge Summary

-  Merge Sort is a Divide algorithm. It divides the input array into two halves, calls itself for the two halves, and then merges the two sorted halves. The merge() function is used for merging two halves. The merge(arr, l, m, r) is a key process that assumes that arr[l..m] and arr[m+1..r] are sorted and merges the two sorted sub-arrays into one. 

## Whiteboard Process

![]()

## Big O___

-  Time: O(nlog(n))

-  Space: O(1)

## Solution

```py

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

```
