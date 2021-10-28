from linked_list.stack_queue_brackets.stack_queue_brackets import validate_brackets


def test_validate_brackets_1():
    actual = validate_brackets({})
    expected = True
    assert actual == expected

