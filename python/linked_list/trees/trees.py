from collections import deque
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

    | Add(self, value): | ==> To adding into a tree ware use the same node class created above and add a Add class to it. The insert class compares the value of the node to the parent node and decides to add it as a left node or a right node.
    The largest numbers from the root to the right and the least numbers to the left.

    Argoments: value --> (Number to add)

    ---
    | contain(self, key): | ==> To searching for a value in a tree comparing the incoming value with the value exiting nodes. and then traverse the nodes from left to right and then finally with the parent. If the searched for values does not match any of the exiting value, then it's return False, else If the searched for value does match any of the exiting values, then it's return True.

    Argoments: key --> (Search for Number)
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

    def contain(self, key):
        if key < self.data:
            if self.left is None:
                print("{} is not found".format(key))
                return False
            return self.left.contain(key)
        elif key > self.data:
            if self.right is None:
                print("{} is not found".format(key))
                return False
            return self.right.contain(key)
        else:
            if key == self.data:
                print("{} is found".format(key))
                return True


class BinaryTree:
    """
    | BinaryTree Depth-first traversal class | is where we prioritize going through the depth (height) of the tree first.
    This class supports three methods to carry out depth-first traversal.

    Arguments
    ---
    res = [ ] --> (to hold the methods output)

    Methods
    ---
    | __init__(self, res=[]): | ==> instantiate data structure with empty list

    ---
    | inorder(self, root): | ==> In this traversal method, the left subtree is visited first, then the root, and later the right sub-tree.
    The In-order traversal logic is implemented by creating an empty list and adding the left node first followed by the root or parent node and then the left node is added to complete the In-order traversal.
    This process is repeated for each sub-tree until all the nodes are traversed.

    Argoments: root --> (root Node)

    ---
    | Preorder(self, root): | ==> In this traversal method, the root node is visited first, then the left subtree, and later the right subtree.
    the Pre-order traversal logic is implemented by creating an empty list and adding the root node first followed by the left node and then the right node is added to complete the Pre-order traversal.
    this process is repeated for each sub-tree until all the nodes are traversed.

    Argoments: root --> (root Node)

    ---
    | Postorder(self, root): | ==> In this traversal method, the root node is visited last, hence the name. First, we traverse the left subtree, then the right subtree, and later the root node.
    the Post-order traversal logic is implemented by creating an empty list and adding the left node first followed by the right node and then the root or parent node is added to complete the Post-order traversal.
    this process is repeated for each sub-tree until all the nodes are traversed.

    Argoments: root --> (root Node)
    """

    def __init__(self, res=[]):
        self.res = res

    # In-order: left >> root >> right
    def inorder(self, root):
        if root.left:
            self.inorder(root.left)

        self.res.append(root.data)

        if root.right:
            self.inorder(root.right)
        return self.res

    # Pre-order: root >> left >> right
    def Preorder(self, root):
        self.res.append(root.data)

        if root.left:
            self.Preorder(root.left)

        if root.right:
            self.Preorder(root.right)
        return self.res

    # Post-order: left >> right >> root
    def Postorder(self, root):
        if root.left:
            self.Postorder(root.left)

        if root.right:
            self.Postorder(root.right)

        self.res.append(root.data)
        return self.res

















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
    root.Add(310)
    root.Add(310)

    #          27
    #       /     \
    #     15       35
    #    /        /  \
    #  10      100   201
    #                  \
    #                  310
    #                    \
    #                    310
    #                      \
    #                      310

    # Searching for a value in a tree involves comparing the incoming value with the value exiting nodes. Here also traverse the nodes from left to right and then finally with the parent. returns True OR False.
    # print(root.contain(1000))
    # print(root.contain(10))
    # print(root.contain(1020))
    # print(root.contain(100))

    BT = BinaryTree()
    print(BT.inorder(root))
    # print(BT.Preorder(root))
    # print(BT.Postorder(root))
