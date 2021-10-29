from linked_list.trees.trees import Node, BinaryTree

def test_import():
    assert Node("")
    assert BinaryTree()


def test_instantiate_an_empty_tree():
    assert Node("")


def test_instantiate_tree_with_a_single_root_node():
    root = Node(0)
    actual = root.data
    expected = 0
    assert actual == expected


def test_add_a_left_child_and_right_child_to_a_single_root_node():
    root = Node(0)
    root.Add(0)
    root.Add(1)
    actual_1 = root.left.data
    actual_2 = root.right.data
    expected_1 = 0
    expected_2 = 1
    assert actual_1 == expected_1
    assert actual_2 == expected_2

