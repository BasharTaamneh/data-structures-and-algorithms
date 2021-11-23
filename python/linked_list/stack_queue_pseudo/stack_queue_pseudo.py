from collections import deque


class PseudoQueue:

    # Constructor
    def __init__(self):
        self.s1 = deque()
        self.s2 = deque()

    # Add an item to the queue
    def enqueue(self, data):
        # Move all elements from the first stack to the second stack
        while len(self.s1):
            self.s2.append(self.s1.pop())
        # push item into the first stack
        self.s1.append(data)
        # Move all elements back to the first stack from the second stack
        while len(self.s2):
            self.s1.append(self.s2.pop())

    # Remove an item from the queue
    def dequeue(self):
        # if the first stack is empty
        if not self.s1:
            raise Exception("Empty queue")
        # return the top item from the first stack
        return self.s1.pop()
