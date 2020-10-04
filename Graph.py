class graph():

    def __init__(self):
        self.vertices = []
        self.grafo = {}

    def showGrafo(self):

        for i in self.grafo.keys():

            print(f"{i}:",end='')

            for j in self.grafo[i].keys():
                print(f" {j} "+f"Peso:{self.grafo[i][j]}|",end="")

            print("")




    def ehRegular(self):
        regular = True
        aux = []

        for i in self.grafo.keys():
            aux.append(i)

        y = len(self.grafo[aux[0]])

        if aux[0] in self.grafo[aux[0]]:
            y = y + 1

        for i in self.grafo.keys():
            x = len(self.grafo[i])

            if i in self.grafo[i]:
                x = x+1

            if x != y:
                regular = False
                break
        return regular


    def ehCompleto(self):
        completo = True
        vertices = []

        for i in self.grafo.keys():
            vertices.append(i)

        for i in self.grafo.keys():
            adj = [i]

            for j in self.grafo[i].keys():
                adj.append(j)

            for k in vertices:
                if k in adj:
                    completo = True
                else:
                    completo = False
                    break


            if completo == False:
                break

        return completo

    def read(self,arquivo):
        data = open(arquivo, "r")

        for i in data:
            j = i.split()
            adj = {}

            for r in range(1, len(j),2):
                adj[j[r]] = j[r+1]

            self.grafo[j[0]] = adj

        data.close()

        for i in self.vertices:
            i.setArestas()

#WIP
    def ehConexo(self):
        loop = True

        p = [self.vertices[0]]
        visitados = [self.vertices[0].getVertice()]
        nVisitados = []

        for j in self.vertices:
            nVisitados.append(j)

        while p != []:

            while nVisitados != []:
                todosVisitados = len(p[len(p)-1].getAjc())

                for i in p[len(p)-1].getAjc():
                    todosVisitados = todosVisitados - 1

                    if i not in visitados:
                        visitados.append(i)

                        for j in self.vertices:
                            if j.getVertice() == i:
                                p.append(j)

                        break



            p.pop()

        return len(visitados) == len(self.vertices)

    def getAjc(self,vertice):
        vertices = []

        for i in self.grafo.keys():
            vertices.append(i)

        if vertice in vertices:
            print(f"{vertice}:", end='')

            for j in self.grafo[vertice].keys():
                print(f" {j} " + f"Peso:{self.grafo[vertice][j]}|", end="")

            print("\n")

        else:
            print("O vertice não esta no vetor\n")




