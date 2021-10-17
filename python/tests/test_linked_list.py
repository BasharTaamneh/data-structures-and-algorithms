
# pylint: disable=missing-module-docstring
# pylint: disable=invalid-name
# pylint: disable=missing-function-docstring
import pytest
from linked_list.linked_list import Node, LinkedList


def test_import():
    assert Node(1)


def test_node_has_int_data():
    # Arrange any data that you need to run your test
    expected = 1

    # Act on the subject of the test to produce some actual output
    node = Node(1)
    actual = node.value

    # Assert
    assert actual == expected


def test_node_has_str_data():
    # Arrange any data that you need to run your test
    expected = "a"

    # Act on the subject of the test to produce some actual output
    node = Node("a")
    actual = node.value

    # Assert
    assert actual == expected


def test_node_is_a_Node():
    # Arrange any data that you need to run your test
    expected = "Node"

    # Act on the subject of the test to produce some actual output
    node = Node(1)
    actual = type(node).__name__

    # Assert
    assert actual == expected


# def test_node_without_value():
#     with pytest.raises(TypeError):
#         node = Node()


# def test_new_linked_list_is_empty():
#     expected = None

#     ll = LinkedList()
#     actual = ll.head

#     assert actual == expected


# def test_linked_list_insert():
#     # Arrange
#     expected = None
#     ll = LinkedList()
#     # Act
#     actual = ll.insert("")
#     assert actual == expected


# def test_link_insert_multiple():
#     # Arrange
#     ll = LinkedList()
#     ll.insert("1")
#     ll.insert("2")
#     ll.insert("3")
#     expected_third = "1"
#     expected_second = "2"
#     expected_first = "3"

#     # Act
#     actual_first = ll.head.value
#     actual_second = ll.head.next.value
#     actual_third = (ll.head.next).next.value

#     # Assert
#     assert actual_first == expected_first
#     assert actual_second == expected_second
#     assert actual_third == expected_third


# def test_link_head_pointer():
#     # Arrange
#     ll = LinkedList()
#     ll.insert("1")
#     ll.insert("2")
#     ll.insert("3")
#     expected = "3"

#     # Act
#     actual = ll.head.value

#     # Assert
#     assert actual == expected


# def test_link_includes_true():
#     # Arrange
#     ll = LinkedList()
#     ll.insert("1")
#     ll.insert("2")
#     ll.insert("3")
#     expected = True

#     # Act
#     actual = ll.includes("1")

#     # Assert
#     assert actual == expected


# def test_link_includes_false():
#     # Arrange
#     ll = LinkedList()
#     ll.insert("1")
#     ll.insert("2")
#     ll.insert("3")
#     expected = False

#     # Act
#     actual = ll.includes("10^6 VALUE")

#     # Assert
#     assert actual == expected


# def test_link_to_string():
#     #Arrange
#     ll = LinkedList()
#     ll.insert(4)
#     ll.insert("3")
#     ll.insert("bashar")
#     ll.insert("taamneh")
#     expected = "{'taamneh'} -> {'bashar'} -> {'3'} -> {4} -> NULL"

#     #Act
#     actual = str(ll)

#     #Assert
#     assert actual == expected
