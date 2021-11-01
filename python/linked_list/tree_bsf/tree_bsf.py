class Node:
    """
    class Node create a tree data structures.
    designate one node as root node and then add more nodes as child nodes.
    One node to marked as Root node --> Root Node.
    Every node other than the root is associated with one parent node.
    Each node can have an arbiatry number of chid node.
    Arguments
    ---
    left = None --> (pointer)
    right = None --> (pointer)
    data = data --> (Node data)
    Methodes
    ---
    | __init__(self, data): | ==> instantiate data structure with nodes data
    """

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def Add(self, value):
        if value <= self.data:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.Add(value)
        elif value >= self.data:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.Add(value)

def bfs(root):
    res = []
    thislevel = [root]
    while thislevel:
        nextlevel = []
        for n in thislevel:
            res.append(n.data)
            if n.left:
                nextlevel.append(n.left)
            if n.right:
                nextlevel.append(n.right)
        thislevel = nextlevel
    return res


if __name__ == "__main__":
    # create a Node class and add assign a value to the node. This becomes tree with only a root node
    root = Node(27)
    # To Add() into a tree we use the same node class created above and add a insert class to it. The insert class compares the value of the node to the parent node and decides to add it as a left node or a right node.
    root.Add(15)
    root.Add(35)
    root.Add(10)
    root.Add(100)
    root.Add(201)
    root.Add(310)
    root.Add(410)
    root.Add(310)
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

    print(bfs(root))


