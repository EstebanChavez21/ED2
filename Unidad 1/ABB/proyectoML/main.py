from modelo.game_model import ModeloJuego
from modelo.minimax_agent import AgenteMinimax
from modelo.ml_agent import AgenteMl
from vista.gui_vista import VistaGui
from controlador.game_controler import ControladorJuego

def main():
    print("iniciando...")
    modelo = ModeloJuego()
    vista = VistaGui()
    minimax = AgenteMinimax()
    ml = AgenteMl()
    print("preparando agente ml...")
    ml.cargar_o_entrenar()
    controlador = ControladorJuego(modelo, vista, minimax, ml)
    controlador.iniciar()

if __name__ == "__main__":
    main()
