import sys

from src.Pokemon import Pokemon
from src.Graph.GraphAlgo import GraphAlgo
from src.Graph.Point3D import Point3D


def edge_of_pokemon(poke: Pokemon, graph: GraphAlgo) -> tuple:
    """
        This function gets a pokemon and finds the  edge is lying on.
        param poke: represent the pokemon to find the edge for
        return: a tuple of 2 numbers (src, dest)- represent the edge of the pokemon
    """
    pokeEdge = ()
    pokePos = Point3D(poke.get_pos()[0], poke.get_pos()[1], poke.get_pos()[2])
    for edge in graph.get_graph().get_all_e().keys():
        srcPos = graph.get_graph().get_all_v()[edge[0]].get_location()
        destPos = graph.get_graph().get_all_v()[edge[1]].get_location()
        src = Point3D(srcPos[0], srcPos[1], srcPos[2])
        dest = Point3D(destPos[0], destPos[1], destPos[2])
        if src.distance(pokePos) + dest.distance(pokePos) == src.distance(dest):
            if ((src < dest) and (poke.get_type() > 0)) or ((src > dest) and (poke.get_type() < 0)):
                pokeEdge = edge
                break
    return pokeEdge


# def place_agents(self):
#     for poke in self.list_of_pokemons:
#         pokeEdge = self.edge_of_pokemon(poke)
#     for agent in self.list_of_agents:
#         pass

def closest_agent(poke_edge: tuple, list_of_agents: dict, graph: GraphAlgo) -> int:
    """
    The function find the best agent to catch a giving pokemon
    :param poke_edge: the edge the pokemon is lying on, represented by a tuple of 2 numbers -> (src, dest)
    :param list_of_agents: the list og agents to check
    :param graph:
    :return: the id of the optimize agent
    """
    id_agent = 0
    min_dis = sys.maxsize
    for agent in list_of_agents.values():
        tmp_dis = graph.shortest_path(agent.get_src(), poke_edge[1])
        if tmp_dis < min_dis:
            min_dis = tmp_dis
            id_agent = agent.get_id()
    return id_agent

# help function to the function above to find the agent for a specific pokemon -> the function gets
# the agent list, the graph and the pokemon to be asign an agent and his edge:
#     *an variable that kepps the id of the best agent
#     *an variable that keeps the min distance between an agent and the pokemon
#     *for every agent in the list of agents we do:
#         *an variable to keep the temporary distance of the current agent and the pokemon
#         *temporary distance = calling the shortest path function from the graph for the agent src to the
#         pokemon dest
#         *if temporary distance < min distance:
#             min distance = temporary distance
#             id of the best agent = id of current agent
#     returning the id of the current agent


def divide_pokemons(list_of_pokemons: list, list_of_agents: dict, graph: GraphAlgo) -> None:
    """
    The function go over all the pokemon and assign for each pokemon the best agent to catch
    him, the function send the pokemon to the agent list of pokemons.
    :param list_of_pokemons: list of all pokemon on the graph to be catch
    :param list_of_agents: the list of all agents
    :param graph: the graph the pokemon are on
    :return:
    """
    for poke in list_of_pokemons:
        # finding the edge that the current pokemon is lying on
        pokeEdge = edge_of_pokemon(poke, graph)
        # finding the best agent to catch the pokemon
        id_best_agent: int = closest_agent(pokeEdge, list_of_agents, graph)
        # add the pokemon to the agent list of pokemon
        list_of_agents[id_best_agent].update_pokemon_list(poke)

#dividing the pokemons to the agents
# function to divide the pokemons to the agent -> this function get the list of pokemons,
# the list of agents and the graph:
#     for every pokemon we do:
#     pokeedge = edge_of_pokemon(poke) -> finding the edge of the current pokemon
#     *find_the closest_agent -> going over the agents list and use shortest path between
#     every agent and the current pokemon -> this function will return an agent
#     *add the current pokemon to the list of pokemon of the returning agent