class BellmanFord:
    def __init__(self, dirigido=True):
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

    def bellman_ford(self, origen):
        if origen not in self.adyacencia:
            raise ValueError("No existe")
        distancia = {}
        anterior = {}
        for vertice in self.adyacencia:
            distancia[vertice] = float("inf")
            anterior[vertice] = None
        distancia[origen] = 0
        for i in range(len(distancia) - 1):
            for vertice, vecinos in self.adyacencia.items():
                if distancia[vertice] == float("inf"):
                    continue
                for vecino, peso in vecinos.items():
                    nueva_distancia = distancia[vertice] + peso
                    if nueva_distancia < distancia[vecino]:
                        distancia[vecino] = nueva_distancia
                        anterior[vecino] = vertice
                        hubo_cambio = True
            if not hubo_cambio:
                break
        for vertice, vecino in self.adyacencia.items():
            if distancia[vertice] == float("inf"):
                continue
            for vecino, peso in vecinos.items():
                nueva_distancia = distancia[vertice] + peso
                if nueva_distancia < distancia[vecino]:
                    raise ValueError("existe un ciclo negativo")
        return distancia, anterior
        
