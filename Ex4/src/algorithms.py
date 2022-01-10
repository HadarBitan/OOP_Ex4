import sys

from src.Graph.GraphAlgo import GraphAlgo
from src.Graph.Point3D import Point3D


def first_init(agents_list: dict, pokemons_list: dict, pokemon_check: dict):
    """
    The function place the agents for the first time according to the first pokemons position that hasn't
    been caught yet.
    :param agents_list:
    :param pokemons_list:
    :param pokemon_check:
    :return:
    """
    IDList: list = list(agents_list.keys())
    index = 0
    for id_agent in IDList:
        while True:
            if not pokemon_check[index]:
                posOfPoke: tuple = pokemons_list[index].get_pos()
                src, dest = pokemons_list[index].get_edge()
                agents_list[id_agent].set_pos(posOfPoke)
                agents_list[id_agent].set_src(src)
                agents_list[id_agent].set_dest(dest)
                agents_list[id_agent].set_pokemon(pokemons_list[index])
                pokemon_check[index] = True
                break
            index += 1


def time_to_catch(agent, pokemon, graph: GraphAlgo) -> (float, list):
    """
    The function calcluate the time it would take a giving agent catch a giving pokemon
    :param agent:
    :param pokemon:
    :return:
    """
    agent_speed = agent.get_speed()
    _, dest = pokemon.get_edge()
    distance, path = graph.shortest_path(agent.get_src(), dest)
    return (distance / agent_speed), path


def divide_pokemon(agents_list: dict, pokemons_list: dict, pokemon_check: dict, graph):
    """
    The function place the agents according to the pokemons all over again after the agents catches their pokemon
    :param agents_list: the agent needs to be placed
    :param pokemons_list: a list of the pokemons
    :param pokemon_check: this list represent if the pokemon got caught or not
    :return:
    """
    IDList: list = list(agents_list.keys())
    index_poke = 0
    best_time = sys.maxsize
    path = []
    for id_agent in IDList:
        for poke in pokemons_list.keys():
            if not pokemon_check[poke]:
                tmp_time, path = time_to_catch(agent=agents_list.get(id_agent), pokemon=pokemons_list.get(poke), graph=graph)
                if tmp_time < best_time:
                    best_time = tmp_time
                    index_poke = poke
        agents_list[id_agent].set_pokemon(pokemons_list[index_poke])
        agents_list[id_agent].set_path(path)
        pokemon_check[index_poke] = True


def catch_pokemons(agents_list: dict, client):
    """
    The function responsible to sent the agents to catch pokemon they assign to,
    :return:
    """
    points = 0
    for agent in agents_list.values():
        for node in agent.get_path():
            client.choose_next_edge(
                '{"agent_id": ' + str(agent.get_id()) + ', "next_node_id": ' + str(node) + '}')
    for agent in agents_list.values():
        points += agent.get_value()
    return points

