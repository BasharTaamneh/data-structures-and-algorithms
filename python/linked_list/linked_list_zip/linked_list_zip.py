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

    # Main function that inserts nodes of linked list q into p at alternate positions.
    # Since head of first list never changes
    # but head of second list/ may change,
    # we need single pointer for first list and double pointer for second list.

    def merge(self, p, q):
        p_curr = p.head
        q_curr = q.head

        # swap their positions until one finishes off
        while p_curr != None and q_curr != None and self.head != None:

            # Save next pointers
            p_next = p_curr.next_
            q_next = q_curr.next_

            # make q_curr as next of p_curr
            q_curr.next_ = p_next  # change next pointer of q_curr
            p_curr.next_ = q_curr  # change next pointer of p_curr

            # update current pointers for next iteration
            p_curr = p_next
            q_curr = q_next
            q.head = q_curr

            # yield linked list from the Head
        while self.head != None:
            yield self.head.data
            self.head = self.head.next_



# # Driver program to test above functions
llist1 = LinkedList()
llist2 = LinkedList()
llist1.append(1)
llist1.append(3)
llist1.append(2)
llist1.append(4)
llist2.append(5)
llist2.append(9)
llist2.append(10)
llist2.append(12)
llist2.append(15)
llist2.merge(llist1, llist2)
dublist = []
for _ in llist1.merge(llist1, llist2):
    dublist.append(_)

print(dublist)
