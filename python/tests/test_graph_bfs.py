from graph.graph import Graph
import pytest


def test_graph_breadth_first_search_1(graph):
    actual = graph[0].breadth_first_search(graph[1])
    expected = [1, 2, 4, 10, 5]
    assert actual == expected


def test_graph_breadth_first_search_2(graph):
    actual = graph[0].breadth_first_search(graph[2])
    expected = [4, 10, 5, 1, 2]
    assert actual == expected


@pytest.fixture
def graph():
    graph = Graph()

    v1 = graph.add_node(1)
    v2 = graph.add_node(2)
    v3 = graph.add_node(10)
    v4 = graph.add_node(4)
    v5 = graph.add_node(5)

    graph.add_edge(v1, v2)
    graph.add_edge(v2, v4)
    graph.add_edge(v3, v5)
    graph.add_edge(v4, v3)
    graph.add_edge(v5, v1)
    return graph, v1, v4

