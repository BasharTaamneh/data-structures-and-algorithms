from tree_intersection.tree_intersection import tree_intersection
from trees.trees import Node
import pytest


def test_tow_string_tree_intersections(trees_str_1, trees_str_2):
    tree_1 = trees_str_1
    tree_2 = trees_str_2
    actual = tree_intersection(tree_1, tree_2)
    expected = {'175', '500', '125', '200', '100', '350', '160'}
    assert actual == expected


def test_tow_tree_intersections(trees_1, trees_2):
    tree_1 = trees_1
    tree_2 = trees_2
    actual = tree_intersection(tree_1, tree_2)
    expected = {160, 100, 200, 175, 500, 125, 350}
    assert actual == expected


def test_tow_tree_with_no_intersections(trees_1):
    tree_1 = trees_1
    tree_2 = Node(0)
    tree_2.Add(1000)

    actual = tree_intersection(tree_1, tree_2)
    expected = "There is no intersections in this trees"
    assert actual == expected


@pytest.fixture
def trees_str_1():
    tree_1 = Node("150")
    tree_1.Add("100")
    tree_1.Add("250")
    tree_1.Add("75")
    tree_1.Add("160")
    tree_1.Add("200")
    tree_1.Add("350")
    tree_1.Add("125")
    tree_1.Add("175")
    tree_1.Add("300")
    tree_1.Add("500")
    return tree_1


@pytest.fixture
def trees_str_2():
    tree_2 = Node("42")
    tree_2.Add("100")
    tree_2.Add("600")
    tree_2.Add("15")
    tree_2.Add("160")
    tree_2.Add("200")
    tree_2.Add("350")
    tree_2.Add("125")
    tree_2.Add("175")
    tree_2.Add("4")
    tree_2.Add("500")
    return tree_2


@pytest.fixture
def trees_1():
    tree_1 = Node(150)
    tree_1.Add(100)
    tree_1.Add(250)
    tree_1.Add(75)
    tree_1.Add(160)
    tree_1.Add(200)
    tree_1.Add(350)
    tree_1.Add(125)
    tree_1.Add(175)
    tree_1.Add(300)
    tree_1.Add(500)
    return tree_1


@pytest.fixture
def trees_2():
    tree_2 = Node(42)
    tree_2.Add(100)
    tree_2.Add(600)
    tree_2.Add(15)
    tree_2.Add(160)
    tree_2.Add(200)
    tree_2.Add(350)
    tree_2.Add(125)
    tree_2.Add(175)
    tree_2.Add(4)
    tree_2.Add(500)
    return tree_2
