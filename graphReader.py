import Graph

data = open("graph.txt","r")

graph = Graph.graph()

for i in data:
    j = i.split()
    aux = []

    for r in range(1,len(j)):
        aux.append(j[r])

    graph.addVector(j[0],aux)

data.close()

graph.showVectors()

print(graph.ehRegular())
print(graph.ehCompleto())


