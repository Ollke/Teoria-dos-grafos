import Graph

graph = Graph.graph()

graph.read("graph.txt")

graph.showGrafo()
print(graph.ehRegular())
print(graph.ehCompleto())
print(graph.ehConexo())

#insira o vertice
graph.getAdj("101")