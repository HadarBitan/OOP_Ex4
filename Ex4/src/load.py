import json

from src.Agent import Agent
from src.Graph.Point3D import Point3D
from src.Pokemon import Pokemon


def load_agents(file_name: str) -> dict:
    list_of_agent: {int: Agent} ={}
    try:
        with open(file_name, 'r') as f:  # Open a file for reading
            Jsonfile = json.load(f)
            for agent in Jsonfile["Agents"]:
                pos = tuple(map(float, str(agent["pos"]).split(",")))
                new_agent = Agent(agent["id"], agent["value"], agent["src"], agent["dest"],
                                  agent["speed"], Point3D(pos[0], pos[1], pos[2]))
                list_of_agent[agent["id"]] = new_agent
        return list_of_agent
    except Exception as e:
        print(e)
        return {}


def load_pokemon(file_name: str) -> list:
    list_of_pokemons: list = []
    try:
        with open(file_name, 'r') as f:  # Open a file for reading
            Jsonfile = json.load(f)
            for pokemon in Jsonfile["Pokemons"]:
                pos = tuple(map(float, str(pokemon["pos"]).split(",")))
                new_pokemon = Pokemon(pokemon["value"], pokemon["type"], Point3D(pos[0], pos[1], pos[2]))
                list_of_pokemons.append(new_pokemon)
        return list_of_pokemons
    except Exception as e:
        print(e)
        return []
