import Graph

graph = Graph.graph()

graph.read("graph.txt")

graph.showGrafo()
print(graph.ehRegular())
print(graph.ehCompleto())
graph.getAjc("101")
