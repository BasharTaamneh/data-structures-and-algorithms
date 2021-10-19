

# A Linked List Node
class Node:
    """
Node class demonstrate all insertion methods of linked list

Attribute
----------

(self, data)

Methodes
-----------

__init__(self, data):\n
function to initialise the node object
Assign data, Initialize next as null.
    """

    def __init__(self, data):
        self.data = data
        self.next_ = None


class LinkedList:
    """
Linked List class contains a Node object

Methodes
----------

__init__():\n
Function to initialize head

append(self, new_data):\n
This function is defined in Linked List class
Appends a new node at the end. This method is
defined inside LinkedList.

getKthFromEnd(self, k):\n
Iterative function to return the k'th node from the end in a linked list
    """
    def __init__(self):
        self.head = None

    def append(self, new_data):
        # 1. Create a new node
        # 2. Put in the data
        # 3. Set next as None
        new_node = Node(new_data)
        # 4. If the Linked List is empty, then make the
        # new node as head
        if self.head is None:
            self.head = new_node
            return
        # 5. Else traverse till the last node
        last = self.head
        while (last.next_):
            last = last.next_
        # 6. Change the next of last node
        last.next_ = new_node

    def getKthFromEnd(self, k):
        n = 0
        curr = self.head.next_
        # count the total number of nodes in the linked list
        while curr:
            curr = curr.next_
            n = n + 1
        # if the total number of nodes is more than or equal to `k`
        if k < 0:
            return "'k' value was rejected --> negative value"
        if n >= k:
            # return (n-k+1)'th node from the beginning
            curr = self.head
            for i in range(n - k):
                curr = curr.next_
        try:
            return curr.data
        except AttributeError:
            return "'Kth' --> is out of range"


if __name__ == '__main__':
    ll = LinkedList()
    ll.append(1)
    ll.append(3)
    ll.append(8)
    ll.append(2)
    print(ll.getKthFromEnd(0))
