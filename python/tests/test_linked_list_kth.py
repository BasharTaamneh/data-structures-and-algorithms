from linked_list.linked_list_kth.linked_list_kth import LinkedList, Node
import pytest

def test_import():
    assert LinkedList()
    assert Node(1)


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
