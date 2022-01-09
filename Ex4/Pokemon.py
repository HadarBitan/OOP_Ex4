import GraphAlgo
import main
from Point3D import Point3D


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
    def __init__(self, value: float, poke_type: int, pos: tuple):
        self._value: float = value
        self._type: int = poke_type
        self._pos: tuple = pos
        self._edge: tuple = ()
        self._find_edge()


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
        return self._pos

    def get_edge(self) -> tuple:
        return self._edge

    def set_value(self, new_value) -> None:
        """
        This function update the value of the pokemon after each time he crea
        param: new_value is the value to update
        """
        self._value = new_value

    def _find_edge(self):
        """
            This function finds edge this pokemon is lying on and update ist edge.
        """
        for edge in main.graph.get_graph().get_all_e().keys():
            srcPos = main.graph.get_graph().get_all_v()[edge[0]].get_location()
            destPos = main.graph.get_graph().get_all_v()[edge[1]].get_location()
            src = Point3D(srcPos[0], srcPos[1], srcPos[2])
            dest = Point3D(destPos[0], destPos[1], destPos[2])
            point_self = Point3D(self._pos[0], self._pos[1], self._pos[2])
            if src.distance(point_self) + dest.distance(point_self) == src.distance(dest):
                if ((src < dest) and (self._type > 0)) or ((src > dest) and (self._type < 0)):
                    self._edge = edge
                    break
