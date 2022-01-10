from unittest import TestCase
from src.Point3D import Point3D
from src.NodeData import NodeData
from src.DiGraph import DiGraph

class TestDiGraph(TestCase):
    id1 = 0
    id2 = 1
    id3 = 2
    id4 = 3
    id5 = 4
    id6 = 5
    id7 = 6
    x1 = 35.18869800968523
    x2 = 35.187594216303474
    x3 = 35.19381366747377
    y1 = 32.104927164705884
    y2 = 32.10378225882353
    y3 = 32.102419275630254
    z = 0.0
    loc1 = Point3D(x=x1, y=y1, z=z)
    loc2 = Point3D(x=x2, y=y2, z=z)
    loc3 = Point3D(x=x3, y=y3, z=z)
    loc4 = Point3D(x=5, y=9, z=0)
    loc5 = Point3D(x=7, y=11, z=0)
    loc6 = Point3D(x=20, y=8, z=0)
    loc7 = Point3D(x=13, y=9, z=0)
    n1 = NodeData(id1, loc1)
    n2 = NodeData(id2, loc2)
    n3 = NodeData(id3, loc3)
    n4 = NodeData(id4, loc4)
    n5 = NodeData(id5, loc5)
    n6 = NodeData(id6, loc6)
    n7 = NodeData(id7, loc7)
    v1_dict = [n1, n2, n3]
    v2_dict = [n1]
    v3_dict = [n1, n2, n3, n4, n5, n6, n7]
    graph = DiGraph()

    def test_v_size(self):
        self.assertEqual(3, len(self.v1_dict))
        self.assertEqual(7, len(self.v3_dict))
        self.assertEqual(1, len(self.v2_dict))

    def test_e_size(self):
        self.graph.add_node(self.id1, (self.x1, self.y1, self.z))
        self.graph.add_node(self.id2, (self.x2, self.y2, self.z))
        self.graph.add_node(self.id3, (self.x3, self.y3, self.z))
        self.graph.add_node(self.id4, (5, 9, 0))
        self.graph.add_edge(self.id1, self.id2, 3)
        self.graph.add_edge(self.id2, self.id4, 6)
        self.graph.add_edge(self.id3, self.id4, 8)
        self.graph.add_edge(self.id3, self.id1, 7)

        self.assertEqual(4, self.graph.e_size())

    def test_get_all_v(self):
        self.graph.add_node(self.id1, (self.x1, self.y1, self.z))
        self.graph.add_node(self.id2, (self.x2, self.y2, self.z))
        self.graph.add_node(self.id3, (self.x3, self.y3, self.z))
        self.graph.add_node(self.id4, (5, 9, 0))
        v = self.graph.get_all_v()
        self.assertEqual(4, len(v))

    def test_all_in_edges_of_node(self):
        self.graph.add_node(self.id1, (self.x1, self.y1, self.z))
        self.graph.add_node(self.id2, (self.x2, self.y2, self.z))
        self.graph.add_edge(self.id1, self.id2, 9)
        ans = {self.id1: 9}
        self.assertEqual(ans, self.graph.all_in_edges_of_node(self.id2))

    def test_all_out_edges_of_node(self):
        self.graph.add_node(self.id1, (self.x1, self.y1, self.z))
        self.graph.add_node(self.id2, (self.x2, self.y2, self.z))
        self.graph.add_edge(self.id1, self.id2, 9)
        ans = {self.id1: 9}
        self.assertEqual({}, self.graph.all_in_edges_of_node(self.id1))
        self.assertEqual(ans, self.graph.all_in_edges_of_node(self.id2))

    def test_get_mc(self):
        self.graph.add_node(self.id1, (self.x1, self.y1, self.z))
        self.graph.add_node(self.id2, (self.x2, self.y2, self.z))
        self.graph.add_node(self.id3, (self.x3, self.y3, self.z))
        self.graph.add_node(self.id4, (5, 9, 0))
        self.graph.add_edge(self.id1, self.id2, 3)
        self.graph.add_edge(self.id2, self.id4, 6)
        self.graph.add_edge(self.id3, self.id4, 8)
        self.graph.add_edge(self.id3, self.id1, 7)
        self.assertEqual(8, self.graph.get_mc())

    def test_add_edge(self):
        graph = DiGraph()
        graph.add_node(1, (2, 3, 0))
        graph.add_node(2, (2, 3, 0))
        graph.add_node(3, (2, 3, 0))
        graph.add_edge(1, 2, 50)
        graph.add_edge(1, 3, 50)
        self.assertEqual(False, graph.add_edge(1, 2, 50))
        self.assertEqual(True, graph.add_edge(2, 3, 9))

    def test_add_node(self):
        self.graph.add_node(self.id1, (self.x1, self.y1, self.z))
        self.graph.add_node(self.id2, (self.x2, self.y2, self.z))
        self.graph.add_node(self.id3, (self.x3, self.y3, self.z))
        self.graph.add_node(self.id4, (5, 9, 0))
        self.assertEqual(4, self.graph.v_size())

    def test_remove_node(self):
        self.graph.add_node(self.id1, (self.x1, self.y1, self.z))
        self.graph.add_node(self.id2, (self.x2, self.y2, self.z))
        self.graph.add_node(self.id3, (self.x3, self.y3, self.z))
        self.graph.add_node(self.id4, (5, 9, 0))
        self.assertEqual(4, self.graph.v_size())
        self.graph.remove_node(self.id2)
        self.graph.remove_node(self.id4)
        self.assertEqual(2, self.graph.v_size())

    def test_remove_edge(self):
        graph = DiGraph()
        graph.add_node(1, (2, 3, 0))
        graph.add_node(2, (2, 3, 0))
        graph.add_node(3, (2, 3, 0))
        graph.add_edge(1, 2, 50)
        graph.add_edge(1, 3, 50)
        self.assertEqual(3, graph.v_size())
        self.assertEqual(2, graph.e_size())
        graph.remove_edge(1, 2)
        self.assertEqual(3, graph.v_size())
        self.assertEqual(1, graph.e_size())