from NodeData import NodeData
from Point3D import Point3D


class DiGraph:

    def __init__(self):
        self._mc = 0
        self._vertices_dict: {int: NodeData} = {}
        self._src_edge_dict: dict = dict([])
        self._dest_edge_dict: dict = dict([])
        self.edges_size = 0

    def v_size(self) -> int:
        return len(self._vertices_dict)

    def e_size(self) -> int:
        return self.edges_size

    def get_all_v(self) -> dict:
        return self._vertices_dict

    def all_in_edges_of_node(self, id1: int) -> dict:
        if id1 not in self._dest_edge_dict.keys():
            return {}
        return self._dest_edge_dict[id1]

    def all_out_edges_of_node(self, id1: int) -> dict:
        if id1 not in self._src_edge_dict.keys():
            return {}
        return self._src_edge_dict[id1]

    def get_mc(self) -> int:
        return self._mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if id1 not in self._vertices_dict.keys():
            return False
        if id2 not in self._vertices_dict.keys():
            return False
        if id1 in self._src_edge_dict.keys():
            if id2 in self._src_edge_dict[id1].keys():
                return False
        if id2 in self._dest_edge_dict.keys():
            if id1 in self._dest_edge_dict[id2].keys():
                return False
        if id1 not in self._src_edge_dict.keys():
            self._src_edge_dict[id1] = {}
        self._src_edge_dict[id1][id2] = weight
        if id2 not in self._dest_edge_dict.keys():
            self._dest_edge_dict[id2] = {}
        self._dest_edge_dict[id2][id1] = weight
        self._vertices_dict.get(id1).update_neighbors_list(id2)
        self._mc += 1
        self.edges_size += 1
        self._vertices_dict[id2].update_number_of_edges_in("+")
        return True

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if node_id in self._vertices_dict.keys():
            return False
        if pos is None:
            new_node = NodeData(node_id, Point3D(0, 0, 0))
        else:
            new_node = NodeData(node_id, Point3D(pos[0], pos[1], pos[2]))
        self._vertices_dict[node_id] = new_node
        self._mc += 1
        return True

    def remove_node(self, node_id: int) -> bool:
        if node_id not in self._vertices_dict.keys():
            return False
        del self._vertices_dict[node_id]
        if node_id in self._dest_edge_dict.keys():
            for e in self._dest_edge_dict[node_id]:
                del self._src_edge_dict[e][node_id]
                e.remove_from_neighbors_list(node_id)
                self.edges_size -= 1
            del self._dest_edge_dict[node_id]
        if node_id in self._src_edge_dict.keys():
            for e in self._src_edge_dict[node_id]:
                del self._dest_edge_dict[e][node_id]
                self._vertices_dict[e].update_number_of_edges_in("-")
                self.edges_size -= 1
            del self._src_edge_dict[node_id]
        self._mc += 1
        return True

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if node_id1 not in self._vertices_dict.keys():
            return False
        if node_id2 not in self._vertices_dict.keys():
            return False
        if node_id2 not in self._src_edge_dict[node_id1].keys():
            return False
        if node_id1 not in self._dest_edge_dict[node_id2].keys():
            return False
        del self._src_edge_dict[node_id1][node_id2]
        del self._dest_edge_dict[node_id2][node_id1]
        self._vertices_dict.get(node_id1).remove_from_neighbors_list(node_id2)
        self._vertices_dict[node_id2].update_number_of_edges_in("-")
        self.edges_size -= 1
        self._mc += 1
        return True

    def get_edge_weigth(self, src: int, dest: int) -> float:
        return self._src_edge_dict[src][dest]

    def get_all_src_dict(self) -> dict:
        return self._src_edge_dict

    def is_edge_excics(self, src, dest):
        if src in self._src_edge_dict.keys():
            if dest in self._src_edge_dict[src].keys():
                return True
        return False

    def get_all_e(self) -> dict:
        edges_dict: {tuple: int} = {}
        for src in self._src_edge_dict.keys():
            for dest in self._src_edge_dict[src].keys():
                edges_dict[(src,dest)] = self._src_edge_dict[src][dest]
        return edges_dict

    def __repr__(self):
        return "Graph: |V|={}, |E|={}".format(self.v_size(), self.e_size())
