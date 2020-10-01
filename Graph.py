class graph():

    def __init__(self):
        self.vertices = []

    def showVectors(self):
        for i in self.vertices:
            i.showVertice()

    def ehRegular(self):
        regular = True
        y = len(self.vertices[0].getAjc())
        for i in self.vertices:
            x = len(i.getAjc())
            if x != y:
                regular = False
                break
        return regular

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
            adj = []
            pesos = []

            for r in range(1, len(j),2):
                adj.append(j[r])
                pesos.append(j[r+1])

            self.vertices.append(vector(j[0], adj,pesos))

        data.close()

        for i in self.vertices:
            i.setArestas()


class vector():

    def __init__(self,vertice,adj,pesos):
        self.vertice = vertice
        self.verticeAjc = adj
        self.arestas = []
        self.pesos = pesos

    def showVertice(self):
        print(f"{self.vertice}:", end="")

        for j in range(0,len(self.verticeAjc)):
            print(f" {self.verticeAjc[j]}",end="")
            print(f" peso: {self.pesos[j]}|",end="")


        print(f" ({len(self.verticeAjc)} vertice(s) adjacente(s))")

    def getAjc(self):
        return self.verticeAjc

    def getVertice(self):
        return self.vertice

#wip
    def setArestas(self):
        for i in range(0,len(self.verticeAjc)):
            self.arestas.append([self.vertice,self.verticeAjc[i],self.pesos[i]])

#wip
    def showArestas(self):

        print("Arestas =",end="")

        for i in self.arestas:
            print(f" [{i[0]},"+f"{i[1]}]"+f" peso: {i[2]}|",end="")

        print("")