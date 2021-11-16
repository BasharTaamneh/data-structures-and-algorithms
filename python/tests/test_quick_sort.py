from Quick_Sort.quick_sort import quicksort


def test_quicksort_1():
    # Arrange
    arr = [8, 4, 23, 42, 16, 15]
    #actual
    actual = quicksort(arr, 0, len(arr)-1)
    #expected
    expected = [4, 8, 15, 16, 23, 42]
    assert actual == expected


def test_quicksort_2():
    # Arrange
    arr = [20, 18, 12, 8, 5, -2]
    #actual
    actual = quicksort(arr, 0, len(arr)-1)
    #expected
    expected = [-2, 5, 8, 12, 18, 20]
    assert actual == expected


def test_quicksort_3():
    # Arrange
    arr = [5, 12, 7, 5, 5, 7]
    #actual
    actual = quicksort(arr, 0, len(arr)-1)
    #expected
    expected = [5, 5, 5, 7, 7, 12]
    assert actual == expected


def test_quicksort_4():
    # Arrange
    arr = [2, 3, 5, 7, 13, 11]
    #actual
    actual = quicksort(arr, 0, len(arr)-1)
    #expected
    expected = [2, 3, 5, 7, 11, 13]
    assert actual == expected
