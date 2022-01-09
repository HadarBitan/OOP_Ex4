import algorithms
from src.Graph.GraphAlgo import GraphAlgo
from client import Client
from src.GUI.game_frame import draw_Frame, draw_points, draw_agent, draw_pokemon, draw_moves
from load import load_agents, load_pokemon


# default port
PORT = 6666
# server host (default localhost 127.0.0.1)
HOST = '127.0.0.1'


client = Client()
client.start_connection(HOST, PORT)

graph_json = client.get_graph()
graph = GraphAlgo()
graph.load_from_json(graph_json)

draw_Frame(graph)

pokemons = load_pokemon()
pokemon_check: dict = dict.fromkeys(pokemons.keys(), False)

points = 0
moves = 0
client.add_agent("{\"id\":0}")
client.start()
count = 0
print("bye")
while client.is_running() == 'true':
    agents = load_agents()
    pokemons = load_pokemon()
    print("hi")
    if count == 0:
        algorithms.first_init(agents_list=agents, pokemons_list=pokemons, pokemon_check=pokemon_check)
        count += 1
    draw_points(points)
    draw_moves(moves)
    draw_agent(agents=agents)
    draw_pokemon(pokemons)
    algorithms.place_agent(agents_list=agents, pokemons_list=pokemons, pokemon_check=pokemon_check)
    algorithms.catch_pokemons(agents_list=agents)
    for agent in agents:
        points += agent.get_value()
        moves += agent.sum_moves

# if __name__ == '__main__':
