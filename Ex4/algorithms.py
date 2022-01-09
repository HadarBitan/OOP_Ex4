import sys

import main
from Agent import Agent
from Pokemon import Pokemon
from Point3D import Point3D
from game_frame import draw_time_to_end


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


def time_to_catch(agent: Agent, pokemon: Pokemon) -> float:
    """
    The function calcluate the time it would take a giving agent catch a giving pokemon
    :param agent:
    :param pokemon:
    :return:
    """
    agent_speed = agent.get_speed()
    xa, ya, za = agent.get_pos()
    agent_pos: Point3D = Point3D(xa, ya, za)
    xp, yp, zp = pokemon.get_pos()
    poke_pos: Point3D = Point3D(xp, yp, zp)
    distance = agent_pos.distance(poke_pos)
    return distance / agent_speed


def place_agent(agents_list: dict, pokemons_list: dict, pokemon_check: dict):
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
    for id_agent in IDList:
        for poke in pokemons_list.keys():
            if not pokemon_check[poke]:
                tmp_time = time_to_catch(agent=agents_list.get(id_agent), pokemon=pokemons_list.get(poke))
                if tmp_time < best_time:
                    best_time = tmp_time
                    index_poke = poke
        posOfPoke: tuple = pokemons_list[index_poke].get_pos()
        src, dest = pokemons_list[index_poke].get_edge()
        agents_list[id_agent].set_pos(posOfPoke)
        agents_list[id_agent].set_src(src)
        agents_list[id_agent].set_dest(dest)
        agents_list[id_agent].set_pokemon(pokemons_list[index_poke])
        pokemon_check[index_poke] = True


def catch_pokemons(agents_list: dict):
    """
    The function responsible to sent the agents to catch pokemon they assign to,
    the function uses Multiple threads
    :return:
    """
    threads = []
    for agent in agents_list.values():
        agent.start()
        threads.append(agent)
        ttl = main.client.time_to_end()
        print(ttl, main.client.get_info())
        draw_time_to_end(ttl)
    for thread in threads:
        thread.join()

# def catch_pokemons(agents_list: dict):
#     """
#     The function responsible to sent the agents to each pokemon on the list
#     :return:
#     """
#     EPS = 0.0000001
#     for agent in agents_list.values():
#         # as long as the pokemon didn't got caught keep on trying to catch him
#         while True:
#             # sent the client to the dest of the edge of the pokemon
#             main.client.choose_next_edge(
#                 '{"agent_id":' + str(agent.get_id()) + ', "next_node_id":' + str(agent.get_pokemon().get_edge()[1]) + '}')
#             # only when the agent is very close to the pokemon act
#             if agent.get_pos().distance(agent.get_pokemon().get_pos()) <= EPS:
#                 # final move to catch the pokemon
#                 main.client.move()
#                 agent.set_dest(-1)
#                 # setting the pokemon as cached
#                 break


# def save_agents(agents_list: dict):
#     """
#     The function saves the agents whith the new details to a json file
#     :param agents_list: dict of all agents
#     :return: json file
#     """
#     dictionary = {"Agents": []}
#     for agent in agents_list.values():
#         agent_dict = {"Agent": {"id": agent.get_id(), "value": agent.get_value(), "src": agent.get_src(),
#                                 "dest": agent.get_dest(), "speed": agent.get_speed(),
#                                 "pos": str(agent.get_pos())}}
#         dictionary["Agents"].append(agent_dict)
#     try:
#         json_object = json.dumps(dictionary, indent=4)
#         with open(file_name, 'w') as outfile:  # Open a file for writing
#             outfile.write(json_object)
#             return True
#     except Exception as e:
#         print(e)
#         return False
