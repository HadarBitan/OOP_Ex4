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

agents_json = json.loads(client.get_agents(), object_hook=lambda d: SimpleNamespace(**d)).Agents
agents = load_agents(agents_json, client)
first_init(agents_list=agents, pokemons_list=pokemons, pokemon_check=pokemon_check)

client.start()

while client.is_running() == 'true':
    pokemons_json = json.loads(client.get_pokemons(), object_hook=lambda d: SimpleNamespace(**d)).Pokemons
    agents_json = json.loads(client.get_agents(), object_hook=lambda d: SimpleNamespace(**d)).Agents
    agents = load_agents(agents_json, client)
    pokemons = load_pokemon(pokemons_json, graph=graph)
    pokemon_check: dict = dict.fromkeys(pokemons.keys(), False)
    draw_Frame(graph, moves, points, client.time_to_end(), agents, pokemons)
    divide_pokemon(agents_list=agents, pokemons_list=pokemons, pokemon_check=pokemon_check)
    catch_pokemons(agents_list=agents, client=client)
    print(client.move())
    moves += 1
    for agent in agents.values():
        points += agent.get_value()
    print(client.get_info())


# if __name__ == '__main__':
