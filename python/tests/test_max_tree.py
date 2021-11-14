from linked_list.max_tree.max_tree import Node, BinaryTree



def test_return_max_node_value_from_binarytree():

    BT = BinaryTree()

    root = Node(1)
    root.Add(2)
    root.Add(3)
    root.Add(4)
    root.Add(5)
    root.Add(100)
    root.Add(20)
    root.Add(30)
    root.Add(40)

    root2 = Node(100)
    root2.Add(2)
    root2.Add(11)
    root2.Add(38)
    root2.Add(7)
    root2.Add(1000)
    root2.Add(55)
    root2.Add(63)
    root2.Add(9)

    actual_1 = BT.tree_max_(root)
    actual_2 = BT.tree_max_(root2)

    expected_1 = 100
    expected_2 = 1000

    assert actual_1 == expected_1
    assert actual_2 == expected_2



