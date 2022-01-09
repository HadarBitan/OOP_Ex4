import json
import math
from typing import List

from DiGraph import DiGraph
from queue import PriorityQueue


class GraphAlgo:

    def __init__(self, graph: DiGraph = None):
        self.__graph = DiGraph()
        if graph is not None:
            for node in graph.get_all_v().values():
                self.__graph.add_node(node.get_ID(), (node.get_location().get_x(), node.get_location().get_y(),
                                                      node.get_location().get_z()))
            for src in graph.get_all_src_dict().keys():
                for dest in graph.all_out_edges_of_node(src).keys():
                    self.__graph.add_edge(src, dest, graph.get_edge_weigth(src, dest))

    def get_graph(self) -> DiGraph:
        return self.__graph

    def load_from_json(self, file_name: str) -> bool:
        try:
            with open(file_name, 'r') as f:  # Open a file for reading
                Jsonfile = json.load(f)
            graph = DiGraph()
            for node in Jsonfile["Nodes"]:
                if "pos" in node:
                    pos = tuple(map(float, str(node["pos"]).split(",")))
                    graph.add_node(node['id'], pos)
                else:
                    graph.add_node(node['id'])
            for edge in Jsonfile["Edges"]:
                graph.add_edge(edge["src"], edge["dest"], edge["w"])
            self.__graph = graph
            return True
        except Exception as e:
            print(e)
            return False

    def save_to_json(self, file_name: str) -> bool:
        dictionary = {"Edges": [], "Nodes": []}
        for src in self.__graph.get_all_src_dict().keys():
            for dest in self.__graph.get_all_src_dict()[src].keys():
                ed_dict = {"src": src, "w": self.__graph.get_edge_weigth(src, dest), "dest": dest}
                dictionary["Edges"].append(ed_dict)
        for node in self.__graph.get_all_v().values():
            pos = "{},{},{}".format(node.get_location().get_x(), node.get_location().get_y(),
                                    node.get_location().get_z())
            id_node = node.get_ID()
            no_dict = {"pos": pos, "id": id_node}
            dictionary["Nodes"].append(no_dict)

        try:
            json_object = json.dumps(dictionary, indent=4)
            with open(file_name, 'w') as outfile:  # Open a file for writing
                outfile.write(json_object)
                return True
        except Exception as e:
            print(e)
            return False

    def _Dijkstra(self, src) -> (list[int], list[int]):
        dist = {src: 0}
        for node in self.__graph.get_all_v().keys():
            if node == src:
                continue
            dist[node] = math.inf
        parantMap = {}
        for node in self.__graph.get_all_v().keys():
            parantMap[node] = None
        heap_queue = PriorityQueue()
        heap_queue.put((0, src))
        while not heap_queue.empty():
            v = heap_queue.get()
            if v[1] not in self.__graph.get_all_src_dict():
                break
            for neighbor in self.__graph.all_out_edges_of_node(v[1]).keys():
                old_dist = dist[neighbor]
                new_dist = dist[v[1]] + self.__graph.get_edge_weigth(v[1], neighbor)
                if new_dist < old_dist:
                    dist[neighbor] = new_dist
                    parantMap[neighbor] = v[1]
                    heap_queue.put((new_dist, neighbor))
        return parantMap, dist

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        if id1 not in self.__graph.get_all_v() or id2 not in self.__graph.get_all_v():
            return math.inf, []
        if id1 is id2:
            return 0, [id1]
        parent, shortest_path_dist = self._Dijkstra(id1)
        if shortest_path_dist[id2] == math.inf:
            return math.inf, []
        path = []
        if id2 in parent:
            v = id2
            while v is not None:
                path.append(v)
                v = parent[v]
        return shortest_path_dist[id2], path[::-1]

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        sum_weight = 0
        path = []
        if len(node_lst) > 0:
            path.append(node_lst[0])
            src = node_lst[0]
            for node in node_lst[1:]:
                calculate = self.shortest_path(src, node)   #return the short path from the src in all the Graph
                way = calculate[1]  #[list]
                sum_weight += calculate[0] #[weight]
                src = node
                for p in way[1:]:
                    path.append(p)
        if sum_weight == math.inf:
            return [], math.inf
        return path, sum_weight
