from ABB import Nodo, ArbolBinarioDinamico

class ArbolExpresion:
    def __init__(self):
        self.arbol = ArbolBinarioDinamico()
        self.raiz = None
        self.expresion = ""

    def prioridades(self,char):
        if char == '*' or char == '/':
            return 2
        elif char == '+' or char == '-':
            return 1
        return 0
    def extraer_numero(self, expresion, pos):
        i = 0
        contador = 0
        switch = False
        numero = ""
        n = len(expresion)
        while i < n:
            if expresion[i].isdigit():
                numero = numero + expresion[i]
                switch = True
            elif switch:
               break
            i += 1  
            contador += 1
        if numero:
            nueva_pos = pos + len(numero)
            self.expresion = expresion[nueva_pos:]
            return int(numero),nueva_pos
        return -1,pos
        
    def construir(self, expresion):
        self.expresion = expresion
        pila_expresion = []
        pila_nodos = []
        i = 0
        while i < len(expresion):
            char = expresion[i]
            if char.isdigit():
                nodo = Nodo()
                numero, i = self.extraer_numero(self.expresion, i)
                nodo.set_dato(numero)
                pila_nodos.append(nodo)
                continue
            else:
                if not pila_expresion:
                    pila_expresion.append(char)
                else:
                    if char == '(':
                        pila_expresion.append(char)
                    elif char == ')':
                        nodo2 = Nodo()
                        nodo2.set_dato(pila_expresion.pop())
                        nodo2.set_enlace_der(pila_nodos.pop())
                        nodo2.set_enlace_izq(pila_nodos.pop())
                        pila_nodos.append(nodo2)
                        pila_expresion.pop()
                    elif self.prioridades(pila_expresion[-1]) < self.prioridades(char):
                        pila_expresion.append(char)
                    else:
                        nodo2 = Nodo()
                        nodo2.set_dato(pila_expresion.pop())
                        nodo2.set_enlace_der(pila_nodos.pop())
                        nodo2.set_enlace_izq(pila_nodos.pop())
                        pila_nodos.append(nodo2)
                        pila_expresion.append(char)
            i += 1
        while pila_expresion:
            nodo3 = Nodo()
            nodo3.set_dato(pila_expresion.pop())
            nodo3.set_enlace_der(pila_nodos.pop())
            nodo3.set_enlace_izq(pila_nodos.pop())
            pila_nodos.append(nodo3)
        if pila_nodos:
            #self.raiz = nodo3
            self.arbol.raiz = pila_nodos[0]

if __name__ == "__main__":
    arbol = ArbolExpresion()
    arbol.construir(input("Escrtibe la Expresion Matematica: "))
    lista = arbol.arbol.postorden()
    print(f"La Expresion PosFija: {lista}")
    arbol.arbol.mostrar(arbol.arbol.raiz)
