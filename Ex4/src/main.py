import json
from types import SimpleNamespace

from src.algorithms import *
from src.Graph.GraphAlgo import GraphAlgo
from src.client import Client
from src.GUI.game_frame import draw_Frame
from src.load import load_agents, load_pokemon


# default port
PORT = 6666
# server host (default localhost 127.0.0.1)
HOST = '127.0.0.1'


client = Client()
client.start_connection(HOST, PORT)

graph_json = client.get_graph()
graph = GraphAlgo()
graph.load_from_json(graph_json)

pokemons_json = json.loads(client.get_pokemons(), object_hook=lambda d: SimpleNamespace(**d)).Pokemons
pokemons = load_pokemon(pokemons_json, graph=graph)
pokemon_check: dict = dict.fromkeys(pokemons.keys(), False)

points = 0
moves = 0
client.add_agent("{\"id\":0}")
client.add_agent("{\"id\":1}")
client.add_agent("{\"id\":2}")
client.add_agent("{\"id\":3}")
client.start()
count = 0
while client.is_running() == 'true':
    pokemons_json = json.loads(client.get_pokemons(), object_hook=lambda d: SimpleNamespace(**d)).Pokemons
    agents_json = json.loads(client.get_agents(), object_hook=lambda d: SimpleNamespace(**d)).Agents
    agents = load_agents(agents_json, client)
    pokemons = load_pokemon(pokemons_json, graph=graph)
    if count == 0:
        first_init(agents_list=agents, pokemons_list=pokemons, pokemon_check=pokemon_check)
        count += 1
    else:
        place_agent(agents_list=agents, pokemons_list=pokemons, pokemon_check=pokemon_check)
    draw_Frame(graph, moves, points, client.time_to_end(), agents, pokemons)
    catch_pokemons(agents_list=agents)
    for agent in agents:
        points += agent.get_value()
        moves += agent.sum_moves

# if __name__ == '__main__':
