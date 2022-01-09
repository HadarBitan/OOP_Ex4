import sys

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


def time_to_catch(agent, pokemon) -> float:
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
        # ttl = main.client.time_to_end()
        # print(ttl, main.client.get_info())
        # draw_time_to_end(ttl)
    for thread in threads:
        thread.join()
