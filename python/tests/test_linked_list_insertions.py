# pylint: disable=missing-module-docstring
# pylint: disable=invalid-name
# pylint: disable=missing-function-docstring
import pytest
from linked_list.linked_list_insertions.linked_list_insertions import Node, LinkedList


def test_import():
    assert Node(1)
    assert LinkedList()


def test_node_has_int_data():
    # Arrange any data that you need to run your test
    expected = 1

    # Act on the subject of the test to produce some actual output
    node = Node(1)
    actual = node.data

    # Assert
    assert actual == expected


def test_node_has_str_data():
    # Arrange any data that you need to run your test
    expected = "a"

    # Act on the subject of the test to produce some actual output
    node = Node("a")
    actual = node.data

    # Assert
    assert actual == expected


def test_node_is_a_Node():
    # Arrange any data that you need to run your test
    expected = "Node"

    # Act on the subject of the test to produce some actual output
    node = Node("")
    actual = type(node).__name__

    # Assert
    assert actual == expected


def test_node_without_value():
    with pytest.raises(TypeError):
        node = Node()


def test_new_linked_list_is_empty():
    expected = None
    ll = LinkedList()
    actual = ll.head

    assert actual == expected


def test_add_a_node_to_the_end_of_the_linked_list():
    # Arrange
    expected_1 = None
    ll = LinkedList()
    # Act
    actual_1 = ll.append("")
    assert actual_1 == expected_1


def test_add_a_multiple_node_to_the_end_of_the_linked_list():
    # Arrange
    ll = LinkedList()
    ll.append("1")
    ll.append("2")
    ll.append("3")
    expected_third = "1"
    expected_second = "2"
    expected_first = "3"
    # Act
    actual_first = (ll.head.next).next.data
    actual_second = ll.head.next.data
    actual_third = ll.head.data
    # Assert
    assert actual_first == expected_first
    assert actual_second == expected_second
    assert actual_third == expected_third


def test_insert_a_node_before_a_node_located_i_the_middle_of_a_linked_list():
    # Arrange
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    actual_1 = 2
    # Act
    ll.insertAfter(ll.head.next, 8)
    expected_1 = ll.head.next.data
    # Assert
    assert ll.head.data == 1
    assert ll.head.next.data == 2
    assert (ll.head.next).next.data == 8
    assert actual_1 == expected_1


