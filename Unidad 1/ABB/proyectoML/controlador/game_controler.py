import time
from modelo.game_model import ModeloJuego


class ControladorJuego:
    def __init__(self, modelo, vista, minimax, ml):
        self.modelo = modelo
        self.vista = vista
        self.agente_minimax = minimax
        self.agente_ml = ml

        self.simbolo_humano = 'X'
        self.simbolo_ia = 'O'

        self.modo = 'H vs Minimax'

        self.vista.controlador = self

    def iniciar(self):
        """comienza la partida y muestra ventana"""
        self.vista.reiniciar_vista(self.modelo)
        self.vista.ventana.mainloop()

    def manejar_click(self, pos):
        """al hacer clic en una casilla"""
        if self.modelo.juego_terminado: # termino el juego?
            return
        #turno del humano?
        if self.modo != 'H vs H' and self.modelo.jugador_actual != self.simbolo_humano:
            return
        #intentar movimiento
        if not self.modelo.hacer_movimiento(pos, self.modelo.jugador_actual):
            return
        #actualizar vidsta
        self.vista.actualizar_tablero(self.modelo)
        #termino el juego?
        if self.modelo.verificar_fin_del_juego():
            self.vista.mostrar_resultado(self.modelo.ganador)
            self.vista.habilitar_botones(False)
            return
        #cambiar turno
        self.modelo.alternar_jugador()
        self.vista.actualizar_turno(self.modelo.jugador_actual)
        #le toca a la ia?
        if self.modo != 'H vs H' and self.modelo.jugador_actual == self.simbolo_ia:
            self._movimiento_ia()


    def _movimiento_ia(self):
        """la ia eligey aplica un movimiento"""
        #medir teimpo
        inicio = time.perf_counter()

        #segun, modo elegir movienteo
        if self.modo == 'H vs Minimax':
            pos = self.agente_minimax.get_mejor_movimiento(self.modelo)
            nodos = self.agente_minimax.nodos_explorados
        elif self.modo == 'H vs ML':
            pos = self.agente_ml.predecir(self.modelo)
            nodos = 0 # no explora nodos el ml
        else:
            return # modo h vs h no llama ia
        fin = time.perf_counter()
        tiempo_ms = int((fin - inicio) * 1000)

        # usar movimiento del modelo
        self.modelo.hacer_movimiento(pos, self.simbolo_ia)

        #actualizar vista
        self.vista.actualizar_tablero(self.modelo)
        self.vista.actualizar_metricas(nodos, tiempo_ms)

        #termino el juego?
        if self.modelo.verificar_fin_del_juego():
            self.vista.mostrar_resultado(self.modelo.ganador)
            self.vista.habilitar_botones(False)
            return
        #cambiar turno
        self.modelo.alternar_jugador()
        self.vista.actualizar_turno(self.modelo.jugador_actual)

    def cambiar_modo(self, nuevo_modo):
        """se cambia de modo"""
        self.modo = nuevo_modo
        self.reiniciar_partida()

    def reiniciar_partida(self):
        """al pulsar reiniciar"""
        self.modelo.reiniciar()

        #reiniciar vista tamnboien
        self.vista.reiniciar_vista(self.modelo)

if __name__ == "__main__":
    import sys
    import os
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    from vista.gui_vista import VistaGui

    modelo = ModeloJuego()
    vista = VistaGui()

    # Agentes falsos para que no falle el constructor
    class AgenteFalso:
        def __init__(self):
            self.nodos_explorados = 0
        def get_best_move(self, modelo):
            return 0
        def predict(self, modelo):
            return 0

    controlador = ControladorJuego(modelo, vista, AgenteFalso(), AgenteFalso())
    controlador.modo = 'H vs H'  # forzamos HH para probar sin agentes
    controlador.iniciar()
