class AgenteMinimax:
    def __init__(self):
        self.simbolo_ia = 'O'
        self.simbolo_humano = 'X'
        self.nodos_explorados = 0

    def get_mejor_movimiento(self, modelo):
        self.nodos_explorados = 0
        mejor_pos = None
        mejor_puntuacion = float('-inf')
        for pos in modelo.movimientos_disponibles():
            modelo.hacer_movimiento(pos, self.simbolo_ia)
            puntuacion = self._minimax(modelo, 0, False)
            modelo.deshacer_movimiento(pos)
            if puntuacion > mejor_puntuacion:
                mejor_puntuacion = puntuacion
                mejor_pos = pos
        return mejor_pos

    def _minimax(self, modelo, profundidad, es_maximizando):
        self.nodos_explorados += 1

        #caso base
        if modelo.verificar_fin_del_juego():
            return self._evaluar(modelo, profundidad)
        if es_maximizando:
            mejor = float('-inf')
            for pos in modelo.movimientos_disponibles():
                modelo.hacer_movimiento(pos, self.simbolo_ia)
                puntuacion = self._minimax(modelo, profundidad + 1, False)
                modelo.deshacer_movimiento(pos)
                mejor = max(mejor, puntuacion)
            return mejor
        else:
            mejor = float('inf')
            for pos in modelo.movimientos_disponibles():
                modelo.hacer_movimiento(pos, self.simbolo_humano)
                puntuacion = self._minimax(modelo, profundidad + 1, True)
                modelo.deshacer_movimiento(pos)
                mejor = min(mejor, puntuacion)
            return mejor

    def _evaluar(self, modelo, profundidad):
        if modelo.verificar_ganador(self.simbolo_ia):
            return 10 - profundidad # gana rapido(mejor)
        elif modelo.verificar_ganador(self.simbolo_humano):
            return -10 + profundidad # pierde lento = menos malo
        else:
            return 0
