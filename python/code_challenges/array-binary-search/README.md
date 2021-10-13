# array-binary-search
<!-- Description of the challenge -->
The program takes a list and key as input and finds the index of the key in the list using binary search.
 The list and key is passed to binary_search.
 If the return value is -1, the key is not found and a message is displayed, otherwise the index of the found item is displayed.

# Problem Solution

1. Create a function binary_search that takes a list and key as arguments.
2. The variable start is set to 0 and end is set to the length of the list.
3. The variable start keeps track of the first element in the part of the list being searched while end keeps track of the element one after the end of the part being searched.
4. A while loop is created that iterates as long as start is less than end.
5. mid is calculated as the floor of the average of start and end.
6. If the element at index mid is less than key, start is set to mid + 1 and if it is more than key, end is set to mid. Otherwise, mid is returned as the index of the found element.
7. If no such item is found, -1 is returned.



## Whiteboard Process
<!-- Embedded whiteboard image -->

![array_insert_shift](insertShift_Arrang)

## Approach & Efficiency
<!-- What approach did you take? Discuss Why. What is the Big O space/time for this approach? -->

**BIG O**

- Time <== O(log n)

- space <== O(1)

[live PR](https://github.com/BasharTaamneh/data-structures-and-algorithms/pull/16)
