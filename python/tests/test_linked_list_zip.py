from linked_list.linked_list_zip.linked_list_zip import LinkedList
import pytest

@pytest.fixture
def zip():
    llist1 = LinkedList()
    llist2 = LinkedList()
    llist1.append(1)
    llist1.append(3)
    llist1.append(2)
    llist1.append(4)
    llist2.append(5)
    llist2.append(9)
    llist2.append(10)
    llist2.append(12)
    llist2.append(15)
    return llist1, llist2

