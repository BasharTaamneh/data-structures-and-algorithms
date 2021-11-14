from Insertion_Sort.Insertion_Sort import InsertionSort

def test_import():
    assert InsertionSort([0])


def test_insertion_sort_1():
    # Arrange
    arr = [8, 4, 23, 42, 16, 15]
    # actual
    actual = InsertionSort(arr)
    # expected
    expected = [4, 8, 15, 16, 23, 42]
    assert actual == expected


def test_insertion_sort_2():
    # Arrange
    arr = [5, 12, 7, 5, 5, 7]
    # actual
    actual = InsertionSort(arr)
    # expected
    expected = [5, 5, 5, 7, 7, 12]
    assert actual == expected


def test_insertion_sort_3():
    # Arrange
    arr = [20, 18, 12, 8, 5, -2]
    # actual
    actual = InsertionSort(arr)
    # expected
    expected = [-2, 5, 8, 12, 18, 20]
    assert actual == expected
