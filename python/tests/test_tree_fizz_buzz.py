from linked_list.tree_fizz_buzz.tree_fizz_buzz import KTree


def test_fizz_buzz_tree_1():
    k = 3
    list_ = [1, 2, 3, 4, 5, 6, 7, 8, 15, 30, 60]
    node = KTree(k, list_)
    actual = node.fizz_buzz_tree()
    expected = ["1", "2", "Fizz", "4", "Buzz","Fizz", "7", "8", "FizzBuzz", "FizzBuzz", "FizzBuzz"]
    assert actual == expected


def test_fizz_buzz_tree_2():
    k = 3
    list_ = []
    for _ in range(3, 100, 2):
        list_.append(_)
    node = KTree(4, list_)
    actual = node.fizz_buzz_tree()
    expected = ['Fizz', 'Buzz', '7', 'Fizz', '11', '13', 'FizzBuzz', '17', '19', 'Fizz', '23', 'Buzz', 'Fizz', '29', '31', 'Fizz', 'Buzz', '37', 'Fizz', '41', '43', 'FizzBuzz', '47', '49','Fizz', '53', 'Buzz', 'Fizz', '59', '61', 'Fizz', 'Buzz', '67', 'Fizz', '71', '73', 'FizzBuzz', '77', '79', 'Fizz', '83', 'Buzz', 'Fizz', '89', '91', 'Fizz', 'Buzz', '97', 'Fizz']
    assert actual == expected
    list_ = []

