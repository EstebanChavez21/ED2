from modelo.game_model import ModeloJuego
from modelo.minimax_agent import AgenteMinimax
from vista.gui_vista import VistaGui
from controlador.game_controler import ControladorJuego

def main():
    modelo = ModeloJuego()
    vista = VistaGui()
    minimax = AgenteMinimax()
    controlador = ControladorJuego(modelo, vista, minimax, None)
    controlador.iniciar()

if __name__ == "__main__":
    main()