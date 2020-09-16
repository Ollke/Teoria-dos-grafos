data = open("graph.txt","r")

graph = {}

for i in data:
    j = i.split()
    aux = []

    for r in range(1,len(j)):
        aux.append(j[r])

    graph[j[0]] = aux

data.close()

for i in graph:
    print(f"{i}:",end="")

    for j in graph[i]:
        print(f" {j}",end="")

    print(f" ({len(graph[i])} vertice(s) adjacente(s))")