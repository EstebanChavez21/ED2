class Grafo:
    def __init__(self, dirigido = False):
        self.adyacencia = {}
        self.dirigido = dirigido

    def agregar_vertice(self, vertice):
        if vertice not in self.adyacencia:
            self.adyacencia.update({vertice:[]})

    def agregar_arista(self, origen, destino): # conectar
        if origen in self.adyacencia and destino in self.adyacencia:
            if origen != destino:
                if destino not in self.adyacencia[origen]:
                    if not self.dirigido:
                        self.adyacencia[origen].append(destino)
                        self.adyacencia[destino].append(origen)
                    else:
                        self.adyacencia[origen].append(destino)

    def existe_conexion_directa(self,vertive_1, vertice_2):
        if vertive_1 in self.adyacencia and vertice_2 in self.adyacencia:
            for vecino in self.adyacencia[vertive_1]:
                if vecino == vertice_2:
                    return True
        return False

    def obtener_vecinos(self, vertice):
        if vertice in self.adyacencia:
            return self.adyacencia[vertice]
        else:
            return None

    def grado_vertice(self, vertice):
        if vertice in self.adyacencia:
            return len(self.adyacencia[vertice])
        else:
            return None

    def matriz_grafos(self):
        if not self.adyacencia:
            return []
        vertices = []
        for nodos in self.adyacencia.keys():
            vertices.append(nodos)
        matriz = [[0 for _ in range(len(vertices))] for _ in range(len(vertices))]
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                if self.existe_conexion_directa(vertices[i], vertices[j]):
                    matriz[i][j] = 1
        return matriz
    
    def bfs(self):
        if not self.adyacencia:
            return []
        cola = []
        visitados = []
        resultado = []
        vertices = []
        for nodos in self.adyacencia.keys():
            vertices.append(nodos)
        cola.append(vertices[0])
        visitados.append(vertices[0])
        resultado.append(vertices[0])
        while cola:
            if cola[0] not in visitados:
                visitados.append(cola[0])
                resultado.append(cola[0])
            vecinos = self.obtener_vecinos(cola[0])
            cola.pop(0)
            for nodo in vecinos:
                if nodo not in visitados:
                    cola.append(nodo)
        return resultado
            

    def dfs(self):
        if not self.adyacencia:
            return []
        resultado = []
        visitados = []
        if not self.dirigido:
            self._dfs_rec(list(self.adyacencia.keys())[0], visitados, resultado)
        else:
            self._dfs_dirigido_rec(
                list(self.adyacencia.keys())[0], visitados, resultado)
            resultado.reverse()
        return resultado

    def _dfs_rec(self, vertice, visitados:list, resultado:list):
        if vertice in visitados:
            return
        visitados.append(vertice)
        resultado.append(vertice)

        vecinos = self.obtener_vecinos(vertice)

        for vecino in vecinos:
            self._dfs_rec(vecino, visitados, resultado)

    def _dfs_dirigido_rec(self, vertice, visitados:list, resultado:list):
        if vertice in visitados:
            return
        visitados.append(vertice)
        vecinos = self.obtener_vecinos(vertice)
        for vecino in vecinos:
            self._dfs_dirigido_rec(vecino, visitados, resultado)
        resultado.append(vertice)    
            

        
""""        
grafo = Grafo()
grafo.agregar_vertice('A')
grafo.agregar_vertice('B')
grafo.agregar_vertice('C')
grafo.agregar_vertice('D')
grafo.agregar_vertice('E')
for vertice in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
    grafo.agregar_vertice(vertice)

print(f"{grafo.adyacencia}\n")

grafo.agregar_arista('A','B')
grafo.agregar_arista('A','C')
grafo.agregar_arista('B','D')
grafo.agregar_arista('C','D')
grafo.agregar_arista('D','E')
grafo.agregar_arista('F', 'G')

print(grafo.adyacencia)
print("\n")
print(grafo.obtener_vecinos('B'))
print(grafo.grado_vertice('B'))
print(grafo.grado_vertice('A'))
print(grafo.grado_vertice('Z'))

print(grafo.matriz_grafos())

print(grafo.bfs())
print(grafo.dfs())
"""
grafo = Grafo(True)

for v in ['A', 'B', 'C', 'D']:
    grafo.agregar_vertice(v)

grafo.agregar_arista('A', 'B')
grafo.agregar_arista('A', 'C')
grafo.agregar_arista('B', 'D')
grafo.agregar_arista('C', 'D')

print(grafo.adyacencia)
print(grafo.dfs())
