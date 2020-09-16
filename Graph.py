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

    def getVector(self):
        return self.vector