import math
from unittest import TestCase

from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo

class TestGraphAlgo(TestCase):

    id1 = 0
    id2 = 1
    id3 = 2
    id4 = 3
    x1 = 35.18869800968523
    x2 = 35.187594216303474
    x3 = 35.19381366747377
    y1 = 32.104927164705884
    y2 = 32.10378225882353
    y3 = 32.102419275630254
    z = 0.0
    graph = DiGraph()
    graph.add_node(id1, (x1, y1, z))
    graph.add_node(id2, (x2, y2, z))
    graph.add_node(id3, (x3, y3, z))
    graph.add_node(id4, (5, 9, 0))
    graph.add_edge(id1, id2, 3)
    graph.add_edge(id2, id4, 6)
    graph.add_edge(id3, id4, 8)
    graph.add_edge(id3, id1, 7)
    g_algo = GraphAlgo(graph)


    def test_get_graph(self):
        graph_alg = self.g_algo.get_graph()
        node_dict_alg = graph_alg.get_all_v()
        node_dict_graph = self.graph.get_all_v()
        for node1 in node_dict_graph.values():
            node2 = node_dict_alg[node1.get_ID()]
            self.assertEqual(node1.get_ID(), node2.get_ID())
            self.assertEqual((node1.get_location().get_x(), node1.get_location().get_y(), node1.get_location().get_z()),
                             (node2.get_location().get_x(), node2.get_location().get_y(), node2.get_location().get_z()))
        mc_alg = graph_alg.get_mc()
        mc_graph = self.graph.get_mc()
        self.assertEqual(mc_graph, mc_alg)
        self.assertEqual(self.graph.e_size(), graph_alg.e_size())

    def test_load_from_json(self):
        alg = GraphAlgo()
        self.assertEqual(True, alg.load_from_json("C:\\Users\hadar\PycharmProjects\Ex3\data\A0.json"))

    def test_save_to_json(self):
        alg2 = GraphAlgo()
        alg3 = GraphAlgo()
        alg2.load_from_json("C:\\Users\hadar\PycharmProjects\Ex3\data\A0.json")
        loadedGraphBeforeSave = alg2.get_graph()
        alg2.save_to_json("C:\\Users\hadar\PycharmProjects\Ex3\data\A0Test.json")
        alg3.load_from_json("C:\\Users\hadar\PycharmProjects\Ex3\data\A0Test.json")
        loadedGraphAfterSave = alg3.get_graph()
        # self.assertEqual(True, flag)
        self.assertEqual(loadedGraphBeforeSave.e_size(), loadedGraphAfterSave.e_size())

    def test_shortest_path(self):
        self.assertEqual((3, [0, 1]), self.g_algo.shortest_path(0, 1))
        self.assertEqual((math.inf, []), self.g_algo.shortest_path(0, 2))
        self.assertEqual((9, [0, 1, 3]), self.g_algo.shortest_path(0, 3))
        self.assertEqual((0, [2]), self.g_algo.shortest_path(2, 2))

    def test_tsp(self):
        graph = DiGraph()
        graph.add_node(0, (1, 1, 1))
        graph.add_node(1, (2, 2, 2))
        graph.add_node(2, (3, 3, 3))
        graph.add_edge(0, 1, 1)
        graph.add_edge(1, 2, 3)
        graph.add_edge(2, 0, 10)
        ag = GraphAlgo(graph)
        lst = [0, 1, 2]
        self.assertEqual(([0, 1, 2], 4), ag.TSP(lst))
        graph2 = DiGraph()
        graph2.add_node(0, (1, 1, 1))
        graph2.add_node(1, (2, 2, 2))
        graph2.add_node(2, (3, 3, 3))
        graph2.add_edge(0, 1, 1)
        graph2.add_edge(1, 2, 3)
        graph2.add_edge(2, 0, 10)
        graph2.add_edge(0, 2, 0.5)
        graph2.add_edge(2, 1, 1)
        algo = GraphAlgo(graph2)
        lst = [0, 1, 2]
        self.assertTrue(1.5 <= algo.TSP(lst)[1] <= 4)
        self.assertTrue(set(lst).issubset(set(algo.TSP(lst)[0])))

    def test_center_point(self):
        self.assertEqual((None, math.inf), self.g_algo.centerPoint())
        graph2 = DiGraph()
        graph2.add_node(self.id1, (self.x1, self.y1, self.z))
        graph2.add_node(self.id2, (self.x2, self.y2, self.z))
        graph2.add_node(self.id3, (self.x3, self.y3, self.z))
        graph2.add_node(self.id4, (5, 9, 0))
        graph2.add_edge(self.id1, self.id2, 3)
        graph2.add_edge(self.id2, self.id4, 6)
        graph2.add_edge(self.id3, self.id4, 8)
        graph2.add_edge(self.id3, self.id1, 7)
        graph2.add_edge(0, 2, 0.8)
        graph2.add_edge(2, 0, 5)
        graph2.add_edge(1, 2, 3.5)
        graph2.add_edge(3, 2, 1)
        graph2.add_edge(3, 1, 1.1)
        graph2.add_edge(1, 0, 4)
        graph2.add_edge(0, 3, 9)
        graph2.add_edge(3, 0, 0.1)
        alg2 = GraphAlgo(graph2)
        self.assertEqual((3, 1.1), alg2.centerPoint())
        alg1 = GraphAlgo()
        alg1.load_from_json("C:\\Users\hadar\PycharmProjects\Ex3\data\A0.json")
        self.assertEqual((7, 6.806805834715163), alg1.centerPoint())









