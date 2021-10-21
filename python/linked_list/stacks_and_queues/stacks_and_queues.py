class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        node = Node(value)
        if not self.rear:
            self.front = node
            self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):

        if self.front is None:
            raise Exception("Dequeue from empty queue.")
        value = self.front.value
        self.front = self.front.next

        if self.front is None:
            self.rear = None
        return value


    def peek(self):
            if self.front == None:
                raise Exception("This Queue is empty")
            else:
                return self.front.value

    def is_empty(self):
        return not self.front

class Stack:

    def __init__(self):
        self.top = None

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.top == None:
            raise Exception("This stack is empty")
        temp = self.top
        self.top = self.top.next
        temp.next = None

        return temp.value

    def peek(self):
        if self.top == None:
            raise Exception("This stack is empty")
        else:
            return self.top.value

    def is_empty(self):
        pass
