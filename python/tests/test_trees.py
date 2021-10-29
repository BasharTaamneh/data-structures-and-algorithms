from linked_list.trees.trees import Node, BinaryTree

def test_import():
    assert Node("")
    assert BinaryTree()


def test_instantiate_an_empty_tree():
    assert Node("")


# def test_instantiate_tree_with_a_single_root_node():
#     root = Node(0)
#     actual = root.data
#     expected = 0
#     assert actual == expected
