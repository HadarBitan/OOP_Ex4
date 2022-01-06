from src import Play
from src.Pokemon import Pokemon
from src.Agent import Agent
from src.Graph.DiGraph import DiGraph
from src.Graph.GraphAlgo import GraphAlgo
from client_python.client import Client
from src.GUI.run_GUI import run_GUI
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
pokemons: list = load.load_pokemon(pokemons_json)
# pokemons.load_from_json(pokemons_json)
graph = GraphAlgo()
graph.load_from_json(graph_json)



client.start()

while client.is_running() == 'true':
    run_GUI(agents, pokemons, graph)


# if __name__ == '__main__':
