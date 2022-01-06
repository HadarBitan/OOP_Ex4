from src.Graph.Point3D import Point3D
from src.Pokemon import Pokemon


class Agent:
    """
    This class represent a single agent shown by:
    id -> an integer that can not be changed
    value -> a float number representing the score of the agent and that grows every time
        the agent catches a pokemon
    src -> a source vertex where the agent comes from
    dest -> the agents destination
    speed -> an float number represent the speed of the agent and grows every time
        the agent catches a pokemon
    pos -> a 3 dimensional point represent the current position of the agent
    """
    def __init__(self, agent_id: int, value: float, src: int, dest: int, speed: float, pos: Point3D):
        self._id: int = agent_id
        self._value: float = value
        self._src: int = src
        self._dest: int = dest
        self._speed: float = speed
        self._pos: Point3D = pos
        self._list_of_poke: {Pokemon: bool} = {}

    def get_id(self) -> int:
        return self._id

    def get_value(self) -> float:
        return self._value

    def get_src(self) -> int:
        return self._src

    def get_dest(self) -> int:
        return self._dest

    def get_speed(self) -> float:
        return self._speed

    def get_pos(self) -> tuple:
        return self._pos.get_x(), self._pos.get_y(), self._pos.get_z()

    def set_value(self, new_value: float) -> None:
        """
        This function update the value of the agent after each time the agent catches a pokemon
        param: new_value is the value to update
        """
        self._value += new_value

    def set_src(self, new_src: int) -> None:
        """
        This function update the src node of the agent aka the new node the agent going out
        from to catch the pokemon
        param: new_src is the src to update
        """
        self._src = new_src

    def set_dest(self, new_dest: int) -> None:
        """
        This function update the dest node of the agent aka the new destination the agent going to
        in purpose to catch the pokemon
        param: new_dest is the destination to update
        """
        self._dest = new_dest

    def set_speed(self, new_speed: float) -> None:
        """
        This function update the speed of the agent after each time the agent catches a pokemon
        param: new_speed is the speed to update
        """
        self._speed += new_speed

    def set_pos(self, new_pos: Point3D) -> None:
        """
        This function update the current position of the agent
        param: new_pos is the new current position of the agent
        """
        self._pos = new_pos

    def update_pokemon_list(self, poke: Pokemon) -> None:
        """
        The function add a giving pokemon to the pokemon list
        :param poke: a pokemon to be add
        :return: the function dosn't return anything
        """
        self._list_of_poke[poke] = False

# a function to send the agents to the pokemons:
#     for every pokemon in the pokemon list we do:
#         if the bool part in the dictionary of this pokemonis false then:
#             check if th

# a function that get an agent and a pokemon and checks the distance the agent needs
# to pass to the pokemon considering the agent speed-> the function would call distance_to_pokemon
# the function will return a tuple containing the distance the agent needs to pass and the time
# it would take him

# a function that calls distance_to_pokemon and for the time she gets she devide it to 10 and
#     call the function move of the client every part of time