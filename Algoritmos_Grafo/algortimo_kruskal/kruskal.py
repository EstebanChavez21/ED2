class Kruskal:
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

    def kruskal(self):
        if self.dirigido:
            raise ValueError("Kruskal requiere un grafo no dirigido")

        if not self.adyacencia:
            return [], 0

        aristas = []
        revisadas = set()

        # Obtener las aristas sin repetirlas
        for origen, vecinos in self.adyacencia.items():
            for destino, peso in vecinos.items():

                if (destino, origen) not in revisadas:
                    aristas.append((origen, destino, peso))
                    revisadas.add((origen, destino))

        # Ordenar por peso
        aristas.sort(key=lambda arista: arista[2])

        # Cada vertice comienza en su propio grupo
        padre = {}
        for vertice in self.adyacencia:
            padre[vertice] = vertice

    # Buscar el representante de un grupo
        def encontrar(vertice):
            while padre[vertice] != vertice:
                vertice = padre[vertice]
            return vertice

        aristas_elegidas = []
        costo_total = 0

        for origen, destino, peso in aristas:

            grupo_origen = encontrar(origen)
            grupo_destino = encontrar(destino)

            # Si pertenecen a grupos diferentes, no hay ciclo
            if grupo_origen != grupo_destino:

                aristas_elegidas.append((origen, destino, peso))
                costo_total += peso

                # Unir los grupos
                padre[grupo_origen] = grupo_destino

            if len(aristas_elegidas) == len(self.adyacencia) - 1:
                break

        if len(aristas_elegidas) != len(self.adyacencia) - 1:
            raise ValueError("El grafo esta desconectado")

        return aristas_elegidas, costo_total
