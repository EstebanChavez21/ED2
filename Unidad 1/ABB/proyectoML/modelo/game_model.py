class ModeloJuego:
    def __init__(self):
        self.tablero = [['' for i in range(3)] for i in range(3)]
        self.jugador_actual = 'X'
        self.ganador = None
        self.juego_terminado = False

    def _coordenadas(self,pos):
        fil = pos//3
        col = pos%3
        return fil,col

    def _obtener(self,pos):
        fil, col = self._coordenadas(pos)
        return self.tablero[fil][col]

    def hacer_movimiento(self,pos,jugador):
        if not (pos >= 0 and pos <= 8):
            return False
        if self.juego_terminado:
            return False
        if jugador not in ('X','O'):
            return False
        if self._obtener(pos) != '':
            return False
        fil,col = self._coordenadas(pos)
        self.tablero[fil][col] = jugador
        return True
    
    def deshacer_movimiento(self,pos):
        if not (pos >= 0 and pos <= 8):
            return False
        fil,col = self._coordenadas(pos)
        self.tablero[fil][col] = ''
        self.ganador = None
        self.juego_terminado = False
        return True

    def movimientos_disponibles(self):
        lista = []
        for i in range(9):
            if self._obtener(i) == '':
                lista.append(i)
        return lista

    def verificar_ganador(self,jugador):
        posibles = [(0,1,2),(3,4,5),(6,7,8),
                    (0,3,6),(1,4,7),(2,5,8),
                    (2,4,6),(0,4,8)]
        for a,b,c in posibles:
            if self._obtener(a) == jugador and \
                self._obtener(b) == jugador and \
                self._obtener(c) == jugador:
                return True
        return False

    def es_empate(self):
        if len(self.movimientos_disponibles()) != 0:
            return False
        if self.verificar_ganador('X'):
            return False
        if self.verificar_ganador('O'):
            return False
        return True

    def verificar_fin_del_juego(self):
        if self.verificar_ganador('X'):
            self.ganador = 'X'
            self.juego_terminado = True
        elif self.verificar_ganador('O'):
            self.ganador = 'O'
            self.juego_terminado = True
        elif self.es_empate():
            self.ganador = None
            self.juego_terminado = True
        return self.juego_terminado

    def alternar_jugador(self):
        if self.jugador_actual == 'X':
            self.jugador_actual = 'O'
        else:
            self.jugador_actual = 'X'

    def reiniciar(self):
        self.tablero = []
        for i in range(3):
            fil = []
            for j in range(3):
                fil.append('')
            self.tablero.append(fil)
        self.jugador_actual = 'X'
        self.ganador = None
        self.juego_terminado = False

    def to_array(self):
        diccionario = {'':0, 'X':1,'O':2}
        resultado = []
        for i in range(9):
            resultado.append(diccionario[self._obtener(i)])
        return resultado

    def __str__(self):
        lineas = []
        for fila in self.tablero:
            lineas.append(' | '.join(fila))
        return '\n--------\n'.join(lineas)
