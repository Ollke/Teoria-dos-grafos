class graph():

    def __init__(self):
        self.vertices = []
        self.grafo = {}

    def showGrafo(self):

        for i in self.grafo.keys():

            print(f"{i}:",end='')

            for j in self.grafo[i].keys():
                print(f" {j} "+f"Peso:{self.grafo[i][j]}|",end="")

            print(f"({len(self.grafo[i])} vertices adjacentes)")




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

    def ehConexo(self):
        testes = []

        for z in range(0,len(self.grafo)):
            vertices = []
            fila = {}

            for i in self.grafo.keys():
                vertices.append(i)

            visitados = {vertices[z]:self.grafo[vertices[z]]}
            fila = [vertices[z]]

            while fila:
                vertice = self.grafo[fila[0]]

                for i in vertice.keys():
                    if i not in visitados:
                        fila.append(i)
                        visitados[i] = self.grafo[i]

                    elif i in fila:
                        vertice = self.grafo[i]

                del fila[0]

            aux = []
            for i in visitados.keys():
                aux.append(i)
            testes.append(aux)

        conectado = []

        for i in testes[0]:
            conectado.append(i)

        for i in range(0,len(testes)):
            for j in conectado:
                if j in testes[i]:
                    for k in testes[i]:
                        if k not in conectado:
                            conectado.append(k)
                    break

        return len(conectado) == len(vertices)



        
        
    def getAdj(self,vertice):
        vertices = []

        for i in self.grafo.keys():
            vertices.append(i)

        if vertice in vertices:
            print(f"{vertice}:", end='')

            for j in self.grafo[vertice].keys():
                print(f" {j} " + f"Peso:{self.grafo[vertice][j]}|", end="")

            print(f"({len(self.grafo[vertice])} vertices adjacentes)")

        else:
            print("O vertice não esta no vetor")




