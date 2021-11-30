from collections import deque


class Vertex:
    """
  Class for Adding a node to the graph
  Arguments: value
  Returns: The added node
  """

    def __init__(self, value):
        """
    Initalization for a Vertex to hold a value.

    """
        self.value = value



class Queue:
    def __init__(self):
        self.dq = deque()

    def enqueue(self, value):
        self.dq.appendleft(value)

    def dequeue(self):
        self.dq.pop()

    def __len__(self):
        return len(self.dq)

class Stack:
    """
        Stack class creates Stack instances.
        Arguments: None
        Methods:
            push
                This method adds a Node to the top of stack.
                Arguments: value: any
                Return: None
            pop
                This method removes a Node to the top of stack.
                Arguments: None
                Return: None
            peek
                This method returns the Node on top of stack.
                Arguments: None
                Return: Node
    """

    def __init__(self):
        self.dq = deque()

    def __len__(self):
        return len(self.dq)

    def push(self, value):
        self.dq.append(value)

    def pop(self):
        return self.dq.pop()

    def peek(self):
        return self.dq[-1]

class Edge:
    """
    a class for Adding a new edge between two nodes in the graph
    If specified, assigning a weight to the edge
    Arguments: 2 nodes to be connected by the edge, weight (optional)
    Returns: nothing

  """

    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight


class Graph:
    def __init__(self):
        """
    Initalization for a hashmap to hold the vertices
    """
        self.__adjacency_list = {}

    def add_node(self, value):
        """
      Method for Adding a node to the graph
      Arguments: value
      Returns: The added node
    """
        # new node
        v = Vertex(value)
        self.__adjacency_list[v] = []
        return v

    def size(self):
        return len(self.__adjacency_list)

    def add_edge(self, start_vertex, end_vertex, weight=0):
        """Adds an edge to the graph"""
        if start_vertex not in self.__adjacency_list:
            raise KeyError("Start Vertex not found in graph")

        if end_vertex not in self.__adjacency_list:
            raise KeyError("End Vertex not found in graph")

        edge = Edge(end_vertex, weight)
        self.__adjacency_list[start_vertex].append(edge)

    def get_nodes(self):
        """
    Method to get all nodes in Graph
    Arguments: None
    return: All nodes
    """
        return self.__adjacency_list.keys()

    def get_neighbors(self, vertex):
        """ """
        return self.__adjacency_list.get(vertex, [])


    def breadth_first_search(self, start_vertex, action=(lambda start_vertex: None)):
        queue = []
        visited = set()
        nodes = []
        try:
            queue.append(start_vertex)
            visited.add(start_vertex)

            while len(queue):

                current_vertex = queue.pop(0)
                nodes.append(current_vertex.value)
                action(current_vertex)
                neighbors = self.get_neighbors(current_vertex)

                for edge in neighbors:
                    neighbor = edge.vertex
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

            return nodes
        except:
            raise Exception("TypeError: please check your input and try again with valid input")

    def depth_first_search(self, start_vertex):
        stack = []
        visited = set()
        nodes = []
        try:
            stack.append(start_vertex)
            visited.add(start_vertex)

            while len(stack):

                current_vertex = stack.pop()
                nodes.append(current_vertex.value)
                neighbors = self.get_neighbors(current_vertex)
                for edge in neighbors:
                    neighbor = edge.vertex
                    if neighbor not in visited:
                        visited.add(neighbor)
                        stack.append(neighbor)

            return nodes
        except:
            raise Exception(
                "TypeError: please check your input and try again with valid input")






