from graph.graph import Graph
import pytest


def test_graph_depth_first_search_1(graph_1):
    actual = graph_1[0].depth_first_search(graph_1[1])
    expected = ['A', 'D', 'F', 'H', 'E', 'B', 'C', 'G']
    assert actual == expected


def test_graph_depth_first_search_2(graph_1):
    actual = graph_1[0].depth_first_search(graph_1[2])
    expected = ['D', 'F', 'H', 'E']
    assert actual == expected


def test_graph_depth_first_search_3(graph_1):
    actual = graph_1[0].depth_first_search(graph_1[3])
    expected = ['C', 'G']
    assert actual == expected

@pytest.fixture

def graph_1():

    graph = Graph()
    A = graph.add_node("A")
    B = graph.add_node("B")
    C = graph.add_node("C")
    D = graph.add_node("D")
    E = graph.add_node("E")
    F = graph.add_node("F")
    G = graph.add_node("G")
    H = graph.add_node("H")

    graph.add_edge(A, B)
    graph.add_edge(A, D)
    graph.add_edge(B, C)
    graph.add_edge(B, D)
    graph.add_edge(C, G)
    graph.add_edge(D, E)
    graph.add_edge(D, H)
    graph.add_edge(D, F)
    graph.add_edge(H, F)

    return graph, A, D, C



