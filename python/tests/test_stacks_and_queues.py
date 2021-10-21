from _pytest.config import exceptions
from linked_list.stacks_and_queues.stacks_and_queues import Node, Stack, Queue
import pytest


def test_stacks_and_queues():
    assert Stack(), Queue()


#stack_test---------------------------------#

#decorator
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



# # queue_test---------------------------------#

# # decorator
@pytest.fixture
def queue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue("Python")
    return queue

def test_enqueue(queue):
    actual = queue.rear.value
    expected = "Python"
    assert actual == expected

# def test_dequeue(queue):
#     actual = queue.front.value
#     expected = 1
#     assert actual == expected


# def test_dequeue_with_empty_queue():
#     with pytest.raises(Exception):
#         assert Queue() == "Dequeue from empty queue."

# def test_peek_queue(queue):
#     actual = queue.peek()
#     expected = 1
#     assert actual == expected

# def test_peek_with_empty_queue():
#     with pytest.raises(Exception):
#         assert Queue() == "This Queue is empty"

# def test_is_empty():
#     assert Queue().is_empty()
