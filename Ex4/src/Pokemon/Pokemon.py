"""        returns the current pokemons state as json str.\n
        for pokemon lying on edge (src,dest), then:\n
        src < dest => type > 0\n
        dest < src => type < 0\n
        example:\n
        {
            "Pokemons":[
                {
                    "Pokemon":{
                        "value":5.0,
                        "type":-1,
                        "pos":"35.197656770719604,32.10191878639921,0.0"
                    }
                }
            ]
"""
from src.Graph.Point3D import Point3D


class Pokemon:
    """
        This class represent a pokemon shown by:
        value ->
        type -> an integer represent if the pokemon is upward or downward,
            the type is calculated according to the edge(src, dest) the pokemon lying on
            according to the next rule:
                    src < dest => type > 0 (downward)
                    dest < src => type < 0 (upward)
        pos -> a 3 dimensional point representing the current position of the pokemon, aka where's
            the pokemon is now on the graph
    """
    def __init__(self, value: float, poke_type: int, pos: Point3D):
        self._value: float = value
        self._type: int = poke_type
        self._pos: Point3D = pos

    def get_value(self) -> float:
        """
        returning the value of the pokemon
        """
        return self._value

    def get_type(self) -> int:
        """
            returning the type of the pokemon
        """
        return self._type

    def get_pos(self) -> tuple:
        """
            returning the position of the pokemon
        """
        return self._pos.get_x(), self._pos.get_y(), self._pos.get_z()

    def set_value(self, new_value) -> None:
        """
        This function update the value of the pokemon after each time he crea
        param: new_value is the value to update

        """
        self._value = new_value

