import main
from Point3D import Point3D
from Pokemon import Pokemon
import threading


class Agent(threading.Thread):
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

    def __init__(self, agent_id: int, value: float, src: int, dest: int, speed: float, pos: tuple):
        threading.Thread.__init__(self)
        self._id: int = agent_id
        self._value: float = value
        self._src: int = src
        self._dest: int = dest
        self._speed: float = speed
        self._pos: tuple = pos
        self._pokemon = None
        self.sum_moves = 0

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
        return self._pos

    def get_pokemon(self):
        return self._pokemon

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

    def set_pos(self, new_pos: tuple) -> None:
        """
        This function update the current position of the agent
        param: new_pos is the new current position of the agent
        """
        self._pos = new_pos

    def set_pokemon(self, new_pokemon: Pokemon):
        self._pokemon = new_pokemon

    def run(self) -> None:
        EPS = 0.0000001
        while True:
            # sent the client to the dest of the edge of the pokemon
            main.client.choose_next_edge(
                '{"agent_id":' + str(self._id) + ', "next_node_id":' + str(self._pokemon.get_edge()[1]) + '}')
            # only when the agent is very close to the pokemon act
            if self._pos.distance(self._pokemon.get_pos()) <= EPS:
                # final move to catch the pokemon
                main.client.move()
                self.sum_moves += 1
                self._dest = -1
                # setting the pokemon as cached
                break

