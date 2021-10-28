

class Node:
    """
    class Node create a tree data structures.
    designate one node as root node and then add more nodes as child nodes.

    Methodes
    ---
    __init__(self, data):

    instantiate data structure

    Arguments
    ---
    # left = None

    # right = None

    data = data
    """
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def Add(self, data):
        if self.data:
            if data == self.data:
                print("warning ({}) is already existe ".format(data))

            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.Add(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.Add(data)
        else:
            self.data = data



class BinaryTree:

    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)
        return res

    def PreorderTraversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.PreorderTraversal(root.left)
            res = res + self.PreorderTraversal(root.right)
        return res

    def PostorderTraversal(self, root):
        res = []
        if root:
            res = self.PostorderTraversal(root.left)
            res = res + self.PostorderTraversal(root.right)
            res.append(root.data)
        return res



root = Node(27)
root.Add(15)
root.Add(35)
root.Add(10)
root.Add(100)
root.Add(100)
root.Add(100)
root.Add(100)
root.Add(100)
root.Add(101)
root.Add(110)

BT = BinaryTree()
print(BT.PostorderTraversal(root))


