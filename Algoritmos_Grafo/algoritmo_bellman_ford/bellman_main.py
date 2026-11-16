from Grafos.bellman_ford import BellmanFord

grafo = BellmanFord()

for vertice in ["A", "B", "C", "D", "E", "F"]:
    grafo.agregar_vertice(vertice)

grafo.agregar_arista("A", "B", 10)
grafo.agregar_arista("A", "D", 2)
grafo.agregar_arista("B", "E", 3)
grafo.agregar_arista("B", "F", 6)
grafo.agregar_arista("C", "B", -1)
grafo.agregar_arista("C", "F", 12)
grafo.agregar_arista("D", "C", 2)
grafo.agregar_arista("D", "E", 9)
grafo.agregar_arista("E", "F", 2)

distancias, anteriores = grafo.bellman_ford("A")

print("Distancias:", distancias)
print("Anteriores:", anteriores)
