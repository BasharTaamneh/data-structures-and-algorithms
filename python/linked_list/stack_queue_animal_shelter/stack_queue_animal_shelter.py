class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class AnimalShelter:
    """
    AnimalShelter class queues which holds only dogs and cats.
     Arguments:
     head: Node
     rear: Node
    """
    def __init__(self):
        self.head = None
        self.rear = None

    def enqueue(self, animal):
        """
        This method adds a Cat or Dog object to the AnimalShelter class.

        Arguments
        ---
        animal: Cat or Dog class object
        """
        if animal.kind == "dog" or animal.kind == "cat":
            if self.head == None:
                self.head = Node(animal)
                self.rear = self.head
            else:
                self.rear.next = Node(animal)
                self.rear = self.rear.next
        else:
            print("AnimalShelter holds only dogs or cats.")
            return False

    def dequeue(self, pref):
        """
        This method eject a Cat or Dog class object from the AnimalShelter class.

        Arguments
        ---
        pref : Cat or Dog object
        Return: Dequeued Cat or Dog object.name || None
        """
        if pref == "dog" or pref == "cat":
            if self.head == None:
                raise Exception("AnimalShelter is empty.")
            if pref == self.head.data.kind:
                eject = self.head.data
                self.head = self.head.next
                if self.head is None:
                    self.rear = None
                return eject.name
        else:
            print("AnimalShelter has only dogs or cats.")
            return None

class Cat:
    """
    Cat class creates Cats.

    Arguments
    ---
    name : str
    kind: cat
    """
    def __init__(self, name, kind="cat"):
        self.name = name
        self.kind = kind


class Dog:
    """
    Dog class creates Dogs.

    Arguments
    ---
    name : str
    kind: dog
    """
    def __init__(self, name, kind="dog"):
        self.name = name
        self.kind = kind


class Anypit:
    """
    Dog class creates Dogs.

    Arguments
    ---
    name : str
    kind: dog
    """

    def __init__(self, name, kind="Anypit"):
        self.name = name
        self.kind = kind


if __name__ == '__main__':
    shelter = AnimalShelter()
    # dog = Dog("dog")
    # cat = Cat("cat")
    # mat = Cat("mat")
    # pat = Cat("pat")
    # bog = Dog("bog")
    # sog = Dog("sog")

    # nog = Anypit()
    # shelter.enqueue(nog)
    # shelter.dequeue("nog")


    # shelter.enqueue(mat)
    # shelter.enqueue(dog)
    # shelter.enqueue(bog)
    # shelter.enqueue(sog)
    # shelter.enqueue(cat)
    # shelter.enqueue(pat)

    # print("before", shelter.head.data.name)
    # print("before", (shelter.head.next).data.name)
    # print("before", (shelter.head.next).next.data.name)

    # shelter.dequeue("doog")

    # print("after", (shelter.head.data.name))
    # print("after", (shelter.head.next).data.name)
    # print("after", (shelter.head.next).next.data.name)
