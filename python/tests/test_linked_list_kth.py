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
    ll.append(1)
    ll.append(2)
    ll.append(3)
    expected_third = 1
    expected_second = 2
    expected_first = 3
    # Act
    actual_first = (ll.head.next_).next_.data
    actual_second = ll.head.next_.data
    actual_third = ll.head.data
    # Assert
    assert actual_first == expected_first
    assert actual_second == expected_second
    assert actual_third == expected_third


def test_get_Kth_From_the_end_of_the_linked_list_1():
    # Arrange
    ll = LinkedList()
    ll.append(1)
    ll.append(3)
    ll.append(8)
    ll.append(2)
    expected = 2
    # Act
    actual = ll.getKthFromEnd(0)
    # Assert
    assert actual == expected


def test_get_Kth_From_the_end_of_the_linked_list_2():
    # Arrange
    ll = LinkedList()
    ll.append(1)
    ll.append(3)
    ll.append(8)
    ll.append(2)
    expected = 3
    # Act
    actual = ll.getKthFromEnd(2)
    # Assert
    assert actual == expected


def test_Where_k_is_greater_than_the_length_of_the_linked_list():
    # Arrange
    ll = LinkedList()
    ll.append(1)
    ll.append(3)
    ll.append(8)
    ll.append(2)
    expected = "'Kth' --> is out of range"
    # Act
    actual = ll.getKthFromEnd(6)
    # Assert
    assert actual == expected


def test_Where_k_and_the_length_of_the_list_are_the_same():
    # Arrange
    ll = LinkedList()
    ll.append(1)
    ll.append(3)
    ll.append(8)
    ll.append(2)
    expected = "'Kth' --> is out of range"
    # Act
    actual = ll.getKthFromEnd(4)
    # Assert
    assert actual == expected


def test_Where_k_is_nor_a_positive_integer():
    # Arrange
    ll = LinkedList()
    ll.append(1)
    ll.append(3)
    ll.append(8)
    ll.append(2)
    expected = "'k' value was rejected --> negative value"
    # Act
    actual = ll.getKthFromEnd(-1)
    # Assert
    assert actual == expected


def test_kth_Where_the_linked_list_is_of_a_size_1_():
    # Arrange
    ll = LinkedList()
    ll.append(1)
    expected = 1
    # Act
    actual = ll.getKthFromEnd(0)
    # Assert
    assert actual == expected

