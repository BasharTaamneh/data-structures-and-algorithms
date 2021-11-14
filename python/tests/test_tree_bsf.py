from linked_list.tree_bsf.tree_bsf import Node, bfs

#          27
#         /  \
#       15    35
#      /        \
#    10         100
#                 \
#                 201
#                   \
#                   310
#                  /   \
#                 310  410

def test_tree_breadth_first_1():
    root = Node(27)
    root.Add(15)
    root.Add(35)
    root.Add(10)
    root.Add(100)
    root.Add(201)
    root.Add(310)
    root.Add(410)
    root.Add(310)
    actual = bfs(root)
    expected = [27, 15, 35, 10, 100, 201, 310, 310, 410]
    assert actual == expected


def test_tree_breadth_first_2():
    root = Node(30)
    root.Add(15)
    root.Add(40)
    root.Add(12)
    root.Add(100)
    root.Add(200)
    root.Add(310)
    root.Add(500)
    root.Add(310)
    actual = bfs(root)
    expected = [30, 15, 40, 12, 100, 200, 310, 310, 500]
    assert actual == expected
