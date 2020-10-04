class graph():

    def __init__(self):
        self.vertices = {}
        self.grafo = {}

    def showGrafo(self):

        for i in self.grafo.keys():

            print(f"{i}: ",end='')

            for j in self.grafo[i].keys():
                print(f"{j} "+f"Peso {self.grafo[i][j]} |",end="")

            print("")


#wip
    def ehRegular(self):
        regular = True
        y = len(self.vertices[0].getAjc())
        for i in self.vertices:
            x = len(i.getAjc())

            if i.getVertice() in i.getAjc():
                x = x+1

            if x != y:
                regular = False
                break
        return regular

#wip
    def ehCompleto(self):
        completo = True
        vertices = []

        for i in self.vertices:
            vertices.append(i.getVertice())

        for i in self.vertices:
            y = i.getAjc()

            for j in vertices:
                if ((j in y) or (j == i.getVertice())) :
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



