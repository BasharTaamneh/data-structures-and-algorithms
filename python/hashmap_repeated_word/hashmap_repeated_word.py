class Node():
    """
    Node class creates Node instances.

    Arguments:
    ---

    value: --> any
    next_: --> Node
    """

    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_


class LinkedList:
    """
    creates Linked Lists instances.

    Arguments:
    ---
    self.head: --> default head is None

    ---

    Methodes
    ---
    insert(self, value): --> Adds nodes to the head of the list.

        Arguments:
        ---
        value: --> any
        Return: --> None
    """

    def __init__(self):
        self.head = None

    def insert(self, value):
        self.head = Node(value, self.head)


class HashTable():
    """
    HashTable is a data structue that stores key/value data pairs.

    Arguments:
    ---
    size: int, number of buckets in the hash table

    ---

    Methods:
    ---
        __hash:
            A method to convert a string into an index number.
            Arguments:
            key: --> str
            Return: --> int, index number
    ------------------------------------------------------------
            add:
            A method to add data pairs to Hash Table.
            Arguments:
            key: --> str
            value: --> str
            Return: --> None
    ------------------------------------------------------------
            contains:
            A method to check if the key exists in the hash table.
            Arguments:
            key: --> str
            Return: --> Boolean.
    ------------------------------------------------------------
            repeated_word:
            A method to return the repeated_word in a givin string if the givin string exists in the hash table.
            Arguments:
            txt: --> str
            Return: --> str.
    """

    def __init__(self, size=1024):
        self.__size = size
        self.keys = []
        self.__buckets = [None] * self.__size

    def __hash(self, key):
        self.keys.append(key)
        return (sum([ord(char) for char in key]) * 1024 % self.__size)


    def repeated_word(self, txt):
        if self.check_repeated(txt) == None:
            return "this is not an existing string --> No matched data"
        else:
            return self.check_repeated(txt)

    def check_repeated(self, txt):
        if self.__buckets[self.__hash(txt)]:
            current = self.__buckets[self.__hash(txt)].head

            while current:
                if current.value[1] == txt:
                    current = current.value[1].split(" ")
                    checker = []
                    for item in current:
                        item = item.replace(",", "").replace(
                            ".", "").replace("!", "").replace("?", "").replace("-", "").replace(";", "").replace(":", "").replace("'", "").replace("_", "")
                        if item.title() in checker:
                            checker = []
                            return item.title()
                        else:
                            checker.append(item.title())

                current = current.next



    def add(self, key, value):

        index = self.__hash(key)
        if not self.__buckets[index]:
            self.__buckets[index] = LinkedList()
        self.__buckets[index].insert([key, value])





if __name__ == '__main__':
    hashtable = HashTable()
    hashtable.add('C', "Once upon a time, there was a brave princess")
    print(hashtable.repeated_word(["dndn"]))


