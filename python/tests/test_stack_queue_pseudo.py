from linked_list.stack_queue_pseudo.stack_queue_pseudo import  PseudoQueue
import pytest

# Pseudo Queue Tests
# -------------------------------------------------------------------

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


def test_pseudo_dequeue_empty():
    # Assert
    with pytest.raises(Exception):
        assert PseudoQueue.dequeue()


def test_pseudo_queue_enqueue_value(pseudo_queue_1):
    # Arrange
    expected = 1
    # Act
    actual = pseudo_queue_1.dequeue()
    # Assert
    assert actual == expected


def test_pseudo_queue_enqueue_multiple(pseudo_queue):
    # Arrange
    expected_1 = 0
    expected_2 = 7
    # Act
    actual_1 = pseudo_queue.dequeue()
    actual_2 = pseudo_queue.dequeue()
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
    pseudo_queue.dequeue()
    pseudo_queue.dequeue()
    pseudo_queue.dequeue()
    pseudo_queue.dequeue()
    pseudo_queue.dequeue()
    with pytest.raises(Exception):
        assert pseudo_queue.dequeue()
