from src import algorithms
from src.Graph.GraphAlgo import GraphAlgo
from client_python.client import Client
# from src.GUI.run_GUI import run_GUI
from src.GUI.game_frame import draw_Frame
import load


# default port
PORT = 6666
# server host (default localhost 127.0.0.1)
HOST = '127.0.0.1'


client = Client()
client.start_connection(HOST, PORT)

agents_json = client.get_agents()
pokemons_json = client.get_pokemons()
graph_json = client.get_graph()

agents: dict = load.load_agents(agents_json)
# agents.load_from_json(agents_json)
pokemons: dict = load.load_pokemon(pokemons_json)
pokemon_check: dict = dict.fromkeys(pokemons.keys(), False)
# pokemons.load_from_json(pokemons_json)
graph = GraphAlgo()
graph.load_from_json(graph_json)
draw_Frame(graph)
algorithms.first_init(agents_list=agents, pokemons_list=pokemons, pokemon_check=pokemon_check)

client.start()


while client.is_running() == 'true':
    # run_GUI(agents, pokemons, graph)
    algorithms.place_agent(agents_list=agents, pokemons_list=pokemons, pokemon_check=pokemon_check)
    algorithms.catch_pokemons(agents_list=agents)
    # algorithms.save_agents(agents_list=agents)
    agents: dict = load.load_agents(agents_json)

# if __name__ == '__main__':
