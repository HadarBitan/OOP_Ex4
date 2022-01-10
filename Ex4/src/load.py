from types import SimpleNamespace

from src.Agent import Agent
from src.Graph.Point3D import Point3D
from src.Pokemon import Pokemon


def load_pokemon(pokemons_json, graph) -> dict:
    list_of_pokemons: {int: Pokemon} = {}
    index = 0
    print(pokemons_json)
    pokemons = [p.Pokemon for p in pokemons_json]
    for p in pokemons:
        x, y, _ = p.pos.split(',')
        p.pos = SimpleNamespace(x=float(x), y=float(y))
        new_pokemon = Pokemon(p.value, p.type, (x, y, 0.0), graph=graph)
        list_of_pokemons[index] = new_pokemon
        index += 1
    return list_of_pokemons


def load_agents(agents_json, client) -> dict:
    agents = [agent.Agent for agent in agents_json]
    agent_dict = {}
    for a in agents:
        x, y, _ = a.pos.split(',')
        a.pos = SimpleNamespace(x=float(x), y=float(y))
        new_agent = Agent(a.id, a.value, a.src, a.dest, a.speed, (x, y, 0.0), client)
        agent_dict[a.id] = new_agent
    return agent_dict







    # try:
    #     with open(file_name, 'r'):  # Open a file for reading
    #         f = json.loads(file_name)
    #         Jsonfile = f
    #         # Jsonfile = json.load(f)
    #         for pokemon in Jsonfile["Pokemons"]:
    #             pos = tuple(map(float, str(pokemon["pos"]).split(",")))
    #             new_pokemon = Pokemon(pokemon["value"], pokemon["type"], Point3D(pos[0], pos[1], pos[2]))
    #             list_of_pokemons[index] = new_pokemon
    #             index += 1
    #     return list_of_pokemons
    # except Exception as e:
    #     print("bye")
    #     print(e)
    #     return {}


    # def load_agents(file_name: str) -> dict:
    #     list_of_agent: {int: Agent} = {}
    #     try:
    #         with open(file_name, 'r') as f:  # Open a file for reading
    #             # f = json.loads(file_name)
    #             # Jsonfile = f
    #             Jsonfile = json.load(f)
    #             print("hi")
    #             for agent in Jsonfile["Agents"]:
    #                 pos = tuple(map(float, str(agent["pos"]).split(",")))
    #                 new_agent = Agent(agent["id"], agent["value"], agent["src"], agent["dest"],
    #                                   agent["speed"], Point3D(pos[0], pos[1], pos[2]))
    #                 list_of_agent[agent["id"]] = new_agent
    #         return list_of_agent
    #     except Exception as e:
    #         # print("bye")
    #         print(e)
    #         return {}


# for a in agents:
#     new_agent = Agent(a.id, a.value, a.src, a.dest,
#                                       a.speed, a.pos)
#     agent_dict[a.id] = new_agent
# print(agents)
# for agent in agents:
#     print(agent.id, agent.value, agent.src)

# def scale(data, min_screen, max_screen, min_data, max_data):
#     """
#     get the scaled data with proportions min_data, max_data
#     relative to min and max screen dimentions
#     """
#     return ((data - min_data) / (max_data-min_data)) * (max_screen - min_screen) + min_screen
#
#
# # decorate scale with the correct values
#
# def my_scale(data, x=False, y=False):
#     if x:
#         return scale(data, 50, screen.get_width() - 50, min_x, max_x)
#     if y:
#         return scale(data, 50, screen.get_height()-50, min_y, max_y)
