from src.Graph.Point3D import Point3D


class NodeData:

    def __init__(self,  node_id: int, location: Point3D):
        self.__id = node_id
        self._location = Point3D(location.get_x(), location.get_y(), location.get_z())
        self._neighbors_list = []
        self.number_of_edges_in = 0

    def get_ID(self) -> int:
        return self.__id

    def get_location(self) -> tuple:
        return self._location.get_x(), self._location.get_y(), self._location.get_z()

    def update_neighbors_list(self, neighbor) -> None:
        self._neighbors_list.append(neighbor)

    def remove_from_neighbors_list(self, neighbor) -> None:
        self._neighbors_list.remove(neighbor)

    def get_neighbors_list(self):
        return self._neighbors_list

    def update_number_of_edges_in(self, action: str):
        if action == "+":
            self.number_of_edges_in += 1
        if action == "-":
            self.number_of_edges_in -= 1


    def __repr__(self):
        return "{}: |edges_out| {} |edges in| {}".format(self.__id, len(self._neighbors_list), self.number_of_edges_in)
