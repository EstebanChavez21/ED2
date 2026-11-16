class Prim:
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

    
    def prim(self, origen):
        if self.dirigido:
            raise ValueError("Prim requiere un grafo no dirigido")

        if origen not in self.adyacencia:
            raise ValueError("El origen no existe")

        seleccionados = {origen}
        aristas_elegidas = []
        costo_total = 0

        while len(seleccionados) < len(self.adyacencia):

            mejor_arista = None

            for vertice in seleccionados:
                for vecino, peso in self.adyacencia[vertice].items():

                    if vecino not in seleccionados:

                        if mejor_arista is None or peso < mejor_arista[2]:
                            mejor_arista = (vertice, vecino, peso)

            if mejor_arista is None:
                raise ValueError("El grafo esta desconectado")

            origen_arista, destino, peso = mejor_arista

            seleccionados.add(destino)
            aristas_elegidas.append(mejor_arista)
            costo_total += peso

        return aristas_elegidas, costo_total
