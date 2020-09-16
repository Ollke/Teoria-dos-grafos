class graph():

    def __init__(self):
        self.vectors = []

    def addVector(self,a,b):
        self.vectors.append(vector(a,b))

    def showVectors(self):
        for i in self.vectors:
            i.showVector()


class vector():

    def __init__(self,vector,adj):
        self.vector = vector
        self.vectorAjc = adj

    def addVectorAjc(self,adj):
        self.vectorAjc.append(adj)

    def showVector(self):
        print(f"{self.vector}:", end="")

        for j in self.vectorAjc:
            print(f" {j}",end="")

        print(f" ({len(self.vectorAjc)} vertice(s) adjacente(s))")
