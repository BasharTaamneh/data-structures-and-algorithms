from linked_list.stack_queue_brackets.stack_queue_brackets import validate_brackets


def test_validate_brackets_1():
    actual = validate_brackets({})
    expected = True
    assert actual == expected


def test_validate_brackets_2():
    actual = validate_brackets("{}(){}")
    expected = True
    assert actual == expected


def test_validate_brackets_3():
    actual = validate_brackets("()[[Extra Characters]]")
    expected = True
    assert actual == expected


def test_validate_brackets_4():
    actual = validate_brackets("(){}[[]]")
    expected = True
    assert actual == expected


def test_validate_brackets_5():
    actual = validate_brackets("{}{Code}[Fellows](())")
    expected = True
    assert actual == expected
