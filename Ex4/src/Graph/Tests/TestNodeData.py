from unittest import TestCase
from src.Point3D import Point3D
from src.NodeData import NodeData


class TestNodeData(TestCase):
    id1 = 0
    id2 = 1
    id3 = 2
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
    n1 = NodeData(id1, loc1)
    n2 = NodeData(id2, loc2)
    n3 = NodeData(id3, loc3)
    neighbor1 = [1, 4, 6]
    neighbor2 = [2, 3, 5]
    neighbor3 = [1, 4, 3]


    def test_get_id(self):
        self.assertEqual(self.id1, self.n1.get_ID())
        self.assertEqual(self.id2, self.n2.get_ID())
        self.assertEqual(self.id3, self.n3.get_ID())

    def test_get_location(self):
        self.assertEqual(self.loc1.__dict__, self.n1.get_location().__dict__)
        self.assertEqual(self.loc2.__dict__, self.n2.get_location().__dict__)
        self.assertEqual(self.loc3.__dict__, self.n3.get_location().__dict__)

    def test_update_neighbors_list(self):
        self.n1.update_neighbors_list(1)
        self.n1.update_neighbors_list(4)
        self.n1.update_neighbors_list(6)
        self.n2.update_neighbors_list(2)
        self.n2.update_neighbors_list(3)
        self.n2.update_neighbors_list(5)
        self.n3.update_neighbors_list(1)
        self.n3.update_neighbors_list(4)
        self.n3.update_neighbors_list(3)
        self.assertEqual(self.neighbor1, self.n1.get_neighbors_list())
        self.assertEqual(self.neighbor2, self.n2.get_neighbors_list())
        self.assertEqual(self.neighbor3, self.n3.get_neighbors_list())

    def test_remove_from_neighbors_list(self):
        self.n1.update_neighbors_list(1)
        self.n1.update_neighbors_list(4)
        self.n1.update_neighbors_list(6)
        self.n2.update_neighbors_list(2)
        self.n2.update_neighbors_list(3)
        self.n2.update_neighbors_list(5)
        self.n3.update_neighbors_list(1)
        self.n3.update_neighbors_list(4)
        self.n3.update_neighbors_list(3)

        self.n1.remove_from_neighbors_list(1)
        self.n2.remove_from_neighbors_list(5)
        self.n3.remove_from_neighbors_list(3)
        ne1 = [4, 6]
        ne2 = [2, 3]
        ne3 = [1, 4]
        self.assertEqual(ne1, self.n1.get_neighbors_list())
        self.assertEqual(ne2, self.n2.get_neighbors_list())
        self.assertEqual(ne3, self.n3.get_neighbors_list())

    def test_get_neighbors_list(self):
        self.n1.update_neighbors_list(1)
        self.n1.update_neighbors_list(4)
        self.n1.update_neighbors_list(6)
        self.n2.update_neighbors_list(2)
        self.n2.update_neighbors_list(3)
        self.n2.update_neighbors_list(5)
        self.n3.update_neighbors_list(1)
        self.n3.update_neighbors_list(4)
        self.n3.update_neighbors_list(3)
        self.assertEqual(self.neighbor1, self.n1.get_neighbors_list())
        self.assertEqual(self.neighbor2, self.n2.get_neighbors_list())
        self.assertEqual(self.neighbor3, self.n3.get_neighbors_list())


