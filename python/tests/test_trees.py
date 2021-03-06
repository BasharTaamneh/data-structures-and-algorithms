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


def test_return_a_collection_from_a_preorder_traversal():
    BT = BinaryTree()
    root = Node(27)
    root.Add(15)
    root.Add(35)
    root.Add(10)
    root.Add(100)
    root.Add(201)
    root.Add(310)
    root.Add(310)
    root.Add(310)
    actual = BT.Preorder(root)
    expected = [27, 15, 10, 35, 100, 201, 310, 310, 310]
    assert actual == expected


def test_return_a_collection_from_an_inorder_traversal():
    BT = BinaryTree()
    root = Node(27)
    root.Add(15)
    root.Add(35)
    root.Add(10)
    root.Add(100)
    root.Add(201)
    root.Add(310)
    root.Add(310)
    root.Add(310)
    actual = BT.inorder(root)
    expected = [10, 15, 27, 35, 100, 201, 310, 310, 310]
    assert actual == expected


def test_return_a_collection_from_a_postorder_traversal():
    BT = BinaryTree()
    root = Node(27)
    root.Add(15)
    root.Add(35)
    root.Add(10)
    root.Add(100)
    root.Add(201)
    root.Add(310)
    root.Add(310)
    root.Add(310)
    actual = BT.Postorder(root)
    expected = [10, 15, 310, 310, 310, 201, 100, 35, 27]
    assert actual == expected


def test_if_a_tree_contain_a_node_at_least_once():
    root = Node(27)
    root.Add(15)
    root.Add(35)
    root.Add(10)
    root.Add(100)
    root.Add(201)
    root.Add(310)
    root.Add(310)
    root.Add(310)
    actual_1 =  root.contain(1000)
    actual_2 = root.contain(10)
    actual_3 = root.contain(27)
    expected_1 = False
    expected_2 = True
    expected_3 = True
    assert actual_1 == expected_1
    assert actual_2 == expected_2
    assert actual_3 == expected_3
