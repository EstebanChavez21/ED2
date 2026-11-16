class floyd:
    def __init__(self, dirigido=False):
        self.adyacencia = {}
        self.dirigido = dirigido

    def agregar_vertice(self, vertice):
        if vertice not in self.adyacencia:
            self.adyacencia[vertice] = {}

    def agregar_arista(self, origen, destino, peso):
        if origen in self.adyacencia and destino in self.adyacencia:
            if origen != destino:
                self.adyacencia[origen][destino] = peso

                if not self.dirigido:
                    self.adyacencia[destino][origen] = peso

    def obtener_vecinos(self, vertice):
        if vertice in self.adyacencia:
            return self.adyacencia[vertice]
        return None

    def floyd_warshall(self):
        matriz = [[float("inf") for _ in range(len(self.adyacencia))] 
                for _ in range(len(self.adyacencia))]
        for i in range(len(matriz)):
            matriz[i][i] = 0
        vertices = list(self.adyacencia)
        n = len(vertices)
        for i in range(n):
            for destino, peso in self.adyacencia[vertices[i]].items():
                matriz[i][vertices.index(destino)] = peso
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if matriz[i][k] + matriz[k][j] < matriz[i][j]:
                        matriz[i][j] = matriz[i][k] + matriz[k][j]
        for i in range(n):
            if matriz[i][i] < 0:
                raise ValueError("Existe un ciclo negativo")
        return vertices, matriz
        
