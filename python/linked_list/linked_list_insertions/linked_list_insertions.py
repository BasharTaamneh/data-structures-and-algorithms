# pylint: disable=missing-module-docstring
# pylint: disable=invalid-name
# pylint: disable=missing-function-docstring


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
        self.next = None

class LinkedList:
    """
Linked List class contains a Node object

Methodes
----------
__init__():\n
Function to initialize head

push(self, new_data):\n
Function to insert a new node at the beginning

insertAfter(self, prev_node, new_data):\n
This function is in LinkedList class. Inserts a
new node after the given prev_node. This method is
defined inside LinkedList class.

append(self, new_data):\n
This function is defined in Linked List class
Appends a new node at the end. This method is
defined inside LinkedList.

    """

    def __init__(self):
        self.head = None

    def push(self, new_data):
        # 1 & 2: Allocate the Node &
        #	 Put in the data
        new_node = Node(new_data)
        # 3. Make next of new Node as head
        new_node.next = self.head
        # 4. Move the head to point to new Node
        self.head = new_node

    def insertAfter(self, prev_node, new_data):
        # 1. check if the given prev_node exists
        if prev_node is None:
            # The given previous node must inLinkedList.
            return
        # 2. create new node & Put in the data
        new_node = Node(new_data)
        # 4. Make next of new Node as next of prev_node
        new_node.next = prev_node.next
        # 5. make next of prev_node as new_node
        prev_node.next = new_node

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
        while (last.next):
            last = last.next
        # 6. Change the next of last node
        last.next = new_node
        
        # Utility function to print the linked list
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next


# Code execution starts here
if __name__ == '__main__':

    # Start with the empty list
    llist = LinkedList()

    # Insert 6. So linked list becomes 6->None
    llist.append(6)

    # Insert 7 at the beginning. So linked list becomes 7->6->None
    llist.push(7)

    # Insert 1 at the beginning. So linked list becomes 1->7->6->None
    llist.push(1)

    # Insert 4 at the end. So linked list becomes 1->7->6->4->None
    llist.append(4)
    llist.append(400)
    # Insert 8, after 7. So linked list becomes 1 -> 7-> 8-> 6-> 4-> None
    llist.insertAfter(llist.head.next, 8)

    print('Created linked list is:')
    llist.printList()

