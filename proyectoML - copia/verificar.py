from modelo.ml_agent import AgenteMl

agente = AgenteMl()
agente.cargar_o_entrenar()

print("Dificultad actual:", agente.dificultad)
print("Árbol actual es:", agente.arbol)

for nivel in ["Facil", "Medio", "Dificil"]:
    agente.cambiar_dificultad(nivel)
    print(f"Dificultad {nivel}: profundidad = {agente.arbol.max_profundidad}, árbol = {agente.arbol}")