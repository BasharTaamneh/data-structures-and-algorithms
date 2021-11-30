from graph.graph import Graph


def business_trip(graph, cities):
    cost = 0
    for i, city in enumerate(cities):
        edges = graph.get_neighbors(city)
        # if city ==  cities[len(cities) - 1]:
        #     return cost
        print(city.value, edges[-4].vertex.value)
        # if city == edges[0]:
        #     # print(edges[0].weight )
        #     cost += edges[0].weight
            # return cost
    #  

    # return f'${cost}'



graph = Graph()

pandora = graph.add_node('Pandora')
arendelle = graph.add_node('Arendelle')
metroville = graph.add_node('Metroville')
monstropolis = graph.add_node('Monstropolis')
narnia = graph.add_node('Narnia')
naboo = graph.add_node('Naboo')

graph.add_edge(pandora, arendelle, 150)
graph.add_edge(arendelle, pandora, 150)

graph.add_edge(pandora, metroville, 82)
graph.add_edge(metroville, pandora, 82)

graph.add_edge(arendelle, metroville, 99)
graph.add_edge(metroville, arendelle, 99)

graph.add_edge(arendelle, monstropolis, 42)
graph.add_edge(monstropolis, arendelle, 42)

graph.add_edge(metroville, monstropolis, 105)
graph.add_edge(monstropolis, metroville, 105)

graph.add_edge(metroville, naboo, 26)
graph.add_edge(naboo, metroville, 26)

graph.add_edge(monstropolis, naboo, 73)
graph.add_edge(naboo, monstropolis, 73)

graph.add_edge(metroville, narnia, 37)
graph.add_edge(narnia, metroville, 37)

graph.add_edge(narnia, naboo, 250)
graph.add_edge(naboo, narnia, 250)



lst_1 = [metroville, pandora]
lst_2 = [arendelle, monstropolis, naboo]
lst_3 = [naboo, pandora]
lst_4 = [narnia, arendelle, naboo]
lst_5 = [narnia, naboo, pandora]

print(business_trip(graph, lst_1))
