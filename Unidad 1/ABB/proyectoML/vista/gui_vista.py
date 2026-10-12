import customtkinter as ctk

class VistaGui:
    def __init__(self):
        self.controlador = None
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")
        #ventana
        self.ventana = ctk.CTk()
        self.ventana.title("TRES EN RAYAS")
        self.ventana.resizable(False,False)
        
        #frame superior(titulo+modos)
        self.superior = ctk.CTkFrame(self.ventana)
        self.superior.pack(pady = 10,padx = 10, fill = "x")

        self.etiqueta_titulo = ctk.CTkLabel(
            self.superior, text = "TRES EN RAYAS", 
            font = ctk.CTkFont(size = 24, weight = "bold")
        )
        self.etiqueta_titulo.pack(pady =(5, 15))
        
        #variable para modo seleccionado
        self.modo_selecionado = ctk.StringVar(value = "H vs Minimax")
        
        #frame interno para radio buttons
        self.modos = ctk.CTkFrame(self.superior, fg_color = "transparent")
        self.modos.pack(pady = (0, 10))
        
        #etiqueta "modos":
        self.etiqueta_modo = ctk.CTkLabel(
            self.modos, text="MODO:"
        )
        self.etiqueta_modo.pack(side = "left", padx = (0, 10))
        
        #radio buttons
        self.radio_hh = ctk.CTkRadioButton(
            self.modos, text="H vs H", variable=self.modo_selecionado,
            value="H vs H", command=self._cambiar_modo
        )
        self.radio_hh.pack(side="left", padx=5)

        self.radio_minimax = ctk.CTkRadioButton(
            self.modos, text="H vs Minimax", variable=self.modo_selecionado,
            value="H vs Minimax", command=self._cambiar_modo
        )
        self.radio_minimax.pack(side="left", padx=5)

        self.radio_ml = ctk.CTkRadioButton(
            self.modos, text="H vs ML", variable=self.modo_selecionado,
            value="H vs ML", command=self._cambiar_modo            
        )
        self.radio_ml.pack(side="left", padx=5)
        #

        #frame central(tablero)
        self.tablero = ctk.CTkFrame(self.ventana)
        self.tablero.pack(pady = 10, padx = 10)

        #tablero 3x3 de botones
        self.botones = [] # lista de 9 botones, indice 0 a 8
        for i in range(9):
            fila = i // 3
            col = i % 3
            boton = ctk.CTkButton(
                self.tablero, text="", width=80, height=80, 
                font=ctk.CTkFont(size=32, weight="bold"),
                command=lambda pos=i: self._al_hacer_click(pos)
            )
            boton.grid(row=fila, column=col, padx=5, pady=5)
            self.botones.append(boton)    
        #
        
        #frame inferior(estado+reinicio)
        self.estado = ctk.CTkFrame(self.ventana)
        self.estado.pack(pady = 10, padx = 10, fill = "x")

        #etiqueta de estados
        self.etiqueta_turno = ctk.CTkLabel(
            self.estado, text="Turno: X", font=ctk.CTkFont(size=16)
        )
        self.etiqueta_turno.pack(pady=3)

        self.etiqueta_nodos = ctk.CTkLabel(
            self.estado, text="Nodos explorados: 0",
            font=ctk.CTkFont(size=14)
        )
        self.etiqueta_nodos.pack(pady=3)

        self.etiqueta_tiempo = ctk.CTkLabel(
            self.estado, text="Tiempo: 0ms",
            font=ctk.CTkFont(size=14)
        )
        self.etiqueta_tiempo.pack(pady=3)

        #boton de reinicio
        self.boton_reiniciar = ctk.CTkButton(
            self.estado, text="Reiniciar", command=self._al_reiniciar
        )
        self.boton_reiniciar.pack(pady=(10,5))
        #
        
        #frame resultado
        self.resultado = ctk.CTkFrame(self.ventana)
        self.resultado.pack(pady = 10, padx = 10, fill = "x")

        #etiqueta resultado
        self.etiqueta_resultado = ctk.CTkLabel(
            self.resultado, text="", font=ctk.CTkFont(size=20, weight="bold")
        )
        self.etiqueta_resultado.pack(pady=5)
        #

    #
    def _cambiar_modo(self):
        """se llama cuando el usuario cambia de modo"""
        if self.controlador:
            self.controlador.cambiar_modo(self.modo_selecionado.get())

    def _al_hacer_click(self, pos):
        """se llama cuando el ususario hace click en una casilla"""
        if self.controlador:
            self.controlador.manejar_click(pos)

    def _al_reiniciar(self):
        """se llama cuando el usuario pulsa reiniciar"""
        if self.controlador:
            self.controlador.reiniciar_partida()

    #

    #metodos del controlador, llama para actualizar vista
    def actualizar_tablero(self, modelo):
        """dibuja el estado actual del tablero"""
        for i in range(9):
            fila = i//3
            col = i % 3
            simbolo = modelo.tablero[fila][col]
            self.botones[i].configure(text=simbolo)

    def actualizar_turno(self, jugador):
        """muestra de quien es el turno"""
        self.etiqueta_turno.configure(text=f"Turno: {jugador}")

    def actualizar_metricas(self, nodos, tiempo_ms):
        """muestra los nodos explorados y el tiempo de la ia"""
        self.etiqueta_nodos.configure(text=f"Nodos explorados: {nodos}")
        self.etiqueta_tiempo.configure(text=f"Tiempo: {tiempo_ms} ms")

    def mostrar_resultado(self,ganador):
        """muestra el mensaje final"""
        if ganador is None:
            self.etiqueta_resultado.configure(text="EMPATE")
        else:
            self.etiqueta_resultado.configure(text=f"GANO {ganador}")

    def limpiar_resultado(self):
        """borra el mensaje final al reiniciar"""
        self.etiqueta_resultado.configure(text="")

    def habilitar_botones(self, habilitar):
        """activa o desactiva los botones del tablero"""
        if habilitar:
            estado = "normal" 
        else:
            estado = "disabled"
        for boton in self.botones:
            boton.configure(state=estado)

    def reiniciar_vista(self, modelo):
        """deja la vista como el principio"""
        self.actualizar_tablero(modelo)
        self.actualizar_turno(modelo.jugador_actual)
        self.actualizar_metricas(0, 0)
        self.limpiar_resultado()
        self.habilitar_botones(True)
    #
