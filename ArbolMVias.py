from M_vias.NodoMVias import NodoVias

class ArbolVias:
    def __init__(self,hijos):
        self.raiz = NodoVias(hijos)
        self.hijos = hijos

    def vacio(self):
        return self.raiz is None

    def insertar(self, elemento):
        self.raiz = self._insertar_rec(self.raiz, elemento)

    def _insertar_rec(self, nodo:NodoVias, elemento):
        if elemento in nodo.claves:
            return nodo
        if not nodo.esta_lleno():
            nodo.set_clave(elemento)
            return nodo
        i = 0
        while i < nodo.cantidad_clave:
            if elemento < nodo.claves[i]:
                if not nodo.ocupado(i):
                    new_nodo = NodoVias(self.hijos)
                    new_nodo.set_clave(elemento)
                    nodo.set_enlace(i, new_nodo)
                    break
                else:
                    nodo.set_enlace(i, self._insertar_rec(
                        nodo.get_enlace(i), elemento))
                    break
            elif i+1 == nodo.cantidad_clave:
                if elemento > nodo.claves[i]:
                    if not nodo.ocupado(i+1):
                        new_nodo = NodoVias(self.hijos)
                        new_nodo.set_clave(elemento)
                        nodo.set_enlace(i+1, new_nodo)
                        break
                    else:
                        nodo.set_enlace(i+1, self._insertar_rec(
                            nodo.get_enlace(i+1), elemento))
                        break
            i += 1
        return nodo

    def buscar(self, elemento):
        return self._buscar_rec(self.raiz, elemento)

    def _buscar_rec(self,nodo:NodoVias, elemento):
        if nodo is None:
            return False
        i=0
        while i < nodo.cantidad_clave:
            if nodo.get_clave(i) is not None:
                if elemento == nodo.get_clave(i):
                    return True
                elif elemento < nodo.get_clave(i):
                    return self._buscar_rec(nodo.get_enlace(i), elemento)
                elif i + 1 == nodo.cantidad_clave:
                    return self._buscar_rec(nodo.get_enlace(i + 1), elemento)
            i += 1
        return False

    def in_orden(self):
        lista = []
        self._in_orden_rec(self.raiz, lista)
        return lista

    def _in_orden_rec(self, nodo:NodoVias, lista:list):
        if nodo is None:
            return
        for i in range(nodo.cantidad_clave):
            if nodo.get_clave(i) is not None:
                self._in_orden_rec(nodo.get_enlace(i), lista)
                lista.append(nodo.get_clave(i))
            if i + 1 == nodo.cantidad_clave:
                if nodo.get_clave(i) is not None:
                    self._in_orden_rec(nodo.get_enlace(i + 1), lista)

    def bfs(self):
        niveles = []
        resultado = []
        niveles.append(self.raiz)
        self._bfs_hacer(niveles, resultado)
        return resultado

    def _bfs_hacer(self, niveles:list, resultado:list):
        if not niveles:
            return
        nodo = niveles.pop(0)
        for i in range(nodo.cantidad_clave):
            if nodo.get_clave(i) is not None:
                resultado.append(nodo.get_clave(i))
        for i in range(nodo.cantidad_hijos):
            if nodo.get_enlace(i) is not None:
                niveles.append(nodo.get_enlace(i))
        self._bfs_hacer(niveles, resultado)
    
    def mostrar(self):
        def recorrer(nodo, nivel, enlace):
            if nodo is None:
                return

            claves = [str(c) for c in nodo.claves if c is not None]

            print("    " * nivel + f"{enlace}: [{' | '.join(claves)}]")

            for i in range(len(nodo.enlaces)):
                if nodo.ocupado(i):
                    recorrer(nodo.get_enlace(i), nivel + 1, f"P{i}")

        recorrer(self.raiz, 0, "Raíz")

if __name__ == "__main__":
    arbol = ArbolVias(3)
    arbol.insertar(10)                
    arbol.insertar(40)
    arbol.insertar(70)
            
