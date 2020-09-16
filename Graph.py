class graph():

    def __init__(self):
        self.vectors = []

    def addVector(self,a,b):
        self.vectors.append(vector(a,b))

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
        x = len(self.vectors)-1

        for i in self.vectors:
            y = len(i.getAjc())
            if x != y:
                completo = False
                break

        return completo

class vector():

    def __init__(self,vector,adj):
        self.vector = vector
        self.vectorAjc = adj

    def showVector(self):
        print(f"{self.vector}:", end="")

        for j in self.vectorAjc:
            print(f" {j}",end="")

        print(f" ({len(self.vectorAjc)} vertice(s) adjacente(s))")

    def getAjc(self):
        return self.vectorAjc
