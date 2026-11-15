class GrafoPesado:
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

    def dijkstra(self, origen):
         # VALIDACIÓN 1: Comprobar que exista el origen
        if origen not in self.adyacencia:
            raise ValueError("El vertice de origen no existe")
        # VALIDACIÓN 2: Comprobar que no existan pesos negativos
        for vecinos in self.adyacencia.values():
            for peso in vecinos.values():
                if peso < 0:
                    raise ValueError("Dijkstra no admite pesos negativos")
        distancias = {}
        visitados = set()
        anteriores = {}
          # 1. Inicializar
        for vertice in self.adyacencia:
            distancias[vertice] = float("inf")
            anteriores[vertice] = None
        distancias[origen] = 0
        # 2. Repetir mientras existan vertices pendientes
        while len(visitados) < len(self.adyacencia):
            actual = None
            # 3. Buscar el pendiente con menor distancia
            for vertice in self.adyacencia:
                if vertice not in visitados:
                    if actual is None or distancias[vertice] < distancias[actual]:
                        actual = vertice
            if distancias[actual] == float("inf"):
                break
            # 4. Consultar sus vecinos
            for vecino, peso in self.adyacencia[actual].items():
                if vecino not in visitados:
                    nueva_distancia = distancias[actual] + peso
                    # 5. Actualizar si encontramos un camino mejor
                    if nueva_distancia < distancias[vecino]:
                        distancias[vecino] = nueva_distancia
                        anteriores[vecino] = actual
            # 6. Marcar como visitado
            visitados.add(actual)
        return distancias, anteriores
        
    
