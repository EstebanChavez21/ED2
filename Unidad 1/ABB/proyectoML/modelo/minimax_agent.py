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

"""        
if __name__ == "__main__":
    import sys
    import os
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    from modelo.game_model import ModeloJuego
    modelo = ModeloJuego()
   
    modelo.hacer_movimiento(0, 'O')
    modelo.hacer_movimiento(4, 'X')
    modelo.hacer_movimiento(1, 'O')
    modelo.hacer_movimiento(8, 'X')
  
    agente = AgenteMinimax()
    pos = agente.get_mejor_movimiento(modelo)
    print("Mejor movimiento para O:", pos)  # 2
    print("Nodos explorados:", agente.nodos_explorados)

    
    modelo2 = ModeloJuego()
    modelo2.hacer_movimiento(0, 'X')
    modelo2.hacer_movimiento(4, 'O')
    modelo2.hacer_movimiento(1, 'X')
    
    agente2 = AgenteMinimax()
    pos2 = agente2.get_mejor_movimiento(modelo2)
    print("Mejor movimiento para O (bloquear):", pos2)  # 2
    print("Nodos explorados:", agente2.nodos_explorados)
    print("\n")
       
    print("\n=== Minimax vs Minimax ===")
    modelo3 = ModeloJuego()
    agente_x = AgenteMinimax()
    agente_x.simbolo_ia = 'X'
    agente_x.simbolo_humano = 'O'

    agente_o = AgenteMinimax()

    while not modelo3.verificar_fin_del_juego():
        if modelo3.jugador_actual == 'X':
            pos = agente_x.get_mejor_movimiento(modelo3)
            modelo3.hacer_movimiento(pos, 'X')
        else:
            pos = agente_o.get_mejor_movimiento(modelo3)
            modelo3.hacer_movimiento(pos, 'O')
        modelo3.alternar_jugador()
        print(modelo3)
        print()

    print("Ganador:", modelo3.ganador)
    print("Empate?", modelo3.ganador is None)
"""