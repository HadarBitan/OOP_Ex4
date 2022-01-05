from src.Pokemon.Pokemon import Pokemon
from src.Pokemon.PokemonAlgo import PokemonAlgo
from src.Agent.Agent import Agent
from src.Agent.AgentAlgo import AgentAlgo
from src.Graph.DiGraph import DiGraph
from src.Graph.GraphAlgo import GraphAlgo
from client_python.client import Client
from src.GUI.run_GUI import run


# default port
PORT = 6666
# server host (default localhost 127.0.0.1)
HOST = '127.0.0.1'


client = Client()
client.start_connection(HOST, PORT)

agents_json = client.get_agents()
pokemons_json = client.get_pokemons()
graph_json = client.get_graph()

agents = AgentAlgo()
agents.load_from_json(agents_json)
pokemons = PokemonAlgo()
pokemons.load_from_json(pokemons_json)
graph = GraphAlgo()
graph.load_from_json(graph_json)

client.start()

while client.is_running() == 'true':
    run(agents, pokemons, graph)
    #choose the next node for each agent
    # client.move()

# if __name__ == '__main__':
