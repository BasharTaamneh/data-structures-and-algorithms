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
