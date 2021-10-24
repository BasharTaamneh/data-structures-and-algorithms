class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


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
        return self.top is None


class PseudoQueue():

    def __init__(self, top=None, rear=None):
        self.top = top
        self.rear = rear
        self.base_stk = Stack()
        self.reverse_stk = Stack()

    def enqueue(self, value):

        if not self.top:
            self.reverse_stk.push(value)
            self.top = Node(self.reverse_stk.peek())
            self.rear = self.top
            self.reverse_stk.pop()
        else:
            self.reverse_stk.push(value)
            current = self.reverse_stk.top
            while current:
                self.base_stk.push(self.reverse_stk.peek())
                self.reverse_stk.pop()
                current = self.reverse_stk.top
            current = self.base_stk.top
            while current:
                self.rear.next = Node(self.base_stk.peek())
                self.base_stk.pop()
                self.rear = self.rear.next
                current = self.base_stk.top

    def dequeue(self):
        dispose = ''
        if not self.top:
            raise Exception("Queue is empty.")
        else:
            current = self.top
            while current:
                self.reverse_stk.push(current.value)
                current = current.next
            current = self.reverse_stk.top
            while current:
                self.base_stk.push(self.reverse_stk.peek())
                self.reverse_stk.pop()
                current = self.reverse_stk.top
            dispose = self.base_stk.peek()
            self.base_stk.pop()
            if self.base_stk.top:
                self.top = Node(self.base_stk.peek())
            self.rear = self.top
            if self.base_stk.top:
                self.base_stk.pop()
                current = self.base_stk.top
                while current:
                    self.rear.next = Node(self.base_stk.peek())
                    self.base_stk.pop()
                    self.rear = self.rear.next
                    current = self.base_stk.top
            else:
                self.top = None
                self.rear = self.top
            return dispose
