import json

from src.Graph.Point3D import Point3D
from src.Pokemon.Pokemon import Pokemon

class PokemonAlgo:
    """
        This class representing an algorithm to agent, its purpose is to run a functions on the agent
    """
    def __init__(self):
        self._list_of_pokemons = []

    def load_from_json(self, file_name: str) -> bool:
        try:
            with open(file_name, 'r') as f:  # Open a file for reading
                Jsonfile = json.load(f)
                for pokemon in Jsonfile["Pokemons"]:
                    pos = tuple(map(float, str(pokemon["pos"]).split(",")))
                    new_pokemon = Pokemon(pokemon["value"], pokemon["type"], Point3D(pos[0], pos[1], pos[2]))
                    self.list_of_pokemons.append(new_pokemon)
            return True
        except Exception as e:
            print(e)
            return False

    def save_to_json(self, file_name: str) -> bool:
        dictionary = {"Pokemons": []}
        for pokemon in self.list_of_pokemons:
            pokemon_dict = {"Pokemon": {"value": pokemon.get_value(),  "type": pokemon.get_type(),"pos": str(pokemon.get_pos())}}
            dictionary["Pokemons"].append(pokemon_dict)
        try:
            json_object = json.dumps(dictionary, indent=4)
            with open(file_name, 'w') as outfile:  # Open a file for writing
                outfile.write(json_object)
                return True
        except Exception as e:
            print(e)
            return False
