from linked_list.linked_list_zip.linked_list_zip import LinkedList
import pytest


@pytest.fixture
def llist1():
    llist1 = LinkedList()
    llist1.append(1)
    llist1.append(3)
    llist1.append(2)
    llist1.append(4)
    return llist1


@pytest.fixture
def llist2():
    llist2 = LinkedList()
    llist2.append(5)
    llist2.append(9)
    llist2.append(10)
    llist2.append(12)
    llist2.append(15)
    return llist2


def test_zip_tow_list_printTHe_first(llist1, llist2):
    actual = []
    for i in llist1.merge(llist1, llist2):
        actual.append(i)
    expected = [1, 5, 3, 9, 2, 10, 4, 12]
    assert actual == expected
