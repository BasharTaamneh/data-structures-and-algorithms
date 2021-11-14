from linked_list.stack_queue_pseudo.stack_queue_pseudo import Stack, PseudoQueue
import pytest


# decorator
@pytest.fixture
def stack():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push("cat")
    return stack


def test_push_stack(stack):
    """
    """
    actual = stack.top.value
    expected = "cat"
    assert actual == expected


def test_pop_stack(stack):
    """
    """
    actual = stack.pop()
    expected = "cat"
    assert actual == expected


def test_stack_is_empty():
    assert Stack().is_empty()


def test_peek_stack(stack):
    # stack = Stack()
    actual = stack.peek()
    expected = 'cat'
    assert actual == expected


def test_peek_with_empty_stack():
    with pytest.raises(Exception):
        assert Stack() == "This stack is empty"


# Pseudo Queue Tests
# -------------------------------------------------------------------

@pytest.fixture
def pseudo_queue_0():
    pseudo = PseudoQueue()
    return pseudo


@pytest.fixture
def pseudo_queue_1():
    pseudo = PseudoQueue()
    pseudo.enqueue(1)
    return pseudo


@pytest.fixture
def pseudo_queue():
    pseudo = PseudoQueue()
    pseudo.enqueue(0)
    pseudo.enqueue(7)
    pseudo.enqueue(9)
    pseudo.enqueue(9)
    pseudo.enqueue(5)
    return pseudo


def test_pseudo_dequeue_empty(pseudo_queue_0):
    # Assert
    with pytest.raises(Exception):
        assert pseudo_queue_0.dequeue()


def test_pseudo_queue_enqueue_value(pseudo_queue_1):
    # Arrange
    expected = 1
    # Act
    actual = pseudo_queue_1.top.value
    # Assert
    assert actual == expected


def test_pseudo_queue_enqueue_multiple(pseudo_queue):
    # Arrange
    expected_1 = 0
    expected_2 = 7
    # Act
    actual_1 = pseudo_queue.top.value
    actual_2 = pseudo_queue.top.next.value
    # Assert
    assert actual_1 == expected_1
    assert expected_2 == actual_2


def test_pseudo_dequeue_value(pseudo_queue):
    # Arrange
    expected = 0
    # Act
    actual = pseudo_queue.dequeue()
    # Assert
    assert actual == expected


def test_pseudo_dequeue_multiple(pseudo_queue):
    # Arrange
    expected = True
    # Act
    pseudo_queue.dequeue()
    pseudo_queue.dequeue()
    pseudo_queue.dequeue()
    pseudo_queue.dequeue()
    pseudo_queue.dequeue()
    # Assert
    with pytest.raises(Exception):
        assert pseudo_queue.dequeue()
