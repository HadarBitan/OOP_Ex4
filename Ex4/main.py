import algorithms
from GraphAlgo import GraphAlgo
from client import Client
from game_frame import draw_Frame, draw_points, draw_agent, draw_pokemon, draw_moves
from load import load_agents, load_pokemon


# default port
PORT = 6666
# server host (default localhost 127.0.0.1)
HOST = '127.0.0.1'


client = Client()
client.start_connection(HOST, PORT)

client.add_agent("{\"id\":0}")
# client.add_agent("{\"id\":1}")
# client.add_agent("{\"id\":2}")
# client.add_agent("{\"id\":3}")

# agents_json = client.get_agents()
# pokemons_json = client.get_pokemons()
graph_json = client.get_graph()
graph = GraphAlgo()
graph.load_from_json(graph_json)
# print(agents_json)
# print(pokemons_json)

agents = load_agents()
# pokemons: dict = load_pokemon(pokemons_json)
pokemons = load_pokemon()
pokemon_check: dict = dict.fromkeys(pokemons.keys(), False)
# print(agents)
# print("end of agents")
# print(pokemons)
# print("end of pokemons")
draw_Frame(graph)

algorithms.first_init(agents_list=agents, pokemons_list=pokemons, pokemon_check=pokemon_check)


client.start()
points = 0
moves = 0

while client.is_running() == 'true':
    draw_points(points)
    draw_moves(moves)
    draw_agent(agents=agents)
    draw_pokemon(pokemons)
    algorithms.place_agent(agents_list=agents, pokemons_list=pokemons, pokemon_check=pokemon_check)
    algorithms.catch_pokemons(agents_list=agents)
    for agent in agents:
        points += agent.get_value()
        moves += agent.sum_moves
    agents = load_agents()
    pokemons = load_pokemon()

# if __name__ == '__main__':
