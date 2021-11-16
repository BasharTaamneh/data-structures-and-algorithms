from Merge_Sort.merge_sort import mergeSort


def test_mergeSort_1():
    #arrang
    arr = [12, 11, 13, 5, 6, 7]
    #act
    actual =  mergeSort(arr)
    #expected
    expected = [5, 6, 7, 11, 12, 13]
    assert actual == expected


def test_mergeSort_2():
    #arrang
    arr = [20, 18, 12, 8, 5, -2]
    #act
    actual = mergeSort(arr)
    #expected
    expected = [-2, 5, 8, 12, 18, 20]
    assert actual == expected


def test_mergeSort_3():
    #arrang
    arr = [5, 12, 7, 5, 5, 7]
    #act
    actual = mergeSort(arr)
    #expected
    expected = [5, 5, 5, 7, 7, 12]
    assert actual == expected


def test_mergeSort_4():
    #arrang
    arr = [2, 3, 5, 7, 13, 11]
    #act
    actual = mergeSort(arr)
    #expected
    expected = [2, 3, 5, 7, 11, 13]
    assert actual == expected
