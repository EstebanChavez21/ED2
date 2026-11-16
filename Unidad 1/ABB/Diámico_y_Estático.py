class Nodo:
    """Representa un nodo de un árbol binario."""

    def __init__(self):
        """Inicializa un nodo vacío."""
        self.dato = None
        self.enlace_izq = None
        self.enlace_der = None

    def get_dato(self):
        """Retorna el dato almacenado en el nodo."""
        return self.dato

    def get_enlace_izq(self):
        """Retorna el enlace hacia el hijo izquierdo."""
        return self.enlace_izq

    def get_enlace_der(self):
        """Retorna el enlace hacia el hijo derecho."""
        return self.enlace_der

    def set_dato(self, new_dato):
        """Establece el dato del nodo."""
        self.dato = new_dato

    def set_enlace_izq(self, new_enlace_izq):
        """Establece el enlace hacia el hijo izquierdo."""
        self.enlace_izq = new_enlace_izq

    def set_enlace_der(self, new_enlace_der):
        """Establece el enlace hacia el hijo derecho."""
        self.enlace_der = new_enlace_der


class ArbolBinarioEstatico:
    """Representa un árbol binario de búsqueda estático."""

    def __init__(self):
        """Inicializa un vector de 50 posiciones."""
        self.vector = [None] * 50

    def vacio(self):
        """Retorna True si el árbol está vacío."""
        return self.vector[0] is None

    def insertar(self, elemento):
        """
        Inserta un elemento en el árbol.

        Los elementos menores se colocan a la izquierda
        y los elementos mayores se colocan a la derecha.
        """
        i = 0
        while self.vector[i] is not None:
            if elemento > self.vector[i]:
                i = 2 * i + 2
            elif elemento < self.vector[i]:
                i = 2 * i + 1
            else:
                return

        self.vector[i] = elemento

    def mostrar(self):
        """Muestra las posiciones ocupadas del vector."""
        for i in range(len(self.vector)):
            if self.vector[i] is not None:
                print(i, ":", self.vector[i])


class ArbolBinarioDinamico:
    """Representa un árbol binario de búsqueda dinámico."""

    def __init__(self):
        """Inicializa un árbol vacío."""
        self.raiz = None

    def vacio(self):
        """Retorna True si el árbol está vacío."""
        return self.raiz is None

    def insertar(self, elemento):
        """
        Inserta un elemento en el árbol binario de búsqueda.

        Los elementos menores se colocan a la izquierda
        y los elementos mayores se colocan a la derecha.
        """
        if self.vacio():
            p = Nodo()
            p.set_dato(elemento)
            self.raiz = p
        else:
            p = Nodo()
            aux = self.raiz
            ant = None
            while aux is not None:
                if elemento > aux.get_dato():
                    ant = aux
                    aux = aux.get_enlace_der()
                elif elemento < aux.get_dato():
                    ant = aux
                    aux = aux.get_enlace_izq()
                else:
                    ant = aux
                    aux = None
            if elemento > ant.get_dato():
                p.set_dato(elemento)
                ant.set_enlace_der(p)
            elif elemento < ant.get_dato():
                p.set_dato(elemento)
                ant.set_enlace_izq(p)

    def buscar(self,elemento):
        nodo = self.raiz
        while nodo is not None:
            if nodo.get_dato() == elemento:
                return True
            elif elemento > nodo.get_dato():
                nodo = nodo.get_enlace_der()
            elif elemento < nodo.get_dato():
                nodo = nodo.get_enlace_izq()
            else:
                return False
        return False

    def mostrar(self, p, nivel=0):
        """
        Muestra el árbol de forma vertical.

        El método utiliza recursividad. Primero muestra
        el subárbol derecho, luego el nodo actual y
        finalmente el subárbol izquierdo.
        """
        if p is not None:
            self.mostrar(p.get_enlace_der(), nivel + 1)
            print("    " * nivel + str(p.get_dato()))
            self.mostrar(p.get_enlace_izq(), nivel + 1)

    def es_hoja(self, nodo):
        if nodo is None:
            return False
        return nodo.get_enlace_izq() is None and nodo.get_enlace_der() is None

    def _inorden_recursivo(self,nodo):
        if nodo is None:
            return
        self._inorden_recursivo(nodo.get_enlace_izq())
        print(nodo.get_dato())
        self._inorden_recursivo(nodo.get_enlace_der())

    def inorden(self):
        self._inorden_recursivo(self.raiz)

    def _preorden_rec(self,nodo,lista):
        if nodo is None:
            return
        lista.append(nodo.get_dato())
        self._preorden_rec(nodo.get_enlace_izq(), lista)
        self._preorden_rec(nodo.get_enlace_der(), lista)

    def preorden(self):
        lista = []
        self._preorden_rec(self.raiz,lista)
        return lista

    def _postorden_rec(self, nodo:Nodo, lista:list):
        if nodo is None:
            return
        self._postorden_rec(nodo.get_enlace_izq(), lista)
        self._postorden_rec(nodo.get_enlace_der(), lista)
        lista.append(nodo.get_dato())   

    def postorden(self):
        lista = []
        self._postorden_rec(self.raiz,lista)
        return lista


if __name__ == "__main__":
    arbol = ArbolBinarioDinamico()
    arbol.insertar(8)
    arbol.insertar(4)
    arbol.insertar(12)
    arbol.insertar(2)
    arbol.insertar(6)
    arbol.insertar(15)
    arbol.mostrar(arbol.raiz)

    """arbol = ArbolBinarioEstatico()
    arbol.insertar(8)
    arbol.insertar(4)
    arbol.insertar(12)
    arbol.insertar(2)
    arbol.insertar(6)
    arbol.insertar(15)
    arbol.mostrar()"""
    arbol.inorden()
    lista_preorden = arbol.preorden()
    print(lista_preorden)
    lista_postorden = arbol.postorden()
    print(lista_postorden)
    busqueda_elemento = arbol.buscar(2)
    print(busqueda_elemento)
    busqueda_elemento = arbol.buscar(11)
    print(busqueda_elemento)

    """https://colab.research.google.com/drive/1Wh-cv2ueWb_Zztuh1m2j6BQbBJkuY7L_?usp=drive_link"""
    """https://github.com/EstebanChavez21/ED2/blob/Unidad-1---ABB/Unidad%201/ABB/Di%C3%A1mico%20y%20Est%C3%A1tico"""
