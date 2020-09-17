class graph():

    def __init__(self):
        self.vectors = []

    def showVectors(self):
        for i in self.vectors:
            i.showVector()

    def ehRegular(self):
        regular = True
        y = len(self.vectors[0].getAjc())
        for i in self.vectors:
            x = len(i.getAjc())
            if x != y:
                regular = False
                break
        return regular

    def ehCompleto(self):
        completo = True
        vectors = []

        for i in self.vectors:
            vectors.append(i.getVector())

        for i in self.vectors:
            y = i.getAjc()

            for j in vectors:
                if ((j in y) or (j == i.getVector())) :
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

            self.vectors.append(vector(j[0], adj,pesos))

        data.close()

        for i in self.vectors:
            i.setArestas()


class vector():

    def __init__(self,vector,adj,pesos):
        self.vector = vector
        self.vectorAjc = adj
        self.arestas = []
        self.pesos = pesos

    def showVector(self):
        print(f"{self.vector}:", end="")

        for j in range(0,len(self.vectorAjc)):
            print(f" {self.vectorAjc[j]}",end="")
            print(f" peso: {self.pesos[j]}|",end="")


        print(f" ({len(self.vectorAjc)} vertice(s) adjacente(s))")

    def getAjc(self):
        return self.vectorAjc

    def getVector(self):
        return self.vector

#wip
    def setArestas(self):
        for i in range(0,len(self.vectorAjc)):
            self.arestas.append([self.vector,self.vectorAjc[i],self.pesos[i]])

#wip
    def showArestas(self):

        print("Arestas =",end="")

        for i in self.arestas:
            print(f" [{i[0]},"+f"{i[1]}]"+f" peso: {i[2]}|",end="")

        print("")