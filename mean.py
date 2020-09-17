import Graph

graph = Graph.graph()

graph.read("graph.txt")

graph.showVectors()

print(graph.ehRegular())
print(graph.ehCompleto())
