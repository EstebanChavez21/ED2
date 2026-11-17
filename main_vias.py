from M_vias.ArbolMVias import ArbolVias

arbol = ArbolVias(3)
datos = [10, 40, 70, 5, 20, 25, 30, 27, 22, 35, 50, 90]

for dato in datos:
    arbol.insertar(dato)

arbol.insertar(26)
arbol.insertar(28)
arbol.insertar(29)

arbol.mostrar()
nodo1 = arbol.raiz
nodo2 = nodo1.get_enlace(1)
nodo3 = nodo2.get_enlace(2)
nodo4 = nodo3.get_enlace(3)

print(nodo1.claves)
print(nodo2.claves)
print(nodo3.claves)
print(nodo4.claves)

if arbol.buscar(3):
    print("True")
else:
    print("False")
print(f"Lista Ordenada(In_orden): {arbol.in_orden()}")
print(f"Recorrido BFS: {arbol.bfs()}")
print("=========================\n")

arbol = ArbolVias(3)

datos = [10, 40, 70, 5, 20, 25, 30,
            27, 22, 35, 50, 90, 26, 28, 29]

for dato in datos:
    arbol.insertar(dato)

print("Inorden:", arbol.in_orden())
print("BFS:", arbol.bfs())
print("Buscar 29:", arbol.buscar(29))
print("Buscar 100:", arbol.buscar(100))
