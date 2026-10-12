import os
import csv
import pickle
from modelo.game_model import ModeloJuego


class NodoMl:
    def __init__(self):
        self.casilla = None # (0-8) = posicion
        self.clase = None
        self.hijos = {}
        self.es_hoja = False
        self.clase_mayoritaria = None

class ArbolDecision:
    def __init__(self, max_profundidad=9):
        self.raiz = None
        self.max_profundidad = max_profundidad

    def entrenar(self, X, y):
        self.raiz = self._construir(X, y, 0)

    def predecir(self, x):
        # tableor nuevo = x o tablero unico, una sola fila
        nodo = self.raiz
        while not nodo.es_hoja:
            valor = x[nodo.casilla]
            if valor not in nodo.hijos:
                return nodo.clase_mayoritaria
            nodo = nodo.hijos[valor]
        return nodo.clase

    def _construir(self, X, y, profundidad):
        # X= tableros, y=jugadas correctas, profundidad= cuantos niveles van
        nodo = NodoMl()
        #caso 1: todas las etiquetas iguales = hoja
        if len(set(y)) == 1:
            nodo.es_hoja = True
            nodo.clase = y[0]
            return nodo
        #caso 2: sin casillas o profundidad maxima = hoja con clase mayoritaria
        if profundidad >= self.max_profundidad or \
            len(X[0]) == 0:
            nodo.es_hoja = True
            nodo.clase = self._clase_mayoritaria(y)
            return nodo
        #caso 3: encontrar mejor dividion
        casilla, gini = self._mejor_division(X, y)
        # si no mejor anada, hoja
        if casilla is None:
            nodo.es_hoja = True
            nodo.clase = self._clase_mayoritaria(y)
            return nodo
        nodo.casilla = casilla
        nodo.clase_mayoritaria = self._clase_mayoritaria(y)
        #agrupar por valor de esa casilla
        grupos_X = {}
        grupos_y = {}
        for i in range(len(y)):
            valor = X[i][casilla]
            if valor not in grupos_X:
                grupos_X[valor] = []
                grupos_y[valor] = []
            grupos_X[valor].append(X[i])
            grupos_y[valor].append(y[i])
        for valor in grupos_X:
            nodo.hijos[valor] = self._construir(
                grupos_X[valor],
                grupos_y[valor],
                profundidad + 1
            )
        return nodo

    def _clase_mayoritaria(self, y):
        conteo = {}
        for clase in y:
            conteo[clase] = conteo.get(clase, 0) + 1
        return max(conteo, key=conteo.get)

    def _mejor_division(self, X, y):
        mejor_casilla = None
        mejor_gini = float('inf')
        n = len(y)
        for casilla in range(len(X[0])): # 9 casillas.
            #agrupar por valor del casilla.
            grupos = {}
            for i in range(n):
                valor = X[i][casilla]
                if valor not in grupos:
                    grupos[valor] = []
                grupos[valor].append(y[i])
            #calcular gini ponderado
            gini_total = 0
            for valor, etiquetas in grupos.items():
                peso = len(etiquetas) / n
                gini_total += peso * self._gini(etiquetas)
            if gini_total < mejor_gini:
                mejor_gini = gini_total
                mejor_casilla = casilla
        return mejor_casilla, mejor_gini

    def _gini(self, y):
        if len(y) == 0: # y = lista de respuestas correctas
            return 0
        conteo = {}
        for clase in y:
            conteo[clase] = conteo.get(clase, 0) + 1
        impureza = 1.0
        for clase, cant in conteo.items():
            probabilidad = cant / len(y)
            impureza -= probabilidad ** 2
        return impureza


class AgenteMl:
    def __init__(self):
        self.arbol = None
        self.ruta_dataset = "data/dataset.csv"
        self.ruta_modelo = "data/modelo_ml.pkl"

    def generar_dataset(self, num_partidas=1000):
        from modelo.game_model import ModeloJuego
        from modelo.minimax_agent import AgenteMinimax

        os.makedirs(os.path.dirname(self.ruta_dataset),
                    exist_ok=True)
        agente_x = AgenteMinimax()
        agente_x.simbolo_ia = 'X'
        agente_x.simbolo_humano = 'O'
        agente_o = AgenteMinimax()
        with open(self.ruta_dataset, 'w', newline='') as archivo:
            escribir = csv.writer(archivo)
            escribir.writerow([f"c{i}" for i in range(9)]+ ["etiqueta"])
            for partida in range(num_partidas):
                modelo = ModeloJuego()
                while not modelo.verificar_fin_del_juego():
                    if modelo.jugador_actual == 'X':
                        pos = agente_x.get_mejor_movimiento(modelo)
                        modelo.hacer_movimiento(pos, 'X')
                    else:
                        casilla = modelo.to_array()
                        pos = agente_o.get_mejor_movimiento(modelo)
                        escribir.writerow(casilla + [pos])
                        modelo.hacer_movimiento(pos, 'O')
                    modelo.alternar_jugador()
                if (partida + 1) % 100 == 0:
                    print(f"partidas generadas: {partida + 1} / {num_partidas}")
        print(f"Dataset guardado en {self.ruta_dataset}")



    def leer_dataset(self):
        X = []
        y = []
        with open(self.ruta_dataset, 'r') as archivo:
            leer = csv.reader(archivo)
            next(leer) # salta cabecera
            for fila in leer:
                X.append([int(v) for v in fila[:9]])
                y.append(int(fila[9]))
        return X, y

    def entrenar(self):
        print("cargando dataset...(puede tardar)..")
        X, y = self.leer_dataset()
        self.arbol = ArbolDecision(max_profundidad=9)
        self.arbol.entrenar(X, y)
        print("modelo entrenado")

    def predict(self, modelo:ModeloJuego):
        if self.arbol is None:
            raise ValueError("ERROR::NO HAY ARBOL CARGADO." \
            "LLAMA A CARGAR_O_ENTRENAR PRIMERO")
        casillas = modelo.to_array()
        pos = self.arbol.predecir(casillas)
        #fallback= si el arbol devuelve none o una casilla ocupada
        #elegimos la primera casilla libre
        if pos is None or \
            pos not in modelo.movimientos_disponibles():
            pos = modelo.movimientos_disponibles()[0]
        return pos

    def guardar_modelo(self):
        os.makedirs(os.path.dirname(self.ruta_modelo), exist_ok=True)
        with open(self.ruta_modelo, 'wb') as archivo:
            pickle.dump(self.arbol, archivo)
        print(f"modelo guardado en: {self.ruta_modelo}")

    def cargar_modelo(self):
        with open(self.ruta_modelo, 'rb') as archivo:
            self.arbol = pickle.load(archivo)
        print(f"modelo cargado desde: {self.ruta_modelo}")

    def cargar_o_entrenar(self):
        if os.path.exists(self.ruta_modelo):
            self.cargar_modelo()
        else:
            if not os.path.exists(self.ruta_dataset):
                self.generar_dataset(num_partidas=200)
            self.entrenar()
            self.guardar_modelo()
