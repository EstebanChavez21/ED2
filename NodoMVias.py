class NodoVias:
    def __init__(self, cantidad_clave):
        self.cantidad_clave = cantidad_clave
        self.cantidad_hijos = cantidad_clave + 1

        self.claves = [] # clave = datos
        for i in range(self.cantidad_clave):
            self.claves.append(None)

        self.enlaces = []
        for i in range(self.cantidad_hijos):
            self.enlaces.append(None)

    def set_clave(self, clave):
        i=0
        while(i < len(self.claves)):
            if self.claves[i] is None:
                self.claves[i] = clave
                self.ordenar()
                return
            i += 1
        return
    
    def ordenar(self):
        n=len(self.claves)
        i=0
        while i<n:
            j=i+1
            while j < n:
                if self.claves[i] is not None and self.claves[j] is not None:
                    if self.claves[i] > self.claves[j]:
                        aux = self.claves[i]
                        self.claves[i] = self.claves[j]
                        self.claves[j] = aux
                j += 1
            i += 1

    def set_enlace(self, pos, nodo:"NodoVias"):
        self.enlaces[pos] = nodo

    def get_clave(self, pos):
        return self.claves[pos]

    def get_enlace(self,pos):
        return self.enlaces[pos]

    def esta_lleno(self):
        for i in range(len(self.claves)):
            if self.claves[i] is None:
                return False
        return True
    def ocupado(self, pos):
        return self.enlaces[pos] is not None        

if __name__ == "__main__":
    nodo = NodoVias(3)
    nodo.set_clave(60)
    nodo.set_clave(20)
    nodo.set_clave(40)
    print(nodo.claves)
    nodo2 = NodoVias(3)
    nodo3 = NodoVias(3)
    nodo.set_enlace(0,nodo2)
    nodo.set_enlace(1,nodo3)
    print(f"{nodo.get_enlace(0).claves}")
    if nodo2.esta_lleno():
        print("True")
    else:
        print("False")
